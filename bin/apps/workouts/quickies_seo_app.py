__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


quickies_seo_app = Blueprint(
    'quickies_seo_app', __name__, template_folder='templates', url_prefix='/workouts/quickies'
)    


@quickies_seo_app.route('/dropdown-menus/',methods=['GET'])
def dropdown_menus():
    return render_template('workouts/quickies/quickies-dropdown-menus.html')

def get_quickies(body_split_ids, quickie_levels):
    return render_template('workouts/quickies/quickies.html', bsIds=body_split_ids, qLevels=quickie_levels)


@quickies_seo_app.route('/faq', methods=['GET'])
def faq():
    return render_template('workouts/quickies/quickies-faq.html')

@quickies_seo_app.route('/', methods=['GET'])
def quickies():
    return get_quickies('', '')



@quickies_seo_app.route('/beginner/', methods=['GET'])
def beginner():
    return get_quickies('all', '1')

@quickies_seo_app.route('/intermediate/', methods=['GET'])
def intermediate():
    return get_quickies('all', '2')

@quickies_seo_app.route('/advanced/', methods=['GET'])
def advanced():
    return get_quickies('all', '3')

@quickies_seo_app.route('/expert/', methods=['GET'])
def expert():
    return get_quickies('all', '4')

@quickies_seo_app.route('/master/', methods=['GET'])
def master():
    return get_quickies('all', '5,6')



@quickies_seo_app.route('/core/', methods=['GET'])
def core():
    return get_quickies('bs0001', 'all')

@quickies_seo_app.route('/core/beginner/', methods=['GET'])
def core_beginner():
    return get_quickies('bs0001', '1')

@quickies_seo_app.route('/core/intermediate/', methods=['GET'])
def core_intermediate():
    return get_quickies('bs0001', '2')

@quickies_seo_app.route('/core/advanced/', methods=['GET'])
def core_advanced():
    return get_quickies('bs0001', '3')

@quickies_seo_app.route('/core/expert/', methods=['GET'])
def core_expert():
    return get_quickies('bs0001', '4')

@quickies_seo_app.route('/core/master/', methods=['GET'])
def core_master():
    return get_quickies('bs0001', '5,6')



@quickies_seo_app.route('/lower-body/', methods=['GET'])
def lower_body():
    return get_quickies('bs0002', 'all')

@quickies_seo_app.route('/lower-body/beginner/', methods=['GET'])
def lower_body_beginner():
    return get_quickies('bs0002', '1')

@quickies_seo_app.route('/lower-body/intermediate/', methods=['GET'])
def lower_body_intermediate():
    return get_quickies('bs0002', '2')

@quickies_seo_app.route('/lower-body/advanced/', methods=['GET'])
def lower_body_advanced():
    return get_quickies('bs0002', '3')

@quickies_seo_app.route('/lower-body/expert/', methods=['GET'])
def lower_body_expert():
    return get_quickies('bs0002', '4')

@quickies_seo_app.route('/lower-body/master/', methods=['GET'])
def lower_body_master():
    return get_quickies('bs0002', '5,6')



@quickies_seo_app.route('/upper-body/', methods=['GET'])
def upper_body():
    return get_quickies('bs0003', 'all')

@quickies_seo_app.route('/upper-body/beginner/', methods=['GET'])
def upper_body_beginner():
    return get_quickies('bs0003', '1')

@quickies_seo_app.route('/upper-body/intermediate/', methods=['GET'])
def upper_body_intermediate():
    return get_quickies('bs0003', '2')

@quickies_seo_app.route('/upper-body/advanced/', methods=['GET'])
def upper_body_advanced():
    return get_quickies('bs0003', '3')

@quickies_seo_app.route('/upper-body/expert/', methods=['GET'])
def upper_body_expert():
    return get_quickies('bs0003', '4')

@quickies_seo_app.route('/upper-body/master/', methods=['GET'])
def upper_body_master():
    return get_quickies('bs0003', '5,6')



@quickies_seo_app.route('/total-body/', methods=['GET'])
def total_body():
    return get_quickies('bs0004', 'all')

@quickies_seo_app.route('/total-body/beginner/', methods=['GET'])
def total_body_beginner():
    return get_quickies('bs0004', '1')

@quickies_seo_app.route('/total-body/intermediate/', methods=['GET'])
def total_body_intermediate():
    return get_quickies('bs0004', '2')

@quickies_seo_app.route('/total-body/advanced/', methods=['GET'])
def total_body_advanced():
    return get_quickies('bs0004', '3')

@quickies_seo_app.route('/total-body/expert/', methods=['GET'])
def total_body_expert():
    return get_quickies('bs0004', '4')

@quickies_seo_app.route('/total-body/master/', methods=['GET'])
def total_body_master():
    return get_quickies('bs0004', '5,6')

