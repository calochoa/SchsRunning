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

def get_quickie_workout(workout_name, body_split, workout_level, quickie_ids):
    return render_template(
        'workouts/quickie-workouts/quickie-workout.html', workoutName=workout_name, bodySplit=body_split, 
        workoutLevel=workout_level, qIds=quickie_ids
    )



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




@quickie_workouts_seo_app.route('/total-body/beginner/workout-101', methods=['GET'])
def workout_101():
    return get_quickie_workout('Workout 101', 'Total Body', 'Beginner', 'q00006,q00004,q00003,q00011') 

@quickie_workouts_seo_app.route('/upper-body/beginner/workout-102', methods=['GET'])
def workout_102():
    return get_quickie_workout('Workout 102', 'Upper Body', 'Beginner', 'q00011,q00007,q00006,q00009') 

@quickie_workouts_seo_app.route('/lower-body/beginner/workout-103', methods=['GET'])
def workout_103():
    return get_quickie_workout('Workout 103', 'Lower Body', 'Beginner', 'q00004,q00008,q00010,q00005') 

@quickie_workouts_seo_app.route('/core/beginner/workout-104', methods=['GET'])
def workout_104():
    return get_quickie_workout('Workout 104', 'Core', 'Beginner', 'q00012,q00002,q00003,q00001') 

@quickie_workouts_seo_app.route('/total-body/beginner/workout-105', methods=['GET'])
def workout_105():
    return get_quickie_workout('Workout 105', 'Total Body', 'Beginner', 'q00010,q00003,q00011,q00012') 

@quickie_workouts_seo_app.route('/total-body/beginner/workout-106', methods=['GET'])
def workout_106():
    return get_quickie_workout('Workout 106', 'Total Body', 'Beginner', 'q00004,q00006,q00012,q00010') 

@quickie_workouts_seo_app.route('/upper-body/beginner/workout-107', methods=['GET'])
def workout_107():
    return get_quickie_workout('Workout 107', 'Upper Body', 'Beginner', 'q00009,q03001,q00007,q03002') 

@quickie_workouts_seo_app.route('/total-body/beginner/workout-108', methods=['GET'])
def workout_108():
    return get_quickie_workout('Workout 108', 'Total Body', 'Beginner', 'q00008,q00001,q00004,q00003') 

@quickie_workouts_seo_app.route('/total-body/beginner/workout-109', methods=['GET'])
def workout_109():
    return get_quickie_workout('Workout 109', 'Total Body', 'Beginner', 'q00005,q00002,q00010,q00012') 

@quickie_workouts_seo_app.route('/total-body/beginner/workout-110', methods=['GET'])
def workout_110():
    return get_quickie_workout('Workout 110', 'Total Body', 'Beginner', 'q00007,q00005,q00001,q00012') 

@quickie_workouts_seo_app.route('/total-body/beginner/workout-111', methods=['GET'])
def workout_111():
    return get_quickie_workout('Workout 111', 'Total Body', 'Beginner', 'q00009,q00008,q00002,q00003') 

@quickie_workouts_seo_app.route('/total-body/beginner/workout-112', methods=['GET'])
def workout_112():
    return get_quickie_workout('Workout 112', 'Total Body', 'Beginner', 'q03001,q00005,q00011,q00009') 

@quickie_workouts_seo_app.route('/total-body/beginner/workout-113', methods=['GET'])
def workout_113():
    return get_quickie_workout('Workout 113', 'Total Body', 'Beginner', 'q03002,q00008,q00006,q00007') 

@quickie_workouts_seo_app.route('/total-body/beginner/workout-114', methods=['GET'])
def workout_114():
    return get_quickie_workout('Workout 114', 'Total Body', 'Beginner', 'q03001,q00004,q00005,q00002') 

@quickie_workouts_seo_app.route('/total-body/beginner/workout-115', methods=['GET'])
def workout_115():
    return get_quickie_workout('Workout 115', 'Total Body', 'Beginner', 'q03002,q00010,q00008,q00001') 

@quickie_workouts_seo_app.route('/total-body/intermediate/workout-201', methods=['GET'])
def workout_201():
    return get_quickie_workout('Workout 201', 'Total Body', 'Intermediate', 'q00006,q00004,q00003,q00011,q02011,q02002,q01001,q02010') 

