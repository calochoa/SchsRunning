__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, json, request
import MySQLdb

from bin.utils import Utils


shared_db_app = Blueprint('shared_db_app', __name__, template_folder='templates')


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


@shared_db_app.route('/getCoachesByYear',methods=['GET'])
def get_coaches_by_year():
    try:
        year = request.args.get('year', default = 2017, type = int)
        coach_type_ids_str = request.args.get('coachTypeIds', default = '1,2', type = str)

        cursor = mydb.cursor()
        cursor.execute('CALL GetCoachesByYear({0}, "{1}")'.format(year,coach_type_ids_str))

        coaches_dict = []
        for row in cursor.fetchall():
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
def get_coach_timeline():
    try:
        coach_type_ids_str = request.args.get('coachTypeIds', default = '1,2', type = str)

        cursor = mydb.cursor()
        cursor.execute('CALL GetCoachTimeline("{0}")'.format(coach_type_ids_str))

        coach_timeline_dict = []
        for row in cursor.fetchall():
            coach_timeline_dict.append({
                'Year': row[0],
                'Coaches': row[1],
            })

        return json.dumps(coach_timeline_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@shared_db_app.route('/getCoachById',methods=['GET'])
def get_coach_by_id():
    try:
        coachId = request.args.get('coachId', default = 1, type = int)
        coach_type_ids_str = request.args.get('coachTypeIds', default = '1,2', type = str)

        cursor = mydb.cursor()
        cursor.execute('CALL GetCoachById({0}, "{1}")'.format(coachId,coach_type_ids_str))

        coaches_dict = []
        for row in cursor.fetchall():
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
def get_coaches():
    try:
        coach_type_ids_str = request.args.get('coachTypeIds', default = '1,2', type = str)

        cursor = mydb.cursor()
        cursor.execute('CALL GetCoaches("{0}")'.format(coach_type_ids_str))

        coaches_dict = []
        for row in cursor.fetchall():
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
def get_awards_by_year():
    try:
        year = request.args.get('year', default = 2017, type = int)
        sport_id = request.args.get('sportId', default = 1, type = int)

        cursor = mydb.cursor()
        cursor.execute('CALL GetAwardsByYear({0}, {1})'.format(year,sport_id))

        awards_dict = []
        for row in cursor.fetchall():
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
def get_award_by_id():
    try:
        awardId = request.args.get('awardId', default = 0, type = int)
        squadId = request.args.get('squadId', default = 0, type = int)
        sportId = request.args.get('sportId', default = 1, type = int)

        if awardId == 0 or awardId == 1 or awardId == 2:
            awardId = '1,2'
        if squadId == 0:
            squadId = '1,2,3,4'

        cursor = mydb.cursor()
        cursor.execute('CALL GetAwardsById("{0}", "{1}", {2})'.format(awardId,squadId,sportId))
        
        awards_dict = []
        for row in cursor.fetchall():
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
def get_awards_timeline():
    try:
        squadId = request.args.get('squadId', default = 0, type = int)
        sportId = request.args.get('sportId', default = 1, type = int)

        if squadId == 0:
            squadId = '1,2,3,4'

        cursor = mydb.cursor()
        cursor.execute('CALL GetAwardsTimeline("{0}", {1})'.format(squadId,sportId))

        awards_dict = []
        for row in cursor.fetchall():
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
def get_special_achievers_by_id():
    try:
        splAchvId = request.args.get('splAchvId', default = 0, type = int)
        sportId = request.args.get('sportId', default = 1, type = int)
        
        specialAchievementIdsStr = '1,2,3' if splAchvId == 0 else str(splAchvId)
        cursor = mydb.cursor()
        cursor.execute('CALL GetSpecialAchieversById("{0}", {1})'.format(specialAchievementIdsStr,sportId))

        special_achievers_dict = []
        for row in cursor.fetchall():
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

