__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

import logging

from bin.db.common.mysql_controller import MySQLController
from bin.entities.common.coaches.coach import Coach
from bin.entities.common.coaches.coach_timeline import CoachTimeline
from bin.entities.common.coaches.coaches import Coaches


class CoachesDAI(object):

    def __init__(self, config_file='bin/conf/config.ini', section='mysql'):
        self.mysql = MySQLController(config_file=config_file, section=section)
    
    def get_coaches_by_year(self, year, coach_type_ids_str):
        """
        Call the stored procedure, `GetCoachesByYear` to get the coach as a list of json
        for the given year and coach type ids string.
        Usage:
            - /bin/apps/common/common_coaches_db_app.py
        :param year: year id (reference `CoachSeason` in DB)
        :param coach_type_ids_str: Coach type ids string (reference `CoachType` in DB)
        :return: list of json from `Coach` object
        """
        query = 'CALL GetCoachesByYear({0}, "{1}")'.format(year, coach_type_ids_str)
        return self.__get_json_coach_list(query)

    def get_coach_by_id(self, coach_id, coach_type_ids_str):
        """
        Call the stored procedure, `GetCoachById` to get the coach as a list of json
        for the given coach id and coach type ids string.
        Usage:
            - /bin/apps/common/common_coaches_db_app.py
        :param coach_id: coach id (reference `Coach` in DB)
        :param coach_type_ids_str: Coach type ids string (reference `CoachType` in DB)
        :return: list of json from `Coach` object
        """
        query = 'CALL GetCoachById({0}, "{1}")'.format(coach_id, coach_type_ids_str)
        return self.__get_json_coach_list(query)

    def __get_json_coach_list(self, query):
        """
        Get the coach as a list of json for the given query.
        :param query: mysql query
        :return: list of json from `Coach` object
        """
        try:
            results = self.__get_results(query)
            return [Coach(result).get_json() for result in results] if results else []
        except Exception as e:
            logging.exception(e)
            raise

    def get_coach_timeline(self, coach_type_ids_str):
        """
        Call the stored procedure, `GetCoachTimeline` to get the coach timeline as a 
        list of json for the given coach type ids string.
        Usage:
            - /bin/apps/common/common_coaches_db_app.py
        :param coach_type_ids_str: Coach type ids string (reference `CoachType` in DB)
        :return: list of json from `CoachTimeline` object
        """
        try:
            results = self.__get_results('CALL GetCoachTimeline("{0}")'.format(coach_type_ids_str))
            return [CoachTimeline(result).get_json() for result in results] if results else []
        except Exception as e:
            logging.exception(e)
            raise

    def get_coaches(self, coach_type_ids_str):
        """
        Call the stored procedure, `GetCoaches` to get the coaches as a list of json
        for the given coach type ids string.
        Usage:
            - /bin/apps/common/common_coaches_db_app.py
        :param coach_type_ids_str: Coach type ids string (reference `CoachType` in DB)
        :return: list of json from `Coaches` object
        """
        try:
            results = self.__get_results('CALL GetCoaches("{0}")'.format(coach_type_ids_str))
            return [Coaches(result).get_json() for result in results] if results else []
        except Exception as e:
            logging.exception(e)
            raise

    def __get_results(self, query):
        """
        Get the results as a dictionary for the given query.
        :param query: mysql query
        :return: dictionary results
        """
        return self.mysql.query_multi_with_fetchall_as_dict(query)
