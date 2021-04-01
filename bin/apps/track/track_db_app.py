__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

import logging

from flask import Blueprint, render_template, json, request
from bin.utils import Utils
from bin.db.track.track_dai import TrackDAI
from bin.db.track.track_results_dai import TrackResultsDAI


track_db_app = Blueprint('track_db_app', __name__, template_folder='templates')

track_dai = TrackDAI()
track_results_dai = TrackResultsDAI()


@track_db_app.route('/getTrackHallfOfFameRaceResults', methods=['GET'])
def get_track_hall_of_fame_race_results():
    """
    Get the hall of fame race results as a list of json for the given `eventId` and `genderId`
    within the request arguments.  Check the cache prior to querying the DB.  If a DB query is 
    required, then cache the results.
    Usage:
        - /templates/track/hall-of-fame/hallOfFameRaceResults.html
    :return: list of json from `TrackRaceResult` object
    """
    try:
        event_id = request.args.get('eventId', default = 1, type = int)
        gender_id = request.args.get('genderId', default = 2, type = int)
        track_hof_race_results_cache_key = Utils.get_cache_key_two('get_track_hall_of_fame_race_results_', event_id, gender_id)
        track_hof_race_results = Utils.cache_get(track_hof_race_results_cache_key)
        if not track_hof_race_results:
            track_hof_race_results = json.dumps(track_results_dai.get_track_hof_race_results(event_id, gender_id))
            Utils.cache_set(track_hof_race_results_cache_key, track_hof_race_results)
        return track_hof_race_results
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackHallfOfFameRelayResults', methods=['GET'])
def get_track_hall_of_fame_relay_results():
    """
    Get the hall of fame relay results as a list of json for the given `eventId` and `genderId`
    within the request arguments.  Check the cache prior to querying the DB.  If a DB query is 
    required, then cache the results.
    Usage:
        - /templates/track/hall-of-fame/hallOfFameRelayResults.html
    :return: list of json from `TrackRelayResult` object
    """
    try:
        event_id = request.args.get('eventId', default = 25, type = int)
        gender_id = request.args.get('genderId', default = 2, type = int)
        track_hof_relay_results_cache_key = Utils.get_cache_key_two('get_track_hall_of_fame_relay_results_', event_id, gender_id)
        track_hof_relay_results = Utils.cache_get(track_hof_relay_results_cache_key)
        if not track_hof_relay_results:
            track_hof_relay_results = json.dumps(track_results_dai.get_track_hof_relay_results(event_id, gender_id))
            Utils.cache_set(track_hof_relay_results_cache_key, track_hof_relay_results)
        return track_hof_relay_results
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackHallfOfFameFieldResults', methods=['GET'])
def get_track_hall_of_fame_field_results():
    """
    Get the hall of fame field results as a list of json for the given `eventId` and `genderId`
    within the request arguments.  Check the cache prior to querying the DB.  If a DB query is 
    required, then cache the results.
    Usage:
        - /templates/track/hall-of-fame/hallOfFameFieldResults.html
    :return: list of json from `TrackFieldResult` object
    """
    try:
        event_id = request.args.get('eventId', default = 29, type = int)
        gender_id = request.args.get('genderId', default = 3, type = int)
        track_hof_field_results_cache_key = Utils.get_cache_key_two('get_track_hall_of_fame_field_results_', event_id, gender_id)
        track_hof_field_results = Utils.cache_get(track_hof_field_results_cache_key)
        if not track_hof_field_results:
            track_hof_field_results = json.dumps(track_results_dai.get_track_hof_field_results(event_id, gender_id))
            Utils.cache_set(track_hof_field_results_cache_key, track_hof_field_results)
        return track_hof_field_results
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackCompetitorsByYear', methods=['GET'])
def get_track_competitors_by_year():
    """
    Get the competitors as a list of json for the given `year` within the request arguments.  
    Check the cache prior to querying the DB.  If a DB query is required, then cache the results.
    Usage:
        - /templates/track/season/season.html
    :return: list of json from `Competitor` object
    """
    try:
        year = request.args.get('year', default = 2019, type = int)
        track_competitors_by_year = json.dumps(track_dai.get_track_competitors_by_year(year))
        '''
        track_competitors_by_year_cache_key = Utils.get_cache_key_one('get_track_competitors_by_year_', year)
        track_competitors_by_year = Utils.cache_get(track_competitors_by_year_cache_key)
        if not track_competitors_by_year:
            track_competitors_by_year = json.dumps(track_dai.get_track_competitors_by_year(year))
            Utils.cache_set(track_competitors_by_year_cache_key, track_competitors_by_year)
        '''
        return track_competitors_by_year
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackEventsByYear', methods=['GET'])
def get_track_events_by_year():
    """
    Get the events/squads as a list of json for the given `year` within the request arguments.  
    Check the cache prior to querying the DB.  If a DB query is required, then cache the results.
    Usage:
        - /templates/track/season/season.html
        - /templates/track/results/fieldResults.html
        - /templates/track/results/raceResults.html
        - /templates/track/results/relayResults.html
    :return: list of json from `EventSquad` object
    """
    try:
        year = request.args.get('year', default = 2019, type = int)
        track_events_by_year_cache_key = Utils.get_cache_key_one('get_track_events_by_year_', year)
        track_events_by_year = Utils.cache_get(track_events_by_year_cache_key)
        if not track_events_by_year:
            track_events_by_year = json.dumps(track_dai.get_track_events_by_year(year))
            Utils.cache_set(track_events_by_year_cache_key, track_events_by_year)
        return track_events_by_year
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackRaceResults', methods=['GET'])
def get_track_race_results():
    """
    Get the race results as a list of json for the given `eventId`, `squadId`, and `year`
    within the request arguments.  Check the cache prior to querying the DB.  If a DB query is 
    required, then cache the results.
    Usage:
        - /templates/track/results/raceResults.html
    :return: list of json from `TrackRaceResult` object
    """
    try:
        event_id = request.args.get('eventId', default = 1, type = int)
        squad_id = request.args.get('squadId', default = 1, type = int)
        year = request.args.get('year', default = 2019, type = int)
        track_race_results_cache_key = Utils.get_cache_key_three('get_track_race_results_', event_id, squad_id, year)
        track_race_results = Utils.cache_get(track_race_results_cache_key)
        if not track_race_results:
            track_race_results = json.dumps(track_results_dai.get_track_race_results(event_id, squad_id, year))
            Utils.cache_set(track_race_results_cache_key, track_race_results)
        return track_race_results
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackFieldResults', methods=['GET'])
def get_track_field_results():
    """
    Get the field results as a list of json for the given `eventId`, `squadId`, and `year`
    within the request arguments.  Check the cache prior to querying the DB.  If a DB query is 
    required, then cache the results.
    Usage:
        - /templates/track/results/fieldResults.html
    :return: list of json from `TrackFieldResult` object
    """
    try:
        event_id = request.args.get('eventId', default = 29, type = int)
        squad_id = request.args.get('squadId', default = 1, type = int)
        year = request.args.get('year', default = 2019, type = int)
        track_field_results_cache_key = Utils.get_cache_key_three('get_track_field_results_', event_id, squad_id, year)
        track_field_results = Utils.cache_get(track_field_results_cache_key)
        if not track_field_results:
            track_field_results = json.dumps(track_results_dai.get_track_field_results(event_id, squad_id, year))
            Utils.cache_set(track_field_results_cache_key, track_field_results)
        return track_field_results
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackRelayResults', methods=['GET'])
def get_track_relay_results():
    """
    Get the relay results as a list of json for the given `eventId`, `squadId`, and `year`
    within the request arguments.  Check the cache prior to querying the DB.  If a DB query is 
    required, then cache the results.
    Usage:
        - /templates/track/results/relayResults.html
    :return: list of json from `TrackRelayResult` object
    """
    try:
        event_id = request.args.get('eventId', default = 25, type = int)
        squad_id = request.args.get('squadId', default = 1, type = int)
        year = request.args.get('year', default = 2019, type = int)
        track_relay_results_cache_key = Utils.get_cache_key_three('get_track_relay_results_', event_id, squad_id, year)
        track_relay_results = Utils.cache_get(track_relay_results_cache_key)
        if not track_relay_results:
            track_relay_results = json.dumps(track_results_dai.get_track_relay_results(event_id, squad_id, year))
            Utils.cache_set(track_relay_results_cache_key, track_relay_results)
        return track_relay_results
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackCompetitorResults', methods=['GET'])
def get_track_competitor_results():
    """
    Get the track competitor results as a list of json for the given `competitorId` within the 
    request arguments.  Check the cache prior to querying the DB.  If a DB query is required, 
    then cache the results.
    Usage:
        - /templates/track/competitors/competitor.html
    :return: list of json from `TrackCompetitorResult` object
    """
    try:
        competitor_id = request.args.get('competitorId', default='1000197.12', type=str)
        track_competitor_results_cache_key = Utils.get_cache_key_one('get_track_competitor_results_', competitor_id)
        track_competitor_results = Utils.cache_get(track_competitor_results_cache_key)
        if not track_competitor_results:
            track_competitor_results = json.dumps(track_results_dai.get_track_competitor_results(competitor_id))
            Utils.cache_set(track_competitor_results_cache_key, track_competitor_results)
        return track_competitor_results
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackAthletes', methods=['GET'])
def get_track_athletes():
    """
    Get the athletes as a list of json for the given `genderId` within the request arguments.  
    Check the cache prior to querying the DB.  If a DB query is required, then cache the results.
    Usage:
        - /templates/track/athlete/athletes.html
    :return: list of json from `Athlete` object
    """
    try:
        gender_id = request.args.get('genderId', default='2,3', type=str)
        track_athletes_cache_key = Utils.get_cache_key_one('get_track_athletes_', gender_id)
        track_athletes = Utils.cache_get(track_athletes_cache_key)
        if not track_athletes:
            track_athletes = json.dumps(track_dai.get_track_athletes(gender_id))
            Utils.cache_set(track_athletes_cache_key, track_athletes)
        return track_athletes
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackAthleteResults',methods=['GET'])
def get_track_athlete_results():
    """
    Get the track athlete results as a list of json for the given `athleteId` within the 
    request arguments.  Check the cache prior to querying the DB.  If a DB query is required, 
    then cache the results.
    Usage:
        - /templates/track/athletes/athlete.html
    :return: list of json from `TrackCompetitorResult` object
    """
    try:
        athlete_id = request.args.get('athleteId', default=1, type=int)
        track_athlete_results_cache_key = Utils.get_cache_key_one('get_track_athlete_results_', athlete_id)
        track_athlete_results = Utils.cache_get(track_athlete_results_cache_key)
        if not track_athlete_results:
            track_athlete_results = json.dumps(track_results_dai.get_track_athlete_results(athlete_id))
            Utils.cache_set(track_athlete_results_cache_key, track_athlete_results)
        return track_athlete_results
    except Exception as e:
        logging.exception(e)
        return render_template('error.html',error = str(e))


