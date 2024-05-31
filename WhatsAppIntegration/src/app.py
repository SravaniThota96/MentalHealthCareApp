from helper.openai_api import text_complition
from helper.twilio_api import send_message


from flask import Flask, request
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)


@app.route('/')
def home():
    return 'All is well...'


@app.route('/twilio/receiveMessage', methods=['POST'])
def receiveMessage():
    try:
        # Extract incomng parameters from Twilio
        message = request.form['Body']
        sender_id = request.form['From']

        # Get response from Openai
        result = text_complition(message)
        
        send_message(sender_id, result)
    except Exception as e:
        print(f"An error occurred: {e}")
    return 'OK', 200
