__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


bodyweight_exercises_seo_app = Blueprint(
    'bodyweight_exercises_seo_app', __name__, template_folder='templates', url_prefix='/workouts/bodyweight-exercises'
)    


@bodyweight_exercises_seo_app.route('/dropdown-menus/',methods=['GET'])
def dropdown_menus():
    return render_template('workouts/bodyweight-exercises/bodyweight-dropdown-menus.html')

def get_exercises(body_split_ids, exercise_levels):
    return render_template('workouts/bodyweight-exercises/bodyweight-exercises.html', bsIds=body_split_ids, eLevels=exercise_levels)

@bodyweight_exercises_seo_app.route('/', methods=['GET'])
def bodyweight_exercises():
    return render_template('workouts/bodyweight-exercises/bodyweight-exercises.html')


@bodyweight_exercises_seo_app.route('/beginner/', methods=['GET'])
def beginner():
    return get_exercises('all', '1')

@bodyweight_exercises_seo_app.route('/intermediate/', methods=['GET'])
def intermediate():
    return get_exercises('all', '2')

@bodyweight_exercises_seo_app.route('/advanced/', methods=['GET'])
def advanced():
    return get_exercises('all', '3')

@bodyweight_exercises_seo_app.route('/expert/', methods=['GET'])
def expert():
    return get_exercises('all', '4')

@bodyweight_exercises_seo_app.route('/master/', methods=['GET'])
def master():
    return get_exercises('all', '5,6')



@bodyweight_exercises_seo_app.route('/core/', methods=['GET'])
def core():
    return get_exercises('bs0001', 'all')

@bodyweight_exercises_seo_app.route('/core/beginner/', methods=['GET'])
def core_beginner():
    return get_exercises('bs0001', '1')

@bodyweight_exercises_seo_app.route('/core/intermediate/', methods=['GET'])
def core_intermediate():
    return get_exercises('bs0001', '2')

@bodyweight_exercises_seo_app.route('/core/advanced/', methods=['GET'])
def core_advanced():
    return get_exercises('bs0001', '3')

@bodyweight_exercises_seo_app.route('/core/expert/', methods=['GET'])
def core_expert():
    return get_exercises('bs0001', '4')

@bodyweight_exercises_seo_app.route('/core/master/', methods=['GET'])
def core_master():
    return get_exercises('bs0001', '5,6')



@bodyweight_exercises_seo_app.route('/lower-body/', methods=['GET'])
def lower_body():
    return get_exercises('bs0002', 'all')

@bodyweight_exercises_seo_app.route('/lower-body/beginner/', methods=['GET'])
def lower_body_beginner():
    return get_exercises('bs0002', '1')

@bodyweight_exercises_seo_app.route('/lower-body/intermediate/', methods=['GET'])
def lower_body_intermediate():
    return get_exercises('bs0002', '2')

@bodyweight_exercises_seo_app.route('/lower-body/advanced/', methods=['GET'])
def lower_body_advanced():
    return get_exercises('bs0002', '3')

@bodyweight_exercises_seo_app.route('/lower-body/expert/', methods=['GET'])
def lower_body_expert():
    return get_exercises('bs0002', '4')

@bodyweight_exercises_seo_app.route('/lower-body/master/', methods=['GET'])
def lower_body_master():
    return get_exercises('bs0002', '5,6')



@bodyweight_exercises_seo_app.route('/upper-body/', methods=['GET'])
def upper_body():
    return get_exercises('bs0003', 'all')

@bodyweight_exercises_seo_app.route('/upper-body/beginner/', methods=['GET'])
def upper_body_beginner():
    return get_exercises('bs0003', '1')

@bodyweight_exercises_seo_app.route('/upper-body/intermediate/', methods=['GET'])
def upper_body_intermediate():
    return get_exercises('bs0003', '2')

@bodyweight_exercises_seo_app.route('/upper-body/advanced/', methods=['GET'])
def upper_body_advanced():
    return get_exercises('bs0003', '3')

@bodyweight_exercises_seo_app.route('/upper-body/expert/', methods=['GET'])
def upper_body_expert():
    return get_exercises('bs0003', '4')

@bodyweight_exercises_seo_app.route('/upper-body/master/', methods=['GET'])
def upper_body_master():
    return get_exercises('bs0003', '5,6')



@bodyweight_exercises_seo_app.route('/total-body/', methods=['GET'])
def total_body():
    return get_exercises('bs0004', 'all')

@bodyweight_exercises_seo_app.route('/total-body/beginner/', methods=['GET'])
def total_body_beginner():
    return get_exercises('bs0004', '1')

@bodyweight_exercises_seo_app.route('/total-body/intermediate/', methods=['GET'])
def total_body_intermediate():
    return get_exercises('bs0004', '2')

@bodyweight_exercises_seo_app.route('/total-body/advanced/', methods=['GET'])
def total_body_advanced():
    return get_exercises('bs0004', '3')

@bodyweight_exercises_seo_app.route('/total-body/expert/', methods=['GET'])
def total_body_expert():
    return get_exercises('bs0004', '4')

@bodyweight_exercises_seo_app.route('/total-body/master/', methods=['GET'])
def total_body_master():
    return get_exercises('bs0004', '5,6')

