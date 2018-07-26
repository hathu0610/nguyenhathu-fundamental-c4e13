from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def index(username):
    users = {
        "quan" : {
                "name": "Nguyen Anh Quan",
                "age": 16,
                "gender": "male"
        },
        "tuananh" : { 
                "name": "Huynh Tuan Anh",
                "age": 23,
                "gender": "male"

        },
        "hathu": {
            "name": "Nguyen Ha Thu",
            "age": 16,
            "gender": "female"
        }
    }
    if username in users.keys():
        boo = True
    else:
        boo = False
    

    return render_template('ex2.html', alluser = users, username = username, boo = boo)

if __name__ == '__main__':
  app.run(debug=True)
 