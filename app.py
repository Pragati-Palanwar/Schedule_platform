from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_wtf.csrf import CSRFProtect
from forms import AvailabilityForm

app = Flask(__name__, static_url_path='/static')


app.config['SECRET_KEY'] = 'random_string'
csrf = CSRFProtect(app)


appointments = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/availability', methods=['GET', 'POST'])
def availability():
    form = AvailabilityForm()
    if request.method == 'POST' and form.validate_on_submit():
        start_time = form.start_time.data
        end_time = form.end_time.data
        appointments.append({'start_time': start_time, 'end_time': end_time})
        return jsonify({'message': 'Appointment scheduled successfully!'})
    return render_template('availability.html', form=form)

@app.route('/appointments')
def get_appointments():
    return jsonify(appointments)

if __name__ == '__main__':
    app.run(debug=True)