@quickie_workouts_seo_app.route('/upper-body/intermediate/workout-202', methods=['GET'])
def workout_202():
    return get_quickie_workout('Workout 202', 'Upper Body', 'Intermediate', 'q00011,q00007,q00006,q00009,q02010,q01017,q02011,q01014') 

@quickie_workouts_seo_app.route('/lower-body/intermediate/workout-203', methods=['GET'])
def workout_203():
    return get_quickie_workout('Workout 203', 'Lower Body', 'Intermediate', 'q00004,q00008,q00010,q00005,q02002,q02001,q02013,q01003') 

@quickie_workouts_seo_app.route('/core/intermediate/workout-204', methods=['GET'])
def workout_204():
    return get_quickie_workout('Workout 204', 'Core', 'Intermediate', 'q00012,q00002,q00003,q00001,q02012,q01009,q01001,q01002') 

@quickie_workouts_seo_app.route('/total-body/intermediate/workout-205', methods=['GET'])
def workout_205():
    return get_quickie_workout('Workout 205', 'Total Body', 'Intermediate', 'q00010,q00003,q00011,q00012,q02013,q01001,q02010,q02012') 

@quickie_workouts_seo_app.route('/total-body/intermediate/workout-206', methods=['GET'])
def workout_206():
    return get_quickie_workout('Workout 206', 'Total Body', 'Intermediate', 'q00004,q00006,q00012,q00010,q02002,q02011,q02012,q02013') 

@quickie_workouts_seo_app.route('/upper-body/intermediate/workout-207', methods=['GET'])
def workout_207():
    return get_quickie_workout('Workout 207', 'Upper Body', 'Intermediate', 'q00009,q03001,q00007,q03002,q01014,q03009,q01017,q03003') 

@quickie_workouts_seo_app.route('/total-body/intermediate/workout-208', methods=['GET'])
def workout_208():
    return get_quickie_workout('Workout 208', 'Total Body', 'Intermediate', 'q00008,q00001,q00004,q00003,q02001,q01002,q02002,q01001') 

@quickie_workouts_seo_app.route('/total-body/intermediate/workout-209', methods=['GET'])
def workout_209():
    return get_quickie_workout('Workout 209', 'Total Body', 'Intermediate', 'q00005,q00002,q00010,q00012,q01003,q01009,q02013,q02012') 

@quickie_workouts_seo_app.route('/total-body/intermediate/workout-210', methods=['GET'])
def workout_210():
    return get_quickie_workout('Workout 210', 'Total Body', 'Intermediate', 'q00007,q00005,q00001,q00012,q01017,q01003,q01002,q02012') 

@quickie_workouts_seo_app.route('/total-body/intermediate/workout-211', methods=['GET'])
def workout_211():
    return get_quickie_workout('Workout 211', 'Total Body', 'Intermediate', 'q00009,q00008,q00002,q00003,q01014,q02001,q01009,q01001') 

@quickie_workouts_seo_app.route('/total-body/intermediate/workout-212', methods=['GET'])
def workout_212():
    return get_quickie_workout('Workout 212', 'Total Body', 'Intermediate', 'q03001,q00005,q00011,q00009,q03009,q01003,q02010,q01014') 

@quickie_workouts_seo_app.route('/total-body/intermediate/workout-213', methods=['GET'])
def workout_213():
    return get_quickie_workout('Workout 213', 'Total Body', 'Intermediate', 'q03002,q00008,q00006,q00007,q03003,q02001,q02011,q01017') 

@quickie_workouts_seo_app.route('/total-body/intermediate/workout-214', methods=['GET'])
def workout_214():
    return get_quickie_workout('Workout 214', 'Total Body', 'Intermediate', 'q03001,q00004,q00005,q00002,q03009,q02002,q01003,q01009') 

@quickie_workouts_seo_app.route('/total-body/intermediate/workout-215', methods=['GET'])
def workout_215():
    return get_quickie_workout('Workout 215', 'Total Body', 'Intermediate', 'q03002,q00010,q00008,q00001,q03003,q02013,q02001,q01002') 

@quickie_workouts_seo_app.route('/total-body/advanced/workout-301', methods=['GET'])
def workout_301():
    return get_quickie_workout('Workout 301', 'Total Body', 'Advanced', 'q00006,q00004,q00003,q00011,q02011,q02002,q01001,q02010,q02004,q02016,q01004,q01008') 

