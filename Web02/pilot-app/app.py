from flask import *
# from mongoengine import *
import mlab
from models.service import Service
from models.customer import Customer
app = Flask(__name__)

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
    service = Service.objects.with_id(service_id)
    return render_template('detail.html', service = service)


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

if __name__ == '__main__':
  app.run(debug=True)
 