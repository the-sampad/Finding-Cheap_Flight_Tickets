import smtplib

USERNAME = 'sampadedge@gmail.com'
PASSWORD = 'Munna@2018'

connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
# connection.login(user=USERNAME, password=PASSWORD)

# class Mail:
#     def __init__(self) -> None:
#         pass
#     def send_mail(self, msg_text, user_email):
#         connection.sendmail(
#             from_addr=USERNAME,
#             to_addrs=user_email,
#             msg=msg_text
#         )


