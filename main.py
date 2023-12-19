import smtplib
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# CHANGE THESE VARIABLES BY YOURS
# IN FILE LOCATION, ON WINDOWS, REPLACE \ WITH //
sender_email = os.getenv("EMAIL")
sender_password = os.getenv("PASSWORD")
full_name = "Idriss Khaled"
resume_location = "C://Users//idriss//Desktop//Resume//eng//idrissKhaled-resume.pdf"
resume_filename = "idrissKhaled-resume.pdf"
recommendation_letter_location = "C://Users//idriss//Desktop//Resume//eng//ElateUp recommendation letter.pdf"
recommendation_letter_filename = "ElateUp recommendation letter.pdf"
data_location = "C://Users//idriss//Desktop//contacts1.txt"
body_template_with_person_name = "Hello {name},\n\nI am writing to express my enthusiastic interest in joining {company} as a software engineering intern.\n\nAllow me to introduce myself. I am Idriss Khaled, a Tunisian final-year software engineering student pursuing a Master's degree at INSAT and currently looking for a six-month end-of-studies internship starting from February 2024. Throughout my five-year journey in software engineering, I have acquired a comprehensive understanding of software development technologies and best practices. My academic journey has been complemented by active participation in significant projects spanning Data Science, Web development, and Cloud technologies.\n\nDuring my internships and part-time engagements at esteemed companies such as ElateUp and Elyadata, I have contributed to the development of robust and scalable solutions. I take pride in having received recognition for my expertise from both previous employers and co-workers.\n\nPlease find attached my resume along with a letter of recommendation from my most recent employer. I would really appreciate it if you take a look at them and see if my skills and experiences align with your goals.\n\nYours sincerely,\nIdriss Khaled"
body_template_without_person_name = "Dear {company} recrutement team,\n\nI am writing to express my enthusiastic interest in joining {company} as a software engineering intern.\n\nAllow me to introduce myself. I am Idriss Khaled, a Tunisian final-year software engineering student pursuing a Master's degree at INSAT and currently looking for a six-month end-of-studies internship starting from February 2024. Throughout my five-year journey in software engineering, I have acquired a comprehensive understanding of software development technologies and best practices. My academic journey has been complemented by active participation in significant projects spanning Data Science, Web development, and Cloud technologies.\n\nDuring my internships and part-time engagements at esteemed companies such as ElateUp and Elyadata, I have contributed to the development of robust and scalable solutions. I take pride in having received recognition for my expertise from both previous employers and co-workers.\n\nPlease find attached my resume along with a letter of recommendation from my most recent employer. I would really appreciate it if you take a look at them and see if my skills and experiences align with your goals.\n\nYours sincerely,\nIdriss Khaled"


def send_email(to_email, body):
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = full_name + " " + sender_email
    message['To'] = to_email
    message['Subject'] = "Spontaneous Application - Software engineering intern"

    # Attach the body to the email
    message.attach(MIMEText(body, 'plain'))

    # Attach resume

    with open(resume_location, 'rb') as resume_file:
        resume_part = MIMEApplication(resume_file.read(), Name=resume_filename)
        resume_part['Content-Disposition'] = f'attachment; filename="{resume_filename}"'
        message.attach(resume_part)

    # Attach recommendation letter
    with open(recommendation_letter_location, 'rb') as resume_file:
        resume_part = MIMEApplication(resume_file.read(), Name=recommendation_letter_filename)
        resume_part['Content-Disposition'] = f'attachment; filename="{recommendation_letter_filename}"'
        message.attach(resume_part)

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        # Send the email
        server.sendmail(sender_email, to_email, message.as_string())


# Read contact emails from a file
with open(data_location, 'r') as file:
    contacts = file.read().splitlines()

# Iterate through contact emails and send emails
for contact in contacts:
    # Extract the name from the email (you may need to adapt this based on your email format)
    [email, company, name] = contact.split(';')

    # Format the subject and body with the name
    if name == company:
        body = body_template_without_person_name.format(company=company, name=name)
    else:
        body = body_template_with_person_name.format(company=company, name=name)

    # Send the email
    send_email(email, body)
print("Emails sent successfully.")
