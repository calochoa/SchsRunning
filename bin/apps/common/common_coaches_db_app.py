__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

import logging

from flask import Blueprint, render_template, json, request
from bin.utils import Utils
from bin.db.common.coaches_dai import CoachesDAI


common_coaches_db_app = Blueprint('common_coaches_db_app', __name__, template_folder='templates')

coaches_dai = CoachesDAI()


@common_coaches_db_app.route('/getCoachesByYear', methods=['GET'])
def get_coaches_by_year():
    """
    Get the coach as a list of json for the given `year` and `coachTypeIds` within the 
    request arguments.  Check the cache prior to querying the DB.  If a DB query is 
    required, then cache the results.
    Usage:
        - /templates/xc/season/season.html
        - /templates/track/season/season.html
    :return: list of json from `Coach` object
    """
    try:
        year = request.args.get('year', default = 2017, type = int)
        coach_type_ids_str = request.args.get('coachTypeIds', default = '1,2', type = str)
        coaches_by_year_cache_key = Utils.get_cache_key_two('get_coaches_by_year_', year, coach_type_ids_str)
        coaches_by_year = Utils.cache_get(coaches_by_year_cache_key)
        if not coaches_by_year:
            coaches_by_year = json.dumps(coaches_dai.get_coaches_by_year(year, coach_type_ids_str))
            Utils.cache_set(coaches_by_year_cache_key, coaches_by_year)
        return coaches_by_year
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error = str(e))


@common_coaches_db_app.route('/getCoachTimeline', methods=['GET'])
def get_coach_timeline():
    """
    Get the coach timeline as a list of json for the given `coachTypeIds` within the 
    request arguments.  Check the cache prior to querying the DB.  If a DB query is
    required, then cache the results.
    Usage:
        - /templates/xc/coaches/coachTimeline.html
        - /templates/track/coaches/coachTimeline.html
    :return: list of json from `CoachTimeline` object
    """
    try:
        coach_type_ids_str = request.args.get('coachTypeIds', default = '1,2', type = str)
        coach_timeline_cache_key = Utils.get_cache_key_one('get_coach_timeline_', coach_type_ids_str)
        coach_timeline = Utils.cache_get(coach_timeline_cache_key)
        if not coach_timeline:
            coach_timeline = json.dumps(coaches_dai.get_coach_timeline(coach_type_ids_str))
            Utils.cache_set(coach_timeline_cache_key, coach_timeline)
        return coach_timeline
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error = str(e))


@common_coaches_db_app.route('/getCoachById', methods=['GET'])
def get_coach_by_id():
    """
    Get the coach as a list of json for the given `coachId` and `coachTypeIds` within 
    the request arguments.  Check the cache prior to querying the DB.  If a DB query 
    is required, then cache the results.
    Usage:
        - /templates/xc/coaches/coach.html
        - /templates/track/coaches/coach.html
    :return: list of json from `Coach` object
    """
    try:
        coach_id = request.args.get('coachId', default = 1, type = int)
        coach_type_ids_str = request.args.get('coachTypeIds', default = '1,2', type = str)
        coach_by_id_cache_key = Utils.get_cache_key_two('get_coach_by_id_', coach_id, coach_type_ids_str)
        coach_by_id = Utils.cache_get(coach_by_id_cache_key)
        if not coach_by_id:
            coach_by_id = json.dumps(coaches_dai.get_coach_by_id(coach_id, coach_type_ids_str))
            Utils.cache_set(coach_by_id_cache_key, coach_by_id)
        return coach_by_id
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error = str(e))


@common_coaches_db_app.route('/getCoaches', methods=['GET'])
def get_coaches():
    """
    Get the coaches as a list of json for the given `coachTypeIds` within the request
    arguments.  Check the cache prior to querying the DB.  If a DB query is required, 
    then cache the results.
    Usage:
        - /templates/xc/coaches/coaches.html
        - /templates/track/coaches/coaches.html
    :return: list of json from `Coaches` object
    """
    try:
        coach_type_ids_str = request.args.get('coachTypeIds', default = '1,2', type = str)
        coaches_cache_key = Utils.get_cache_key_one('get_coaches_', coach_type_ids_str)
        coaches = Utils.cache_get(coaches_cache_key)
        if not coaches:
            coaches = json.dumps(coaches_dai.get_coaches(coach_type_ids_str))
            Utils.cache_set(coaches_cache_key, coaches)
        return coaches
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error = str(e))
