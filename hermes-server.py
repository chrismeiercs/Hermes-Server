from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    return "You have found a Hermes Server."
 
if __name__ == "__main__":
    app.run(debug=True)
