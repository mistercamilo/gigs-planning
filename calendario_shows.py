#!/usr/bin/python3
import calendar
import holidays
from datetime import date, timedelta

diasdasemana = ["Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]

def days(start, end, step=timedelta(days=1)):
    curr = start
    while curr <= end:
        yield curr
        curr += step

dias = list(days(date(2020, 1, 1), date(2020, 6, 30)))

for a in dias:
    if str(a) in holidays.Brazil():
        print(str(a) + " - " + diasdasemana[a.weekday()] + " - Feriado")
    elif a.weekday() in range(2,6):
        print(str(a) + " - " + diasdasemana[a.weekday()])
            
                