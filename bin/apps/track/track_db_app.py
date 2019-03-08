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

track_db_app = Blueprint('track_db_app', __name__, template_folder='templates')


@track_db_app.route('/getTrackHallfOfFameRaceResults',methods=['GET'])
def get_track_hall_of_fame_race_results():
    try:
        event_id = request.args.get('eventId', default = 1, type = int)
        gender_id = request.args.get('genderId', default = 2, type = int)
        limit = 25
        max_rank_in_hall_of_fame = 10
        cursor = mydb.cursor()
        cursor.callproc('GetTopTrackRaceIndividual', (event_id, gender_id, limit))
        for result in cursor.stored_results():
            data = result.fetchall()

        top_race_results_dict = []
        last_rank = 0
        last_time = 0
        for row in data:
            current_rank = row[0]
            current_time = Utils.format_track_time(row[4])
            if last_rank > 0:
                if current_time == last_time:
                    current_rank = last_rank
                else:
                    last_rank = current_rank
                    last_time = current_time
            else:
                last_rank = current_rank
                last_time = current_time

            if last_rank > max_rank_in_hall_of_fame:
                break

            top_race_results_dict.append({
                'Rank': current_rank,
                'Event': row[1],
                'FirstName': row[2],
                'LastName': row[3],
                'Time': current_time,
                'RaceTimeTypeId': row[5],
                'Year': row[6],
                'Grade': row[7],
                'CompetitorId': row[8],
            })

        return json.dumps(top_race_results_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@track_db_app.route('/getTrackHallfOfFameRelayResults',methods=['GET'])
def get_track_hall_of_fame_relay_results():
    try:
        event_id = request.args.get('eventId', default = 1, type = int)
        gender_id = request.args.get('genderId', default = 2, type = int)
        limit = 25
        max_rank_in_hall_of_fame = 10
        cursor = mydb.cursor()
        cursor.callproc('GetTopTrackRelayTeam', (event_id, gender_id, limit))
        for result in cursor.stored_results():
            data = result.fetchall()

        top_race_results_dict = []
        last_rank = 0
        last_time = 0
        for row in data:
            current_rank = row[0]
            current_time = Utils.format_track_time(row[2])
            if last_rank > 0:
                if current_time == last_time:
                    current_rank = last_rank
                else:
                    last_rank = current_rank
                    last_time = current_time
            else:
                last_rank = current_rank
                last_time = current_time

            if last_rank > max_rank_in_hall_of_fame:
                break

            top_race_results_dict.append({
                'Rank': current_rank,
                'Event': row[1],
                'Time': current_time,
                'RaceTimeTypeId': row[3],
                'Year': row[4],
                'CompetitorId1': row[5],
                'FullName1': row[6],
                'Grade1': row[7],
                'CompetitorId2': row[8],
                'FullName2': row[9],
                'Grade2': row[10],
                'CompetitorId3': row[11],
                'FullName3': row[12],
                'Grade3': row[13],
                'CompetitorId4': row[14],
                'FullName4': row[15],
                'Grade4': row[16],
            })

        return json.dumps(top_race_results_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))


@track_db_app.route('/getTrackHallfOfFameFieldResults',methods=['GET'])
def get_track_hall_of_fame_field_results():
    try:
        event_id = request.args.get('eventId', default = 29, type = int)
        gender_id = request.args.get('genderId', default = 3, type = int)
        limit = 25
        max_rank_in_hall_of_fame = 10
        cursor = mydb.cursor()
        cursor.callproc('GetTopFieldIndividual', (event_id, gender_id, limit))
        for result in cursor.stored_results():
            data = result.fetchall()

        top_race_results_dict = []
        last_rank = 0
        last_distance = 0
        for row in data:
            current_rank = row[0]
            foot_part_of_distance = row[4]
            inch_part_of_distance = float(row[5])
            current_distance_in_inches = (12 * foot_part_of_distance) + inch_part_of_distance
            if last_rank > 0:
                if current_distance_in_inches == last_distance:
                    current_rank = last_rank
                else:
                    last_rank = current_rank
                    last_distance = current_distance_in_inches
            else:
                last_rank = current_rank
                last_distance = current_distance_in_inches

            if last_rank > max_rank_in_hall_of_fame:
                break

            top_race_results_dict.append({
                'Rank': current_rank,
                'Event': row[1],
                'FirstName': row[2],
                'LastName': row[3],
                'FootPartOfDistance': foot_part_of_distance,
                'InchPartOfDistance': inch_part_of_distance,
                'Year': row[6],
                'Grade': row[7],
                'CompetitorId': row[8],
            })

        return json.dumps(top_race_results_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))
