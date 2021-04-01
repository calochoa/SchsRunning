__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

import logging

from flask import Blueprint, render_template, json, request
from bin.utils import Utils
from bin.db.common.special_achievers_dai import SpecialAchieversDAI


common_special_achievers_db_app = Blueprint('common_special_achievers_db_app', __name__, template_folder='templates')

special_achievers_dai = SpecialAchieversDAI()


@common_special_achievers_db_app.route('/getSpecialAchieversById', methods=['GET'])
def get_special_achievers_by_id():
    """
    Get the special achievers as a list of json for the given `splAchvId` and `sportId` 
    within the request arguments.  Check the cache prior to querying the DB.  If a DB
    query is required, then cache the results.
    Usage:
        - /templates/xc/special-achievements/specialAchievement.html
        - /templates/track/special-achievements/specialAchievement.html
    :return: list of json from `SpecialAchievers` object
    """
    try:
        spl_achv_id = request.args.get('splAchvId', default = 0, type = int)
        sport_id = request.args.get('sportId', default = 1, type = int)
        special_achievement_ids_str = '1,2,3' if spl_achv_id == 0 else str(spl_achv_id)
        special_achievers_by_id_cache_key = Utils.get_cache_key_two('get_special_achievers_by_id_', special_achievement_ids_str, sport_id)
        special_achievers_by_id = Utils.cache_get(special_achievers_by_id_cache_key)
        if not special_achievers_by_id:
            special_achievers_by_id = json.dumps(special_achievers_dai.get_special_achievers_by_id(special_achievement_ids_str, sport_id))
            Utils.cache_set(special_achievers_by_id_cache_key, special_achievers_by_id)
        return special_achievers_by_id
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error = str(e))
