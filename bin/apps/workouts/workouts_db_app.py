__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, json, request
import mysql.connector

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

        all_exercises_dict_list = []
        for row in data:
            all_exercises_dict_list.append({
                'ExerciseId': str(row[0]),
                'ExerciseName': str(row[1]).title(),
                'ExerciseLevel': row[2],
                'BodySplit': str(row[3]),
                'ExerciseType': str(row[4]),
                'YouTubeId': str(row[5]),
                'All': all_exercises
            })

        return json.dumps(all_exercises_dict_list)
    except Exception as e:
        return render_template('error.html',error = str(e))

