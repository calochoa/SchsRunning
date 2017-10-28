from flask import Flask, render_template, json, request, redirect, session, jsonify, url_for
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
from werkzeug.wsgi import LimitedStream
import uuid
import os

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'b31e9fc461a5fd'
app.config['MYSQL_DATABASE_PASSWORD'] = '105c24d7'
app.config['MYSQL_DATABASE_DB'] = 'heroku_d5e2f87dc3f9601'
app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-iron-east-05.cleardb.net'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('index.html')	


@app.route('/getTopResults',methods=['GET'])
def getTopResults():
    try:
        courseId = request.args.get('courseId', default = 1, type = int)
        genderId = request.args.get('genderId', default = 2, type = int)
        limit = request.args.get('limit', default = 25, type = int)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('GetTopIndividual',(courseId,genderId,limit))
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
                'Grade': row[6]
            }
            top_results_dict.append(result_dict)

        return json.dumps(top_results_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


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
    return render_template('results.html', cId = 1, gId = 3, limit = 25)


@app.route('/top25CsBoys')
def top25CsBoys():
    return render_template('results.html', cId = 1, gId = 2, limit = 25)


@app.route('/top25TpGirls')
def top25TpGirls():
    return render_template('results.html', cId = 2, gId = 3, limit = 25)


@app.route('/top25TpBoys')
def top25TpBoys():
    return render_template('results.html', cId = 2, gId = 2, limit = 25)


@app.route('/top25CpGirls')
def top25CpGirls():
    return render_template('results.html', cId = 6, gId = 3, limit = 25)


@app.route('/top25CpBoys')
def top25CpBoys():
    return render_template('results.html', cId = 6, gId = 2, limit = 25)


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
        for row in data:
            team_course_result_dict = {
                'Rank': row[0],
                'Year': row[1],
                'TeamTime': formatTime(row[2]),
                'TeamPace': formatTime(row[3]),
            }
            top_team_course_results_dict.append(team_course_result_dict)

        return json.dumps(top_team_course_results_dict)
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

	
if __name__ == "__main__":
	app.run()
