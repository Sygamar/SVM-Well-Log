import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('final_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    litho_keys = {0: 30000,
1: 65000,
2: 65030,
3: 70000,
4: 70032,
5: 74000,
6: 80000,
7: 88000,
8: 90000,
9: 99000,
}
    
    litho_result = {
       30000: "Sandstone",
65000: "Shale",
65030: "Sandstone/Shale",
70000: "Limestone",
70032: "Chalk",
74000: "Dolomite",
80000: "Marl",
88000: "Halite",
90000: "Coal",
93000: "Basement",     
   }
    
    int_features = [int(float(x)) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = litho_keys[prediction[0]]
    sediment = litho_result[output]
    sanswer = 'Lithology Number predicted by the model is ' + str(output) + ' and the resulting sedimentary composition is ' + sediment + '.'

    return render_template('index.html', prediction_text=sanswer)


if __name__ == "__main__":
    app.run(debug=True)