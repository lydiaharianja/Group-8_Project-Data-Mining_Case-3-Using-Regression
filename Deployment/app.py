from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Memuat model
model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

# Fungsi untuk merender halaman utama
@app.route('/')
def index():
    return render_template('templates/Web Application.html', case=0)

@app.route('/predict', methods=['POST'])
def predict():
    PNK09, PNK10, PNK11, PNK16, PNK17, PNKI18 = [x for x in request.form.values()]

    data = []

    data.append(object(PNK09))
    data.append(object(PNK10))
    data.append(object(PNK11))
    data.append(object(PNK16))
    data.append(int64(PNK17))
    data.append(int64(PNK18))

    prediction = model.predict([data])
    output = object(prediction[0])
    output = int64(prediction[0])
    
    return render_template('templates/Web Application.html', case=output, PNK09=PNK09, PNK10=PNK10, PNK11=PNK11, PNK16=PNK16, PNK17=PNK17, PNK18=PNK18)

if __name__ == '__main__':
    app.run(debug=True)
