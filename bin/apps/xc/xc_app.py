__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect, request


xc_app = Blueprint('xc_app', __name__, template_folder='templates')


@xc_app.route('/santa-clara-high-cross-country')
@xc_app.route('/xc')
def main_xc():
    return render_template('xc/index.html')

@xc_app.route('/xcTopCourseResults')
def xcTopCourseResults():
    return render_template('xc/course-results/topCourseResults.html', cId=0, gId=0, limit=0, grade=0)

@xc_app.route('/xcResults')
def xcResults():
    return render_template('xc/results.html')

@xc_app.route('/xcTop25CsGirls')
def xcTop25CsGirls():
    return redirect('/santa-clara-high-cross-country/course-results/top-25-all-time-girls-crystal-springs')

@xc_app.route('/xcTop25CsBoys')
def xcTop25CsBoys():
    return redirect('/santa-clara-high-cross-country/course-results/top-25-all-time-boys-crystal-springs')

@xc_app.route('/xcTop25TpGirls')
def xcTop25TpGirls():
    return redirect('/santa-clara-high-cross-country/course-results/top-25-all-time-girls-toro-park')

@xc_app.route('/xcTop25TpBoys')
def xcTop25TpBoys():
    return redirect('/santa-clara-high-cross-country/course-results/top-25-all-time-boys-toro-park')

@xc_app.route('/xcTop25CpGirls')
def xcTop25CpGirls():
    return redirect('/santa-clara-high-cross-country/course-results/top-25-all-time-girls-central-park')

@xc_app.route('/xcTop25CpBoys')
def xcTop25CpBoys():
    return redirect('/santa-clara-high-cross-country/course-results/top-25-all-time-boys-central-park')

@xc_app.route('/xcTop25BpGirls')
def xcTop25BpGirls():
    return redirect('/santa-clara-high-cross-country/course-results/top-25-all-time-girls-baylands-park')

@xc_app.route('/xcTop25BpBoys')
def xcTop25BpBoys():
    return redirect('/santa-clara-high-cross-country/course-results/top-25-all-time-boys-baylands-park')

@xc_app.route('/xcTop25LynHsGirls')
def xcTop25LynHsGirls():
    return redirect('/santa-clara-high-cross-country/course-results/top-25-all-time-girls-lynbrook-high-school')

@xc_app.route('/xcTop25LynHsBoys')
def xcTop25LynHsBoys():
    return redirect('/santa-clara-high-cross-country/course-results/top-25-all-time-boys-lynbrook-high-school')

@xc_app.route('/xcTop25CsTeamGirls')
def xcTop25CsTeamGirls():
    return redirect('/santa-clara-high-cross-country/course-results/top-15-all-time-team-girls-crystal-springs')

@xc_app.route('/xcTop25CsTeamBoys')
def xcTop25CsTeamBoys():
    return redirect('/santa-clara-high-cross-country/course-results/top-15-all-time-team-boys-crystal-springs')

@xc_app.route('/xcTop25TpTeamGirls')
def xcTop25TpTeamGirls():
    return redirect('/santa-clara-high-cross-country/course-results/top-15-all-time-team-girls-toro-park')

@xc_app.route('/xcTop25TpTeamBoys')
def xcTop25TpTeamBoys():
    return redirect('/santa-clara-high-cross-country/course-results/top-15-all-time-team-boys-toro-park')

@xc_app.route('/xcTop25CpTeamGirls')
def xcTop25CpTeamGirls():
    return redirect('/santa-clara-high-cross-country/course-results/top-15-all-time-team-girls-central-park')

@xc_app.route('/xcTop25CpTeamBoys')
def xcTop25CpTeamBoys():
    return redirect('/santa-clara-high-cross-country/course-results/top-15-all-time-team-boys-central-park')

@xc_app.route('/xcTop25BpTeamGirls')
def xcTop25BpTeamGirls():
    return redirect('/santa-clara-high-cross-country/course-results/top-15-all-time-team-girls-baylands-park')

