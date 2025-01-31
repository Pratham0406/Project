from flask import Flask, render_template, request
import packing_logic  # Ensure this module exists and works correctly

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/index.html')
def submit():
    return render_template('index.html')

@app.route('/get_packing_list', methods=['POST'])
def get_packing_list():
    destination = request.form.get('destination', '')  # Avoid KeyError
    date = request.form.get('date', '')  # Handle missing date safely
    activities = request.form.get('activities', '')  # Handle missing activities safely
    activity_list = [activity.strip() for activity in activities.split(',')] if activities else []  # Remove spaces

    packing_list = packing_logic.generate_packing_list(destination, date, activity_list)
    return render_template('result.html', packing_list=packing_list)  # Removed extra space in filename

if __name__ == '__main__':
    app.run(debug=True)
