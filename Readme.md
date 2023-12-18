# Email Sender Script

## What Does This Script Do?

This script iterates over a data file and sends an email for each line. The line format should be: `{email};{companyName};{personName}`. If `personName` is different from `companyName`, the script sends the email with the body template `body_template_with_person_name`; otherwise, it uses the `body_template_without_person_name`.

## How to Run the Script

1. Prepare your contacts data in a file. Each line should follow the format `{email};{companyName};{personName}`. If you don't have the person's name, repeat the `companyName` in the `personName` field.

2. Generate an app password at [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).

3. Change the global variables at the top of the script with your information.

4. Create a .env file in the root and place your email credentials in it.

5. Install the script dependencies. 
```
pip install requirements.txt
```
6. Run the script.
