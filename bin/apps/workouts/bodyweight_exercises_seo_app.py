__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


bodyweight_exercises_seo_app = Blueprint(
    'bodyweight_exercises_seo_app', __name__, template_folder='templates', url_prefix='/workouts/bodyweight-exercises'
)    


@bodyweight_exercises_seo_app.route('/dropdown-menus',methods=['GET'])
def dropdown_menus():
    return render_template('workouts/bodyweight-exercises/bodyweight-dropdown-menus.html')

def get_exercises(body_split_id, exercise_levels, title):
    return render_template('workouts/bodyweight-exercises/bodyweight-exercises.html', bsId=body_split_id, eLevels=exercise_levels, title=title)

@bodyweight_exercises_seo_app.route('/', methods=['GET'])
def bodyweight_exercises():
    return render_template('workouts/bodyweight-exercises/bodyweight-exercises.html', title='Bodyweight Exercises')

@bodyweight_exercises_seo_app.route('/core', methods=['GET'])
def core():
    return get_exercises('bs0001', '1,2,3,4,5,6', title='Core')

@bodyweight_exercises_seo_app.route('/lower-body', methods=['GET'])
def lower_body():
    return get_exercises('bs0002', '1,2,3,4,5,6', title='Lower Body')

@bodyweight_exercises_seo_app.route('/upper-body', methods=['GET'])
def upper_body():
    return get_exercises('bs0003', '1,2,3,4,5,6', title='Upper Body')

@bodyweight_exercises_seo_app.route('/total-body', methods=['GET'])
def total_body():
    return get_exercises('bs0004', '1,2,3,4,5,6', title='Total Body')


@bodyweight_exercises_seo_app.route('/beginner', methods=['GET'])
def beginner(difficulty=None):
    return get_exercises('bs0001,bs0002,bs0003,bs0004', '1', title='Beginner')

@bodyweight_exercises_seo_app.route('/intermediate', methods=['GET'])
def intermediate(difficulty=None):
    return get_exercises('bs0001,bs0002,bs0003,bs0004', '2', title='Intermediate')

@bodyweight_exercises_seo_app.route('/advanced', methods=['GET'])
def advanced(difficulty=None):
    return get_exercises('bs0001,bs0002,bs0003,bs0004', '3', title='Advanced')

@bodyweight_exercises_seo_app.route('/expert', methods=['GET'])
def expert(difficulty=None):
    return get_exercises('bs0001,bs0002,bs0003,bs0004', '4', title='Expert')

@bodyweight_exercises_seo_app.route('/master', methods=['GET'])
def master(difficulty=None):
    return get_exercises('bs0001,bs0002,bs0003,bs0004', '5,6', title='Master')

