AWS_REGION="eu-central-1" # שנה לאזור ה-AWS שלך (חייב להתאים לשאר הקבצים)
DYNAMODB_TABLE_NAME="PokemonCollection" # חייב להתאים לשם שבחרת
IAM_ROLE_NAME="PokemonAppEC2Role" # חייב להתאים לשם שהגדרת ב-deploy.sh
SECURITY_GROUP_NAME="PokemonAppSG" # חייב להתאים לשם שהגדרת ב-deploy.sh
LAUNCH_TEMPLATE_NAME="PokemonAppLaunchTemplate" # חייב להתאים לשם שהגדרת ב-deploy.sh
# ייתכן שתצטרך להכניס כאן את ה-INSTANCE_ID ידנית אם סקריפט הניקוי לא מוצא אותו אוטומטית.
# לדוגמה: INSTANCE_ID="i-0xxxxxxxxxxxxxxxxxxxx"