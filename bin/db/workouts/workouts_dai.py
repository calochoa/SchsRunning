__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

import logging

from bin.db.common.mysql_controller import MySQLController
from bin.entities.workouts.exercise import Exercise
from bin.entities.workouts.quickie import Quickie
from bin.entities.workouts.quickie_workout import QuickieWorkout


class WorkoutsDAI(object):

    def __init__(self, config_file='bin/conf/config.ini', section='mysql workout'):
        self.mysql = MySQLController(config_file=config_file, section=section)

    def get_exercises(self, exercise_levels, body_split_ids):
        """
        Call the stored procedure, `GetExercises`, to get the exercises as a list of json for 
        the given exercise levels and body split ids.
        Usage:
            - /bin/apps/workouts/workouts_db_app.py
        :param exercise_levels: exercise levels (reference `Exercises` in DB)
        :param body_split_ids: body split ids (reference `BodySplits` in DB)
        :return: list of json from `Exercise` object
        """
        print('get_exercises')
        query = 'CALL GetExercises("{0}", "{1}")'.format(exercise_levels, body_split_ids)
        return self.__get_json_exercise_list(query)

    def get_all_exercises(self):
        """
        Call the stored procedure, `GetAllExercises`, to get all the exercises as a list of json.
        Usage:
            - /bin/apps/workouts/workouts_db_app.py
        :return: list of json from `Exercise` object
        """
        print('get_all_exercises')
        query = 'CALL GetAllExercises()'
        return self.__get_json_exercise_list(query, all_exercises=True)

    def __get_json_exercise_list(self, query, all_exercises=False):
        """
        Get the exercises as a list of json for the given query.
        :param query: mysql query
        :param all_exercises: boolean indicating all exercises
        :return: list of json from `Exercise` object
        """
        try:
            results = self.__get_results(query)
            return [Exercise(result, all_exercises=all_exercises).get_json() for result in results] if results else []
        except Exception as e:
            logging.exception(e)
            raise

    def get_quickies(self, quickie_levels, body_split_ids):
        """
        Call the stored procedure, `GetQuickies`, to get the quickies as a list of json for 
        the given quickie levels and body split ids.
        Usage:
            - /bin/apps/workouts/workouts_db_app.py
        :param quickie_levels: quickie levels (reference `Quickies` in DB)
        :param body_split_ids: body split ids (reference `BodySplits` in DB)
        :return: list of json from `Quickie` object
        """
        query = 'CALL GetQuickies("{0}","{1}")'.format(quickie_levels, body_split_ids)
        return self.__get_json_quickie_list(query)

    def get_all_quickies(self):
        """
        Call the stored procedure, `GetAllQuickies`, to get all the quickies as a list of json.
        Usage:
            - /bin/apps/workouts/workouts_db_app.py
        :return: list of json from `Quickie` object
        """
        query = 'CALL GetAllQuickies()'
        return self.__get_json_quickie_list(query, all_quickies=True)

    def __get_json_quickie_list(self, query, all_quickies=False):
        """
        Get the quickies as a list of json for the given query.
        :param query: mysql query
        :param all_quickies: boolean indicating all quickies
        :return: list of json from `Quickie` object
        """
        try:
            results = self.__get_results(query)
            return [Quickie(result, all_quickies=all_quickies).get_json() for result in results] if results else []
        except Exception as e:
            logging.exception(e)
            raise

    def get_quickie_workouts(self, workout_levels, body_split_ids):
        """
        Call the stored procedure, `GetQuickieWorkouts`, to get the quickie workouts as a  
        list of json for the given workout levels and body split ids.
        Usage:
            - /bin/apps/workouts/workouts_db_app.py
        :param workout_levels: workout levels (reference `QuickieWorkouts` in DB)
        :param body_split_ids: body split ids (reference `BodySplits` in DB)
        :return: list of json from `QuickieWorkout` object
        """
        query = 'CALL GetQuickieWorkouts("{0}", "{1}")'.format(workout_levels, body_split_ids)
        return self.__get_json_quickie_workout_list(query)

    def get_all_quickie_workouts(self):
        """
        Call the stored procedure, `GetAllQuickieWorkouts`, to get all the quickie workouts 
        as a list of json.
        Usage:
            - /bin/apps/workouts/workouts_db_app.py
        :return: list of json from `QuickieWorkout` object
        """
        query = 'CALL GetAllQuickieWorkouts()'
        return self.__get_json_quickie_workout_list(query, all_workouts=True)

    def __get_json_quickie_workout_list(self, query, all_workouts=False):
        """
        Get the quickie workouts as a list of json for the given query.
        :param query: mysql query
        :param all_workouts: boolean indicating all workouts
        :return: list of json from `QuickieWorkout` object
        """
        try:
            quickie_workouts = []
            quickie_json_dict = {}
            for result in self.__get_results(query):
                if len(result) == 5:
                    quickie_workouts.append(QuickieWorkout(result, all_workouts=all_workouts))
                else:
                    quickie = Quickie(result)
                    quickie_json_dict[quickie.quickie_id] = quickie.get_json()
            for quickie_workout in quickie_workouts:
                quickie_workout.set_quickie_json_list(quickie_json_dict)
            return [quickie_workout.get_json() for quickie_workout in quickie_workouts] if quickie_workouts else []
        except Exception as e:
            logging.exception(e)
            raise

    def get_quickies_by_ids(self, quickie_ids):
        """
        Call the stored procedure, `GetQuickiesById`, to get the quickies as a list of json for 
        the given quickie ids (in the order provided).
        Usage:
            - /bin/apps/workouts/workouts_db_app.py
        :param quickie_ids: quickie ids (reference `Quickies` in DB)
        :return: list of json from `Quickie` object
        """
        quickies_dict = {}
        for result in self.__get_results('CALL GetQuickiesById("{0}")'.format(quickie_ids)):
            quickie = Quickie(result)
            quickies_dict[quickie.quickie_id] = quickie.get_json()
        return [quickies_dict.get(quickie_id.strip()) for quickie_id in quickie_ids.split(',')]

    def __get_results(self, query):
        """
        Get the results as a dictionary for the given query.
        :param query: mysql query
        :return: dictionary results
        """
        return self.mysql.query_multi_with_fetchall_as_dict(query)