@quickie_workouts_seo_app.route('/upper-body/advanced/workout-302', methods=['GET'])
def workout_302():
    return get_quickie_workout('Workout 302', 'Upper Body', 'Advanced', 'q00011,q00007,q00006,q00009,q02010,q01017,q02011,q01014,q01008,q01016,q02004,q01015') 

@quickie_workouts_seo_app.route('/lower-body/advanced/workout-303', methods=['GET'])
def workout_303():
    return get_quickie_workout('Workout 303', 'Lower Body', 'Advanced', 'q00004,q00008,q00010,q00005,q02002,q02001,q02013,q01003,q02016,q01013,q02015,q02005') 

@quickie_workouts_seo_app.route('/core/advanced/workout-304', methods=['GET'])
def workout_304():
    return get_quickie_workout('Workout 304', 'Core', 'Advanced', 'q00012,q00002,q00003,q00001,q02012,q01009,q01001,q01002,q02014,q01010,q01004,q01005') 

@quickie_workouts_seo_app.route('/total-body/advanced/workout-305', methods=['GET'])
def workout_305():
    return get_quickie_workout('Workout 305', 'Total Body', 'Advanced', 'q00010,q00003,q00011,q00012,q02013,q01001,q02010,q02012,q02015,q01004,q01008,q02014') 

@quickie_workouts_seo_app.route('/total-body/advanced/workout-306', methods=['GET'])
def workout_306():
    return get_quickie_workout('Workout 306', 'Total Body', 'Advanced', 'q00004,q00006,q00012,q00010,q02002,q02011,q02012,q02013,q02016,q02004,q02014,q02015') 

@quickie_workouts_seo_app.route('/upper-body/advanced/workout-307', methods=['GET'])
def workout_307():
    return get_quickie_workout('Workout 307', 'Upper Body', 'Advanced', 'q00009,q03001,q00007,q03002,q01014,q03009,q01017,q03003,q01015,q03004,q01016,q03005') 

@quickie_workouts_seo_app.route('/total-body/advanced/workout-308', methods=['GET'])
def workout_308():
    return get_quickie_workout('Workout 308', 'Total Body', 'Advanced', 'q00008,q00001,q00004,q00003,q02001,q01002,q02002,q01001,q01013,q01005,q02016,q01004') 

@quickie_workouts_seo_app.route('/total-body/advanced/workout-309', methods=['GET'])
def workout_309():
    return get_quickie_workout('Workout 309', 'Total Body', 'Advanced', 'q00005,q00002,q00010,q00012,q01003,q01009,q02013,q02012,q02005,q01010,q02015,q02014') 

@quickie_workouts_seo_app.route('/total-body/advanced/workout-310', methods=['GET'])
def workout_310():
    return get_quickie_workout('Workout 310', 'Total Body', 'Advanced', 'q00007,q00005,q00001,q00012,q01017,q01003,q01002,q02012,q01016,q02005,q01005,q02014') 

@quickie_workouts_seo_app.route('/total-body/advanced/workout-311', methods=['GET'])
def workout_311():
    return get_quickie_workout('Workout 311', 'Total Body', 'Advanced', 'q00009,q00008,q00002,q00003,q01014,q02001,q01009,q01001,q01015,q01013,q01010,q01004') 

@quickie_workouts_seo_app.route('/total-body/advanced/workout-312', methods=['GET'])
def workout_312():
    return get_quickie_workout('Workout 312', 'Total Body', 'Advanced', 'q03001,q00005,q00011,q00009,q03009,q01003,q02010,q01014,q03004,q02005,q01008,q01015') 

@quickie_workouts_seo_app.route('/total-body/advanced/workout-313', methods=['GET'])
def workout_313():
    return get_quickie_workout('Workout 313', 'Total Body', 'Advanced', 'q03002,q00008,q00006,q00007,q03003,q02001,q02011,q01017,q03005,q01013,q02004,q01016') 

@quickie_workouts_seo_app.route('/total-body/advanced/workout-314', methods=['GET'])
def workout_314():
    return get_quickie_workout('Workout 314', 'Total Body', 'Advanced', 'q03001,q00004,q00005,q00002,q03009,q02002,q01003,q01009,q03004,q02016,q02005,q01010') 

@quickie_workouts_seo_app.route('/total-body/advanced/workout-315', methods=['GET'])
def workout_315():
    return get_quickie_workout('Workout 315', 'Total Body', 'Advanced', 'q03002,q00010,q00008,q00001,q03003,q02013,q02001,q01002,q03005,q02015,q01013,q01005') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-401', methods=['GET'])
