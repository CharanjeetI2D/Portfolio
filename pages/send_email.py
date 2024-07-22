import smtplib, ssl

host = 'smtp.gmail.com'
port = 8501

user_name = "charanjeet.rec@gmail.com"
sender = "charanjeet.rec@gmail.com"
password = "utljjxbdvgjmkbaw"

receiver = "charanjeet.rec@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Test Email
Hello this is from the other side."""

# with smtplib.SMTP_SSL(host, port, context=context) as server:
#     server.login(user_name, password)
#     server.sendmail(user_name, receiver, message)

with smtplib.SMTP("smtp.gmail.com") as server:
    server.starttls() and server.login(user=user_name, password=password)
    server.sendmail(from_addr=sender,
                    to_addrs=receiver,
                    msg=message)