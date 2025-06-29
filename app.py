from flask import Flask, render_template, request
from lumi_small import get_lumi_reply

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    user_message = ""
    bot_response = ""
    if request.method == 'POST':
        user_message = request.form['message']
        bot_response = get_lumi_reply(user_message)
    return render_template('chat.html', user_message=user_message, bot_response=bot_response)

if __name__ == '__main__':
    app.run(debug=True)