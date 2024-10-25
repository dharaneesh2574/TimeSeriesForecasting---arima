from flask import Flask, jsonify, request
import pickle
from datetime import datetime, timedelta

app = Flask(__name__)

with open('arima.pkl', 'rb') as file:
    arima_model = pickle.load(file)

last_date = datetime.strptime("2020-02-03", "%Y-%m-%d")

@app.route('/forecast', methods=['GET'])
def forecast():
    try:
        steps = int(request.args.get('steps', 5))
        forecast_values = arima_model.forecast(steps=steps)
        future_dates = [(last_date + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(1, steps + 1)]
        response = {
            'forecast': [{'date': date, 'value': value} for date, value in zip(future_dates, forecast_values)]
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)