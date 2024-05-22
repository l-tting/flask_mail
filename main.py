from flask import Flask,render_template,request,flash,redirect,url_for
from flask_mail import Mail,Message

app = Flask(__name__)
app.secret_key = 'ufjjf8839003nbnfj'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS']= False
app.config['MAIL_USE_SSL']= True
app.config['MAIL_USERNAME'] = 'brianletting01@gmail.com'
app.config['MAIL_DEFAULT_SENDER'] = 'brianletting01@gmail.com'
app.config['MAIL_PASSWORD'] = 'tmlr uehu ftjs pyky'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send',methods =['GET','POST'])
def send():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        msg = Message(subject,sender=email,recipients=['brianletting01@gmail.com'])
        msg.body = f'from {email}\n\n{message}'
        try:
            mail.send(msg)
            flash('Email sent successfully!')
        except Exception as e:
            flash(f'Failed to send email. Error: {str(e)}')

        return redirect(url_for('index'))
app.run(debug=True)