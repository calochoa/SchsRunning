__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


track_competitors_seo_app = Blueprint(
    'track_competitors_seo_app', __name__, template_folder='templates', url_prefix='/santa-clara-high-track-and-field/competitors'
)    


@track_competitors_seo_app.route('/<string:competitor_id>',methods=['GET'])
def trackCompetitor(competitor_id):
    competitor_id_parts = competitor_id.split('.')
    if len(competitor_id_parts) == 2:
        athlete_id = competitor_id_parts[0]
        grade = competitor_id_parts[1]
        if grade == "12":
            return redirect('/santa-clara-high-track-and-field/competitors/Senior/{0}'.format(athlete_id))
        elif grade == "11":
            return redirect('/santa-clara-high-track-and-field/competitors/Junior/{0}'.format(athlete_id))
        elif grade == "10":
            return redirect('/santa-clara-high-track-and-field/competitors/Sophomore/{0}'.format(athlete_id))
        elif grade == "9":
            return redirect('/santa-clara-high-track-and-field/competitors/Freshman/{0}'.format(athlete_id))
    return render_template('track/competitors/competitor.html', competitorId=competitor_id)

@track_competitors_seo_app.route('/Senior/<string:athlete_id>',methods=['GET'])
def trackSeniorCompetitor(athlete_id):
    return render_template('track/competitors/competitor.html', competitorId='{0}.12'.format(athlete_id))

@track_competitors_seo_app.route('/Junior/<string:athlete_id>',methods=['GET'])
def trackJuniorCompetitor(athlete_id):
    return render_template('track/competitors/competitor.html', competitorId='{0}.11'.format(athlete_id))

@track_competitors_seo_app.route('/Sophomore/<string:athlete_id>',methods=['GET'])
def trackSophomoreCompetitor(athlete_id):
    return render_template('track/competitors/competitor.html', competitorId='{0}.10'.format(athlete_id))

@track_competitors_seo_app.route('/Freshman/<string:athlete_id>',methods=['GET'])
def trackFreshmanCompetitor(athlete_id):
    return render_template('track/competitors/competitor.html', competitorId='{0}.9'.format(athlete_id))

