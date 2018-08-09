from flask import *
# from mongoengine import *
import mlab
from datetime import *
from models.service import Service
from models.customer import Customer
from models.user import User
from models.order import Order
from flask_mail import Message
app = Flask(__name__)
app.secret_key = 'a secrey key'
mlab.connect()

# design database


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<g>')
def search(g):
    all_service = Service.objects(gender=g, yob__lte=1999, address__exact = "ha noi")
    return render_template('search.html', all_service = all_service)

@app.route('/search')
def anothersearch():
    all_service = Service.objects()
    return render_template('search.html', all_service = all_service)

@app.route('/detail/<service_id>')
def detail(service_id):
    if 'logged_in' in session: 
        if session['logged_in']:
            service = Service.objects.with_id(service_id)
            return render_template('detail.html', service = service)
    else:
        return redirect(url_for('login'))


@app.route('/customer')
def customer():
    all_customer = Customer.objects()
    return render_template('customer.html', all_customer = all_customer)

@app.route('/customernotcontact')
def customernotcontact():
    ten_customer = Customer.objects(gender = 1, contacted = False)[:10]
    return render_template('customer.html', all_customer = ten_customer)

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template("admin.html", all_service = all_service)

@app.route('/delete/<service_id>')
def delete(service_id):
    service = Service.objects.with_id(service_id)
    if service is not None:
        service.delete()
        return redirect(url_for('admin'))
    else:
        return "Service not found"

@app.route('/new-service', methods = ["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template('new-service.html')
    elif request.method == "POST":
        form = request.form 
        name = form['name']
        yob = form['yob']

        gender = form['gender']


        new_service = Service(
            name = name,
            yob = yob,

            gender = gender
        )
        new_service.save()

        return redirect(url_for('admin'))

@app.route('/update-service/<service_id>', methods = ["GET", "POST"])
def updatenew(service_id):
    if request.method == "GET":
        service = Service.objects.with_id(service_id)
        
        return render_template('update-service.html', service_id = service)

    elif request.method == "POST":
        form = request.form 
        name = form['name']
        yob = form['yob']

        gender = form['gender']

        service = Service.objects.with_id(service_id)
        service['name'] = name
        service['yob'] = yob
        service['gender'] = gender
        service.save()

        return redirect(url_for('admin'))



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
        return redirect(url_for('anothersearch'))

@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']

        users = User.objects(username = username, password = password)


        if not users:
            return "Sai tên đăng nhập hoặc mk rồi nha"
        else:
            session['user_name'] = username
            session['logged_in'] = True
            return redirect(url_for('anothersearch'))

@app.route('/servicerequest/<service_id>')
def servicerequest(service_id):

    currentime= datetime.now()

    userid = session.get('user_name')

    service_req = Order (
        serviceid = service_id,
        userid = userid,
        currentime = currentime,
        is_accepted= False
    )

    service_req.save()
    return "Đã gửi yêu cầu!"   

@app.route('/logout')
def logout():
    del session['logged_in']
    return redirect(url_for('index'))

@app.route('/order/')
def order():
    orders = Order.objects(is_accepted = False)
    the_list = []

    for order in orders:
        service_id = order['serviceid']
        user_id = order['userid']
        service = Service.objects.with_id(service_id)
        user = User.objects(username = user_id).first()
        the_key = {
        "servicename" : service['name'], 
        "username" : user['fullname'],
        "time" : order['currentime'].replace(second=0, microsecond=0),
        "orderid": order['id']
        }
        the_list.append(the_key)
    
    return render_template('order.html', the_list = the_list)

@app.route('/accept/<orderid>')
def accept(orderid):
    order = Order.objects.with_id(orderid)
    order['is_accepted'] = True
    order.save()
    return redirect(url_for('order'))
      
if __name__ == '__main__':
  app.run(debug=True)
 