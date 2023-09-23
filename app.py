import os
from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wagmi$@#'
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'apikey' #All sendgrid accounts most use 'apikey' as username
app.config['MAIL_PASSWORD'] = os.environ.get('SENDGRID_API_KEY')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')
mail = Mail(app)

@app.route('/', methods=['POST'])
def send_email():
    json_data = request.get_json()
    if not json_data:
        return jsonify({'message': 'Invalid JSON data in the request'}), 400
    
    recipient = json_data.get('recipient')
    if not recipient:
        return jsonify({'message': 'Recipient email is required'}), 400
    name = json_data.get('name')
    docid = json_data.get('id')

    try:
        msg = Message('EMAIL SUBJECT GOES HERE', recipients=[recipient])
        msg.body = ('THIS IS THE BODY')
        msg.html = ('<h1>HTML CONTENT HERE</h1>')
        mail.send(msg)
        response_message = 'Email sent successfully'
        status_code = 200
    except Exception as e:
        response_message = f'Error sending email: {str(e)}'
        status_code = 500
        
    return jsonify({'message': response_message}), status_code

if __name__ == '__main__':
    app.run(debug=True)
