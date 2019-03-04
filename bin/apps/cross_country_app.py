__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template


cross_country_app = Blueprint('cross_country_app', __name__, template_folder='templates')


@cross_country_app.route('/xc')
def main_xc():
    return render_template('xc/index.html')


@cross_country_app.route('/xcTopCourseResults')
def xcTopCourseResults():
    return render_template('xc/topCourseResults.html', cId = 0, gId = 0, limit = 0)


@cross_country_app.route('/xcResults')
def xcResults():
    return render_template('xc/results.html')    


@cross_country_app.route('/xcTop25CsGirls')
def xcTop25CsGirls():
    return render_template('xc/topCourseResults.html', cId = 1, gId = 3, limit = 25)


@cross_country_app.route('/xcTop25CsBoys')
def xcTop25CsBoys():
    return render_template('xc/topCourseResults.html', cId = 1, gId = 2, limit = 25)


@cross_country_app.route('/xcTop25TpGirls')
def xcTop25TpGirls():
    return render_template('xc/topCourseResults.html', cId = 2, gId = 3, limit = 25)


@cross_country_app.route('/xcTop25TpBoys')
def xcTop25TpBoys():
    return render_template('xc/topCourseResults.html', cId = 2, gId = 2, limit = 25)


@cross_country_app.route('/xcTop25CpGirls')
def xcTop25CpGirls():
    return render_template('xc/topCourseResults.html', cId = 6, gId = 3, limit = 25)


@cross_country_app.route('/xcTop25CpBoys')
def xcTop25CpBoys():
    return render_template('xc/topCourseResults.html', cId = 6, gId = 2, limit = 25)


@cross_country_app.route('/xcTop25BpGirls')
def xcTop25BpGirls():
    return render_template('xc/topCourseResults.html', cId = 4, gId = 3, limit = 25)


@cross_country_app.route('/xcTop25BpBoys')
def xcTop25BpBoys():
    return render_template('xc/topCourseResults.html', cId = 4, gId = 2, limit = 25)


@cross_country_app.route('/xcTop25LynHsGirls')
def xcTop25LynHsGirls():
    return render_template('xc/topCourseResults.html', cId = 25, gId = 3, limit = 25)


@cross_country_app.route('/xcTop25LynHsBoys')
def xcTop25LynHsBoys():
    return render_template('xc/topCourseResults.html', cId = 25, gId = 2, limit = 25)


@cross_country_app.route('/xcTop25CsTeamGirls')
def xcTop25CsTeamGirls():
    return render_template('xc/teamCourseResults.html', cId = 1, gId = 3, limit = 15)


@cross_country_app.route('/xcTop25CsTeamBoys')
def xcTop25CsTeamBoys():
    return render_template('xc/teamCourseResults.html', cId = 1, gId = 2, limit = 15)


@cross_country_app.route('/xcTop25TpTeamGirls')
def xcTop25TpTeamGirls():
    return render_template('xc/teamCourseResults.html', cId = 2, gId = 3, limit = 15)


@cross_country_app.route('/xcTop25TpTeamBoys')
def xcTop25TpTeamBoys():
    return render_template('xc/teamCourseResults.html', cId = 2, gId = 2, limit = 15)


@cross_country_app.route('/xcTop25CpTeamGirls')
def xcTop25CpTeamGirls():
    return render_template('xc/teamCourseResults.html', cId = 6, gId = 3, limit = 15)


@cross_country_app.route('/xcTop25CpTeamBoys')
def xcTop25CpTeamBoys():
    return render_template('xc/teamCourseResults.html', cId = 6, gId = 2, limit = 15)


@cross_country_app.route('/xcTop25BpTeamGirls')
def xcTop25BpTeamGirls():
    return render_template('xc/teamCourseResults.html', cId = 4, gId = 3, limit = 15)


@cross_country_app.route('/xcTop25BpTeamBoys')
def top25BpTeamBoys():
    return render_template('xc/teamCourseResults.html', cId = 4, gId = 2, limit = 15)


@cross_country_app.route('/xcMRunners')
def xcMRunners():
    return render_template('xc/runners.html', gId = 2)


@cross_country_app.route('/xcFRunners')
def xcFRunners():
    return render_template('xc/runners.html', gId = 3)


@cross_country_app.route('/xcRunner')
def xcRunner():
    return render_template('xc/runner.html')


@cross_country_app.route('/xcSeason',methods=['GET'])
def xcSeason():
    return render_template('xc/season.html')


@cross_country_app.route('/xcCompetitor',methods=['GET'])
def xcCompetitor():
    return render_template('xc/competitor.html')


@cross_country_app.route('/xcRaceResults',methods=['GET'])
def xcRaceResults():
    return render_template('xc/raceResults.html')


@cross_country_app.route('/xcCoachTimeline',methods=['GET'])
def xcCoachTimeline():
    return render_template('xc/coachTimeline.html')


@cross_country_app.route('/xcCoach',methods=['GET'])
def xcCoach():
    return render_template('xc/coach.html')


@cross_country_app.route('/xcCoaches',methods=['GET'])
def xcCoaches():
    return render_template('xc/coaches.html')


@cross_country_app.route('/xcAward',methods=['GET'])
def xcAward():
    return render_template('xc/award.html')


@cross_country_app.route('/xcAwardsTimeline',methods=['GET'])
def xcAwardsTimeline():
    return render_template('xc/awardsTimeline.html')


@cross_country_app.route('/xcPhotosTeamTimeline',methods=['GET'])
def xcPhotosTeamTimeline():
    return render_template('xc/photosTeamTimeline.html')


@cross_country_app.route('/xcPhotosCsAlumniRace',methods=['GET'])
def xcPhotosCsAlumniRace():
    return render_template('xc/photosCsAlumniRace.html')


@cross_country_app.route('/xcVideosCsAlumniRace',methods=['GET'])
def xcVideosCsAlumniRace():
    return render_template('xc/videosCsAlumniRace.html')


@cross_country_app.route('/pastXcAlumniChampions',methods=['GET'])
def pastXcAlumniChampions():
    return render_template('xc/pastXcAlumniChampions.html')


@cross_country_app.route('/xcAllSpecialAchievements',methods=['GET'])
def xcAllSpecialAchievements():
    return render_template('xc/specialAchievement.html', splAchvId=0, sportId=1)


@cross_country_app.route('/xcLeagueChampions',methods=['GET'])
def xcLeagueChampions():
    return render_template('xc/specialAchievement.html', splAchvId=1, sportId=1)


@cross_country_app.route('/xcSectionChampions',methods=['GET'])
def xcSectionChampions():
    return render_template('xc/specialAchievement.html', splAchvId=2, sportId=1)


@cross_country_app.route('/xcStateQualifiers',methods=['GET'])
def xcStateQualifiers():
    return render_template('xc/specialAchievement.html', splAchvId=3, sportId=1)

