__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

from bin.utils import Utils
from bin.entities.common.misc.competitor import Competitor
from bin.entities.track.event_squad import EventSquad


class TrackRaceResult(object):

    MYSQL_KEY_RANK = "myrank"
    MYSQL_KEY_TIME  = "time"
    MYSQL_KEY_TIME_2  = "result1"
    MYSQL_KEY_RACE_TIME_TYPE_ID = "raceTimeTypeId"
    MYSQL_KEY_RACE_TIME_TYPE_ID_2 = "result2"

    JSON_KEY_RANK = "Rank"
    JSON_KEY_TIME = "Time"
    JSON_KEY_RACE_TIME_TYPE_ID = "RaceTimeTypeId"
    JSON_KEY_RESULT = "Result"

    def __init__(self, db_row):
        self.rank = db_row.get(self.MYSQL_KEY_RANK)
        self.time = self.__get_time(db_row)
        self.race_time_type_id = self.__get_race_time_type_id(db_row)
        self.result_str = self.__get_result_str(self.time, self.race_time_type_id)
        self.competitor = Competitor(db_row)
        self.event_squad = EventSquad(db_row)

    def __get_time(self, db_row):
        time = db_row.get(self.MYSQL_KEY_TIME)
        if time is None:
            time = db_row.get(self.MYSQL_KEY_TIME_2)
        return Utils.format_track_time(time) if time else time

    def __get_race_time_type_id(self, db_row):
        race_time_type_id = db_row.get(self.MYSQL_KEY_RACE_TIME_TYPE_ID)
        if race_time_type_id is None:
            race_time_type_id = db_row.get(self.MYSQL_KEY_RACE_TIME_TYPE_ID_2)
        return str(race_time_type_id) if race_time_type_id else race_time_type_id

    def __get_result_str(self, time, race_time_type_id):
        return '{0}{1}'.format(time, race_time_type_id)

    def get_measurement(self):
        return self.time

    def get_json(self):
        my_dict = {
            self.JSON_KEY_RANK: self.rank,
            self.JSON_KEY_TIME: self.time,
            self.JSON_KEY_RACE_TIME_TYPE_ID: self.race_time_type_id,
            self.JSON_KEY_RESULT: self.result_str,
        }
        my_dict.update(self.competitor.get_json())
        my_dict.update(self.event_squad.get_json())
        return my_dict