@track_db_app.route('/getTrackRaceResultsByEvent', methods=['GET'])
def get_track_race_results_by_event():
    """
    Get the race results by event as a list of json for the given `eventId`, `genderId`, and 
    `grade` within the request arguments.  Check the cache prior to querying the DB.  If a DB 
    query is required, then cache the results.
    Usage:
        - /templates/track/events/race-results.html
    :return: list of json from `TrackRaceResult` object
    """
    try:
        event_id = request.args.get('eventId', default = 1, type = int)
        gender_id = request.args.get('genderId', default = 2, type = int)
        grade = request.args.get('grade', default = 0, type = int)
        track_race_results_by_event_cache_key = Utils.get_cache_key_three('get_track_race_results_by_event_', event_id, gender_id, grade)
        track_race_results_by_event = Utils.cache_get(track_race_results_by_event_cache_key)
        if not track_race_results_by_event:
            track_race_results_by_event = json.dumps(track_results_dai.get_track_race_results_by_event(event_id, gender_id, grade))
            Utils.cache_set(track_race_results_by_event_cache_key, track_race_results_by_event)
        return track_race_results_by_event
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackFieldResultsByEvent', methods=['GET'])
def get_track_field_results_by_event():
    """
    Get the field results by event as a list of json for the given `eventId`, `genderId`, and 
    `grade` within the request arguments.  Check the cache prior to querying the DB.  If a DB 
    query is required, then cache the results.
    Usage:
        - /templates/track/events/field-results.html
    :return: list of json from `TrackFieldResult` object
    """
    try:
        event_id = request.args.get('eventId', default = 29, type = int)
        gender_id = request.args.get('genderId', default = 3, type = int)
        grade = request.args.get('grade', default = 0, type = int)
        track_field_results_by_event_cache_key = Utils.get_cache_key_three('get_track_field_results_by_event_', event_id, gender_id, grade)
        track_field_results_by_event = Utils.cache_get(track_field_results_by_event_cache_key)
        if not track_field_results_by_event:
            track_field_results_by_event = json.dumps(track_results_dai.get_track_field_results_by_event(event_id, gender_id, grade))
            Utils.cache_set(track_field_results_by_event_cache_key, track_field_results_by_event)
        return track_field_results_by_event
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error=str(e))


@track_db_app.route('/getTrackRelayResultsByEvent', methods=['GET'])
def get_track_relay_results_by_event():
    """
    Get the relay results by event as a list of json for the given `eventId`, `genderId`, and 
    `squadId` within the request arguments.  Check the cache prior to querying the DB.  If a DB 
    query is required, then cache the results.
    Usage:
        - /templates/track/events/relay-results.html
    :return: list of json from `TrackRelayResult` object
    """
    try:
        event_id = request.args.get('eventId', default = 25, type = int)
        gender_id = request.args.get('genderId', default = 2, type = int)
        squad_id = request.args.get('squadId', default = 0, type = int)
        track_relay_results_by_event_cache_key = Utils.get_cache_key_three('get_track_relay_results_by_event_', event_id, gender_id, squad_id)
        track_relay_results_by_event = Utils.cache_get(track_relay_results_by_event_cache_key)
        if not track_relay_results_by_event:
            track_relay_results_by_event = json.dumps(track_results_dai.get_track_relay_results_by_event(event_id, gender_id, squad_id))
            Utils.cache_set(track_relay_results_by_event_cache_key, track_relay_results_by_event)
        return track_relay_results_by_event
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error=str(e))

