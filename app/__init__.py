from flask import Flask, flash, redirect, render_template, request, session, abort, send_from_directory
from flask_mail import Mail
from app.config import configure_app
import os

app = Flask(__name__, 
    static_url_path='', 
    instance_path=os.path.join(os.path.dirname(os.path.realpath(__file__)),'instance'),
    instance_relative_config=True)

mail = Mail(app)
configure_app(app)

def email_us():
    msg = Message("Hello",
                 recipients=["littlesucculentstudio@gmail.com"],
                 body="hello")
    mail.send(msg)

@app.route("/")
def index():
    return send_from_directory('', "index.html")

@app.route("/contactus/", methods=["POST"])
def contact_us():
    if request.method == "POST":
        email_us()
    return redirect(url_for('index')) 
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