def workout_401():
    return get_quickie_workout('Workout 401', 'Total Body', 'Expert', 'q00006,q00004,q00003,q00011,q02008,q02011,q02004,q02016,q02002,q01008,q02010,q02007') 

@quickie_workouts_seo_app.route('/upper-body/expert/workout-402', methods=['GET'])
def workout_402():
    return get_quickie_workout('Workout 402', 'Upper Body', 'Expert', 'q00011,q00007,q00006,q00009,q01007,q01017,q02017,q01016,q01015,q02008,q01014,q01006') 

@quickie_workouts_seo_app.route('/lower-body/expert/workout-403', methods=['GET'])
def workout_403():
    return get_quickie_workout('Workout 403', 'Lower Body', 'Expert', 'q00004,q00008,q00010,q00005,q02009,q02001,q02008,q01013,q02005,q02007,q01003,q02006') 

@quickie_workouts_seo_app.route('/core/expert/workout-404', methods=['GET'])
def workout_404():
    return get_quickie_workout('Workout 404', 'Core', 'Expert', 'q00012,q00002,q00003,q00001,q01011,q01009,q02003,q01010,q01005,q02007,q01002,q01012') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-405', methods=['GET'])
def workout_405():
    return get_quickie_workout('Workout 405', 'Total Body', 'Expert', 'q00010,q00003,q00011,q00012,q03008,q01001,q02017,q01004,q02014,q02003,q02012,q03010') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-406', methods=['GET'])
def workout_406():
    return get_quickie_workout('Workout 406', 'Total Body', 'Expert', 'q00004,q00006,q00012,q00010,q02017,q02002,q02016,q02004,q02011,q02015,q02013,q02003') 

@quickie_workouts_seo_app.route('/upper-body/expert/workout-407', methods=['GET'])
def workout_407():
    return get_quickie_workout('Workout 407', 'Upper Body', 'Expert', 'q00009,q03001,q00007,q03002,q03006,q03009,q03004,q01007,q03005,q01006,q03003,q03007') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-408', methods=['GET'])
def workout_408():
    return get_quickie_workout('Workout 408', 'Total Body', 'Expert', 'q00008,q00001,q00004,q00003,q02009,q01002,q02007,q01004,q01013,q01012,q02002,q03007') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-409', methods=['GET'])
def workout_409():
    return get_quickie_workout('Workout 409', 'Total Body', 'Expert', 'q00005,q00002,q00010,q00012,q02006,q01009,q02017,q02014,q02005,q01011,q02013,q03006') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-410', methods=['GET'])
def workout_410():
    return get_quickie_workout('Workout 410', 'Total Body', 'Expert', 'q00007,q00005,q00001,q00012,q01007,q01003,q01012,q02014,q01016,q02006,q01002,q03006') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-411', methods=['GET'])
def workout_411():
    return get_quickie_workout('Workout 411', 'Total Body', 'Expert', 'q00009,q00008,q00002,q00003,q01006,q02001,q01011,q01004,q01015,q02009,q01009,q03007') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-412', methods=['GET'])
def workout_412():
    return get_quickie_workout('Workout 412', 'Total Body', 'Expert', 'q03001,q00005,q00011,q00009,q03010,q01003,q02003,q01015,q03004,q02006,q02010,q01006') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-413', methods=['GET'])
def workout_413():
    return get_quickie_workout('Workout 413', 'Total Body', 'Expert', 'q03002,q00008,q00006,q00007,q03008,q02001,q02008,q01016,q03005,q02009,q02011,q01007') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-414', methods=['GET'])
def workout_414():
    return get_quickie_workout('Workout 414', 'Total Body', 'Expert', 'q03001,q00004,q00005,q00002,q03010,q02002,q02006,q01010,q03004,q02007,q01003,q01011') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-415', methods=['GET'])
def workout_415():
    return get_quickie_workout('Workout 415', 'Total Body', 'Expert', 'q03002,q00010,q00008,q00001,q03008,q02013,q02009,q01005,q03005,q02017,q02001,q01012') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-416', methods=['GET'])
def workout_416():
    return get_quickie_workout('Workout 416', 'Total Body', 'Expert', 'q00008,q00001,q00004,q00003,q02005,q00006,q03006,q01001,q04001,q02004,q01004,q03003') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-417', methods=['GET'])
