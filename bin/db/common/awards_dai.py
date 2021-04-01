__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

import logging

from bin.db.common.mysql_controller import MySQLController
from bin.entities.common.awards.award import Award


class AwardsDAI(object):

    def __init__(self, config_file='bin/conf/config.ini', section='mysql'):
        self.mysql = MySQLController(config_file=config_file, section=section)

    def get_awards_by_year(self, year, sport_id):
        """
        Call the stored procedure, `GetAwardsByYear` to get the awards as a list of json
        for the given year and sport id.
        Usage:
            - /bin/apps/common/common_awards_db_app.py
        :param squad_id: year (reference `Awardee` in DB)
        :param sport_id: sport id (reference `Awardee` in DB)
        :return: list of json from `Award` object
        """
        query = 'CALL GetAwardsByYear({0}, {1})'.format(year, sport_id)
        return self.__get_json_award_list(query)

    def get_award_by_id(self, award_id, squad_id, sport_id):
        """
        Call the stored procedure, `GetAwardsById` to get the awards as a list of json
        for the given award id, squad id, and sport id.
        Usage:
            - /bin/apps/common/common_awards_db_app.py
        :param award_id: award id (reference `Award` in DB)
        :param squad_id: squad id (reference `Squad` in DB)
        :param sport_id: sport id (reference `Awardee` in DB)
        :return: list of json from `Award` object
        """
        query = 'CALL GetAwardsById("{0}", "{1}", {2})'.format(award_id, squad_id, sport_id)
        return self.__get_json_award_list(query)

    def get_awards_timeline(self, squad_id, sport_id):
        """
        Call the stored procedure, `GetAwardsTimeline` to get the awards as a list of json
        for the given squad id and sport id.
        Usage:
            - /bin/apps/common/common_awards_db_app.py
        :param squad_id: squad id (reference `Squad` in DB)
        :param sport_id: sport id (reference `Awardee` in DB)
        :return: list of json from `Award` object
        """
        query = 'CALL GetAwardsTimeline("{0}", {1})'.format(squad_id,sport_id)
        return self.__get_json_award_list(query)

    def __get_json_award_list(self, query):
        """
        Get the awards as a list of json for the given query.
        :param query: mysql query
        :return: list of json from `Award` object
        """
        try:
            results = self.mysql.query_multi_with_fetchall_as_dict(query)
            return [Award(result).get_json() for result in results] if results else []
        except Exception as e:
            logging.exception(e)
            raise
