__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


class Coach(object):

    MYSQL_KEY_FIRST_NAME = "firstName"
    MYSQL_KEY_LAST_NAME = "lastName"
    MYSQL_KEY_COACH_TYPE = "coachType"
    MYSQL_KEY_YEAR = "year"
    MYSQL_KEY_COACH_ID = "coachId"
    MYSQL_KEY_COACH_TYPE_ID = "coachTypeId"

    JSON_KEY_FIRST_NAME = "FirstName"
    JSON_KEY_LAST_NAME = "LastName"
    JSON_KEY_COACH_TYPE = "CoachType"
    JSON_KEY_YEAR = "Year"
    JSON_KEY_COACH_ID = "CoachId"

    def __init__(self, db_row):
        self.first_name = db_row.get(self.MYSQL_KEY_FIRST_NAME)
        self.last_name = db_row.get(self.MYSQL_KEY_LAST_NAME)
        self.coach_type = db_row.get(self.MYSQL_KEY_COACH_TYPE)
        self.year = db_row.get(self.MYSQL_KEY_YEAR)
        self.coach_id = db_row.get(self.MYSQL_KEY_COACH_ID)
        self.coach_type_id = db_row.get(self.MYSQL_KEY_COACH_TYPE_ID)

    def get_json(self):
        return {
            self.JSON_KEY_FIRST_NAME: self.first_name,
            self.JSON_KEY_LAST_NAME: self.last_name,
            self.JSON_KEY_COACH_TYPE: self.coach_type,
            self.JSON_KEY_YEAR: self.year,
            self.JSON_KEY_COACH_ID: self.coach_id,
        }
