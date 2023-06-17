from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/home.html')
def home():
    return render_template('index.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/about.html')
def blog():
    return render_template('about.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_file(data)
        return redirect('thankyou.html')
    return "something went wrong ! Please try again !"

def write_to_file(data):
    with open('database.txt',mode='a') as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        db.write(f'\n {email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv',mode='a') as db2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(db2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(f'\n {email}, {subject}, {message}')

# return render_template('login.html',error=error)
@app.route('/login',methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'

    return render_template('login.html', error=error)



