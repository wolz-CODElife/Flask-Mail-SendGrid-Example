# SendGrid Email Sender - Flask App

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.0%2B-green)
[![Flask_mail](https://img.shields.io/badge/Flask__mail-Official%20Library-orange)](https://pythonhosted.org/Flask-Mail/)

This is a simple Flask application for sending emails using the SendGrid service. It provides a basic API endpoint that allows you to send emails by making a POST request with recipient details. You can easily integrate this into your own projects.

## 📦 Features

- Send emails using SendGrid.
- Simple API endpoint for sending emails.
- Easily customizable for your specific use cases.

## 📚 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## 🛠️ Installation

To set up and run this application locally, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/wolz-CODElife/Flask-Mail-SendGrid-Example.git
   cd Flask-Mail-SendGrid-Example
   ```
2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Set your SendGrid API key and default sender email as environment variables or create a `.env` file. You can obtain your [SendGrid API key](https://docs.sendgrid.com/ui/account-and-settings/api-keys) by signing up for a SendGrid account.
    ```bash
    export SENDGRID_API_KEY='your_sendgrid_api_key'
    export MAIL_DEFAULT_SENDER='your_sender_email'
    ```
5. Run the Flask application:
    ```bash
    flask run
    ```

The application should now be running locally at http://localhost:5000.

## 🚀 Usage
To send an email using this Flask app, make a `POST` request to the `/` endpoint with a JSON payload containing the recipient's email address. Here's an example using curl:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"recipient": "recipient@example.com"}' http://localhost:5000/
```

You can modify the email subject, body, and HTML content in the Flask app code to suit your specific needs.

## 🤝 Contributing
Contributions are welcome! 

If you'd like to contribute to this project, please follow these guidelines:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them.
4. Commit your changes with descriptive commit messages.
5. Push your changes to your fork.
6. Create a pull request to the main repository's main branch.

Please make sure to follow the GitHub's [contribution guidelines](https://github.com/github/docs/blob/main/CONTRIBUTING.md).

## 🛡️ License
This project is licensed under the MIT License - see the [LICENSE file](https://github.com/wolz-CODElife/Flask-Mail-SendGrid-Example/blob/master/LICENSE) for details.