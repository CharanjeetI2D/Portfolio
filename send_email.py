import smtplib, ssl, os

def send_email(message):
    host = 'smtp.gmail.com'
    port = 8501

    user_name = "charanjeet.rec@gmail.com"
    sender = "charanjeet.rec@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "charanjeet.rec@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP("smtp.gmail.com") as server:
        server.starttls() and server.login(user=user_name, password=password)
        server.sendmail(from_addr=sender,
                        to_addrs=receiver,
                        msg=message)