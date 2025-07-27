from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_city():
    city_input = request.form['city'].strip().lower()

    with open('citywise_disease_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['City'].strip().lower() == city_input:
                return render_template(
                    'map.html',
                    city=row['City'],
                    lat=row['Latitude'],
                    lon=row['Longitude'],
                    status=row['Status']
                )

    return "City not found. Please go back and try again."

if __name__ == '__main__':
    app.run(debug=True)
