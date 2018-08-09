from flask import *
import mlab
from models.video import Video
from youtube_dl import YoutubeDL
app = Flask(__name__)

app.secret_key = 'a secrey key'

mlab.connect()

@app.route('/', methods = ["GET", "POST"])
def index():
    videos = Video.objects()
    return render_template('index.html', videos = videos)

@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']

        # user = User.objects(username = username, password = password)

        # if user is not None

        if username == 'admin' and password == 'admin':
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            return "sai ten dang nhap hc mk"


@app.route('/detail/<youtubeid>')
def detail(youtubeid):
    return render_template('detail.html', youtubeid = youtubeid)

@app.route('/logout')
def logout():
    del session['logged_in']
    return redirect(url_for('index'))

@app.route('/admin', methods = ["GET", "POST"])
def admin():
    # check key in dictionary
    if 'logged_in' in session: 
        if session['logged_in']:
            if request.method == "GET":
                videos = Video.objects()
                return render_template('admin.html', videos = videos)
            elif request.method == "POST":
                form = request.form
                link = form['link']
                ydl = YoutubeDL()
                data = ydl.extract_info(link,download = False)
            
                title = data['title']
                views = data['view_count']
                thumbnail = data['thumbnail']
                youtubeid = data['id']

                new_video = Video (
                    title = title,
                    views = views,
                    linkyoutube = link,
                    thumbnail = thumbnail,
                    youtubeid = youtubeid
                )
                new_video.save()
                return redirect(url_for('admin'))
    else:
        return "di cho khac"
if __name__ == '__main__':
  app.run(debug=True)
 

