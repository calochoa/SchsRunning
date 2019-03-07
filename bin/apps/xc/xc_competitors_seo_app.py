__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


xc_competitors_seo_app = Blueprint(
    'xc_competitors_seo_app', __name__, template_folder='templates', url_prefix='/santa-clara-high-cross-country/competitors'
)    


@xc_competitors_seo_app.route('/<string:competitor_id>',methods=['GET'])
def xcCompetitor(competitor_id):
    competitor_id_parts = competitor_id.split('.')
    if len(competitor_id_parts) == 2:
        runner_id = competitor_id_parts[0]
        grade = competitor_id_parts[1]
        if grade == "12":
            return redirect('/santa-clara-high-cross-country/competitors/Senior/{0}'.format(runner_id))
        elif grade == "11":
            return redirect('/santa-clara-high-cross-country/competitors/Junior/{0}'.format(runner_id))
        elif grade == "10":
            return redirect('/santa-clara-high-cross-country/competitors/Sophomore/{0}'.format(runner_id))
        elif grade == "9":
            return redirect('/santa-clara-high-cross-country/competitors/Freshman/{0}'.format(runner_id))
    return render_template('xc/competitors/competitor.html', competitorId=competitor_id)

@xc_competitors_seo_app.route('/Senior/<string:runner_id>',methods=['GET'])
def xcSeniorCompetitor(runner_id):
    return render_template('xc/competitors/competitor.html', competitorId='{0}.12'.format(runner_id))

@xc_competitors_seo_app.route('/Junior/<string:runner_id>',methods=['GET'])
def xcJuniorCompetitor(runner_id):
    return render_template('xc/competitors/competitor.html', competitorId='{0}.11'.format(runner_id))

@xc_competitors_seo_app.route('/Sophomore/<string:runner_id>',methods=['GET'])
def xcSophomoreCompetitor(runner_id):
    return render_template('xc/competitors/competitor.html', competitorId='{0}.10'.format(runner_id))

@xc_competitors_seo_app.route('/Freshman/<string:runner_id>',methods=['GET'])
def xcFreshmanCompetitor(runner_id):
    return render_template('xc/competitors/competitor.html', competitorId='{0}.9'.format(runner_id))

