__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"



from flask import Blueprint, render_template, json, request
import mysql.connector

from bin.utils import Utils


# MySQL configurations
"""
# heroku - ClearDB
mydb = mysql.connector.connect(
    host="us-cdbr-iron-east-05.cleardb.net",
    user="b31e9fc461a5fd",
    passwd="105c24d7",
    database="heroku_d5e2f87dc3f9601",
    auth_plugin='mysql_native_password'
)
"""
# heroku - JawsDB
mydb = mysql.connector.connect(
    host="ofcmikjy9x4lroa2.cbetxkdyhwsb.us-east-1.rds.amazonaws.com ",
    user="wrcpd5zfxppr2cew",
    passwd="deyz4an53hsnvwko",
    database="sodfafe0xvqscbco",
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


track_and_field_db_app = Blueprint('track_and_field_db_app', __name__, template_folder='templates')


@track_and_field_db_app.route('/getTopTrackRaceResults',methods=['GET'])
def getTopTrackRaceResults():
    try:
        eventId = request.args.get('eventId', default = 1, type = int)
        genderId = request.args.get('genderId', default = 2, type = int)
        limit = request.args.get('limit', default = 25, type = int)
        cursor = mydb.cursor()
        cursor.callproc('GetTopTrackRaceIndividual',(eventId,genderId,limit))
        for result in cursor.stored_results():
            data = result.fetchall()

        top_race_results_dict = []
        lastRank = 0
        lastTime = 0
        for row in data:
            currentRank = row[0]
            currentTime = Utils.formatTrackTime(row[4])
            if lastRank > 0:
                if currentTime == lastTime:
                    currentRank = lastRank
                else:
                    lastRank = currentRank
                    lastTime = currentTime
            else:
                lastRank = currentRank
                lastTime = currentTime

            top_race_results_dict.append({
                'Rank': currentRank,
                'Event': row[1],
                'FirstName': row[2],
                'LastName': row[3],
                'Time': currentTime,
                'RaceTimeTypeId': row[5],
                'StatMark': row[6],
                'Year': row[7],
                'Grade': row[8],
                'CompetitorId': row[9],
            })

        return json.dumps(top_race_results_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))
