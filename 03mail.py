import smtplib
from email.message import EmailMessage

EMAIL_ADD = 'ashishpoudel523@gmail.com'
e_pass = '{M@#a$h!lA4%}3325'

msg = EmailMessage()
msg['Subject'] = 'grab dinner'
msg['From'] = EMAIL_ADD
msg['To'] = EMAIL_ADD

msg.set_content('whats cooking?')

with smtplib.SMTP_SSL('ashmitapoudel058@gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADD, e_pass)
    smtp.send_message(msg)