from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('final_classification_model.pkl', 'rb'))




@app.route('/', methods=['GET','POST'])
def predict():
        if request.method == 'GET':
                return render_template('index.html')
        else:
                plot_text_list = request.form.to_dict()
                plot_text = plot_text_list['plot_text']
                genre_prediction_text = model.predict([plot_text])

                return render_template('index.html', prediction_text='For the plot description:<br><br>' + plot_text + '<br><br>The predicted genre is ' + genre_prediction_text[0])

if __name__ == '__main__':
    app.run(debug=True)
