from flask import Flask, flash, redirect, render_template, request, session, abort, send_from_directory, url_for
from flask_mail import Mail, Message
from app.config import configure_app
import os

app = Flask(__name__, 
    instance_path=os.path.join(os.path.dirname(os.path.realpath(__file__)),'instance'),
    instance_relative_config=True,
    template_folder='templates')

configure_app(app)
mail = Mail(app)

def email_us(name, email, message):
    try:
        msg = Message("New Form Submitted from ({},{})".format(name, email),
                     recipients=["littlesucculentstudio@gmail.com"],
                     body="""{} has submitted a contact form: 
                            Name: {}
                            Email: {}
                            Message: {}
                            """.format(name, name, email, message))
        mail.send(msg)
        return "Mail Sent!"
    except Exception as e:
        return str(e)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contactus", methods=["POST"])
def contact_us():
    if request.method == "POST":
        return email_us(request.form['name'], request.form['email'], request.form['message'])
    return redirect(url_for('index')) 
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

