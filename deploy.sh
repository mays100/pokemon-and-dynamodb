AWS_REGION="eu-central-1" # שנה לאזור ה-AWS שלך (חייב להתאים ל-app.py)
EC2_AMI_ID="ami-0xxxxxxxxxxxxxx" # מזהה AMI של Ubuntu/Amazon Linux 2/3 באזור שלך. מצא אותו בקונסולת EC2.
EC2_INSTANCE_TYPE="t2.micro" # או t3.micro, בהתאם לדרישות
EC2_KEY_PAIR_NAME="your-key-pair-name" # שנה לשם Key Pair קיים שלך
GITHUB_REPO_URL="https://github.com/your-username/pokemon-collector.git" # שנה לכתובת ה-GitHub המדויקת של הריפוזיטורי שלך
DYNAMODB_TABLE_NAME="PokemonCollection" # חייב להתאים לשם ב-app.py
DYNAMODB_PRIMARY_KEY="pokemon_name" # חייב להתאים לסכמה שלך ב-app.py