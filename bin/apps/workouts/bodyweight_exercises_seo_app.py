__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


bodyweight_exercises_seo_app = Blueprint(
    'bodyweight_exercises_seo_app', __name__, template_folder='templates', url_prefix='/workouts/bodyweight-exercises'
)    


@bodyweight_exercises_seo_app.route('/', methods=['GET'])
def bodyweight_exercises():
    return render_template('workouts/bodyweight-exercises/bodyweight-exercises.html')

