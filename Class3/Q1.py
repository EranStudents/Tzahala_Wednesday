'''
המחשב יבקש להכניס מספר מ-10 עד 100
המחשב יבקש להכניס מספר שני מ-10 עד 100

נגדיר משתנה N1 יקבל את הערך של הספרה הראשונה במשתנה num_1
נגדיר משתנה N2 יקבל את הערך של הספרה הראשונה במשתנה num_2

נהפוך את המשתנה n1 למשתנה מסוג מספר int
נהפוך את המשתנה n2 למשתנה מסוג מספר int
ניצור משתנה בשם result שיחשב כמה זה n1+n2
המחשב ירשום את התוצאה בחיבור 2 הספרות הראשונות בכל מספר
'''
# type - סוג המשתנה
# print - מדפיס משהו למשתמש
# input - קולט משהו מהמשתמש

num_1 = input("Enter a number between 10-100: ")  # 749
num_2 = input("Enter another number between 10-100: ")  # 243

print(type(num_1))
print(type(num_2))

# אם num1_1 או num_2 היו משתנים מסוג int לא היה ניתן לגשת לספרה מסוימת
n1 = num_1[0]  # לגשת לספרה הראשונה ב-num_1
n2 = num_2[0]  # לגשת לספרה הראשונה ב-num_2

print(f'n1 = {n1}')
print(f'n2 = {n2}')

# דרך אחת לחשב את n1 ו-n2
# n1 = int(n1)
# n2 = int(n2)
#
# result = n1 + n2

# דרך שנייה לפתור את התרגיל הסופי
result = int(n1) + int(n2)
print(f'result = {result}')



