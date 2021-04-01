__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

from bin.entities.common.misc.athlete import Athlete


class Competitor(object):
    
    MYSQL_KEY_COMPETITOR_ID = "competitorid"
    MYSQL_KEY_YEAR = "year"
    MYSQL_KEY_GRADE = "grade"

    JSON_KEY_COMPETITOR_ID = "CompetitorId"
    JSON_KEY_YEAR = "Year"
    JSON_KEY_GRADE = "Grade"

    def __init__(self, db_row, competitor_id=None, grade=None, full_name=None, athlete_id=None):
        self.competitor_id = self.__get_str_value(
            self.__get_valid_value(competitor_id, db_row, self.MYSQL_KEY_COMPETITOR_ID)
        )
        self.year = db_row.get(self.MYSQL_KEY_YEAR)
        self.grade = self.__get_valid_value(grade, db_row, self.MYSQL_KEY_GRADE)
        self.athlete = Athlete(db_row, full_name=full_name, athlete_id=athlete_id)

    def __get_valid_value(self, value, db_row, key):
        return value if value else db_row.get(key)

    def __get_str_value(self, value):
        return str(value) if value else value

    def get_json(self):
        my_dict = {
            self.JSON_KEY_COMPETITOR_ID: self.competitor_id,
            self.JSON_KEY_YEAR: self.year,
            self.JSON_KEY_GRADE: self.grade,
        }
        my_dict.update(self.athlete.get_json())
        return my_dict
        