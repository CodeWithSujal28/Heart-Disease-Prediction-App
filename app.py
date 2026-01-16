from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('KNN_Heart.pkl')
scaler = joblib.load('scaler.pkl')
columns = joblib.load('columns.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        input_data = []

        for col in columns:
            value = float(request.form[col])
            input_data.append(value)

        input_array = np.array(input_data).reshape(1, -1)
        scaled_input = scaler.transform(input_array)
        result = model.predict(scaled_input)[0]

        prediction = "❤️ Heart Disease Detected" if result == 1 else "✅ No Heart Disease Detected"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
