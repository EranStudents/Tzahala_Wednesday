'''
איך מכריזים על משתנים בשפה כמו java

String name = "Eran Levy"
int age = 58
float avg = 75.6
'''

# מחרוזת או string זהו רצף תווים כלשהו
name = "Eran Levy"
# פעולה שנקראת type - לדעת מה סוג המשתנה
print(type(name))  # --> str - string

# מספר שלם, integer
age = 29
print(type(age))  # --> int - integer

# מספר עשרוני, float
avg = 89.65
print(type(avg))  # --> float

# -----------------------------------
# str, int, float
# כברירת מחדל, הפעולה input תהיה str. אלא אם נציין אחרת
name = input("Enter your name : ")
print(type(name))

# יש לנו את האפשרות כמתכנתים לבצע המרה
# אני רוצה להמיר את מה שחוזר מ-input ל-int
age = int(input("Enter your age : \n"))

# שיטה 2 - פחות מומלצת
age_new = input("Enter your age: ")
age_new = int(age_new)

print(type(age))

avg = float(input("Enter you avg in English :"))
print(avg)
print(type(avg))
