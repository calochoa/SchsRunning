__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, json, request
from bin.cache import cache as mc_cache
from iron_cache import *
import MySQLdb

from bin.utils import Utils


workouts_db_app = Blueprint('workouts_db_app', __name__, template_folder='templates')


workouts_ic_cache = IronCache()
IC_CACHE_NAME = 'workouts_cache'


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
    db="quickies"
)
"""


@workouts_db_app.route('/getExercises',methods=['GET'])
def get_exercises():
    try:
        body_split_ids = request.args.get('bodySplitIds', default='all', type=str)
        exercise_levels = request.args.get('exerciseLevels', default='all', type=str)
        if exercise_levels == 'all':
            exercise_levels = '1,2,3,4,5,6'
        if body_split_ids == 'all':
            body_split_ids = 'bs0001,bs0002,bs0003,bs0004'
        return __mc_get_exercises(exercise_levels, body_split_ids)
    except Exception as e:
        return render_template('error.html',error = str(e))


def __mc_get_exercises(exercise_levels, body_split_ids):
    # First, check MemCachier for exercises
    try:
        exercises_cache_key = __get_exercises_cache_key(exercise_levels, body_split_ids)
        exercises = mc_cache.get(exercises_cache_key)
        if not exercises:
            exercises = __ic_get_exercises(exercise_levels, body_split_ids)
            mc_cache.set(exercises_cache_key, exercises)
        return exercises
    except Exception as e:
        return render_template('error.html',error = str(e))


def __ic_get_exercises(exercise_levels, body_split_ids):
    # Second, check Iron Cache for exercises
    try:
        exercises_cache_key = __get_exercises_cache_key(exercise_levels, body_split_ids)
        exercises = workouts_ic_cache.get(cache=IC_CACHE_NAME, key=exercises_cache_key)
        return exercises.value
    except Exception as e:
        exercises = __db_get_exercises(exercise_levels, body_split_ids)
        workouts_ic_cache.put(cache=IC_CACHE_NAME, key=exercises_cache_key, value=exercises)
        return exercises


def __get_exercises_cache_key(exercise_levels, body_split_ids):
    return Utils.get_cache_key_two('get_exercises_', exercise_levels, body_split_ids)


def __db_get_exercises(exercise_levels, body_split_ids):
    # Third, get exercises from MySQL database
    try:
        cursor = mydb.cursor()
        if body_split_ids:
            cursor.execute('CALL GetExercises("{0}", "{1}")'.format(exercise_levels, body_split_ids))
            all_exercises = False
        else:
            cursor.execute('CALL GetAllExercises()')
            all_exercises = True
        exercises_dict_list = []
        for row in cursor.fetchall():
            exercises_dict_list.append({
                'ExerciseId': str(row[0]),
                'ExerciseName': str(row[1]).title(),
                'ExerciseLevel': row[2],
                'BodySplit': str(row[3]),
                'ExerciseType': str(row[4]),
                'YouTubeId': str(row[5]),
                'All': all_exercises
            })
        return json.dumps(exercises_dict_list)
    except Exception as e:
        return render_template('error.html',error = str(e))


@workouts_db_app.route('/getQuickies',methods=['GET'])
def get_quickies():
    try:
        body_split_ids = request.args.get('bodySplitIds', default='all', type=str)
        quickie_levels = request.args.get('quickieLevels', default='all', type=str)
        if quickie_levels == 'all':
            quickie_levels = '1,2,3,4,5'
        if body_split_ids == 'all':
            body_split_ids = 'bs0001,bs0002,bs0003,bs0004'
        return __mc_get_quickies(quickie_levels, body_split_ids)
    except Exception as e:
        return render_template('error.html',error = str(e))


def __mc_get_quickies(quickie_levels, body_split_ids):
    # First, check MemCachier for quickies
    try:
        quickies_cache_key = __get_quickies_cache_key(quickie_levels, body_split_ids)
        quickies = mc_cache.get(quickies_cache_key)
        if not quickies:
            quickies = __ic_get_quickies(quickie_levels, body_split_ids)
            mc_cache.set(quickies_cache_key, quickies)
        return quickies
    except Exception as e:
        return render_template('error.html',error = str(e))


def __ic_get_quickies(quickie_levels, body_split_ids):
    # Second, check Iron Cache for quickies
    try:
        quickies_cache_key = __get_quickies_cache_key(quickie_levels, body_split_ids)
        quickies = workouts_ic_cache.get(cache=IC_CACHE_NAME, key=quickies_cache_key)
        return quickies.value
    except Exception as e:
        quickies = __db_get_quickies(quickie_levels, body_split_ids)
        workouts_ic_cache.put(cache=IC_CACHE_NAME, key=quickies_cache_key, value=quickies)
        return quickies


def __get_quickies_cache_key(quickie_levels, body_split_ids):
    return Utils.get_cache_key_two('get_quickies_', quickie_levels, body_split_ids)


def __db_get_quickies(quickie_levels, body_split_ids):
    # Third, get quickies from MySQL database
    try:
        cursor = mydb.cursor()
        if body_split_ids:
            cursor.execute('CALL GetQuickies("{0}","{1}")'.format(quickie_levels, body_split_ids))
            all_quickies = False
        else:
            cursor.execute('CALL GetAllQuickies()')
            all_quickies = True
        quickies_dict_list = []
        for row in cursor.fetchall():
            quickies_dict_list.append({
                'QuickieId': str(row[0]),
                'QuickieName': str(row[1]),
                'QuickieLevel': row[2],
                'QuickieType': str(row[3]),
                'BodySplit': str(row[4]),
                'Reps1': row[5],
                'ExerciseName1': str(row[6]).title(),
                'YouTubeId1': str(row[7]),
                'Reps2': row[8],
                'ExerciseName2': str(row[9]).title(),
                'YouTubeId2': str(row[10]),
                'Reps3': row[11],
                'ExerciseName3': str(row[12]).title(),
                'YouTubeId3': str(row[13]),
                'Reps4': row[14],
                'ExerciseName4': str(row[15]).title(),
                'YouTubeId4': str(row[16]),
                'All': all_quickies
            })
        return json.dumps(quickies_dict_list)
    except Exception as e:
        return render_template('error.html',error = str(e))


@workouts_db_app.route('/getQuickieWorkouts',methods=['GET'])
def get_quickie_workouts():
    try:
        body_split_ids = request.args.get('bodySplitIds', default='all', type=str)
        workout_levels = request.args.get('workoutLevels', default='all', type=str)
        if workout_levels == 'all':
            workout_levels = '1,2,3,4,5'
        if body_split_ids == 'all':
            body_split_ids = 'bs0001,bs0002,bs0003,bs0004'
        return __mc_get_quickie_workouts(workout_levels, body_split_ids)
    except Exception as e:
        return render_template('error.html',error = str(e))


def __mc_get_quickie_workouts(workout_levels, body_split_ids):
    # First, check MemCachier for quickie workouts
    try:
        quickie_workouts_cache_key = __get_quickie_workouts_cache_key(workout_levels, body_split_ids)
        quickie_workouts = mc_cache.get(quickie_workouts_cache_key)
        if not quickie_workouts:
            quickie_workouts = __ic_get_quickie_workouts(workout_levels, body_split_ids)
            mc_cache.set(quickie_workouts_cache_key, quickie_workouts)
        return quickie_workouts
    except Exception as e:
        return render_template('error.html',error = str(e))


def __ic_get_quickie_workouts(workout_levels, body_split_ids):
    # Second, check Iron Cache for quickie workouts
    try:
        quickie_workouts_cache_key = __get_quickie_workouts_cache_key(workout_levels, body_split_ids)
        quickie_workouts = workouts_ic_cache.get(cache=IC_CACHE_NAME, key=quickie_workouts_cache_key)
        return quickie_workouts.value
    except Exception as e:
        quickie_workouts = __db_get_quickie_workouts(workout_levels, body_split_ids)
        workouts_ic_cache.put(cache=IC_CACHE_NAME, key=quickie_workouts_cache_key, value=quickie_workouts)
        return quickie_workouts


def __get_quickie_workouts_cache_key(workout_levels, body_split_ids):
    return Utils.get_cache_key_two('get_quickie_workouts_', workout_levels, body_split_ids)


def __db_get_quickie_workouts(workout_levels, body_split_ids):
    # Third, get quickie workouts from MySQL database
    try:
        cursor = mydb.cursor()
        if body_split_ids:
            cursor.execute('CALL GetQuickieWorkouts("{0}", "{1}")'.format(workout_levels, body_split_ids))
            all_quickie_workouts = False
        else:
            cursor.execute('CALL GetAllQuickieWorkouts()')
            all_quickie_workouts = True
        quickies_dict = {}
        # so iterate over each row to populate the quickies dictionary
        for row in cursor.fetchall():
            quickie_id = str(row[0])
            quickies_dict[quickie_id] = {
                'QuickieId': quickie_id,
                'QuickieName': str(row[1]),
                'QuickieLevel': row[2],
                'QuickieType': str(row[3]),
                'BodySplit': str(row[4]),
                'Reps1': row[5],
                'ExerciseName1': str(row[6]).title(),
                'YouTubeId1': str(row[7]),
                'Reps2': row[8],
                'ExerciseName2': str(row[9]).title(),
                'YouTubeId2': str(row[10]),
                'Reps3': row[11],
                'ExerciseName3': str(row[12]).title(),
                'YouTubeId3': str(row[13]),
                'Reps4': row[14],
                'ExerciseName4': str(row[15]).title(),
                'YouTubeId4': str(row[16]),
            }
        cursor.nextset()
        quickie_workouts_dict_list = []
        # iterate over the quickie workout results
        for row in cursor.fetchall():
            quickie_list = []
            # iterate over the quickie ids
            for quickie_id in str(row[4]).split(','):
                # look up the quickie id in the dictionary and add it to the quickie list
                quickie_list.append(quickies_dict.get(quickie_id.strip()))
            quickie_workouts_dict_list.append({
                'WorkoutId': str(row[0]),
                'WorkoutName': str(row[1]).title(),
                'WorkoutLevel': row[2],
                'BodySplit': str(row[3]),
                'Quickies': quickie_list,
                'All': all_quickie_workouts
            })
        return json.dumps(quickie_workouts_dict_list)
    except Exception as e:
        return render_template('error.html',error = str(e))


@workouts_db_app.route('/getQuickiesByIds',methods=['GET'])
def get_quickies_by_ids():
    try:
        quickie_ids = request.args.get('quickieIds', default=None, type=str)
        return __mc_get_quickies_by_ids(quickie_ids)
    except Exception as e:
        return render_template('error.html',error = str(e))


def __mc_get_quickies_by_ids(quickie_ids):
    # First, check MemCachier for quickies by ids
    try:
        quickies_by_ids_cache_key = __get_quickies_by_ids_cache_key(quickie_ids)
        quickies_by_ids = mc_cache.get(quickies_by_ids_cache_key)
        if not quickies_by_ids:
            quickies_by_ids = __ic_get_quickies_by_ids(quickie_ids)
            mc_cache.set(quickies_by_ids_cache_key, quickies_by_ids)
        return quickies_by_ids
    except Exception as e:
        return render_template('error.html',error = str(e))


def __ic_get_quickies_by_ids(quickie_ids):
    # Second, check Iron Cache for quickies by ids
    try:
        quickies_by_ids_cache_key = __get_quickies_by_ids_cache_key(quickie_ids)
        quickies_by_ids = workouts_ic_cache.get(cache=IC_CACHE_NAME, key=quickies_by_ids_cache_key)
        return quickies_by_ids.value
    except Exception as e:
        quickies_by_ids = __db_get_quickies_by_ids(quickie_ids)
        workouts_ic_cache.put(cache=IC_CACHE_NAME, key=quickies_by_ids_cache_key, value=quickies_by_ids)
        return quickies_by_ids


def __get_quickies_by_ids_cache_key(quickie_ids):
    return Utils.get_cache_key_one('get_quickies_by_ids_', quickie_ids)


def __db_get_quickies_by_ids(quickie_ids):
    # Third, get quickies by ids from MySQL database
    try:
        cursor = mydb.cursor()
        cursor.execute('CALL GetQuickiesById("{0}")'.format(quickie_ids))
        # populate the quickies dictionary
        quickies_dict = {}
        for row in cursor.fetchall():
            quickie_id = str(row[0])
            quickies_dict[quickie_id] = {
                'QuickieId': quickie_id,
                'QuickieName': str(row[1]),
                'QuickieLevel': row[2],
                'QuickieType': str(row[3]),
                'BodySplit': str(row[4]),
                'Reps1': row[5],
                'ExerciseName1': str(row[6]).title(),
                'YouTubeId1': str(row[7]),
                'Reps2': row[8],
                'ExerciseName2': str(row[9]).title(),
                'YouTubeId2': str(row[10]),
                'Reps3': row[11],
                'ExerciseName3': str(row[12]).title(),
                'YouTubeId3': str(row[13]),
                'Reps4': row[14],
                'ExerciseName4': str(row[15]).title(),
                'YouTubeId4': str(row[16]),
            }
        # create the list of quickies dictionary based on the input quickie ids
        quickies_dict_list = []
        for quickie_id in quickie_ids.split(','):
            quickies_dict_list.append(quickies_dict.get(quickie_id.strip()))
        return json.dumps(quickies_dict_list)
    except Exception as e:
        return render_template('error.html',error = str(e))

