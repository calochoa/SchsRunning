__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, json, request
import MySQLdb
import collections

from bin.utils import Utils


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


track_db_app = Blueprint('track_db_app', __name__, template_folder='templates')


@track_db_app.route('/getTrackHallfOfFameRaceResults', methods=['GET'])
def get_track_hall_of_fame_race_results():
    try:
        event_id = request.args.get('eventId', default = 1, type = int)
        gender_id = request.args.get('genderId', default = 2, type = int)
        limit = 40
        max_rank_in_hall_of_fame = 15
        cursor = mydb.cursor()
        cursor.execute('CALL GetTopTrackRaceIndividual({0}, {1}, {2})'.format(event_id, gender_id, limit))

        top_race_results_dict = []
        last_rank = 0
        last_time = 0
        for row in cursor.fetchall():
            current_rank = row[0]
            current_time = Utils.format_track_time(row[4])
            current_rank, last_rank, current_time, last_time = __get_rank_measurement_metadata(
                current_rank, last_rank, current_time, last_time
            )

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
        limit = 40
        max_rank_in_hall_of_fame = 15
        cursor = mydb.cursor()
        cursor.execute('CALL GetTopTrackRelayTeam({0}, {1}, {2})'.format(event_id, gender_id, limit))

        top_relay_results_dict = []
        last_rank = 0
        last_time = 0
        for row in cursor.fetchall():
            current_rank = row[0]
            current_time = Utils.format_track_time(row[2])
            current_rank, last_rank, current_time, last_time = __get_rank_measurement_metadata(
                current_rank, last_rank, current_time, last_time
            )

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
        limit = 40
        max_rank_in_hall_of_fame = 15
        cursor = mydb.cursor()
        cursor.execute('CALL GetTopFieldIndividual({0}, {1}, {2})'.format(event_id, gender_id, limit))

        top_field_results_dict = []
        last_rank = 0
        last_distance = 0
        for row in cursor.fetchall():
            current_rank = row[0]
            foot_part_of_distance = int(row[4])
            inch_part_of_distance = float(row[5])
            current_distance_in_inches = __get_distance_in_inches(foot_part_of_distance, inch_part_of_distance)
            current_rank, last_rank, current_distance_in_inches, last_distance = __get_rank_measurement_metadata(
                current_rank, last_rank, current_distance_in_inches, last_distance
            )

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
        cursor.execute('CALL GetTrackCompetitorsByYear({0})'.format(year))

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
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackEventsByYear', methods=['GET'])
def get_track_events_by_year():
    try:
        year = request.args.get('year', default = 2018, type = int)

        cursor = mydb.cursor()
        cursor.execute('CALL GetTrackEventsByYear({0})'.format(year))

        races_dict = []
        for row in cursor.fetchall():
            races_dict.append({
                'Event': str(row[0]),
                'EventId': row[1],
                'Squad': str(row[2]),
                'SquadId': row[3],
                'EventBySquad': str(row[4]),
                'NumResults': row[5],
                'EventSubType': str(row[6]),
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
        cursor.execute('CALL GetTrackRaceResults({0}, {1}, {2})'.format(event_id, squad_id, year))

        race_results_dict = []
        last_rank = 0
        last_time = 0
        for row in cursor.fetchall():
            current_rank = row[0]
            current_time = Utils.format_track_time(row[4])
            current_rank, last_rank, current_time, last_time = __get_rank_measurement_metadata(
                current_rank, last_rank, current_time, last_time
            )

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
        cursor.execute('CALL GetTrackFieldResults({0}, {1}, {2})'.format(event_id, squad_id, year))

        field_results_dict = []
        last_rank = 0
        last_distance = 0
        for row in cursor.fetchall():
            current_rank = row[0]
            foot_part_of_distance = int(row[4])
            inch_part_of_distance = float(row[5])
            current_distance_in_inches = __get_distance_in_inches(foot_part_of_distance, inch_part_of_distance)
            current_rank, last_rank, current_distance_in_inches, last_distance = __get_rank_measurement_metadata(
                current_rank, last_rank, current_distance_in_inches, last_distance
            )

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
        cursor.execute('CALL GetTrackRelayResults({0}, {1}, {2})'.format(event_id, squad_id, year))

        relay_results_dict = []
        last_rank = 0
        last_time = 0
        for row in cursor.fetchall():
            current_rank = row[0]
            current_time = Utils.format_track_time(row[2])
            current_rank, last_rank, current_time, last_time = __get_rank_measurement_metadata(
                current_rank, last_rank, current_time, last_time
            )

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
        cursor.execute('CALL GetTrackCompetitorResults("{0}")'.format(competitor_id))

        competitor_results_dict = []
        more_results = True
        while more_results:
            mysql_rows = cursor.fetchall()
            all_rank_dict = __get_all_ranking_dict(competitor_id, mysql_rows)
            if all_rank_dict:
                grade_rank, grade_rank_total = __get_all_grade_ranking(competitor_id, mysql_rows, all_rank_dict['Grade'])
                all_rank_dict['GradeRank'] = grade_rank
                all_rank_dict['GradeRankTotal'] = grade_rank_total

                year_squad_rank, year_squad_rank_total = __get_year_squad_ranking(
                    competitor_id, mysql_rows, all_rank_dict['Year'], all_rank_dict['SquadId']
                )
                all_rank_dict['YearSquadRank'] = year_squad_rank
                all_rank_dict['YearSquadRankTotal'] = year_squad_rank_total

                competitor_results_dict.append(all_rank_dict)
            more_results = cursor.nextset()

        return json.dumps(competitor_results_dict)
    except Exception as e:
        return render_template('error.html', error=str(e))


def __get_all_ranking_dict(competitor_id, mysql_rows):
    # misc data to return
    year = 0
    squad_id = 0
    grade = 0

    last_rank = 0
    last_measurement = 0
    current_measurement = 0
    all_rank_dict = {}
    all_rank_total = 0
    event_id = 0
    for row in mysql_rows:
        all_rank_total +=1
        result_competitor_id = str(row[6])
        current_rank = row[12]
        event_id = row[1]
        resultStr = 'Unknown'
        if __is_race_event(event_id):
            current_measurement = Utils.format_track_time(row[3])
            resultStr = '{0}{1}'.format(current_measurement, row[4])
        elif __is_field_event(event_id):
            foot_part_of_distance = int(row[3])
            inch_part_of_distance = float(row[4])
            current_measurement = __get_distance_in_inches(foot_part_of_distance, inch_part_of_distance)
            if str(inch_part_of_distance).endswith('.0'):
                inch_part_of_distance = int(inch_part_of_distance)
            resultStr = '{0}\' {1}"'.format(foot_part_of_distance, inch_part_of_distance)

        current_rank, last_rank, current_measurement, last_measurement = __get_rank_measurement_metadata(
            current_rank, last_rank, current_measurement, last_measurement
        )

        if competitor_id == result_competitor_id and not all_rank_dict:
            all_rank_dict = {
                'Event': str(row[0]),
                'EventId': event_id,
                'FullName': str(row[2]),
                'Result': resultStr,
                'Grade': row[5],
                'CompetitorId': str(row[6]),
                'Year': row[7],
                'Squad': str(row[8]),
                'SquadId': row[9],
                'AthleteId': row[10],
                'GenderId': row[11],
                'AllRank': __get_rank(current_rank, event_id),
            }

    if all_rank_dict:
        # need to divide the total by 4 for relay events because there are 4 people with the same results
        all_rank_dict['AllTotal'] = __get_rank_total(all_rank_total, event_id)

    return all_rank_dict


def __get_rank_total(rank_total, event_id):
    return (rank_total / 4) if __is_relay_event(event_id) else rank_total


def __get_rank(rank, event_id):
    return ((rank + 3) / 4) if __is_relay_event(event_id) else rank


def __get_all_grade_ranking(competitor_id, mysql_rows, grade):
    last_rank = 0
    last_measurement = 0
    current_measurement = 0
    grade_rank = 0
    grade_rank_total = 0
    event_id = 0
    for row in mysql_rows:
        if grade == row[5]:
            grade_rank_total +=1
            current_rank = grade_rank_total
            event_id = row[1]
            if __is_race_event(event_id):
                current_measurement = Utils.format_track_time(row[3])
            elif __is_field_event(event_id):
                foot_part_of_distance = int(row[3])
                inch_part_of_distance = float(row[4])
                current_measurement = __get_distance_in_inches(foot_part_of_distance, inch_part_of_distance)
                if str(inch_part_of_distance).endswith('.0'):
                    inch_part_of_distance = int(inch_part_of_distance)

            current_rank, last_rank, current_measurement, last_measurement = __get_rank_measurement_metadata(
                current_rank, last_rank, current_measurement, last_measurement
            )

            if competitor_id == str(row[6]):
                grade_rank = current_rank

    return __get_rank(grade_rank, event_id), __get_rank_total(grade_rank_total, event_id)


def __get_year_squad_ranking(competitor_id, mysql_rows, year, squad_id):
    last_rank = 0
    last_measurement = 0
    current_measurement = 0
    year_squad_rank = 0
    year_squad_rank_total = 0
    event_id = 0
    for row in mysql_rows:
        if year == row[7] and squad_id == row[9]:
            year_squad_rank_total +=1
            current_rank = year_squad_rank_total
            event_id = row[1]
            if __is_race_event(event_id):
                current_measurement = Utils.format_track_time(row[3])
            elif __is_field_event(event_id):
                foot_part_of_distance = int(row[3])
                inch_part_of_distance = float(row[4])
                current_measurement = __get_distance_in_inches(foot_part_of_distance, inch_part_of_distance)
                if str(inch_part_of_distance).endswith('.0'):
                    inch_part_of_distance = int(inch_part_of_distance)

            current_rank, last_rank, current_measurement, last_measurement = __get_rank_measurement_metadata(
                current_rank, last_rank, current_measurement, last_measurement
            )

            if competitor_id == str(row[6]):
                year_squad_rank = current_rank

    return __get_rank(year_squad_rank, event_id), __get_rank_total(year_squad_rank_total, event_id)


@track_db_app.route('/getTrackAthletes', methods=['GET'])
def get_track_athletes():
    try:
        gender_id_str = request.args.get('genderId', default='2,3', type=str)

        cursor = mydb.cursor()
        cursor.execute('CALL GetTrackAthletes("{0}")'.format(gender_id_str))

        track_athletes_dict = []
        for row in cursor.fetchall():
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

        track_athlete_results = []
        personal_record_dict = {}
        cursor = mydb.cursor()
        cursor.execute('CALL GetTrackAthleteResults({0})'.format(athlete_id))

        more_results = True
        athlete_result_metadata_dict_tuple = ()
        event_to_result_dict = {}
        while more_results:
            # first save all the events, years, squad ids, competitor ids for the athlete
            if not athlete_result_metadata_dict_tuple:
                athlete_result_metadata_dict_tuple = cursor.fetchall()
            else:
                # save all the results for each of the events that the athlete competed in
                result_list = cursor.fetchall()
                if result_list:
                    event_id = result_list[0][1]
                    event_to_result_dict[event_id] = result_list
            more_results = cursor.nextset()

        # iterate over the metadata
        for athlete_result_metadata_dict in athlete_result_metadata_dict_tuple:
            # construct personal record key
            event_id = athlete_result_metadata_dict[0]
            event_sub_type_id = athlete_result_metadata_dict[3]
            event_id_str = '0{0}'.format(event_id) if event_id < 10 else event_id
            pr_key = '{0}.{1}'.format(event_sub_type_id, event_id_str)

            competitor_id = athlete_result_metadata_dict[2]
            mysql_rows = event_to_result_dict.get(event_id)
            # calculate the rankings by looking up the competitor id in the event specific results 
            all_rank_dict = __get_all_ranking_dict(competitor_id, mysql_rows)
            if all_rank_dict:
                grade_rank, grade_rank_total = __get_all_grade_ranking(competitor_id, mysql_rows, all_rank_dict['Grade'])
                all_rank_dict['GradeRank'] = grade_rank
                all_rank_dict['GradeRankTotal'] = grade_rank_total

                year_squad_rank, year_squad_rank_total = __get_year_squad_ranking(
                    competitor_id, mysql_rows, all_rank_dict['Year'], all_rank_dict['SquadId']
                )
                all_rank_dict['YearSquadRank'] = year_squad_rank
                all_rank_dict['YearSquadRankTotal'] = year_squad_rank_total

                track_athlete_results.append(all_rank_dict)

                # determine which are the personal records
                pr_result_dict = personal_record_dict.get(pr_key)
                update_pr = True if pr_result_dict is None else False
                if pr_result_dict is not None:
                    if all_rank_dict['AllRank'] <= pr_result_dict['AllRank']:
                        update_pr = True
                if update_pr:
                    personal_record_dict[pr_key] = all_rank_dict.copy()
                    personal_record_dict[pr_key]['PR'] = True

        # sort and add the personal records
        for pr_key in collections.OrderedDict(sorted(personal_record_dict.items())):
            track_athlete_results.append(personal_record_dict.get(pr_key))

        return json.dumps(track_athlete_results)
    except Exception as e:
        return render_template('error.html',error = str(e))


@track_db_app.route('/getTrackRaceResultsByEvent', methods=['GET'])
def get_track_race_results_by_event():
    try:
        event_id = request.args.get('eventId', default = 1, type = int)
        gender_id = request.args.get('genderId', default = 2, type = int)
        grade = request.args.get('grade', default = 0, type = int)

        cursor = mydb.cursor()
        if grade == 0:
            cursor.execute('CALL GetAllTrackRaceResults({0}, {1})'.format(event_id, gender_id))
        else:
            cursor.execute('CALL GetTrackRaceResultsByGrade({0}, {1}, {2})'.format(event_id, gender_id, grade))

        top_race_results_dict = []
        last_rank = 0
        last_time = 0
        for row in cursor.fetchall():
            current_rank = row[0]
            current_time = Utils.format_track_time(row[3])
            current_rank, last_rank, current_time, last_time = __get_rank_measurement_metadata(
                current_rank, last_rank, current_time, last_time
            )

            top_race_results_dict.append({
                'Rank': current_rank,
                'Event': row[1],
                'FullName': row[2],
                'Time': current_time,
                'RaceTimeTypeId': row[4],
                'Grade': row[5],
                'Year': row[6],
                'CompetitorId': row[7],
                'AthleteId': row[8],
            })

        return json.dumps(top_race_results_dict)
    except Exception as e:
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackFieldResultsByEvent', methods=['GET'])
def get_track_field_results_by_event():
    try:
        event_id = request.args.get('eventId', default = 29, type = int)
        gender_id = request.args.get('genderId', default = 3, type = int)
        grade = request.args.get('grade', default = 0, type = int)
 
        cursor = mydb.cursor()
        if grade == 0:
            cursor.execute('CALL GetAllTrackFieldResults({0}, {1})'.format(event_id, gender_id))
        else:
            cursor.execute('CALL GetTrackFieldResultsByGrade({0}, {1}, {2})'.format(event_id, gender_id, grade))

        top_field_results_dict = []
        last_rank = 0
        last_distance = 0
        for row in cursor.fetchall():
            current_rank = row[0]
            foot_part_of_distance = int(row[3])
            inch_part_of_distance = float(row[4])
            current_distance_in_inches = __get_distance_in_inches(foot_part_of_distance, inch_part_of_distance)
            current_rank, last_rank, current_distance_in_inches, last_distance = __get_rank_measurement_metadata(
                current_rank, last_rank, current_distance_in_inches, last_distance
            )

            top_field_results_dict.append({
                'Rank': current_rank,
                'Event': row[1],
                'FullName': row[2],
                'FootPartOfDistance': foot_part_of_distance,
                'InchPartOfDistance': inch_part_of_distance,
                'Grade': row[5],
                'Year': row[6],
                'CompetitorId': row[7],
                'AthleteId': row[8],
            })

        return json.dumps(top_field_results_dict)
    except Exception as e:
        return render_template('error.html', error=str(e))



@track_db_app.route('/getTrackRelayResultsByEvent', methods=['GET'])
def get_track_relay_results_by_event():
    try:
        event_id = request.args.get('eventId', default = 25, type = int)
        gender_id = request.args.get('genderId', default = 2, type = int)
        squad_id = request.args.get('squadId', default = 0, type = int)

        cursor = mydb.cursor()
        if squad_id == 0:
            cursor.execute('CALL GetAllTrackRelayResults({0}, {1})'.format(event_id, gender_id))
        else:
            cursor.execute('CALL GetTrackRelayResultsBySquad({0}, {1}, {2})'.format(event_id, gender_id, squad_id))

        top_relay_results_dict = []
        last_rank = 0
        last_time = 0
        for row in cursor.fetchall():
            current_rank = row[0]
            current_time = Utils.format_track_time(row[2])
            current_rank, last_rank, current_time, last_time = __get_rank_measurement_metadata(
                current_rank, last_rank, current_time, last_time
            )

            top_relay_results_dict.append({
                'Rank': current_rank,
                'Event': row[1],
                'Time': current_time,
                'RaceTimeTypeId': row[3],
                'Year': row[4],
                'FullName1': row[5],
                'Grade1': row[6],
                'CompetitorId1': row[7],
                'AthleteId1': row[8],
                'FullName2': row[9],
                'Grade2': row[10],
                'CompetitorId2': row[11],
                'AthleteId2': row[12],
                'FullName3': row[13],
                'Grade3': row[14],
                'CompetitorId3': row[15],
                'AthleteId3': row[16],
                'FullName4': row[17],
                'Grade4': row[18],
                'CompetitorId4': row[19],
                'AthleteId4': row[20],                
            })

        return json.dumps(top_relay_results_dict)
    except Exception as e:
        return render_template('error.html', error=str(e))


def __is_race_event(event_id):
    return (event_id >= 1 and event_id <= 28) or (event_id >= 38 and event_id <= 41)


def __is_field_event(event_id):
    return event_id >= 29 and event_id <= 37


def __is_relay_event(event_id):
    return (event_id >= 25 and event_id <= 28) or (event_id == 41)


def __get_distance_in_inches(foot_part_of_distance, inch_part_of_distance):
    return (12 * foot_part_of_distance) + inch_part_of_distance


def __get_rank_measurement_metadata(current_rank, last_rank, current_measurement, last_measurement):
    if last_rank > 0:
        if current_measurement == last_measurement:
            current_rank = last_rank
        else:
            last_rank = current_rank
            last_measurement = current_measurement
    else:
        last_rank = current_rank
        last_measurement = current_measurement
    return current_rank, last_rank, current_measurement, last_measurement

