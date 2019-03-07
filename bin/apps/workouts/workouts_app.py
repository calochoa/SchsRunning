__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template


workouts_app = Blueprint('workouts_app', __name__, template_folder='templates')


@workouts_app.route('/workouts')
def main_workouts():
    return render_template('workouts/index.html')

