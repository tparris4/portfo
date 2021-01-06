from flask import Flask, request
from flask import Flask, render_template, url_for, redirect
import csv
app = Flask(__name__)

#decorater -> higher level of abstraction from the framework (flask)
#@app.route('/<username>/<int:post_id>')
#def hello_world(username=None, post_id=None):
 #   return render_template('index.html', name=username, post_id=post_id)

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimeter=',', quotechar='|', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, try again'
   


#@app.route('/work.html')
#def work():
 #   return render_template('work.html')

#@app.route('/works.html')
#def works():
 #   return render_template('works.html')


#@app.route('/contact.html')
#def works():
  #  return render_template('contact.html')

#@app.route('/about.html')
#def blog():
 #   return 'These are my thoughts on blog!'



@app.route('/blog/2020/dogs')
def blog2():
    return 'This is my dog'
