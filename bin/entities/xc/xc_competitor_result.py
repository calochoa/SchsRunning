__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

from bin.utils import Utils
from bin.entities.common.misc.competitor import Competitor
from bin.entities.xc.xc_race import XcRace


class XcCompetitorResult(object):

    MYSQL_KEY_TIME = "time"
    MYSQL_KEY_PACE = "pace"

    JSON_KEY_TIME = "Time"
    JSON_KEY_PACE = "Pace"
    JSON_KEY_DISPLAY = "Display"

    def __init__(self, db_row):
        self.time = Utils.formatTime(db_row.get(self.MYSQL_KEY_TIME))
        self.pace = Utils.formatTime(db_row.get(self.MYSQL_KEY_PACE))
        self.competitor = Competitor(db_row)
        self.xc_race = XcRace(db_row)

    def get_json(self):
        my_dict = {
            self.JSON_KEY_TIME: self.time,
            self.JSON_KEY_PACE: self.pace,
        }
        my_dict.update(self.competitor.get_json())
        my_dict.update(self.xc_race.get_json())
        return my_dict

    def get_key(self):
        return f"{self.xc_race.race_id}:{self.competitor.competitor_id}"

    def get_value(self):
        return {
            self.JSON_KEY_DISPLAY : self.__get_display(),
            self.JSON_KEY_TIME: self.time
        }

    def __get_display(self):
        return f"{self.competitor.athlete.first_name} {self.competitor.athlete.last_name} ({self.competitor.grade}) - {self.time} ({self.pace})"
