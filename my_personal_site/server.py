from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

e_mail = "k.robak1993@gmail.com"
password = "dndssmadhdkbvsvi"
second_mail = "kamil.robak93@interia.pl"


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form
        sendmail(data["name"], data["email"], data["message"])
        return render_template("index.html", msg_sent=True)
    return render_template("index.html", msg_sent=False)


def sendmail(name, email, message):
    msg = EmailMessage()
    msg.set_content(f'New message from: {name}, e-mail: {email}, \n Message is: \n {message}')

    msg['Subject'] = 'New contact from CV website'
    msg['From'] = e_mail
    msg['To'] = second_mail

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(user=e_mail, password=password)
    server.send_message(msg)
    server.quit()


if __name__ == "__main__":
    app.run(debug=True)



