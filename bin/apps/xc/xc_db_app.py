__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, json, request
import MySQLdb

from bin.utils import Utils


xc_db_app = Blueprint('xc_db_app', __name__, template_folder='templates')


# MySQL configurations
# heroku - JawsDB
mydb = MySQLdb.connect(
    host="ofcmikjy9x4lroa2.cbetxkdyhwsb.us-east-1.rds.amazonaws.com",
    user="wrcpd5zfxppr2cew",
    passwd="deyz4an53hsnvwko",
    db="sodfafe0xvqscbco"
)
"""
# localhost
mydb = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="run4fun1986",
    db="highSchoolRunning"
)
"""


@xc_db_app.route('/getTopCourseResults',methods=['GET'])
def get_top_course_results():
    try:
        courseId = request.args.get('courseId', default = 1, type = int)
        genderId = request.args.get('genderId', default = 2, type = int)
        limit = request.args.get('limit', default = 25, type = int)
        grade = request.args.get('grade', default = 0, type = int)

        cursor = mydb.cursor()
        if grade == 0:
            cursor.execute('CALL GetTopXcIndividual({0}, {1}, {2})'.format(courseId,genderId,limit))
        else:
            cursor.execute('CALL GetTopXcIndividualByGrade({0}, {1}, {2}, {3})'.format(courseId,genderId,grade,limit))

        top_results_dict = []
        for row in cursor.fetchall():
            top_results_dict.append({
                'Rank': row[0],
                'FirstName': row[1],
                'LastName': row[2],
                'Time': Utils.formatTime(row[3]),
                'Pace': Utils.formatTime(row[4]),
                'Year': row[5],
                'Grade': row[6],
                'CompetitorId': row[7],
            })

        return json.dumps(top_results_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@xc_db_app.route('/getCourseInfo',methods=['GET'])
def get_course_info():
    try:
        courseId = request.args.get('courseId', default = 1, type = int)

        cursor = mydb.cursor()
        cursor.execute('CALL GetCourseInfo({0})'.format(courseId))

        courses_dict = []
        for row in cursor.fetchall():
            courses_dict.append({
                'CourseId': row[0],
                'CourseName': row[1],
                'CourseDistance': Utils.formatDistance(row[2]),
                'City': row[3],
                'State': row[4],
                'CourseType': row[5]
            })

        return json.dumps(courses_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@xc_db_app.route('/getTopTeamCourseResults',methods=['GET'])
def get_top_team_course_results():
    try:
        courseId = request.args.get('courseId', default = 1, type = int)
        genderId = request.args.get('genderId', default = 2, type = int)
        limit = request.args.get('limit', default = 15, type = int)

        cursor = mydb.cursor()
        cursor.execute('CALL GetTopTeamCourse({0}, {1}, {2})'.format(courseId,genderId,limit))

        top_team_course_results_dict = []
        all_top_race_ids = []
        all_top_competitor_ids = []
        for row in cursor.fetchall():
            top_team_course_results_dict.append({
                'Rank': row[0],
                'Year': row[1],
                'TeamTime': Utils.formatTime(row[2]),
                'TeamPace': Utils.formatTime(row[3]),
                'RaceId': row[4],
                'CompetitorIds': row[5],                
            })
            all_top_race_ids.append(row[4])
            all_top_competitor_ids.append(row[5])

        race_competitor_data_dict = get_xc_results_by_race_competitor(all_top_race_ids,all_top_competitor_ids)

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
            team_time = Utils.convertTeamTime(team_time_min,team_time_sec)
            result['TeamTimeCalc'] = team_time
            result['TeamAvgIndTimeCalc'] = Utils.getTeamAvgIndTime(team_time)
            result['Spread'] = Utils.convertTeamTime(0, Utils.getTimeDiff(first_time, fifth_time))

        return json.dumps(top_team_course_results_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@xc_db_app.route('/getXcResultsByRaceCompetitor',methods=['GET'])
def get_xc_results_by_race_competitor(race_ids,competitor_ids):
    try:
        race_ids_str = ','.join(str(e) for e in race_ids)
        competitor_ids_str = ','.join(str(e) for e in competitor_ids)

        cursor = mydb.cursor()
        cursor.execute('CALL GetXcResultsByRaceCompetitor("{0}", "{1}")'.format(race_ids_str,competitor_ids_str))

        race_competitor_data_dict = {}
        for row in cursor.fetchall():
            race_id = str(row[0])
            competitor_id = str(row[1])
            time = Utils.formatTime(row[2])
            pace = Utils.formatTime(row[3])
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


@xc_db_app.route('/getXcRunners',methods=['GET'])
def get_xc_runners():
    try:
        genderId = request.args.get('genderId', default = '2,3', type = str)

        cursor = mydb.cursor()
        cursor.execute('CALL GetXcRunners("{0}")'.format(genderId))

        runners_dict = []
        for row in cursor.fetchall():
            runners_dict.append({
                'RunnerId': row[0],
                'FirstName': row[1],
                'LastName': row[2],
                'Years': row[3],
            })

        return json.dumps(runners_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@xc_db_app.route('/getXcRunnerResults',methods=['GET'])
def get_xc_runner_results():
    try:
        runnerId = request.args.get('runnerId', default = 1, type = int)

        cursor = mydb.cursor()
        cursor.execute('CALL GetXcRunnerResults({0})'.format(runnerId))

        runner_results_dict = []
        for row in cursor.fetchall():
            runner_results_dict.append({
                'Time': Utils.formatTime(row[0]),
                'Pace': Utils.formatTime(row[1]),
                'Grade': row[2],
                'Date': str(row[3]),
                'RaceName': row[4],
                'CourseName': row[5],
                'CourseDistance': Utils.formatDistance(row[6]),
                'RaceCondition': row[7],
                'FirstName': row[8],
                'LastName': row[9],
                'RaceId': row[10],
                'GenderId': row[11],
            })

        return json.dumps(runner_results_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@xc_db_app.route('/getXcCompetitorsByYear',methods=['GET'])
def get_xc_competitors_by_year():
    try:
        year = request.args.get('year', default = 2003, type = int)
        genderId = request.args.get('genderId', default = 2, type = int)

        cursor = mydb.cursor()
        cursor.execute('CALL GetXcCompetitorsByYear({0}, {1})'.format(year,genderId))

        competitors_dict = []
        for row in cursor.fetchall():
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


@xc_db_app.route('/getXcRacesByYear',methods=['GET'])
def get_xc_races_by_year():
    try:
        year = request.args.get('year', default = 2003, type = int)

        cursor = mydb.cursor()
        cursor.execute('CALL GetXcRacesByYear({0})'.format(year))

        races_dict = []
        for row in cursor.fetchall():
            races_dict.append({
                'RaceId': row[0],
                'Date': str(row[1]),
                'RaceName': row[2],
                'CourseName': row[3],
                'CourseDistance': Utils.formatDistance(row[4]),
            })

        return json.dumps(races_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@xc_db_app.route('/getXcCompetitorResults',methods=['GET'])
def get_xc_competitor_results():
    try:
        competitorId = request.args.get('competitorId', default = 1.12, type = str)

        cursor = mydb.cursor()
        cursor.execute('CALL GetXcCompetitorResults("{0}")'.format(competitorId))
 
        competitor_results_dict = []
        for row in cursor.fetchall():
            competitor_results_dict.append({
                'Time': Utils.formatTime(row[0]),
                'Pace': Utils.formatTime(row[1]),
                'Grade': row[2],
                'Date': str(row[3]),
                'RaceName': row[4],
                'CourseName': row[5],
                'CourseDistance': Utils.formatDistance(row[6]),
                'RaceCondition': row[7],
                'FirstName': row[8],
                'LastName': row[9],
                'Year': row[10],
                'RaceId': row[11],
                'AthleteId': row[12],
            })

        return json.dumps(competitor_results_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@xc_db_app.route('/getXcRaceResults',methods=['GET'])
def get_xc_race_results():
    try:
        raceId = request.args.get('raceId', default = 1000132, type = int)
        genderId = request.args.get('genderId', default = 0, type = int)

        cursor = mydb.cursor()
        if genderId == 0:
            cursor.execute('CALL GetAllXcRaceResults({0})'.format(raceId))
        else:
            cursor.execute('CALL GetXcRaceResults({0}, {1})'.format(raceId,genderId))

        race_results_dict = []
        for row in cursor.fetchall():
            race_results_dict.append({
                'Rank': row[0],
                'Time': Utils.formatTime(row[1]),
                'Pace': Utils.formatTime(row[2]),
                'Grade': row[3],
                'Date': str(row[4]),
                'RaceName': row[5],
                'CourseName': row[6],
                'CourseDistance': Utils.formatDistance(row[7]),
                'RaceCondition': row[8],
                'FirstName': row[9],
                'LastName': row[10],
                'Year': row[11],
                'CompetitorId': row[12],
            })

        return json.dumps(race_results_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@xc_db_app.route('/getPastXcAlumniChampions',methods=['GET'])
def get_past_xc_alumni_champions():
    try:
        cursor = mydb.cursor()
        cursor.execute('CALL GetPastXcAlumniChampions()')

        alumni_race_dict = []
        for row in cursor.fetchall():
            alumni_race_dict.append({
                'Time': Utils.formatTime(row[0]),
                'Pace': Utils.formatTime(row[1]),
                'Grade': row[2],
                'FirstName': row[3],
                'LastName': row[4],
                'RunnerId': row[5],
                'Date': str(row[6]),
                'RaceName': row[7],
                'CourseName': row[8],
                'CourseDistance': Utils.formatDistance(row[9]),
                'RaceCondition': row[10],
                'RaceId': row[11],
            })

        return json.dumps(alumni_race_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))

