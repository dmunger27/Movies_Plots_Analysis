import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
model = pickle.load(open('final_classification_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    final_features = request.form.values()
    prediction = model.predict(final_features)
    output = prediction[0]

    return render_template('index.html', prediction_text='The predicted genre should be {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)