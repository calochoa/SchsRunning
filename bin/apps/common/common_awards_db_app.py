__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

import logging

from flask import Blueprint, render_template, json, request
from bin.utils import Utils
from bin.db.common.awards_dai import AwardsDAI


common_awards_db_app = Blueprint('common_awards_db_app', __name__, template_folder='templates')

awards_dai = AwardsDAI()


@common_awards_db_app.route('/getAwardsByYear', methods=['GET'])
def get_awards_by_year():
    """
    Get the awards as a list of json for the given `year` and `sportId` within the  
    request arguments.  Check the cache prior to querying the DB.  If a DB query is 
    required, then cache the results.
    Usage:
        - /templates/xc/season/season.html
    :return: list of json from `Award` object
    """
    try:
        year = request.args.get('year', default = 2017, type = int)
        sport_id = request.args.get('sportId', default = 1, type = int)
        awards_by_year_cache_key = Utils.get_cache_key_two('get_awards_by_year_', year, sport_id)
        awards_by_year = Utils.cache_get(awards_by_year_cache_key)
        if not awards_by_year:
            awards_by_year = json.dumps(awards_dai.get_awards_by_year(year, sport_id))
            Utils.cache_set(awards_by_year_cache_key, awards_by_year)
        return awards_by_year
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error = str(e))


@common_awards_db_app.route('/getAwardById', methods=['GET'])
def get_award_by_id():
    """
    Get the awards as a list of json for the given `awardId`, `squadId`, and `sportId` 
    within the request arguments.  Check the cache prior to querying the DB.  If a DB
    query is required, then cache the results.
    Usage:
        - /templates/xc/awards/award.html
    :return: list of json from `Award` object
    """
    try:
        award_id = request.args.get('awardId', default = 0, type = int)
        squad_id = request.args.get('squadId', default = 0, type = int)
        sport_id = request.args.get('sportId', default = 1, type = int)
        if award_id == 0 or award_id == 1 or award_id == 2:
            award_id = '1,2'
        if squad_id == 0:
            squad_id = '1,2,3,4'
        award_by_id_cache_key = Utils.get_cache_key_three('get_award_by_id_', award_id, squad_id, sport_id)
        award_by_id = Utils.cache_get(award_by_id_cache_key)
        if not award_by_id:
            award_by_id = json.dumps(awards_dai.get_award_by_id(award_id, squad_id, sport_id))
            Utils.cache_set(award_by_id_cache_key, award_by_id)
        return award_by_id
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error = str(e))


@common_awards_db_app.route('/getAwardsTimeline', methods=['GET'])
def get_awards_timeline():
    """
    Get the timeline of awards as a list of json for the given `squadId` and `sportId` 
    within the request arguments.  Check the cache prior to querying the DB.  If a DB
    query is required, then cache the results.
    Usage:
        - /templates/xc/awards/awardsTimeline.html
    :return: list of json from `Award` object
    """
    try:
        squad_id = request.args.get('squadId', default = 0, type = int)
        sport_id = request.args.get('sportId', default = 1, type = int)
        if squad_id == 0:
            squad_id = '1,2,3,4'
        awards_timeline_cache_key = Utils.get_cache_key_two('get_awards_timeline_', squad_id, sport_id)
        awards_timeline = Utils.cache_get(awards_timeline_cache_key)
        if not awards_timeline:
            awards_timeline = json.dumps(awards_dai.get_awards_timeline(squad_id, sport_id))
            Utils.cache_set(awards_timeline_cache_key, awards_timeline)
        return awards_timeline
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error = str(e))
