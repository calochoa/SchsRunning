__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, json, request
import mysql.connector
import HTMLParser

from bin.utils import Utils


workouts_db_app = Blueprint('workouts_db_app', __name__, template_folder='templates')


# MySQL configurations
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
    database="quickies",
    auth_plugin='mysql_native_password'
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

        cursor = mydb.cursor()
        if body_split_ids:
            cursor.callproc('GetExercises', (exercise_levels, body_split_ids))
            all_exercises = False
        else:
            cursor.callproc('GetAllExercises')
            all_exercises = True
        for result in cursor.stored_results():
            data = result.fetchall()

        exercises_dict_list = []
        for row in data:
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

        cursor = mydb.cursor()
        if body_split_ids:
            cursor.callproc('GetQuickies', (quickie_levels, body_split_ids))
            all_quickies = False
        else:
            cursor.callproc('GetAllQuickies')
            all_quickies = True
        for result in cursor.stored_results():
            data = result.fetchall()

        quickies_dict_list = []
        for row in data:
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

        cursor = mydb.cursor()
        if body_split_ids:
            cursor.callproc('GetQuickieWorkouts', (workout_levels, body_split_ids))
            all_quickie_workouts = False
        else:
            cursor.callproc('GetAllQuickieWorkouts')
            all_quickie_workouts = True

        quickies_dict = {}
        quickie_workouts_dict_list = []
        for result in cursor.stored_results():
            data = result.fetchall()

            # check if the quickies dictionary is empty
            if not quickies_dict:
                # this assumes it is the first set of results
                # so iterate over each row to populate the quickies dictionary
                for row in data:
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
            else:
                # iterate over the quickie workout results
                for row in data:
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
        quickie_ids = HTMLParser.HTMLParser().unescape(request.args.get('quickieIds', default=None, type=str))

        cursor = mydb.cursor()
        cursor.callproc('GetQuickiesById', [quickie_ids])
        for result in cursor.stored_results():
            data = result.fetchall()

        # populate the quickies dictionary
        quickies_dict = {}
        for row in data:
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

