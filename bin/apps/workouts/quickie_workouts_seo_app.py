__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


quickie_workouts_seo_app = Blueprint(
    'quickie_workouts_seo_app', __name__, template_folder='templates', url_prefix='/workouts/quickie-workouts'
)    


@quickie_workouts_seo_app.route('/dropdown-menus/',methods=['GET'])
def dropdown_menus():
    return render_template('workouts/quickie-workouts/quickie-workouts-dropdown-menus.html')

def get_quickie_workouts(body_split_ids, workout_levels):
    return render_template('workouts/quickie-workouts/quickie-workouts.html', bsIds=body_split_ids, wLevels=workout_levels)


@quickie_workouts_seo_app.route('/faq', methods=['GET'])
def faq():
    return render_template('workouts/quickie-workouts/quickie-workouts-faq.html')

@quickie_workouts_seo_app.route('/', methods=['GET'])
def quickie_workouts():
    return get_quickie_workouts('', '')



@quickie_workouts_seo_app.route('/beginner/', methods=['GET'])
def beginner():
    return get_quickie_workouts('all', '1')

@quickie_workouts_seo_app.route('/intermediate/', methods=['GET'])
def intermediate():
    return get_quickie_workouts('all', '2')

@quickie_workouts_seo_app.route('/advanced/', methods=['GET'])
def advanced():
    return get_quickie_workouts('all', '3')

@quickie_workouts_seo_app.route('/expert/', methods=['GET'])
def expert():
    return get_quickie_workouts('all', '4')

@quickie_workouts_seo_app.route('/master/', methods=['GET'])
def master():
    return get_quickie_workouts('all', '5')



@quickie_workouts_seo_app.route('/core/', methods=['GET'])
def core():
    return get_quickie_workouts('bs0001', 'all')

@quickie_workouts_seo_app.route('/core/beginner/', methods=['GET'])
def core_beginner():
    return get_quickie_workouts('bs0001', '1')

@quickie_workouts_seo_app.route('/core/intermediate/', methods=['GET'])
def core_intermediate():
    return get_quickie_workouts('bs0001', '2')

@quickie_workouts_seo_app.route('/core/advanced/', methods=['GET'])
def core_advanced():
    return get_quickie_workouts('bs0001', '3')

@quickie_workouts_seo_app.route('/core/expert/', methods=['GET'])
def core_expert():
    return get_quickie_workouts('bs0001', '4')

@quickie_workouts_seo_app.route('/core/master/', methods=['GET'])
def core_master():
    return get_quickie_workouts('bs0001', '5')



@quickie_workouts_seo_app.route('/lower-body/', methods=['GET'])
def lower_body():
    return get_quickie_workouts('bs0002', 'all')

@quickie_workouts_seo_app.route('/lower-body/beginner/', methods=['GET'])
def lower_body_beginner():
    return get_quickie_workouts('bs0002', '1')

@quickie_workouts_seo_app.route('/lower-body/intermediate/', methods=['GET'])
def lower_body_intermediate():
    return get_quickie_workouts('bs0002', '2')

@quickie_workouts_seo_app.route('/lower-body/advanced/', methods=['GET'])
def lower_body_advanced():
    return get_quickie_workouts('bs0002', '3')

@quickie_workouts_seo_app.route('/lower-body/expert/', methods=['GET'])
def lower_body_expert():
    return get_quickie_workouts('bs0002', '4')

@quickie_workouts_seo_app.route('/lower-body/master/', methods=['GET'])
def lower_body_master():
    return get_quickie_workouts('bs0002', '5')



@quickie_workouts_seo_app.route('/upper-body/', methods=['GET'])
def upper_body():
    return get_quickie_workouts('bs0003', 'all')

@quickie_workouts_seo_app.route('/upper-body/beginner/', methods=['GET'])
def upper_body_beginner():
    return get_quickie_workouts('bs0003', '1')

@quickie_workouts_seo_app.route('/upper-body/intermediate/', methods=['GET'])
def upper_body_intermediate():
    return get_quickie_workouts('bs0003', '2')

@quickie_workouts_seo_app.route('/upper-body/advanced/', methods=['GET'])
def upper_body_advanced():
    return get_quickie_workouts('bs0003', '3')

@quickie_workouts_seo_app.route('/upper-body/expert/', methods=['GET'])
def upper_body_expert():
    return get_quickie_workouts('bs0003', '4')

@quickie_workouts_seo_app.route('/upper-body/master/', methods=['GET'])
def upper_body_master():
    return get_quickie_workouts('bs0003', '5')



@quickie_workouts_seo_app.route('/total-body/', methods=['GET'])
def total_body():
    return get_quickie_workouts('bs0004', 'all')

@quickie_workouts_seo_app.route('/total-body/beginner/', methods=['GET'])
def total_body_beginner():
    return get_quickie_workouts('bs0004', '1')

@quickie_workouts_seo_app.route('/total-body/intermediate/', methods=['GET'])
def total_body_intermediate():
    return get_quickie_workouts('bs0004', '2')

@quickie_workouts_seo_app.route('/total-body/advanced/', methods=['GET'])
def total_body_advanced():
    return get_quickie_workouts('bs0004', '3')

@quickie_workouts_seo_app.route('/total-body/expert/', methods=['GET'])
def total_body_expert():
    return get_quickie_workouts('bs0004', '4')

@quickie_workouts_seo_app.route('/total-body/master/', methods=['GET'])
def total_body_master():
    return get_quickie_workouts('bs0004', '5')

