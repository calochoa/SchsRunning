__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

from bin.entities.xc.xc_course import XcCourse


class XcRace(object):

    MYSQL_KEY_RACE_ID = "raceid"
    MYSQL_KEY_DATE = "date"
    MYSQL_KEY_RACE_NAME = "racename"
    MYSQL_KEY_RACE_CONDITION = "racecondition"

    JSON_KEY_RACE_ID = "RaceId"
    JSON_KEY_DATE = "Date"
    JSON_KEY_RACE_NAME = "RaceName"
    JSON_KEY_RACE_CONDITION = "RaceCondition"

    def __init__(self, db_row):
        self.race_id = db_row.get(self.MYSQL_KEY_RACE_ID)
        self.date = db_row.get(self.MYSQL_KEY_DATE)
        self.race_name = db_row.get(self.MYSQL_KEY_RACE_NAME)
        self.race_condition = db_row.get(self.MYSQL_KEY_RACE_CONDITION)
        self.xc_course = XcCourse(db_row)

    def get_json(self):
        my_dict = {
            self.JSON_KEY_RACE_ID: self.race_id,
            self.JSON_KEY_DATE: str(self.date),
            self.JSON_KEY_RACE_NAME: self.race_name,
            self.JSON_KEY_RACE_CONDITION: self.race_condition,
        }
        my_dict.update(self.xc_course.get_json())
        return my_dict
