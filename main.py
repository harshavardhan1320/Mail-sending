import smtplib

email = "qazmko.1331@gmail.com"
password = "*******"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs="teja04032002@gmail.com", msg="fuck u bitch")

