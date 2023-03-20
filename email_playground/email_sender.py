import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path("index.html").read_text())
email = EmailMessage()
email['from'] = "SaM"
email['to'] = "sam.saakshat1@gmail.com"
email['subject'] = "What is this?"

email.set_content(html.substitute(name="TinTin"), "html")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # smtp.login(#"login id", "pswd")
    smtp.send_message(email)
    print("all good")
