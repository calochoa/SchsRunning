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


@track_db_app.route('/getTrackHallfOfFameRaceResults', methods=['GET'])
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
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackHallfOfFameRelayResults', methods=['GET'])
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

        top_relay_results_dict = []
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

            top_relay_results_dict.append({
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

        return json.dumps(top_relay_results_dict)
    except Exception as e:
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackHallfOfFameFieldResults', methods=['GET'])
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

        top_field_results_dict = []
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

            top_field_results_dict.append({
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

        return json.dumps(top_field_results_dict)
    except Exception as e:
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackCompetitorsByYear', methods=['GET'])
def get_track_competitors_by_year():
    try:
        year = request.args.get('year', default = 2018, type = int)

        cursor = mydb.cursor()
        cursor.callproc('GetTrackCompetitorsByYear',[year])
        for result in cursor.stored_results():
            data = result.fetchall()

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
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackEventsByYear', methods=['GET'])
def get_track_events_by_year():
    try:
        year = request.args.get('year', default = 2018, type = int)

        cursor = mydb.cursor()
        cursor.callproc('GetTrackEventsByYear',[year])
        for result in cursor.stored_results():
            data = result.fetchall()

        races_dict = []
        for row in data:
            races_dict.append({
                'Event': str(row[0]),
                'EventId': row[1],
                'Squad': str(row[2]),
                'SquadId': row[3],
                'EventBySquad': str(row[4]),
                'NumResults': row[5],
            })

        return json.dumps(races_dict)
    except Exception as e:
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackRaceResults', methods=['GET'])
def get_track_race_results():
    try:
        event_id = request.args.get('eventId', default = 1, type = int)
        squad_id = request.args.get('squadId', default = 1, type = int)
        year = request.args.get('year', default = 2018, type = int)
        cursor = mydb.cursor()
        cursor.callproc('GetTrackRaceResults', (event_id, squad_id, year))
        for result in cursor.stored_results():
            data = result.fetchall()

        race_results_dict = []
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

            race_results_dict.append({
                'Rank': current_rank,
                'Event': str(row[1]),
                'FirstName': row[2],
                'LastName': row[3],
                'Time': current_time,
                'RaceTimeTypeId': str(row[5]),
                'Grade': row[6],
                'CompetitorId': str(row[7]),
                'Year': row[8],
                'Squad': str(row[9]),
            })

        return json.dumps(race_results_dict)
    except Exception as e:
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackFieldResults', methods=['GET'])
def get_track_field_results():
    try:
        event_id = request.args.get('eventId', default = 29, type = int)
        squad_id = request.args.get('squadId', default = 1, type = int)
        year = request.args.get('year', default = 2018, type = int)
        cursor = mydb.cursor()
        cursor.callproc('GetTrackFieldResults', (event_id, squad_id, year))
        for result in cursor.stored_results():
            data = result.fetchall()

        field_results_dict = []
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

            field_results_dict.append({
                'Rank': current_rank,
                'Event': str(row[1]),
                'FirstName': row[2],
                'LastName': row[3],
                'FootPartOfDistance': foot_part_of_distance,
                'InchPartOfDistance': inch_part_of_distance,
                'Grade': row[6],
                'CompetitorId': str(row[7]),
                'Year': row[8],
                'Squad': str(row[9]),
            })

        return json.dumps(field_results_dict)
    except Exception as e:
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackRelayResults', methods=['GET'])
def get_track_relay_results():
    try:
        event_id = request.args.get('eventId', default = 25, type = int)
        squad_id = request.args.get('squadId', default = 1, type = int)
        year = request.args.get('year', default = 2018, type = int)
        cursor = mydb.cursor()
        cursor.callproc('GetTrackRelayResults', (event_id, squad_id, year))
        for result in cursor.stored_results():
            data = result.fetchall()

        relay_results_dict = []
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

            relay_results_dict.append({
                'Rank': current_rank,
                'Event': str(row[1]),
                'Time': current_time,
                'RaceTimeTypeId': str(row[3]),
                'Year': row[4],
                'Squad': str(row[5]),
                'CompetitorId1': str(row[6]),
                'FullName1': str(row[7]),
                'Grade1': row[8],
                'CompetitorId2': str(row[9]),
                'FullName2': str(row[10]),
                'Grade2': row[11],
                'CompetitorId3': str(row[12]),
                'FullName3': str(row[13]),
                'Grade3': row[14],
                'CompetitorId4': str(row[15]),
                'FullName4': str(row[16]),
                'Grade4': row[17],
            })

        return json.dumps(relay_results_dict)
    except Exception as e:
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackCompetitorResults', methods=['GET'])
def get_track_competitor_results():
    try:
        competitor_id = request.args.get('competitorId', default='1000197.12', type=str)
        cursor = mydb.cursor()
        cursor.callproc('GetTrackCompetitorResults', [competitor_id])
        for result in cursor.stored_results():
            data = result.fetchall()

        competitor_results_dict = []
        for row in data:
            event_id = row[1]
            resultStr = 'Unknown'
            if event_id >= 1 and event_id <= 28:
                current_time = row[3]
                resultStr = '{0}{1}'.format(Utils.format_track_time(row[3]), row[4])
            elif event_id >= 29 and event_id <= 37:
                inch_part_of_distance = float(row[4])
                if str(inch_part_of_distance).endswith('.0'):
                    inch_part_of_distance = int(inch_part_of_distance)
                resultStr = '{0}\' {1}"'.format(row[3], inch_part_of_distance)

            competitor_results_dict.append({
                'Event': str(row[0]),
                'EventId': event_id,
                'FullName': str(row[2]),
                'Result': resultStr,
                'Grade': row[5],
                'CompetitorId': str(row[6]),
                'Year': row[7],
                'Squad': str(row[8]),
                'SquadId': row[9],
            })

        return json.dumps(competitor_results_dict)
    except Exception as e:
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackAthletes', methods=['GET'])
def get_track_athletes():
    try:
        gender_id = request.args.get('genderId', default=2, type=int)

        cursor = mydb.cursor()
        cursor.callproc('GetTrackAthletes', [gender_id])
        for result in cursor.stored_results():
            data = result.fetchall()

        track_athletes_dict = []
        for row in data:
            print row
            track_athletes_dict.append({
                'AthleteId': row[0],
                'FirstName': row[1],
                'LastName': row[2],
                'Years': str(row[3]),
            })

        return json.dumps(track_athletes_dict)
    except Exception as e:
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackAthleteResults',methods=['GET'])
def get_track_athlete_results():
    try:
        athlete_id = request.args.get('athleteId', default=1, type=int)

        cursor = mydb.cursor()
        cursor.callproc('GetTrackAthleteResults', [athlete_id])
        for result in cursor.stored_results():
            data = result.fetchall()

        track_athlete_results_dict = []
        for row in data:
            event_id = row[1]
            resultStr = 'Unknown'
            if event_id >= 1 and event_id <= 28:
                current_time = row[3]
                resultStr = '{0}{1}'.format(Utils.format_track_time(row[3]), row[4])
            elif event_id >= 29 and event_id <= 37:
                inch_part_of_distance = float(row[4])
                if str(inch_part_of_distance).endswith('.0'):
                    inch_part_of_distance = int(inch_part_of_distance)
                resultStr = '{0}\' {1}"'.format(row[3], inch_part_of_distance)

            track_athlete_results_dict.append({
                'Event': str(row[0]),
                'EventId': event_id,
                'FullName': str(row[2]),
                'Result': resultStr,
                'Grade': row[5],
                'CompetitorId': str(row[6]),
                'Year': row[7],
                'Squad': str(row[8]),
                'SquadId': row[9],
            })

        return json.dumps(track_athlete_results_dict)
    except Exception as e:
        return render_template('error.html',error = str(e))
