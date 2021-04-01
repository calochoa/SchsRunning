__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

import logging

from bin.db.common.mysql_controller import MySQLController
from bin.entities.common.special_achievements.special_achievers import SpecialAchievers


class SpecialAchieversDAI(object):

    def __init__(self, config_file='config/config.ini', section='mysql'):
        self.mysql = MySQLController(config_file=config_file, section=section)

    def get_special_achievers_by_id(self, special_achievement_ids_str, sport_id):
        """
        Call the stored procedure, `GetSpecialAchieversById` to get the special achievers 
        as a list of json for the given special achievement ids string and sport id.
        Usage:
            - /bin/apps/common/common_special_achievers_app.py
        :param special_achievement_ids_str: special achievement ids string (reference `SpecialAchievement` in DB)
        :param sport_id: sport id (reference `SpecialAchiever` in DB)
        :return: list of json from `SpecialAchievers` object
        """
        try:
            query = 'CALL GetSpecialAchieversById("{0}", {1})'.format(special_achievement_ids_str, sport_id)
            results = self.mysql.query_multi_with_fetchall_as_dict(query)
            return [SpecialAchievers(result).get_json() for result in results] if results else []
        except Exception as e:
            logging.exception(e)
            raise
