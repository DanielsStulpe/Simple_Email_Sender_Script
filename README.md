# Email Sender Script

This script allows you to send emails to multiple recipients using SMTP with a Gmail account. It reads email addresses from a specified database file and the email content from another file.

## Features
- Reads recipient email addresses from a file.
- Reads email content from a separate file.
- Sends emails via Gmail SMTP.
- Handles exceptions for missing files and email sending errors.

## Prerequisites

### Python Packages Required
Ensure you have Python installed and install the required dependencies using:
```sh
pip install -r requirements.txt
```

### Gmail SMTP Configuration
Make sure to enable "Less Secure Apps" or use an App Password for authentication if needed.

## Setup
1. Clone or download this script.
2. Ensure you have a `user_login.py` file that contains the following:
   ```python
   email = "your_email@gmail.com"
   password_key = "your_email_password_key"
   ```
3. Create a text file (e.g., `database.txt`) with recipient email addresses (one per line).
4. Create another text file (e.g., `content.txt`) with the message body.
5. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the script from the terminal:
```sh
python main.py <database_file> <content_file>
```
Example:
```sh
python main.py database.txt content.txt
```

## Script Breakdown
- `read_file(file_path)`: Reads and returns the content of a file.
- `send_email(recipients, content, subject)`: Sends an email to the recipients.
- `main()`: Handles command-line arguments and initiates the email-sending process.

## Error Handling
- If a file is missing, an error message is displayed, and the script exits.
- If sending an email fails, an error message is printed with the recipient's email.

## Security Note
Do **not** store sensitive credentials in plain text. Use environment variables or a secure secrets manager.

## License
This script is provided "as is" without warranty. Use at your own risk.

## Author
Daniels Stulpe
