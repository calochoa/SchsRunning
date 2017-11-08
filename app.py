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
# aws 
app.config['MYSQL_DATABASE_USER'] = 'calworkouts'
app.config['MYSQL_DATABASE_PASSWORD'] = 'quickies'
app.config['MYSQL_DATABASE_DB'] = 'highSchoolCrossCountry'
app.config['MYSQL_DATABASE_HOST'] = 'rds-mysql-calworkouts.cu1fjz4ompeu.us-west-1.rds.amazonaws.com'

# heroku
#app.config['MYSQL_DATABASE_USER'] = 'b31e9fc461a5fd'
#app.config['MYSQL_DATABASE_PASSWORD'] = '105c24d7'
#app.config['MYSQL_DATABASE_DB'] = 'heroku_d5e2f87dc3f9601'
#app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-iron-east-05.cleardb.net'

# localhost
#app.config['MYSQL_DATABASE_USER'] = 'nova'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'stardust'
#app.config['MYSQL_DATABASE_DB'] = 'highSchoolCrossCountry'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')


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
            result_dict = {
                'Rank': row[0],
                'FirstName': row[1],
                'LastName': row[2],
                'Time': formatTime(row[3]),
                'Pace': formatTime(row[4]),
                'Year': row[5],
                'Grade': row[6],
                'CompetitorId': row[7],
            }
            top_results_dict.append(result_dict)

        return json.dumps(top_results_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/topCourseResults')
def topCourseResults():
    return render_template('topCourseResults.html', cId = 0, gId = 0, limit = 0)


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
            course_dict = {
                'CourseId': row[0],
                'CourseName': row[1],
                'CourseDistance': formatDistance(row[2]),
                'City': row[3],
                'State': row[4],
                'CourseType': row[5]
            }
            courses_dict.append(course_dict)

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
    

@app.route('/results')
def results():
    return render_template('results.html')    


@app.route('/top25CsGirls')
def top25CsGirls():
    return render_template('topCourseResults.html', cId = 1, gId = 3, limit = 25)


@app.route('/top25CsBoys')
def top25CsBoys():
    return render_template('topCourseResults.html', cId = 1, gId = 2, limit = 25)


@app.route('/top25TpGirls')
def top25TpGirls():
    return render_template('topCourseResults.html', cId = 2, gId = 3, limit = 25)


@app.route('/top25TpBoys')
def top25TpBoys():
    return render_template('topCourseResults.html', cId = 2, gId = 2, limit = 25)


@app.route('/top25CpGirls')
def top25CpGirls():
    return render_template('topCourseResults.html', cId = 6, gId = 3, limit = 25)


@app.route('/top25CpBoys')
def top25CpBoys():
    return render_template('topCourseResults.html', cId = 6, gId = 2, limit = 25)


@app.route('/top25BpGirls')
def top25BpGirls():
    return render_template('topCourseResults.html', cId = 4, gId = 3, limit = 25)


@app.route('/top25BpBoys')
def top25BpBoys():
    return render_template('topCourseResults.html', cId = 4, gId = 2, limit = 25)


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
            team_course_result_dict = {
                'Rank': row[0],
                'Year': row[1],
                'TeamTime': formatTime(row[2]),
                'TeamPace': formatTime(row[3]),
                'RaceId': row[4],
                'CompetitorIds': row[5],                
            }
            top_team_course_results_dict.append(team_course_result_dict)
            all_top_race_ids.append(row[4])
            all_top_competitor_ids.append(row[5])

        race_competitor_data_dict = getResultsByRaceCompetitor(all_top_race_ids,all_top_competitor_ids)

        for result in top_team_course_results_dict:
            race_id = str(result['RaceId'])
            competitor_times = []
            team_time_min = 0
            team_time_sec = 0.0
            for competitor_id in str(result['CompetitorIds']).split(','):
                key = race_id + ':' + competitor_id
                competitor_data = race_competitor_data_dict[key]
                competitor_times.append(competitor_data['Display'])
                competitor_time_parts = competitor_data['Time'].split(':')
                if len(competitor_time_parts) == 2:
                     team_time_min += int(competitor_time_parts[0])
                     team_time_sec += float(competitor_time_parts[1])

            result['CompetitorTimes'] = competitor_times
            team_time = convertTeamTime(team_time_min,team_time_sec)
            result['TeamTimeCalc'] = team_time
            result['TeamAvgIndTimeCalc'] = getTeamAvgIndTime(team_time)

        return json.dumps(top_team_course_results_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


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
            value = {
                'Display': first_name + ' ' + last_name + ' (' + grade + ') - ' + time + ' (' + pace + ')',
                'Time': time
            }
            race_competitor_data_dict[key] = value

        return race_competitor_data_dict
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/top25CsTeamGirls')
def top25CsTeamGirls():
    return render_template('teamCourseResults.html', cId = 1, gId = 3, limit = 15)


@app.route('/top25CsTeamBoys')
def top25CsTeamBoys():
    return render_template('teamCourseResults.html', cId = 1, gId = 2, limit = 15)


@app.route('/top25TpTeamGirls')
def top25TpTeamGirls():
    return render_template('teamCourseResults.html', cId = 2, gId = 3, limit = 15)


@app.route('/top25TpTeamBoys')
def top25TpTeamBoys():
    return render_template('teamCourseResults.html', cId = 2, gId = 2, limit = 15)


@app.route('/top25CpTeamGirls')
def top25CpTeamGirls():
    return render_template('teamCourseResults.html', cId = 6, gId = 3, limit = 15)


@app.route('/top25CpTeamBoys')
def top25CpTeamBoys():
    return render_template('teamCourseResults.html', cId = 6, gId = 2, limit = 15)


@app.route('/top25BpTeamGirls')
def top25BpTeamGirls():
    return render_template('teamCourseResults.html', cId = 4, gId = 3, limit = 15)


@app.route('/top25BpTeamBoys')
def top25BpTeamBoys():
    return render_template('teamCourseResults.html', cId = 4, gId = 2, limit = 15)


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
            runner_dict = {
                'RunnerId': row[0],
                'FirstName': row[1],
                'LastName': row[2],
                'Years': row[3],
            }
            runners_dict.append(runner_dict)

        return json.dumps(runners_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/mRunners')
def mRunners():
    return render_template('runners.html', gId = 2)


@app.route('/fRunners')
def fRunners():
    return render_template('runners.html', gId = 3)


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
            result_dict = {
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
            }
            runner_results_dict.append(result_dict)

        return json.dumps(runner_results_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/runner')
def runner():
    return render_template('runner.html')


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
            competitor_dict = {
                'CompetitorId': row[0],
                'Year': row[1],
                'Grade': row[2],
                'FirstName': row[3],
                'LastName': row[4],
                'Gender': row[5],
            }
            competitors_dict.append(competitor_dict)

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
            race_dict = {
                'RaceId': row[0],
                'Date': str(row[1]),
                'RaceName': row[2],
                'CourseName': row[3],
                'CourseDistance': formatDistance(row[4]),
            }
            races_dict.append(race_dict)

        return json.dumps(races_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/season',methods=['GET'])
def season():
    return render_template('season.html')


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
            result_dict = {
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
            }
            competitor_results_dict.append(result_dict)

        return json.dumps(competitor_results_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/competitor',methods=['GET'])
def competitor():
    return render_template('competitor.html')


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
            result_dict = {
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
            }
            race_results_dict.append(result_dict)

        return json.dumps(race_results_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/raceResults',methods=['GET'])
def raceResults():
    return render_template('raceResults.html')


if __name__ == "__main__":
    app.run()
