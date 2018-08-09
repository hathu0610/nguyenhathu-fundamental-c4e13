from flask import Flask, render_template,request
app = Flask(__name__)
from models.user import User
from models.service import Service

import mlab

mlab.connect()

@app.route('/')
def search():
    all_service = Service.objects()
    return render_template('search.html', all_service = all_service)


@app.route('/sign-in', methods = ["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template('signin.html')
    elif request.method == "POST":
        form = request.form
        fullname = form['fullname']
        email = form['email']
        username = form['username']
        password = form['password']
        
        new_user = User(
            fullname = fullname,
            email = email,
            username = username,
            password = password
        )
        new_user.save()
        return "Đăng kí đc rồi nha ^^"


if __name__ == '__main__':
  app.run(debug=True)
 