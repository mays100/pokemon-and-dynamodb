import requests
import boto3
import random
import json # יעזור להדפיס JSON יפה

# הגדרות DynamoDB
DYNAMODB_TABLE_NAME = "PokemonCollection" # שנה לשם הטבלה שבחרת
REGION_NAME = "your-aws-region" # לדוגמה: "eu-central-1" או "us-east-1"

# אובייקט DynamoDB Resource (ישתמש בפרטי תפקיד ה-IAM של ה-EC2)
dynamodb = boto3.resource('dynamodb', region_name=REGION_NAME)
table = dynamodb.Table(DYNAMODB_TABLE_NAME)

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/"

def get_random_pokemon_name():
    """אחזור שם פוקימון אקראי מ-PokeAPI."""
    try:
        response = requests.get(f"{POKEAPI_BASE_URL}pokemon?limit=10000") # הגדל את הלימיט כדי לקבל יותר פוקימונים
        response.raise_for_status() # Raise an exception for HTTP errors
        data = response.json()
        pokemon_list = data['results']
        random_pokemon = random.choice(pokemon_list)
        return random_pokemon['name']
    except requests.exceptions.RequestException as e:
        print(f"שגיאה באחזור רשימת פוקימונים: {e}")
        return None

def get_pokemon_details(pokemon_name):
    """אחזור פרטי פוקימון ספציפי מ-PokeAPI."""
    try:
        response = requests.get(f"{POKEAPI_BASE_URL}pokemon/{pokemon_name}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"שגיאה באחזור פרטי פוקימון '{pokemon_name}': {e}")
        return None

def save_pokemon_to_db(pokemon_data):
    """שמירת פרטי פוקימון ב-DynamoDB."""
    try:
        # כאן תממש את הלוגיקה לשמירת הנתונים לפי הסכמה שלך
        # לדוגמה:
        item = {
            'pokemon_name': pokemon_data['name'],
            'id': pokemon_data['id'],
            'height': pokemon_data['height'],
            'weight': pokemon_data['weight'],
            'types': [t['type']['name'] for t in pokemon_data['types']],
            'abilities': [a['ability']['name'] for a in pokemon_data['abilities']],
            'base_experience': pokemon_data.get('base_experience'), # שימוש ב-get למקרה שאין
            'sprite_front_default': pokemon_data['sprites']['front_default'] if 'front_default' in pokemon_data['sprites'] else None
        }
        table.put_item(Item=item)
        print(f"הפוקימון '{pokemon_data['name']}' נשמר בהצלחה ב-DynamoDB.")
    except Exception as e:
        print(f"שגיאה בשמירת הפוקימון ל-DB: {e}")

def get_pokemon_from_db(pokemon_name):
    """אחזור פרטי פוקימון מ-DynamoDB."""
    try:
        response = table.get_item(Key={'pokemon_name': pokemon_name})
        return response.get('Item')
    except Exception as e:
        print(f"שגיאה באחזור הפוקימון מ-DB: {e}")
        return None

def display_pokemon_details(pokemon_details):
    """הצגת פרטי פוקימון בצורה יפה."""
    if not pokemon_details:
        print("לא נמצאו פרטים על הפוקימון.")
        return

    print("\n--- פרטי פוקימון ---")
    print(f"שם: {pokemon_details.get('pokemon_name', 'N/A').capitalize()}")
    print(f"מזהה: {pokemon_details.get('id', 'N/A')}")
    print(f"גובה: {pokemon_details.get('height', 'N/A')}")
    print(f"משקל: {pokemon_details.get('weight', 'N/A')}")
    print(f"סוגים: {', '.join([t.capitalize() for t in pokemon_details.get('types', ['N/A'])])}")
    print(f"יכולות: {', '.join([a.capitalize() for a in pokemon_details.get('abilities', ['N/A'])])}")
    print(f"ניסיון בסיסי: {pokemon_details.get('base_experience', 'N/A')}")
    if pokemon_details.get('sprite_front_default'):
        print(f"תמונה: {pokemon_details['sprite_front_default']}")
    print("---------------------\n")


def main():
    while True:
        choice = input("האם תרצה לשלוף פוקימון אקראי? (כן/לא): ").lower()

        if choice == 'כן':
            pokemon_name = get_random_pokemon_name()
            if not pokemon_name:
                continue

            print(f"נבחר פוקימון: {pokemon_name.capitalize()}")

            # בדוק אם הפוקימון כבר קיים ב-DB
            db_pokemon = get_pokemon_from_db(pokemon_name)

            if db_pokemon:
                print(f"הפוקימון '{pokemon_name.capitalize()}' כבר קיים בבסיס הנתונים.")
                display_pokemon_details(db_pokemon)
            else:
                print(f"הפוקימון '{pokemon_name.capitalize()}' אינו קיים בבסיס הנתונים, מוריד פרטים ומוסיף...")
                api_pokemon_details = get_pokemon_details(pokemon_name)
                if api_pokemon_details:
                    save_pokemon_to_db(api_pokemon_details)
                    display_pokemon_details(api_pokemon_details)
        elif choice == 'לא':
            print("להתראות! מקווה שנהנית מאוסף הפוקימונים שלך!")
            break
        else:
            print("קלט לא חוקי. אנא הקלד 'כן' או 'לא'.")

if __name__ == "__main__":
    main()