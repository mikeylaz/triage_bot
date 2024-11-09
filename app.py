# app.py
from flask import Flask, request, jsonify, render_template
from conversation_handler import get_response, get_initial_greeting

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    initial_message = get_initial_greeting()
    return render_template('index.html', initial_message=initial_message)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)