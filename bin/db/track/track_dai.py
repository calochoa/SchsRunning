__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

import logging

from bin.db.common.mysql_controller import MySQLController
from bin.entities.common.misc.competitor import Competitor
from bin.entities.common.misc.athlete import Athlete
from bin.entities.track.event_squad import EventSquad


class TrackDAI(object):

    def __init__(self, config_file='bin/conf/config.ini', section='mysql'):
        self.mysql = MySQLController(config_file=config_file, section=section)

    def get_track_competitors_by_year(self, year):
        """
        Call the stored procedure, `GetTrackCompetitorsByYear`, to get the competitor 
        as a list of json for the given year.
        Usage:
            - /bin/apps/track/track_db_app.py
        :param year: year
        :return: list of json from `Competitor` object
        """
        try:
            results = self.__get_results('CALL GetTrackCompetitorsByYear({0})'.format(year))
            return [Competitor(result).get_json() for result in results] if results else []
        except Exception as e:
            logging.exception(e)
            raise

    def get_track_athletes(self, gender_id):
        """
        Call the stored procedure, `GetTrackAthletes`, to get the athlete as a list of json
        for the given gender id.
        Usage:
            - /bin/apps/track/track_db_app.py
        :param gender_id: gender id (reference `Gender` in DB)
        :return: list of json from `Athlete` object
        """
        try:
            results = self.__get_results('CALL GetTrackAthletes("{0}")'.format(gender_id))
            return [Athlete(result).get_json() for result in results] if results else []
        except Exception as e:
            logging.exception(e)
            raise

    def get_track_events_by_year(self, year):
        """
        Call the stored procedure, `GetTrackEventsByYear`, to get the event squad as a list
        of json for the given year.
        Usage:
            - /bin/apps/track/track_db_app.py
        :param year: year
        :return: list of json from `EventSquad` object
        """
        try:
            results = self.__get_results('CALL GetTrackEventsByYear({0})'.format(year))
            return [EventSquad(result).get_json() for result in results] if results else []
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
