from flask import Flask, render_template, request
import packing_logic

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_packing_list', methods=['POST'])
def get_packing_list():
    destination = request.form['destination']
    travel_dates = request.form['travel_dates']
    activities = request.form['activities'].split(',')  # Input as comma-separated
    packing_list = packing_logic.generate_packing_list(destination, travel_dates, activities)
    return render_template('result.html', packing_list=packing_list)

if __name__ == '__main__':
    app.run(debug=True)
