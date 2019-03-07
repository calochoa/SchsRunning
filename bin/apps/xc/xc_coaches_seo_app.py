__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


xc_coaches_seo_app = Blueprint(
    'xc_coaches_seo_app', __name__, template_folder='templates', url_prefix='/santa-clara-high-cross-country/coaches'
)    


@xc_coaches_seo_app.route('/timeline',methods=['GET'])
def xcCoachesTimeline():
    return render_template('xc/coaches/coachTimeline.html')

@xc_coaches_seo_app.route('/',methods=['GET'])
def xcCoaches():
    return render_template('xc/coaches/coaches.html')

def getXcCoachData(coach_id):
    return render_template('xc/coaches/coach.html', coachId=coach_id)

@xc_coaches_seo_app.route('/<int:coach_id>',methods=['GET'])
def xcCoach(coach_id):
    if coach_id == 1:
        return redirect('/santa-clara-high-cross-country/coaches/julie-lheureux')
    elif coach_id == 2:
        return redirect('/santa-clara-high-cross-country/coaches/cal-ochoa')
    elif coach_id == 6:
        return redirect('/santa-clara-high-cross-country/coaches/jamie-vierling')
    elif coach_id == 7:
        return redirect('/santa-clara-high-cross-country/coaches/mario-bouza')
    return getXcCoachData(coach_id)

@xc_coaches_seo_app.route('/julie-lheureux',methods=['GET'])
def xcCoachJulieLHeureux():
    return getXcCoachData(1)

@xc_coaches_seo_app.route('/cal-ochoa',methods=['GET'])
def xcCoachCalOchoa():
    return getXcCoachData(2)

@xc_coaches_seo_app.route('/jamie-vierling',methods=['GET'])
def xcCoachJamieVierling():
    return getXcCoachData(6)

@xc_coaches_seo_app.route('/mario-bouza',methods=['GET'])
def xcCoachMarioBouza():
    return getXcCoachData(7)


