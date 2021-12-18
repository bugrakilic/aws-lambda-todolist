import smtplib, sys, json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

def lambda_handler(event, context):
    #TODO implement 
    main()
    return {
        'statusCode': 200, 
        'body': json.dumps('The script has been worked successfully.')
    }
    
def main():
    # TODO implement
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login("*******", "*******")
    
    sender = '*******'
    recipients = ['*******']
    
    # now = datetime.now()
    # dtstring = now.strftime("%d/%m/%Y %H+3:%M")
 
    mesaj = MIMEMultipart()
    mesaj["From"] = sender
    mesaj["To"] = ", ".join(recipients)
    mesaj["Subject"] = "Cloud Reminder"    
 
    body = """
    *** Reminder from AWS Lambda *** 
    - Python networking. 
    - GNS3 lab environment. 
    """#+str(dtstring)
 
    body_text = MIMEText(body, "plain")
    mesaj.attach(body_text)
 
    mail.sendmail(mesaj["From"], recipients, mesaj.as_string())
    print("The mail has been sent from AWS Lambda.")
    mail.close()