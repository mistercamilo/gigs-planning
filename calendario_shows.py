#!/usr/bin/python3
import calendar
import holidays
import sys
from datetime import date, timedelta

diasdasemana = ["Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]

def days(start, end, step=timedelta(days=1)):
    curr = start
    while curr <= end:
        yield curr
        curr += step


if __name__ == "__main__":

    dias = list(days(date(2020, 1, 1), date(2020, 12, 31)))

    for a in dias:
        if str(a) in holidays.Brazil():
            print(str(a) + " - " + diasdasemana[a.weekday()] + " - Feriado")
        elif a.weekday() in range(2,5):
            print(str(a) + " - " + diasdasemana[a.weekday()])
            
                