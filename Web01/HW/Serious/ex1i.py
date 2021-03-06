# without
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight,height):
    bmi = round((weight/(height*height))*10000)
    if bmi < 16:
        content = "Severely underweight"
    elif 16 <= bmi < 18.5:
        content =  "Underweight"
    elif 18.5 <= bmi < 25: 
        content = "Normal"
    elif 25 <= bmi < 30: 
        content = "Overweight"
    else: 
        content = "Obese"
    return "Your bmi is {0} and you are {1}".format(bmi, content)

if __name__ == '__main__':
  app.run(debug=True)
 