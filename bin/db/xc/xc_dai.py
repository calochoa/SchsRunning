__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

import logging

from bin.db.common.mysql_controller import MySQLController
from bin.entities.xc.xc_course import XcCourse
from bin.entities.common.misc.athlete import Athlete
from bin.entities.common.misc.competitor import Competitor
from bin.entities.xc.xc_race import XcRace


class XcDAI(object):

    def __init__(self, config_file='bin/conf/config.ini', section='mysql'):
        self.mysql = MySQLController(config_file=config_file, section=section)

    def get_course_info(self, course_id):
        """
        Call the stored procedure, `GetCourseInfo`, to get the course as a list of json
        for the given course id.
        Usage:
            - /bin/apps/xc/xc_db_app.py
        :param course_id: course id (reference `Course` in DB)
        :return: list of json from `XcCourse` object
        """
        try:
            results = self.__get_results('CALL GetCourseInfo({0})'.format(course_id))
            return [XcCourse(result).get_json() for result in results] if results else []
        except Exception as e:
            logging.exception(e)
            raise

    def get_xc_runners(self, gender_id):
        """
        Call the stored procedure, `GetXcRunners`, to get the runner as a list of json
        for the given gender id.
        Usage:
            - /bin/apps/xc/xc_db_app.py
        :param gender_id: gender id (reference `Gender` in DB)
        :return: list of json from `Athlete` object
        """
        try:
            results = self.__get_results('CALL GetXcRunners("{0}")'.format(gender_id))
            return [Athlete(result).get_json() for result in results] if results else []
        except Exception as e:
            logging.exception(e)
            raise

    def get_xc_competitors_by_year(self, year, gender_id):
        """
        Call the stored procedure, `GetXcCompetitorsByYear`, to get the competitor as a 
        list of json for the given year and gender id.
        Usage:
            - /bin/apps/xc/xc_db_app.py
        :param year: year 
        :param gender_id: gender id (reference `Gender` in DB)
        :return: list of json from `Competitor` object
        """
        try:
            results = self.__get_results('CALL GetXcCompetitorsByYear({0}, {1})'.format(year, gender_id))
            return [Competitor(result).get_json() for result in results] if results else []
        except Exception as e:
            logging.exception(e)
            raise

    def get_xc_races_by_year(self, year):
        """
        Call the stored procedure, `GetXcRacesByYear`, to get the race as a list of json 
        for the given year.
        Usage:
            - /bin/apps/xc/xc_db_app.py
        :param year: year 
        :return: list of json from `XcRace` object
        """
        try:
            results = self.__get_results('CALL GetXcRacesByYear({0})'.format(year))
            return [XcRace(result).get_json() for result in results] if results else []
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
