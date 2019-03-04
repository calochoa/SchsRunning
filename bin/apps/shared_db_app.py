__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, json, request
import mysql.connector

from bin.utils import Utils


shared_db_app = Blueprint('shared_db_app', __name__, template_folder='templates')


# MySQL configurations
# heroku
mydb = mysql.connector.connect(
    host="us-cdbr-iron-east-05.cleardb.net",
    user="b31e9fc461a5fd",
    passwd="105c24d7",
    database="heroku_d5e2f87dc3f9601",
    auth_plugin='mysql_native_password'
)
"""
# localhost
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="run4fun1986",
    database="highSchoolRunning",
    auth_plugin='mysql_native_password'
)
"""


@shared_db_app.route('/getCoachesByYear',methods=['GET'])
def getCoachesByYear():
    try:
        year = request.args.get('year', default = 2017, type = int)
        coach_type_ids_str = request.args.get('coachTypeIds', default = '1,2', type = str)

        cursor = mydb.cursor()
        cursor.callproc('GetCoachesByYear',(year,coach_type_ids_str))
        for result in cursor.stored_results():
            data = result.fetchall()

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


@shared_db_app.route('/getCoachTimeline',methods=['GET'])
def getCoachTimeline():
    try:
        coach_type_ids_str = request.args.get('coachTypeIds', default = '1,2', type = str)

        cursor = mydb.cursor()
        cursor.callproc('GetCoachTimeline',[coach_type_ids_str])
        for result in cursor.stored_results():
            data = result.fetchall()

        coach_timeline_dict = []
        for row in data:
            coach_timeline_dict.append({
                'Year': row[0],
                'Coaches': row[1],
            })

        return json.dumps(coach_timeline_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@shared_db_app.route('/getCoachById',methods=['GET'])
def getCoachById():
    try:
        coachId = request.args.get('coachId', default = 1, type = int)
        coach_type_ids_str = request.args.get('coachTypeIds', default = '1,2', type = str)

        cursor = mydb.cursor()
        cursor.callproc('GetCoachById',(coachId,coach_type_ids_str))
        for result in cursor.stored_results():
            data = result.fetchall()

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


@shared_db_app.route('/getCoaches',methods=['GET'])
def getCoaches():
    try:
        coach_type_ids_str = request.args.get('coachTypeIds', default = '1,2', type = str)

        cursor = mydb.cursor()
        cursor.callproc('GetCoaches',[coach_type_ids_str])
        for result in cursor.stored_results():
            data = result.fetchall()

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


@shared_db_app.route('/getAwardsByYear',methods=['GET'])
def getAwardsByYear():
    try:
        year = request.args.get('year', default = 2017, type = int)
        sport_id = request.args.get('sportId', default = 1, type = int)

        cursor = mydb.cursor()
        cursor.callproc('GetAwardsByYear',(year,sport_id))
        for result in cursor.stored_results():
            data = result.fetchall()

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


@shared_db_app.route('/getAwardById',methods=['GET'])
def getAwardById():
    try:
        awardId = request.args.get('awardId', default = 0, type = int)
        squadId = request.args.get('squadId', default = 0, type = int)
        sportId = request.args.get('sportId', default = 1, type = int)

        if awardId == 0 or awardId == 1 or awardId == 2:
            awardId = '1,2'
        if squadId == 0:
            squadId = '1,2,3,4'

        cursor = mydb.cursor()
        cursor.callproc('GetAwardsById',(awardId,squadId,sportId))
        for result in cursor.stored_results():
            data = result.fetchall()
        
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


@shared_db_app.route('/getAwardsTimeline',methods=['GET'])
def getAwardsTimeline():
    try:
        squadId = request.args.get('squadId', default = 0, type = int)
        sportId = request.args.get('sportId', default = 1, type = int)

        if squadId == 0:
            squadId = '1,2,3,4'

        cursor = mydb.cursor()
        cursor.callproc('GetAwardsTimeline',(squadId,sportId))
        for result in cursor.stored_results():
            data = result.fetchall()

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


@shared_db_app.route('/getSpecialAchieversById',methods=['GET'])
def getSpecialAchieversById():
    try:
        splAchvId = request.args.get('splAchvId', default = 0, type = int)
        sportId = request.args.get('sportId', default = 1, type = int)
        

        specialAchievementIdsStr = '1,2,3' if splAchvId == 0 else str(splAchvId)
        cursor = mydb.cursor()
        cursor.callproc('GetSpecialAchieversById',(specialAchievementIdsStr,sportId))
        for result in cursor.stored_results():
            data = result.fetchall()

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

