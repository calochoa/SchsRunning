__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


xc_race_results_seo_app = Blueprint(
    'xc_race_results_seo_app', __name__, template_folder='templates', url_prefix='/santa-clara-high-cross-country/race-results'
)    


def getXcRaceResultsData(race_id, gender_id=0):
    return render_template('xc/race-results/raceResults.html', raceId=race_id, genderId=gender_id)

@xc_race_results_seo_app.route('/<int:race_id>/<int:gender_id>',methods=['GET'])
def xcRaceResults(race_id, gender_id):
    if race_id == 100000:
        return redirect('/santa-clara-high-cross-country/race-results/1st-annual-crystal-springs-alumni-race-2012/')
    elif race_id == 100001:
        return redirect('/santa-clara-high-cross-country/race-results/2nd-annual-crystal-springs-alumni-race-2013/')
    elif race_id == 100002:
        return redirect('/santa-clara-high-cross-country/race-results/3rd-annual-crystal-springs-alumni-race-2014/')
    elif race_id == 100003:
        return redirect('/santa-clara-high-cross-country/race-results/4th-annual-crystal-springs-alumni-race-2015/')
    elif race_id == 100004:
        return redirect('/santa-clara-high-cross-country/race-results/5th-annual-crystal-springs-alumni-race-2016/')
    elif race_id == 100005:
        return redirect('/santa-clara-high-cross-country/race-results/6th-annual-crystal-springs-alumni-race-2017/')
    elif race_id == 100006:
        return redirect('/santa-clara-high-cross-country/race-results/7th-annual-crystal-springs-alumni-race-2018/')
    elif gender_id == 2:
        return redirect('/santa-clara-high-cross-country/race-results/boys/{0}'.format(race_id))
    elif gender_id == 3:
        return redirect('/santa-clara-high-cross-country/race-results/girls/{0}'.format(race_id))
    return getXcRaceResultsData(race_id, gender_id)

@xc_race_results_seo_app.route('/boys/<int:race_id>',methods=['GET'])
def xcBoysRaceResults(race_id):
    return getXcRaceResultsData(race_id, 2)

@xc_race_results_seo_app.route('/girls/<int:race_id>',methods=['GET'])
def xcGirlsRaceResults(race_id):
    return getXcRaceResultsData(race_id, 3)

@xc_race_results_seo_app.route('/1st-annual-crystal-springs-alumni-race-2012/',methods=['GET'])
def xc1stAnnualCrystalSpringsAlumniRace():
    return getXcRaceResultsData(100000)

@xc_race_results_seo_app.route('/2nd-annual-crystal-springs-alumni-race-2013/',methods=['GET'])
def xc2ndAnnualCrystalSpringsAlumniRace():
    return getXcRaceResultsData(100001)

@xc_race_results_seo_app.route('/3rd-annual-crystal-springs-alumni-race-2014/',methods=['GET'])
def xc3rdAnnualCrystalSpringsAlumniRace():
    return getXcRaceResultsData(100002)

@xc_race_results_seo_app.route('/4th-annual-crystal-springs-alumni-race-2015/',methods=['GET'])
def xc4thAnnualCrystalSpringsAlumniRace():
    return getXcRaceResultsData(100003)

@xc_race_results_seo_app.route('/5th-annual-crystal-springs-alumni-race-2016/',methods=['GET'])
def xc5thAnnualCrystalSpringsAlumniRace():
    return getXcRaceResultsData(100004)

@xc_race_results_seo_app.route('/6th-annual-crystal-springs-alumni-race-2017/',methods=['GET'])
def xc6thAnnualCrystalSpringsAlumniRace():
    return getXcRaceResultsData(100005)

@xc_race_results_seo_app.route('/7th-annual-crystal-springs-alumni-race-2018/',methods=['GET'])
def xc7thAnnualCrystalSpringsAlumniRace():
    return getXcRaceResultsData(100006)



