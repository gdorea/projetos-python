import smtplib
import datetime as dt
import random

nova_lista =[]
now = dt.datetime.now()
day_of_week = now.weekday()

my_email = "gerzianniteste@gmail.com"
password = "fxriivcbcaylrtzz"

if day_of_week == 1: #É bom colocar esse if aqui pois já checa logo no começo do código se é o dia de mandar email.
    with open("day-32/quotes.txt") as file:
        lista = file.readlines()
        for quote in lista:
            nova_lista.append(quote[0:-2])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="gerzii@hotmail.com",
            msg=f"Subject:Frase motivacional da semana\n\n{random.choice(nova_lista)}"
            )
  