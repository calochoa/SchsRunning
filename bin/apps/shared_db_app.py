__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, json, request
from bin.cache import cache
from iron_cache import *
import MySQLdb

from bin.utils import Utils


shared_db_app = Blueprint('shared_db_app', __name__, template_folder='templates')


shared_iron_cache = IronCache()
CACHE_NAME = 'shared_cache'
KEY_DELIM = '[#]'


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
        print (' + + + + ')
        val = cache.get('foo')
        print (val)
        if not val:
            cache.set('foo', 'barzz')
            print (' woot ')
        print (cache.get('foo'))
        print (' + + + + ')
        year = request.args.get('year', default = 2017, type = int)
        coach_type_ids_str = request.args.get('coachTypeIds', default = '1,2', type = str)

        coaches_by_year_cache_key = 'get_coaches_by_year_{0}{1}{2}'.format(year, KEY_DELIM, coach_type_ids_str)
        coaches_by_year = shared_iron_cache.get(cache=CACHE_NAME, key=coaches_by_year_cache_key)
        return coaches_by_year.value
    except Exception as e:
        coaches_by_year = db_get_coaches_by_year(year, coach_type_ids_str)
        shared_iron_cache.put(cache=CACHE_NAME, key=coaches_by_year_cache_key, value=coaches_by_year)
        return coaches_by_year


def db_get_coaches_by_year(year, coach_type_ids_str):
    try:
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

        coach_timeline_cache_key = 'get_coach_timeline_{0}'.format(coach_type_ids_str)
        coach_timeline = shared_iron_cache.get(cache=CACHE_NAME, key=coach_timeline_cache_key)
        return coach_timeline.value
    except Exception as e:
        coach_timeline = db_get_coach_timeline(coach_type_ids_str)
        shared_iron_cache.put(cache=CACHE_NAME, key=coach_timeline_cache_key, value=coach_timeline)
        return coach_timeline


def db_get_coach_timeline(coach_type_ids_str):
    try:
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
        coach_id = request.args.get('coachId', default = 1, type = int)
        coach_type_ids_str = request.args.get('coachTypeIds', default = '1,2', type = str)

        coach_by_id_cache_key = 'get_coach_by_id_{0}{1}{2}'.format(coach_id, KEY_DELIM, coach_type_ids_str)
        coach_by_id = shared_iron_cache.get(cache=CACHE_NAME, key=coach_by_id_cache_key)
        return coach_by_id.value
    except Exception as e:
        coach_by_id = db_get_coach_by_id(coach_id, coach_type_ids_str)
        shared_iron_cache.put(cache=CACHE_NAME, key=coach_by_id_cache_key, value=coach_by_id)
        return coach_by_id


def db_get_coach_by_id(coach_id, coach_type_ids_str):
    try:
        cursor = mydb.cursor()
        cursor.execute('CALL GetCoachById({0}, "{1}")'.format(coach_id,coach_type_ids_str))

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

        coaches_cache_key = 'get_coaches_{0}'.format(coach_type_ids_str)
        coaches = shared_iron_cache.get(cache=CACHE_NAME, key=coaches_cache_key)
        return coaches.value
    except Exception as e:
        coaches = db_get_coaches(coach_type_ids_str)
        shared_iron_cache.put(cache=CACHE_NAME, key=coaches_cache_key, value=coaches)
        return coaches


def db_get_coaches(coach_type_ids_str):
    try:
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

        awards_by_year_cache_key = 'get_awards_by_year_{0}{1}{2}'.format(year, KEY_DELIM, sport_id)
        awards_by_year = shared_iron_cache.get(cache=CACHE_NAME, key=awards_by_year_cache_key)
        return awards_by_year.value
    except Exception as e:
        awards_by_year = db_get_awards_by_year(year, sport_id)
        shared_iron_cache.put(cache=CACHE_NAME, key=awards_by_year_cache_key, value=awards_by_year)
        return awards_by_year


def db_get_awards_by_year(year, sport_id):
    try:
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
        award_id = request.args.get('awardId', default = 0, type = int)
        squad_id = request.args.get('squadId', default = 0, type = int)
        sport_id = request.args.get('sportId', default = 1, type = int)

        if award_id == 0 or award_id == 1 or award_id == 2:
            award_id = '1,2'
        if squad_id == 0:
            squad_id = '1,2,3,4'

        award_by_id_cache_key = 'get_award_by_id_{0}{1}{2}{3}{4}'.format(award_id, KEY_DELIM, squad_id, KEY_DELIM, sport_id)
        award_by_id = shared_iron_cache.get(cache=CACHE_NAME, key=award_by_id_cache_key)
        return award_by_id.value
    except Exception as e:
        award_by_id = db_get_award_by_id(award_id, squad_id, sport_id)
        shared_iron_cache.put(cache=CACHE_NAME, key=award_by_id_cache_key, value=award_by_id)
        return award_by_id


def db_get_award_by_id(award_id, squad_id, sport_id):
    try:
        cursor = mydb.cursor()
        cursor.execute('CALL GetAwardsById("{0}", "{1}", {2})'.format(award_id,squad_id,sport_id))
        
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
        squad_id = request.args.get('squadId', default = 0, type = int)
        sport_id = request.args.get('sportId', default = 1, type = int)

        if squad_id == 0:
            squad_id = '1,2,3,4'

        awards_timeline_cache_key = 'get_awards_timeline_{0}{1}{2}'.format(squad_id, KEY_DELIM, sport_id)
        awards_timeline = shared_iron_cache.get(cache=CACHE_NAME, key=awards_timeline_cache_key)
        return awards_timeline.value
    except Exception as e:
        awards_timeline = db_get_awards_timeline(squad_id, sport_id)
        shared_iron_cache.put(cache=CACHE_NAME, key=awards_timeline_cache_key, value=awards_timeline)
        return awards_timeline


def db_get_awards_timeline(squad_id, sport_id):
    try:
        cursor = mydb.cursor()
        cursor.execute('CALL GetAwardsTimeline("{0}", {1})'.format(squad_id,sport_id))

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
        spl_achv_id = request.args.get('splAchvId', default = 0, type = int)
        sport_id = request.args.get('sportId', default = 1, type = int)
        
        special_achievement_ids_str = '1,2,3' if spl_achv_id == 0 else str(spl_achv_id)

        special_achievers_by_id_cache_key = 'get_special_achievers_by_id_{0}{1}{2}'.format(special_achievement_ids_str, KEY_DELIM, sport_id)
        special_achievers_by_id = shared_iron_cache.get(cache=CACHE_NAME, key=special_achievers_by_id_cache_key)
        return special_achievers_by_id.value
    except Exception as e:
        special_achievers_by_id = db_get_special_achievers_by_id(special_achievement_ids_str, sport_id)
        shared_iron_cache.put(cache=CACHE_NAME, key=special_achievers_by_id_cache_key, value=special_achievers_by_id)
        return special_achievers_by_id


def db_get_special_achievers_by_id(special_achievement_ids_str, sport_id):
    try:
        cursor = mydb.cursor()
        cursor.execute('CALL GetSpecialAchieversById("{0}", {1})'.format(special_achievement_ids_str,sport_id))

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

