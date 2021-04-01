__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

import logging

from bin.db.common.mysql_controller import MySQLController
from bin.entities.xc.xc_race_result import XcRaceResult
from bin.entities.xc.xc_top_team_result import XcTopTeamResult
from bin.entities.xc.xc_competitor_result import XcCompetitorResult


class XcResultsDAI(object):

    def __init__(self, config_file='bin/conf/config.ini', section='mysql'):
        self.mysql = MySQLController(config_file=config_file, section=section)

    def get_xc_top_individual(self, course_id, gender_id, limit):
        """
        Call the stored procedure, `GetTopXcIndividual`, to get the race result as a list
        of json for the given course id, gender id, and limit.
        Usage:
            - /bin/apps/xc/xc_db_app.py
        :param course_id: course id (reference `Course` in DB)
        :param gender_id: gender id (reference `Gender` in DB)
        :param limit: limit
        :return: list of json from `XcRaceResult` object
        """
        query = 'CALL GetTopXcIndividual({0}, {1}, {2})'.format(course_id, gender_id, limit)
        return self.__get_json_xc_race_result_list(query)

    def get_xc_top_individual_by_grade(self, course_id, gender_id, grade, limit):
        """
        Call the stored procedure, `GetTopXcIndividualByGrade`, to get the race result as 
        a list of json for the given course id, gender id, grade, and limit.
        Usage:
            - /bin/apps/xc/xc_db_app.py
        :param course_id: course id (reference `Course` in DB)
        :param gender_id: gender id (reference `Gender` in DB)
        :param grade: grade
        :param limit: limit
        :return: list of json from `XcRaceResult` object
        """
        query = 'CALL GetTopXcIndividualByGrade({0}, {1}, {2}, {3})'.format(course_id, gender_id, grade, limit)
        return self.__get_json_xc_race_result_list(query)

    def get_all_xc_race_results(self, race_id):
        """
        Call the stored procedure, `GetAllXcRaceResults`, to get the race result as a list
        of json for the given race id.
        Usage:
            - /bin/apps/xc/xc_db_app.py
        :param race_id: race id (reference `Race` in DB)
        :return: list of json from `XcRaceResult` object
        """
        query = 'CALL GetAllXcRaceResults({0})'.format(race_id)
        return self.__get_json_xc_race_result_list(query)

    def get_xc_race_results(self, race_id, gender_id):
        """
        Call the stored procedure, `GetXcRaceResults`, to get the race result as a list
        of json for the given race id and gender id.
        Usage:
            - /bin/apps/xc/xc_db_app.py
        :param race_id: race id (reference `Race` in DB)
        :param gender_id: gender id (reference `Gender` in DB)
        :return: list of json from `XcRaceResult` object
        """
        query = 'CALL GetXcRaceResults({0}, {1})'.format(race_id, gender_id)
        return self.__get_json_xc_race_result_list(query)

    def __get_json_xc_race_result_list(self, query):
        """
        Get the race results as a list of json for the given query.
        :param query: mysql query
        :return: list of json from `XcRaceResult` object
        """
        try:
            results = self.__get_results(query)
            return [XcRaceResult(result).get_json() for result in results] if results else []
        except Exception as e:
            logging.exception(e)
            raise

    def get_top_team_course(self, course_id, gender_id, limit):
        """
        Call the stored procedure, `GetTopTeamCourse`, to get list of the xc top team results,
        list of top race ids, and list of top competitors ids for the given course id, gender
        id, and limit.
        Usage:
            - /bin/apps/xc/xc_db_app.py
        :param course_id: course id (reference `Course` in DB)
        :param gender_id: gender id (reference `Gender` in DB)
        :param limit: limit
        :return: list of `XcTopTeamResult` object, list of race ids, list of competitor ids
        """
        try:
            top_team_course_results = []
            top_race_ids = []
            top_competitor_ids = []
            results = self.__get_results('CALL GetTopTeamCourse({0}, {1}, {2})'.format(course_id, gender_id, limit))
            for result in results:
                xc_top_team_result = XcTopTeamResult(result)
                top_team_course_results.append(xc_top_team_result)
                top_race_ids.append(xc_top_team_result.race_id)
                top_competitor_ids.append(xc_top_team_result.competitors)
            return top_team_course_results, top_race_ids, top_competitor_ids
        except Exception as e:
            logging.exception(e)
            raise

    def get_xc_results_by_race_competitor(self, race_ids, competitor_ids):
        """
        Call the stored procedure, `GetXcResultsByRaceCompetitor`, to get the dictionary of
        race competitor data given the race ids and competitor ids.
        Usage:
            - /bin/apps/xc/xc_db_app.py
        :param race_ids: race ids (reference `Race` in DB)
        :param competitor_ids: competitor ids (reference `Competitor` in DB)
        :return: dictionary of race competitor data
        """
        try:
            race_ids_str = ','.join(str(race_id) for race_id in race_ids)
            competitor_ids_str = ','.join(str(competitor_id) for competitor_id in competitor_ids)
            results = self.__get_results('CALL GetXcResultsByRaceCompetitor("{0}", "{1}")'.format(race_ids_str, competitor_ids_str))
            race_competitor_data_dict = {}
            for result in results:
                xc_competitor_result = XcCompetitorResult(result)
                race_competitor_data_dict[xc_competitor_result.get_key()] = xc_competitor_result.get_value()
            return race_competitor_data_dict
        except Exception as e:
            logging.exception(e)
            raise

    def get_xc_competitor_results(self, competitor_id):
        """
        Call the stored procedure, `GetXcCompetitorResults`, to get the xc competitor results 
        for the given competitor id.
        Usage:
            - /bin/apps/xc/xc_db_app.py
        :param competitor_id: competitor id (reference `Competitor` in DB)
        :return: list of json from `XcCompetitorResult` object
        """
        query = 'CALL GetXcCompetitorResults("{0}")'.format(competitor_id)
        return self.__get_json_xc_competitor_result_list(query)

    def get_xc_runner_results(self, runner_id):
        """
        Call the stored procedure, `GetXcRunnerResults`, to get the xc competitor results 
        for the given runner id.
        Usage:
            - /bin/apps/xc/xc_db_app.py
        :param runner_id: runner id (reference `Athlete` in DB)
        :return: list of json from `XcCompetitorResult` object
        """
        query = 'CALL GetXcRunnerResults({0})'.format(runner_id)
        return self.__get_json_xc_competitor_result_list(query)

    def get_past_xc_alumni_champions(self):
        """
        Call the stored procedure, `GetPastXcAlumniChampions`, to get the xc competitor 
        results for the past alumni champions.
        Usage:
            - /bin/apps/xc/xc_db_app.py
        :return: list of json from `XcCompetitorResult` object
        """
        query = 'CALL GetPastXcAlumniChampions()'
        return self.__get_json_xc_competitor_result_list(query)

    def __get_json_xc_competitor_result_list(self, query):
        """
        Get the competitor results as a list of json for the given query.
        :param query: mysql query
        :return: list of json from `XcCompetitorResult` object
        """
        try:
            results = self.__get_results(query)
            return [XcCompetitorResult(result).get_json() for result in results] if results else []
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