@xc_app.route('/xcTop25BpTeamBoys')
def top25BpTeamBoys():
    return redirect('/santa-clara-high-cross-country/course-results/top-15-all-time-team-boys-baylands-park')

@xc_app.route('/xcSeason',methods=['GET'])
def xcSeason():
    yr = request.args.get('yr', default=2003, type=int)
    return redirect('/santa-clara-high-cross-country/season/{0}'.format(yr))

@xc_app.route('/xcMRunners')
def xcMRunners():
    return redirect('/santa-clara-high-cross-country/runners/boys')

@xc_app.route('/xcFRunners')
def xcFRunners():
    return redirect('/santa-clara-high-cross-country/runners/girls')

@xc_app.route('/xcRunner')
def xcRunner():
    rId = request.args.get('rId', default=1, type=int)
    return redirect('/santa-clara-high-cross-country/runners/{0}'.format(rId))

@xc_app.route('/xcCoachTimeline',methods=['GET'])
def xcCoachTimeline():
    return redirect('/santa-clara-high-cross-country/coaches/timeline')

@xc_app.route('/xcCoach',methods=['GET'])
def xcCoach():
    coachId = request.args.get('coachId', default=1, type=int)
    return redirect('/santa-clara-high-cross-country/coaches/{0}'.format(coachId))

@xc_app.route('/xcCoaches',methods=['GET'])
def xcCoaches():
    return redirect('/santa-clara-high-cross-country/coaches/')

@xc_app.route('/xcAllSpecialAchievements',methods=['GET'])
def xcAllSpecialAchievements():
    return redirect('/santa-clara-high-cross-country/special-achievements/')

@xc_app.route('/xcLeagueChampions',methods=['GET'])
def xcLeagueChampions():
    return redirect('/santa-clara-high-cross-country/special-achievements/league-champions')

@xc_app.route('/xcSectionChampions',methods=['GET'])
def xcSectionChampions():
    return redirect('/santa-clara-high-cross-country/special-achievements/section-champions')

@xc_app.route('/xcStateQualifiers',methods=['GET'])
def xcStateQualifiers():
    return redirect('/santa-clara-high-cross-country/special-achievements/state-qualifiers')

@xc_app.route('/pastXcAlumniChampions',methods=['GET'])
def pastXcAlumniChampions():
    return redirect('/santa-clara-high-cross-country/special-achievements/past-crystal-springs-alumni-race-champions')

@xc_app.route('/xcAward',methods=['GET'])
def xcAward():
    awardId = request.args.get('awardId', default=0, type=int)
    squadId = request.args.get('squadId', default=0, type=int)
    return redirect('/santa-clara-high-cross-country/awards/{0}/{1}'.format(awardId, squadId))

@xc_app.route('/xcAwardsTimeline',methods=['GET'])
def xcAwardsTimeline():
    squadId = request.args.get('squadId', default=0, type=int)
    return redirect('/santa-clara-high-cross-country/awards/timeline/{0}'.format(squadId))

@xc_app.route('/xcPhotosTeamTimeline',methods=['GET'])
def xcPhotosTeamTimeline():
    return redirect('/santa-clara-high-cross-country/photos/team-timeline')

@xc_app.route('/xcPhotosCsAlumniRace',methods=['GET'])
def xcPhotosCsAlumniRace():
    return redirect('/santa-clara-high-cross-country/photos/crystal-springs-alumni-race')

@xc_app.route('/xcVideosCsAlumniRace',methods=['GET'])
def xcVideosCsAlumniRace():
    return redirect('/santa-clara-high-cross-country/videos/crystal-springs-alumni-race')

@xc_app.route('/xcRaceResults',methods=['GET'])
def xcRaceResults():
    raceId = request.args.get('raceId', default=0, type=int)
    genderId = request.args.get('gId', default=0, type=int)
    return redirect('/santa-clara-high-cross-country/race-results/{0}/{1}'.format(raceId, genderId))

@xc_app.route('/xcCompetitor',methods=['GET'])
def xcCompetitor():
    competitorId = request.args.get('cId', default="1.12", type=str)
    return redirect('/santa-clara-high-cross-country/competitors/{0}'.format(competitorId))

