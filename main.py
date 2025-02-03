import smtplib
import sys
from email.message import EmailMessage
from user_login import email, password_key

def read_recipients(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            recipients = []
            for recipient in file.read().splitlines():
                if recipient not in recipients:
                    recipients.append(recipient)
            return recipients   # Returns a list of lines
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(1)


def read_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = ""
            for line in file:
                content += line
            return content
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)


def send_email(recipients, content, subject):
    """Sends an email using SMTP."""
    gmail_server = "smtp.gmail.com"
    gmail_port = 587

    try:
        # Start connection
        my_server = smtplib.SMTP(gmail_server, gmail_port)
        my_server.ehlo()
        my_server.starttls()
        
        # Login with your email and password
        my_server.login(email, password_key)
        
        for recipient in recipients:
            msg = EmailMessage()
            msg.set_content(content)
            msg['Subject'] = subject
            msg['From'] = email
            msg['To'] = recipient
            # Sending mail
            my_server.send_message(msg)
            print(f'Mail sent to {recipient}')

        my_server.quit()
        print("Finished sending emails")
        
    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")


def main():
    """Main function to handle command-line arguments."""
    if len(sys.argv) != 3:
        print("Usage: python main.py <database_file> <content_file>")
        sys.exit(1)

    database_file = sys.argv[1]
    content_file = sys.argv[2]

    recipients = read_recipients(database_file)  # Read recipient emails
    content = read_content(content_file)  # Read content as a string

    subject = "Test mail"

    if (input(f"Start sending emails to {len(recipients)} recipients. Y/n : ") == "Y"):
        send_email(recipients, content, subject)
    else:
        sys.exit(2)


if __name__ == "__main__":
    main()