def workout_417():
    return get_quickie_workout('Workout 417', 'Total Body', 'Expert', 'q00005,q00002,q00004,q00003,q02008,q00007,q03004,q01006,q04003,q02003,q01005,q03001') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-418', methods=['GET'])
def workout_418():
    return get_quickie_workout('Workout 418', 'Total Body', 'Expert', 'q00008,q00001,q00004,q00003,q02007,q00006,q03008,q01003,q04001,q02002,q01007,q03002') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-419', methods=['GET'])
def workout_419():
    return get_quickie_workout('Workout 419', 'Total Body', 'Expert', 'q00005,q00002,q00004,q00003,q02006,q00007,q03007,q01002,q04002,q02001,q01008,q03005') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-420', methods=['GET'])
def workout_420():
    return get_quickie_workout('Workout 420', 'Total Body', 'Expert', 'q00008,q00001,q00004,q00006,q02008,q03003,q02006,q01007,q02004,q03005,q02001,q01003') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-421', methods=['GET'])
def workout_421():
    return get_quickie_workout('Workout 421', 'Total Body', 'Expert', 'q00005,q00002,q00003,q00007,q02007,q03004,q02005,q01004,q02004,q03007,q02002,q01001') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-422', methods=['GET'])
def workout_422():
    return get_quickie_workout('Workout 422', 'Total Body', 'Expert', 'q00008,q00001,q00004,q00006,q02008,q03002,q02005,q01005,q02003,q03008,q02002,q01006') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-423', methods=['GET'])
def workout_423():
    return get_quickie_workout('Workout 423', 'Total Body', 'Expert', 'q00005,q00002,q00003,q00007,q02007,q03001,q02006,q01002,q02003,q03006,q02001,q01008') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-424', methods=['GET'])
def workout_424():
    return get_quickie_workout('Workout 424', 'Total Body', 'Expert', 'q00008,q00001,q00004,q00003,q04002,q02001,q01005,q02004,q01003,q01002,q01008,q02007') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-425', methods=['GET'])
def workout_425():
    return get_quickie_workout('Workout 425', 'Total Body', 'Expert', 'q00005,q00002,q00004,q00003,q04001,q02002,q01006,q02005,q01001,q01004,q02003,q02006') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-426', methods=['GET'])
def workout_426():
    return get_quickie_workout('Workout 426', 'Total Body', 'Expert', 'q00005,q00002,q00004,q00003,q02002,q01006,q02005,q02006,q02001,q01003,q01008,q02007') 

@quickie_workouts_seo_app.route('/total-body/expert/workout-427', methods=['GET'])
def workout_427():
    return get_quickie_workout('Workout 427', 'Total Body', 'Expert', 'q00008,q00001,q00004,q00003,q04001,q01001,q02004,q01002,q04002,q01004,q02003,q01005') 

@quickie_workouts_seo_app.route('/total-body/master/workout-501', methods=['GET'])
def workout_501():
    return get_quickie_workout('Workout 501', 'Total Body', 'Master', 'q00006,q00004,q00003,q00011,q04006,q02004,q02008,q02007,q02016,q02003,q01008,q04002') 

@quickie_workouts_seo_app.route('/upper-body/master/workout-502', methods=['GET'])
def workout_502():
    return get_quickie_workout('Workout 502', 'Upper Body', 'Master', 'q00011,q00007,q00006,q00009,q04012,q01016,q04008,q01007,q01006,q04006,q01015,q04004') 

@quickie_workouts_seo_app.route('/lower-body/master/workout-503', methods=['GET'])
def workout_503():
    return get_quickie_workout('Workout 503', 'Lower Body', 'Master', 'q00004,q00008,q00010,q00005,q04011,q01013,q04002,q02009,q02006,q04014,q02005,q04010') 

@quickie_workouts_seo_app.route('/core/master/workout-504', methods=['GET'])
def workout_504():
    return get_quickie_workout('Workout 504', 'Core', 'Master', 'q00012,q00002,q00003,q00001,q04001,q01010,q04013,q01011,q01012,q04002,q01005,q04009') 

@quickie_workouts_seo_app.route('/total-body/master/workout-505', methods=['GET'])
def workout_505():
    return get_quickie_workout('Workout 505', 'Total Body', 'Master', 'q00010,q00003,q00011,q00012,q04007,q01004,q04014,q03008,q03010,q04008,q02014,q04013') 

