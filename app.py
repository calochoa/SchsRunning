# https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql-part-3--cms-23120

from flask import Flask, render_template, json, request, redirect, session, jsonify, url_for
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
from werkzeug.wsgi import LimitedStream
import uuid
import os

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
# heroku
app.config['MYSQL_DATABASE_USER'] = 'b31e9fc461a5fd'
app.config['MYSQL_DATABASE_PASSWORD'] = '105c24d7'
app.config['MYSQL_DATABASE_DB'] = 'heroku_d5e2f87dc3f9601'
app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-iron-east-05.cleardb.net'

# localhost
#app.config['MYSQL_DATABASE_USER'] = 'nova'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'stardust'
#app.config['MYSQL_DATABASE_DB'] = 'highSchoolCrossCountry'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/xc')
def main_xc():
    return render_template('xc/index.html')


@app.route('/track')
def main_track():
    return render_template('track/index.html')


@app.route('/getTopCourseResults',methods=['GET'])
def getTopCourseResults():
    try:
        courseId = request.args.get('courseId', default = 1, type = int)
        genderId = request.args.get('genderId', default = 2, type = int)
        limit = request.args.get('limit', default = 25, type = int)
        grade = request.args.get('grade', default = 0, type = int)

        conn = mysql.connect()
        cursor = conn.cursor()
        if grade == 0:
            cursor.callproc('GetTopIndividual',(courseId,genderId,limit))
        else:
            cursor.callproc('GetTopIndividualByGrade',(courseId,genderId,grade,limit))
        data = cursor.fetchall()

        top_results_dict = []
        for row in data:
            top_results_dict.append({
                'Rank': row[0],
                'FirstName': row[1],
                'LastName': row[2],
                'Time': formatTime(row[3]),
                'Pace': formatTime(row[4]),
                'Year': row[5],
                'Grade': row[6],
                'CompetitorId': row[7],
            })

        return json.dumps(top_results_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/xcTopCourseResults')
def xcTopCourseResults():
    return render_template('xc/topCourseResults.html', cId = 0, gId = 0, limit = 0)


def formatTime(time):
    timeStr = str(time)[:9]
    if timeStr.startswith('0:'):
        timeStr = timeStr[2:]
    if timeStr.startswith('0'):
        timeStr = timeStr[1:]
    return timeStr


@app.route('/getCourseInfo',methods=['GET'])
def getCourseInfo():
    try:
        courseId = request.args.get('courseId', default = 1, type = int)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('GetCourseInfo',[courseId])
        data = cursor.fetchall()

        courses_dict = []
        for row in data:
            courses_dict.append({
                'CourseId': row[0],
                'CourseName': row[1],
                'CourseDistance': formatDistance(row[2]),
                'City': row[3],
                'State': row[4],
                'CourseType': row[5]
            })

        return json.dumps(courses_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


def formatDistance(distance):
    distanceStr = str(distance)
    if distanceStr.endswith('.00'):
        distanceStr = distanceStr[:-3]
    elif distanceStr.endswith('0'):
        distanceStr = distanceStr[:-1]
    return distanceStr
    

@app.route('/xcResults')
def xcResults():
    return render_template('xc/results.html')    


@app.route('/xcTop25CsGirls')
def xcTop25CsGirls():
    return render_template('xc/topCourseResults.html', cId = 1, gId = 3, limit = 25)


@app.route('/xcTop25CsBoys')
def xcTop25CsBoys():
    return render_template('xc/topCourseResults.html', cId = 1, gId = 2, limit = 25)


@app.route('/xcTop25TpGirls')
def xcTop25TpGirls():
    return render_template('xc/topCourseResults.html', cId = 2, gId = 3, limit = 25)


@app.route('/xcTop25TpBoys')
def xcTop25TpBoys():
    return render_template('xc/topCourseResults.html', cId = 2, gId = 2, limit = 25)


@app.route('/xcTop25CpGirls')
def xcTop25CpGirls():
    return render_template('xc/topCourseResults.html', cId = 6, gId = 3, limit = 25)


@app.route('/xcTop25CpBoys')
def xcTop25CpBoys():
    return render_template('xc/topCourseResults.html', cId = 6, gId = 2, limit = 25)


@app.route('/xcTop25BpGirls')
def xcTop25BpGirls():
    return render_template('xc/topCourseResults.html', cId = 4, gId = 3, limit = 25)


@app.route('/xcTop25BpBoys')
def xcTop25BpBoys():
    return render_template('xc/topCourseResults.html', cId = 4, gId = 2, limit = 25)


@app.route('/xcTop25LynHsGirls')
def xcTop25LynHsGirls():
    return render_template('xc/topCourseResults.html', cId = 25, gId = 3, limit = 25)


@app.route('/xcTop25LynHsBoys')
def xcTop25LynHsBoys():
    return render_template('xc/topCourseResults.html', cId = 25, gId = 2, limit = 25)


@app.route('/getTopTeamCourseResults',methods=['GET'])
def getTopTeamCourseResults():
    try:
        courseId = request.args.get('courseId', default = 1, type = int)
        genderId = request.args.get('genderId', default = 2, type = int)
        limit = request.args.get('limit', default = 15, type = int)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('GetTopTeamCourse',(courseId,genderId,limit))
        data = cursor.fetchall()

        top_team_course_results_dict = []
        all_top_race_ids = []
        all_top_competitor_ids = []
        for row in data:
            top_team_course_results_dict.append({
                'Rank': row[0],
                'Year': row[1],
                'TeamTime': formatTime(row[2]),
                'TeamPace': formatTime(row[3]),
                'RaceId': row[4],
                'CompetitorIds': row[5],                
            })
            all_top_race_ids.append(row[4])
            all_top_competitor_ids.append(row[5])

        race_competitor_data_dict = getResultsByRaceCompetitor(all_top_race_ids,all_top_competitor_ids)

        for result in top_team_course_results_dict:
            race_id = str(result['RaceId'])
            competitor_times = []
            team_time_min = 0
            team_time_sec = 0.0
            
            for idx,competitor_id in enumerate(str(result['CompetitorIds']).split(',')):
                key = race_id + ':' + competitor_id
                competitor_data = race_competitor_data_dict[key]
                competitor_times.append(competitor_data['Display'])
                competitor_time_parts = competitor_data['Time'].split(':')
                if len(competitor_time_parts) == 2:
                     team_time_min += int(competitor_time_parts[0])
                     team_time_sec += float(competitor_time_parts[1])
                if idx == 0:
                     first_time = competitor_data['Time']
                elif idx == 4:
                     fifth_time = competitor_data['Time']

            result['CompetitorTimes'] = competitor_times
            team_time = convertTeamTime(team_time_min,team_time_sec)
            result['TeamTimeCalc'] = team_time
            result['TeamAvgIndTimeCalc'] = getTeamAvgIndTime(team_time)
            result['Spread'] = convertTeamTime(0, getTimeDiff(first_time, fifth_time))

        return json.dumps(top_team_course_results_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


def getTimeDiff(time_1, time_2):
    time_1_sec = getSecondsFromTime(time_1)
    time_2_sec = getSecondsFromTime(time_2)
    return time_2_sec - time_1_sec


def getSecondsFromTime(time):
    time_parts = time.split(':')
    return (int(time_parts[0]) * 60) + float(time_parts[1])


def convertTeamTime(team_time_min,team_time_sec):
    time_min = team_time_min
    time_sec = team_time_sec
    if team_time_sec >= 60:
        extra_min = team_time_sec / 60
        time_sec = (extra_min - int(extra_min)) * 60
        time_min += int(extra_min)

    return formatTeamTime(time_min,time_sec)


def getTeamAvgIndTime(team_time):
    time_parts = team_time.split(':')
    if len(time_parts) == 2:
        time_min = int(time_parts[0])
        time_sec = float(time_parts[1]) + (time_min * 60)
        avg_time = time_sec / 5 / 60
        avg_time_min = int(avg_time)
        avg_time_sec = (avg_time - avg_time_min) * 60
        return formatTeamTime(avg_time_min,avg_time_sec)


def formatTeamTime(team_time_min,team_time_sec):
    min_str = str(team_time_min)
    sec_str = ('0' if team_time_sec < 10 else '') + str(round(team_time_sec,1))
    if sec_str.endswith('.0'):
       sec_str = sec_str[:-2]

    return min_str + ':' + sec_str


@app.route('/getResultsByRaceCompetitor',methods=['GET'])
def getResultsByRaceCompetitor(race_ids,competitor_ids):
    try:
        race_ids_str = ','.join(str(e) for e in race_ids)
        competitor_ids_str = ','.join(str(e) for e in competitor_ids)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('GetResultsByRaceCompetitor',(race_ids_str,competitor_ids_str))
        data = cursor.fetchall()

        race_competitor_data_dict = {}
        for row in data:
            race_id = str(row[0])
            competitor_id = str(row[1])
            time = formatTime(row[2])
            pace = formatTime(row[3])
            grade = str(row[4])
            first_name = row[5]
            last_name = row[6]
            key = race_id + ':' + competitor_id
            race_competitor_data_dict[key] = {
                'Display': first_name + ' ' + last_name + ' (' + grade + ') - ' + time + ' (' + pace + ')',
                'Time': time
            }

        return race_competitor_data_dict
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/xcTop25CsTeamGirls')
def xcTop25CsTeamGirls():
    return render_template('xc/teamCourseResults.html', cId = 1, gId = 3, limit = 15)


@app.route('/xcTop25CsTeamBoys')
def xcTop25CsTeamBoys():
    return render_template('xc/teamCourseResults.html', cId = 1, gId = 2, limit = 15)


@app.route('/xcTop25TpTeamGirls')
def xcTop25TpTeamGirls():
    return render_template('xc/teamCourseResults.html', cId = 2, gId = 3, limit = 15)


@app.route('/xcTop25TpTeamBoys')
def xcTop25TpTeamBoys():
    return render_template('xc/teamCourseResults.html', cId = 2, gId = 2, limit = 15)


@app.route('/xcTop25CpTeamGirls')
def xcTop25CpTeamGirls():
    return render_template('xc/teamCourseResults.html', cId = 6, gId = 3, limit = 15)


@app.route('/xcTop25CpTeamBoys')
def xcTop25CpTeamBoys():
    return render_template('xc/teamCourseResults.html', cId = 6, gId = 2, limit = 15)


@app.route('/xcTop25BpTeamGirls')
def xcTop25BpTeamGirls():
    return render_template('xc/teamCourseResults.html', cId = 4, gId = 3, limit = 15)


@app.route('/xcTop25BpTeamBoys')
def top25BpTeamBoys():
    return render_template('xc/teamCourseResults.html', cId = 4, gId = 2, limit = 15)


@app.route('/getRunners',methods=['GET'])
def getRunners():
    try:
        genderId = request.args.get('genderId', default = 2, type = int)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('GetRunners',[genderId])
        data = cursor.fetchall()

        runners_dict = []
        for row in data:
            runners_dict.append({
                'RunnerId': row[0],
                'FirstName': row[1],
                'LastName': row[2],
                'Years': row[3],
            })

        return json.dumps(runners_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/xcMRunners')
def xcMRunners():
    return render_template('xc/runners.html', gId = 2)


@app.route('/xcFRunners')
def xcFRunners():
    return render_template('xc/runners.html', gId = 3)


@app.route('/getRunnerResults',methods=['GET'])
def getRunnerResults():
    try:
        runnerId = request.args.get('runnerId', default = 1, type = int)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('GetRunnerResults',[runnerId])
        data = cursor.fetchall()

        runner_results_dict = []
        for row in data:
            runner_results_dict.append({
                'Time': formatTime(row[0]),
                'Pace': formatTime(row[1]),
                'Grade': row[2],
                'Date': str(row[3]),
                'RaceName': row[4],
                'CourseName': row[5],
                'CourseDistance': formatDistance(row[6]),
                'RaceCondition': row[7],
                'FirstName': row[8],
                'LastName': row[9],
                'RaceId': row[10],
            })

        return json.dumps(runner_results_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/xcRunner')
def xcRunner():
    return render_template('xc/runner.html')


@app.route('/getCompetitorsByYear',methods=['GET'])
def getCompetitorsByYear():
    try:
        year = request.args.get('year', default = 2003, type = int)
        genderId = request.args.get('genderId', default = 2, type = int)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('GetCompetitorsByYear',(year,genderId))
        data = cursor.fetchall()

        competitors_dict = []
        for row in data:
            competitors_dict.append({
                'CompetitorId': row[0],
                'Year': row[1],
                'Grade': row[2],
                'FirstName': row[3],
                'LastName': row[4],
                'Gender': row[5],
            })

        return json.dumps(competitors_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/getRacesByYear',methods=['GET'])
def getRacesByYear():
    try:
        year = request.args.get('year', default = 2003, type = int)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('GetRacesByYear',[year])
        data = cursor.fetchall()

        races_dict = []
        for row in data:
            races_dict.append({
                'RaceId': row[0],
                'Date': str(row[1]),
                'RaceName': row[2],
                'CourseName': row[3],
                'CourseDistance': formatDistance(row[4]),
            })

        return json.dumps(races_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/xcSeason',methods=['GET'])
def xcSeason():
    return render_template('xc/season.html')


@app.route('/getCompetitorResults',methods=['GET'])
def getCompetitorResults():
    try:
        competitorId = request.args.get('competitorId', default = 1.12, type = str)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('GetCompetitorResults',[competitorId])
        data = cursor.fetchall()
 
        competitor_results_dict = []
        for row in data:
            competitor_results_dict.append({
                'Time': formatTime(row[0]),
                'Pace': formatTime(row[1]),
                'Grade': row[2],
                'Date': str(row[3]),
                'RaceName': row[4],
                'CourseName': row[5],
                'CourseDistance': formatDistance(row[6]),
                'RaceCondition': row[7],
                'FirstName': row[8],
                'LastName': row[9],
                'Year': row[10],
                'RaceId': row[11],
            })

        return json.dumps(competitor_results_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/xcCompetitor',methods=['GET'])
def xcCompetitor():
    return render_template('xc/competitor.html')


@app.route('/getRaceResults',methods=['GET'])
def getRaceResults():
    try:
        raceId = request.args.get('raceId', default = 1000132, type = int)
        genderId = request.args.get('genderId', default = 0, type = int)

        conn = mysql.connect()
        cursor = conn.cursor()
        if genderId == 0:
            cursor.callproc('GetAllRaceResults',[raceId])
        else:
            cursor.callproc('GetRaceResults',(raceId,genderId))
        data = cursor.fetchall()

        race_results_dict = []
        for row in data:
            race_results_dict.append({
                'Rank': row[0],
                'Time': formatTime(row[1]),
                'Pace': formatTime(row[2]),
                'Grade': row[3],
                'Date': str(row[4]),
                'RaceName': row[5],
                'CourseName': row[6],
                'CourseDistance': formatDistance(row[7]),
                'RaceCondition': row[8],
                'FirstName': row[9],
                'LastName': row[10],
                'Year': row[11],
                'CompetitorId': row[12],
            })

        return json.dumps(race_results_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/xcRaceResults',methods=['GET'])
def xcRaceResults():
    return render_template('xc/raceResults.html')


@app.route('/getCoachesByYear',methods=['GET'])
def getCoachesByYear():
    try:
        year = request.args.get('year', default = 2017, type = int)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('GetCoachesByYear',[year])
        data = cursor.fetchall()

        coaches_dict = []
        for row in data:
            coaches_dict.append({
                'FirstName': row[0],
                'LastName': row[1],
                'CoachType': row[2],
                'Year': row[3],
                'CoachId': row[4],
            })

        return json.dumps(coaches_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/getCoachTimeline',methods=['GET'])
def getCoachTimeline():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('GetCoachTimeline')
        data = cursor.fetchall()

        coach_timeline_dict = []
        for row in data:
            coach_timeline_dict.append({
                'Year': row[0],
                'Coaches': row[1],
            })

        return json.dumps(coach_timeline_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/xcCoachTimeline',methods=['GET'])
def xcCoachTimeline():
    return render_template('xc/coachTimeline.html')


@app.route('/getCoachById',methods=['GET'])
def getCoachById():
    try:
        coachId = request.args.get('coachId', default = 1, type = int)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('GetCoachById',[coachId])
        data = cursor.fetchall()

        coaches_dict = []
        for row in data:
            coaches_dict.append({
                'FirstName': row[0],
                'LastName': row[1],
                'CoachType': row[2],
                'Year': row[3],
            })

        return json.dumps(coaches_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/xcCoach',methods=['GET'])
def xcCoach():
    return render_template('xc/coach.html')


@app.route('/getCoaches',methods=['GET'])
def getCoaches():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('GetCoaches')
        data = cursor.fetchall()

        coaches_dict = []
        for row in data:
            coaches_dict.append({
                'CoachId': row[0],
                'FirstName': row[1],
                'LastName': row[2],
                'NumSeasons': row[3],
                'Years': row[4],
            })

        return json.dumps(coaches_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/xcCoaches',methods=['GET'])
def xcCoaches():
    return render_template('xc/coaches.html')


@app.route('/getAwardsByYear',methods=['GET'])
def getAwardsByYear():
    try:
        year = request.args.get('year', default = 2017, type = int)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('GetAwardsByYear',[year])
        data = cursor.fetchall()

        awards_dict = []
        for row in data:
            awards_dict.append({
                'FirstName': row[0],
                'LastName': row[1],
                'AwardId': row[2],
                'AwardName': row[3],
                'AwardShortName': row[4],
                'SquadId': row[5],
                'SquadName': row[6],
                'SquadAbbr': row[7],
                'Year': row[8],
            })

        return json.dumps(awards_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/getAwardById',methods=['GET'])
def getAwardById():
    try:
        awardId = request.args.get('awardId', default = 0, type = int)
        squadId = request.args.get('squadId', default = 0, type = int)

        if awardId == 0 or awardId == 1 or awardId == 2:
            awardId = '1,2'
        if squadId == 0:
            squadId = '1,2,3,4'

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('GetAwardsById',(awardId,squadId))
        data = cursor.fetchall()

        awards_dict = []
        for row in data:
            awards_dict.append({
                'FirstName': row[0],
                'LastName': row[1],
                'Award': row[2],
                'Squad': row[3],
                'Year': row[4],
                'RunnerId': row[5],
            })

        return json.dumps(awards_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/xcAward',methods=['GET'])
def xcAward():
    return render_template('xc/award.html')


@app.route('/getAwardsTimeline',methods=['GET'])
def getAwardsTimeline():
    try:
        squadId = request.args.get('squadId', default = 0, type = int)

        if squadId == 0:
            squadId = '1,2,3,4'

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('GetAwardsTimeline',[squadId])
        data = cursor.fetchall()

        awards_dict = []
        for row in data:
            awards_dict.append({
                'FirstName': row[0],
                'LastName': row[1],
                'AwardName': row[2],
                'SquadName': row[3],
                'Year': row[4],
                'RunnerId': row[5],
            })

        return json.dumps(awards_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/xcAwardsTimeline',methods=['GET'])
def xcAwardsTimeline():
    return render_template('xc/awardsTimeline.html')


@app.route('/xcPhotosTeamTimeline',methods=['GET'])
def xcPhotosTeamTimeline():
    return render_template('xc/photosTeamTimeline.html')


@app.route('/relatedSites',methods=['GET'])
def relatedSites():
    return render_template('relatedSites.html')


@app.route('/xcPhotosCsAlumniRace',methods=['GET'])
def xcPhotosCsAlumniRace():
    return render_template('xc/photosCsAlumniRace.html')


@app.route('/xcVideosCsAlumniRace',methods=['GET'])
def xcVideosCsAlumniRace():
    return render_template('xc/videosCsAlumniRace.html')


@app.route('/pastXcAlumniChampions',methods=['GET'])
def pastXcAlumniChampions():
    return render_template('xc/pastXcAlumniChampions.html')


@app.route('/getPastXcAlumniChampions',methods=['GET'])
def getPastXcAlumniChampions():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('GetPastXcAlumniChampions')
        data = cursor.fetchall()

        alumni_race_dict = []
        for row in data:
            alumni_race_dict.append({
                'Time': formatTime(row[0]),
                'Pace': formatTime(row[1]),
                'Grade': row[2],
                'FirstName': row[3],
                'LastName': row[4],
                'RunnerId': row[5],
                'Date': str(row[6]),
                'RaceName': row[7],
                'CourseName': row[8],
                'CourseDistance': formatDistance(row[9]),
                'RaceCondition': row[10],
                'RaceId': row[11],
            })

        return json.dumps(alumni_race_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/xcAllSpecialAchievements',methods=['GET'])
def xcAllSpecialAchievements():
    return render_template('xc/specialAchievement.html', splAchvId=0)


@app.route('/xcLeagueChampions',methods=['GET'])
def xcLeagueChampions():
    return render_template('xc/specialAchievement.html', splAchvId=1)


@app.route('/xcSectionChampions',methods=['GET'])
def xcSectionChampions():
    return render_template('xc/specialAchievement.html', splAchvId=2)


@app.route('/xcStateQualifiers',methods=['GET'])
def xcStateQualifiers():
    return render_template('xc/specialAchievement.html', splAchvId=3)


@app.route('/getSpecialAchieversById',methods=['GET'])
def getSpecialAchieversById():
    try:
        splAchvId = request.args.get('splAchvId', default = 0, type = int)

        specialAchievementIds = '1,2,3' if splAchvId == 0 else str(splAchvId)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('GetSpecialAchieversById',[specialAchievementIds])
        data = cursor.fetchall()

        special_achievers_dict = []
        for row in data:
            special_achievers_dict.append({
                'SpecialAchievementName': row[0],
                'RunnerId': row[1],
                'FirstName': row[2],
                'LastName': row[3],
                'Grade': row[4],
                'Year': row[5],
                'Notes': row[6],
            })
        return json.dumps(special_achievers_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


if __name__ == "__main__":
    app.run()
