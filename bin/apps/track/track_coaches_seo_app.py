__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


track_coaches_seo_app = Blueprint(
    'track_coaches_seo_app', __name__, template_folder='templates', url_prefix='/santa-clara-high-track-and-field/coaches'
)    


@track_coaches_seo_app.route('/timeline',methods=['GET'])
def track_coaches_timeline():
    return render_template('track/coaches/coachTimeline.html', coachTypeIds='3,4,5,6,7,8,9')

@track_coaches_seo_app.route('/',methods=['GET'])
def track_coaches():
    return render_template('track/coaches/coaches.html', coachTypeIds='3,4,5,6,7,8,9')

def get_track_coach_data(coach_id):
    return render_template('track/coaches/coach.html', coachId=coach_id, coachTypeIds='3,4,5,6,7,8,9')

@track_coaches_seo_app.route('/<int:coach_id>',methods=['GET'])
def track_coach(coach_id):
    if coach_id == 1:
        return redirect('/santa-clara-high-track-and-field/coaches/julie-lheureux')
    elif coach_id == 2:
        return redirect('/santa-clara-high-track-and-field/coaches/cal-ochoa')
    elif coach_id == 100:
        return redirect('/santa-clara-high-track-and-field/coaches/chuck-kappen')
    elif coach_id == 101:
        return redirect('/santa-clara-high-track-and-field/coaches/margaret-demorest')
    elif coach_id == 102:
        return redirect('/santa-clara-high-track-and-field/coaches/paul-fuller')
    elif coach_id == 103:
        return redirect('/santa-clara-high-track-and-field/coaches/darrin-garcia')
    return get_track_coach_data(coach_id)

@track_coaches_seo_app.route('/julie-lheureux',methods=['GET'])
def track_coach_julie_lheureux():
    return get_track_coach_data(1)

@track_coaches_seo_app.route('/cal-ochoa',methods=['GET'])
def track_coach_cal_ochoa():
    return get_track_coach_data(2)

@track_coaches_seo_app.route('/chuck-kappen',methods=['GET'])
def track_coach_chuck_kappen():
    return get_track_coach_data(100)

@track_coaches_seo_app.route('/margaret-demorest',methods=['GET'])
def track_coach_margaret_demorest():
    return get_track_coach_data(101)

@track_coaches_seo_app.route('/paul-fuller',methods=['GET'])
def track_coach_paul_fuller():
    return get_track_coach_data(102)

@track_coaches_seo_app.route('/darrin-garcia',methods=['GET'])
def track_coach_darrin_garcia():
    return get_track_coach_data(103)

