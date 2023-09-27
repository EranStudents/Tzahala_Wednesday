'''

לכל תו במחרוזת בפייתון יש אינדקס (מיקום).
הספירה מתחילה מ-0
והמיקום האחרון הוא אורך המחרוזת פחות 1

len(מחרוזת) - מחזירה את כמות התווים במחרוזת
len - length - אורך

name = "Eran Levy"
        012345678

'''
# float
name = "Eran Levy"
#       012345678
print(f'The length of name is {len(name)}')
print(f'The letter in name[2] is : {name[2]}')
# print(f'The letter in name[9] is : {name[9]}')  # טעות, כי אין תו במיקום ה-9
print(f'The letter in name[8] is : {name[8]}')  # טעות, כי אין תו במיקום ה-9




