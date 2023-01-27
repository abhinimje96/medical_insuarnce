from flask import Flask, render_template, jsonify, request
import config1
from utils import MedicalInsurance
import traceback

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/medicalinsurance/predict')
def predict():
    try:
        data = request.args.get

        print('Data :::', data)
        age = int(data('age'))
        gender = data('gender')
        bmi = eval(data('bmi'))
        children = int(data('children'))
        smoker = data('smoker')
        region = data('region')

        med_ins = MedicalInsurance(age, gender, bmi, children, smoker, region)
        charges = med_ins.get_predicted_price()

        # return jsonify({'Result': f'The Charges for medical insurance {charges}'})
        return render_template('index.html', prediction = charges)
    except:
        print(traceback.print_exc())
        return jsonify({"Message":"Unsuccessful"})

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = config1.PORT_NUMBER, debug = True)
