from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts = [
        {
        "title": "Thơ con cóc",
        "content": "Hôm nay trăng lên cao quá Anh muốn hôn em vào má",
        "author": "tuan anh"
        "gender": 1
    },
    {
        "title": "Thu",
        "content": "Thu xinh",
        "author": "Thu xinhh",
        "gender": 0
    }
    ]
   
    return render_template(
        "index.html",
        allposts = posts
        )

@app.route('/hello')
def hello():
    return "<h1>hello c4e19</h1>"

@app.route('/say-hi/<name>/<age>')
def sayhi(name, age): 
    return "Hi {0} you're {1} years old".format(name,age)

@app.route('/sum/<int:x>/<int:y>')
def sum(x, y):
    z = x+y
    return str(z)

if __name__ == '__main__':
  app.run(debug=True)
 