@quickie_workouts_seo_app.route('/total-body/master/workout-506', methods=['GET'])
def workout_506():
    return get_quickie_workout('Workout 506', 'Total Body', 'Master', 'q00004,q00006,q00012,q00010,q04014,q02016,q02007,q02008,q02004,q02017,q02015,q04008') 

@quickie_workouts_seo_app.route('/upper-body/master/workout-507', methods=['GET'])
def workout_507():
    return get_quickie_workout('Workout 507', 'Upper Body', 'Master', 'q00009,q03001,q00007,q03002,q04012,q03004,q03006,q04005,q03007,q04003,q03005,q04004') 

@quickie_workouts_seo_app.route('/total-body/master/workout-508', methods=['GET'])
def workout_508():
    return get_quickie_workout('Workout 508', 'Total Body', 'Master', 'q00008,q00001,q00004,q00003,q04011,q01005,q04002,q03007,q02009,q04009,q02016,q04007') 

@quickie_workouts_seo_app.route('/total-body/master/workout-509', methods=['GET'])
def workout_509():
    return get_quickie_workout('Workout 509', 'Total Body', 'Master', 'q00005,q00002,q00010,q00012,q04010,q01010,q04014,q03006,q02006,q04001,q02015,q04013') 

@quickie_workouts_seo_app.route('/total-body/master/workout-510', methods=['GET'])
def workout_510():
    return get_quickie_workout('Workout 510', 'Total Body', 'Master', 'q00007,q00005,q00001,q00012,q04012,q02005,q04009,q03006,q01007,q04010,q01005,q04013') 

@quickie_workouts_seo_app.route('/total-body/master/workout-511', methods=['GET'])
def workout_511():
    return get_quickie_workout('Workout 511', 'Total Body', 'Master', 'q00009,q00008,q00002,q00003,q04004,q01013,q04001,q03007,q01006,q04011,q01010,q04007') 

@quickie_workouts_seo_app.route('/total-body/master/workout-512', methods=['GET'])
def workout_512():
    return get_quickie_workout('Workout 512', 'Total Body', 'Master', 'q03001,q00005,q00011,q00009,q04005,q02005,q04008,q01006,q03010,q04010,q01008,q04004') 

@quickie_workouts_seo_app.route('/total-body/master/workout-513', methods=['GET'])
def workout_513():
    return get_quickie_workout('Workout 513', 'Total Body', 'Master', 'q03002,q00008,q00006,q00007,q04003,q01013,q04006,q01007,q03008,q04011,q02004,q04012') 

@quickie_workouts_seo_app.route('/total-body/master/workout-514', methods=['GET'])
def workout_514():
    return get_quickie_workout('Workout 514', 'Total Body', 'Master', 'q03001,q00004,q00005,q00002,q04005,q02016,q04010,q01011,q03010,q04002,q02005,q04001') 

@quickie_workouts_seo_app.route('/total-body/master/workout-515', methods=['GET'])
def workout_515():
    return get_quickie_workout('Workout 515', 'Total Body', 'Master', 'q03002,q00010,q00008,q00001,q04003,q02015,q04011,q01012,q03008,q04014,q01013,q04009') 

@quickie_workouts_seo_app.route('/total-body/master/workout-516', methods=['GET'])
def workout_516():
    return get_quickie_workout('Workout 516', 'Total Body', 'Master', 'q00008,q00001,q00004,q00006,q04008,q03001,q02004,q01007,q04001,q01001,q03006,q02005') 

@quickie_workouts_seo_app.route('/total-body/master/workout-517', methods=['GET'])
def workout_517():
    return get_quickie_workout('Workout 517', 'Total Body', 'Master', 'q00005,q00002,q00003,q00007,q04007,q03004,q01003,q01006,q04003,q02002,q03005,q02006') 

@quickie_workouts_seo_app.route('/total-body/master/workout-518', methods=['GET'])
def workout_518():
    return get_quickie_workout('Workout 518', 'Total Body', 'Master', 'q00008,q00001,q00004,q00006,q04006,q03003,q01008,q01005,q04002,q02001,q03008,q02007') 

@quickie_workouts_seo_app.route('/total-body/master/workout-519', methods=['GET'])
def workout_519():
    return get_quickie_workout('Workout 519', 'Total Body', 'Master', 'q00005,q00002,q00003,q00007,q04005,q03002,q02003,q01004,q04004,q01002,q03007,q02008')

