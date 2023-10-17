import smtplib

my_email = "gerzianniteste@gmail.com"
password = "fxriivcbcaylrtzz"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="gerzii@hotmail.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )
