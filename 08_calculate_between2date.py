from datetime import date

f_date = date(1997, 6,13)
l_date = date(2023, 7, 27)

delta = l_date - f_date
print(delta.days)