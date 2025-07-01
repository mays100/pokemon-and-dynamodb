# פרויקט אוסף הפוקימונים עם AWS DynamoDB ו-EC2

![Pokemon Logo Placeholder](https://raw.githubusercontent.com/PokeAPI/pokeapi/master/logo.png) ## מבוא

פרויקט זה ממחיש יישום Python פשוט המקיים אינטראקציה עם PokeAPI כדי לאסוף ולנהל נתוני פוקימונים, תוך שימוש ב-AWS DynamoDB לאחסון. הפרויקט כולל פריסה אוטומטית של תשתית ה-AWS הנדרשת (EC2, DynamoDB, IAM, Security Groups) באמצעות סקריפטי Bash, ומבטיח שהיישום יותקן ויפעל באופן אוטומטי על שרת ה-EC2.

## מטרות הפרויקט

* איסוף נתוני פוקימונים אקראיים מ-PokeAPI.
* אחסון נתוני הפוקימונים ב-AWS DynamoDB.
* אחזור נתוני פוקימונים מ-DynamoDB והצגתם למשתמש.
* זיהוי ושמירה של פוקימונים חדשים בלבד (אם הפוקימון כבר קיים ב-DB, ישלוף משם).
* אוטומציה מלאה של פריסת התשתית ב-AWS.
* אוטומציה של התקנת היישום והפעלתו על שרת ה-EC2.

## ארכיטקטורה

הארכיטקטורה של הפרויקט מורכבת מהרכיבים הבאים:

* **Amazon EC2 Instance:** שרת לינוקס המארח את יישום ה-Python.
* **AWS DynamoDB:** בסיס נתונים NoSQL מנוהל המשמש לאחסון נתוני הפוקימונים.
* **AWS IAM Role:** תפקיד IAM מוקצה ל-EC2 Instance, המספק לו את ההרשאות הנדרשות לגישה ל-DynamoDB.
* **AWS Security Group:** קבוצת אבטחה השולטת בתעבורה נכנסת ויוצאת ל-EC2 Instance (מאפשרת SSH נכנס ותעבורה יוצאת לאינטרנט).
* **PokeAPI:** ממשק API ציבורי ממנו נשלפים נתוני הפוקימונים.

```mermaid
graph TD
    A[משתמש] -->|SSH| B(EC2 Instance)
    B -->|בקשות HTTP| C(PokeAPI)
    B -->|boto3 API Calls| D(AWS DynamoDB)
    D -->|Persistent Storage| E[טבלת PokemonCollection]
    B -->|IAM Role| F(AWS Services)