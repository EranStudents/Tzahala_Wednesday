'''
תרגיל
ברוכים הבאים למחשבון המשקל הרצוי
המחשב יבקש להכניס את הגובה במטרים
המחשב יבקש להכניס את המשקל
נמיר את המשתנה height למספר עשרוני
נמיר את המשתנה weight למספר עשרוני
ניצר משתנה total שיחשב את הנוסחה
המחשב יציג את המשקל הרצוי - BMI
'''
print('Welcome :)')
height = float(input("Enter your height : "))  # 168, 1.68
weight = float(input("Enter your weight : "))  # 72

# / - סימון של חילוק
# * - סימון של כפל
bmi = weight / (height * height)
print(f'My BMI is {bmi}')
