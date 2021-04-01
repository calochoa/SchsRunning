__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

import logging

from flask import Blueprint, render_template, json, request
from bin.utils import Utils
from bin.db.workouts.workouts_dai import WorkoutsDAI


workouts_db_app = Blueprint('workouts_db_app', __name__, template_folder='templates')

workouts_dai = WorkoutsDAI()


@workouts_db_app.route('/getExercises',methods=['GET'])
def get_exercises():
    """
    Get the exercises as a list of json for the given `bodySplitIds` and `exerciseLevels`
    within the request arguments.  Check the cache prior to querying the DB.  If a DB query 
    is required, then cache the results.
    Usage:
        - /templates/workouts/bodyweight-exercises/bodyweight-exercises.html
    :return: list of json from `Exercise` object
    """
    try:
        body_split_ids = request.args.get('bodySplitIds', default='all', type=str)
        exercise_levels = request.args.get('exerciseLevels', default='all', type=str)
        if exercise_levels == 'all':
            exercise_levels = '1,2,3,4,5,6'
        if body_split_ids == 'all':
            body_split_ids = 'bs0001,bs0002,bs0003,bs0004'
        exercises_cache_key = Utils.get_cache_key_two('get_exercises_', exercise_levels, body_split_ids)
        exercises = Utils.cache_get(exercises_cache_key)
        if not exercises:
            exercises = json.dumps(
                workouts_dai.get_exercises(exercise_levels, body_split_ids) if body_split_ids 
                else workouts_dai.get_all_exercises()
            )
            Utils.cache_set(exercises_cache_key, exercises)
        return exercises
    except Exception as e:
        logging.exception(e)
        return render_template('error.html',error = str(e))


@workouts_db_app.route('/getQuickies',methods=['GET'])
def get_quickies():
    """
    Get the quickies as a list of json for the given `bodySplitIds` and `quickieLevels`
    within the request arguments.  Check the cache prior to querying the DB.  If a DB 
    query is required, then cache the results.
    Usage:
        - /templates/workouts/quickies/quickies.html
    :return: list of json from `Quickie` object
    """
    try:
        body_split_ids = request.args.get('bodySplitIds', default='all', type=str)
        quickie_levels = request.args.get('quickieLevels', default='all', type=str)
        if quickie_levels == 'all':
            quickie_levels = '1,2,3,4,5'
        if body_split_ids == 'all':
            body_split_ids = 'bs0001,bs0002,bs0003,bs0004'
        quickies_cache_key = Utils.get_cache_key_two('get_quickies_', quickie_levels, body_split_ids)
        quickies = Utils.cache_get(quickies_cache_key)
        if not quickies:
            quickies = json.dumps(
                workouts_dai.get_quickies(quickie_levels, body_split_ids) if body_split_ids 
                else workouts_dai.get_all_quickies()
            )
            Utils.cache_set(quickies_cache_key, quickies)
        return quickies
    except Exception as e:
        logging.exception(e)
        return render_template('error.html',error = str(e))


@workouts_db_app.route('/getQuickieWorkouts',methods=['GET'])
def get_quickie_workouts():
    """
    Get the quickie workouts as a list of json for the given `bodySplitIds` and `workoutLevels`
    within the request arguments.  Check the cache prior to querying the DB.  If a DB query is 
    required, then cache the results.
    Usage:
        - /templates/workouts/quickie-workouts/quickie-workouts.html
    :return: list of json from `QuickieWorkout` object
    """
    try:
        body_split_ids = request.args.get('bodySplitIds', default='all', type=str)
        workout_levels = request.args.get('workoutLevels', default='all', type=str)
        if workout_levels == 'all':
            workout_levels = '1,2,3,4,5'
        if body_split_ids == 'all':
            body_split_ids = 'bs0001,bs0002,bs0003,bs0004'
        quickie_workouts_cache_key = Utils.get_cache_key_two('get_quickie_workouts_', workout_levels, body_split_ids)
        quickie_workouts = Utils.cache_get(quickie_workouts_cache_key)
        if not quickie_workouts:
            quickie_workouts = json.dumps(
                workouts_dai.get_quickie_workouts(workout_levels, body_split_ids) if body_split_ids 
                else workouts_dai.get_all_quickie_workouts()
            )
            Utils.cache_set(quickie_workouts_cache_key, quickie_workouts)
        return quickie_workouts
    except Exception as e:
        logging.exception(e)
        return render_template('error.html',error = str(e))


@workouts_db_app.route('/getQuickiesByIds',methods=['GET'])
def get_quickies_by_ids():
    """
    Get the quickies as a list of json for the given `quickieIds` within the request 
    arguments.  Check the cache prior to querying the DB.  If a DB query is required, 
    then cache the results.
    Usage:
        - /templates/workouts/quickie-workouts/quickie-workout.html
    :return: list of json from `Quickie` object
    """
    try:
        quickie_ids = request.args.get('quickieIds', default=None, type=str)
        quickies_by_ids_cache_key = Utils.get_cache_key_one('get_quickies_by_ids_', quickie_ids)
        quickies_by_ids = Utils.cache_get(quickies_by_ids_cache_key)
        if not quickies_by_ids:
            quickies_by_ids = json.dumps(workouts_dai.get_quickies_by_ids(quickie_ids))
            Utils.cache_set(quickies_by_ids_cache_key, quickies_by_ids)
        return quickies_by_ids
    except Exception as e:
        logging.exception(e)
        return render_template('error.html',error = str(e))
