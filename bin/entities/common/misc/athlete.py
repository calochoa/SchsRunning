__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


class Athlete(object):

    MYSQL_KEY_ATHLETE_ID_LC = "athleteid"
    MYSQL_KEY_ATHLETE_ID = "athleteId"
    MYSQL_KEY_FIRST_NAME = "firstname"
    MYSQL_KEY_LAST_NAME = "lastname"
    MYSQL_KEY_YEARS = "years"
    MYSQL_KEY_GENDER = "gender"
    MYSQL_KEY_GENDER_ID = "genderId"
    MYSQL_KEY_FULL_NAME = "fullName"
    MYSQL_KEY_END_HS_YEAR = "endHsYear"

    JSON_KEY_ATHLETE_ID = "AthleteId"
    JSON_KEY_RUNNER_ID = "RunnerId"
    JSON_KEY_FIRST_NAME = "FirstName"
    JSON_KEY_LAST_NAME = "LastName"
    JSON_KEY_YEARS = "Years"
    JSON_KEY_GENDER = "Gender"
    JSON_KEY_GENDER_ID = "GenderId"
    JSON_KEY_FULL_NAME = "FullName"
    JSON_KEY_END_HS_YEAR = "EndHsYear"

    def __init__(self, db_row, full_name=None, athlete_id=None):
        self.athlete_id = self.__get_valid_athlete_id(athlete_id, db_row)
        self.first_name = db_row.get(self.MYSQL_KEY_FIRST_NAME)
        self.last_name = db_row.get(self.MYSQL_KEY_LAST_NAME)
        self.years = db_row.get(self.MYSQL_KEY_YEARS)
        self.gender = db_row.get(self.MYSQL_KEY_GENDER)
        self.gender_id = db_row.get(self.MYSQL_KEY_GENDER_ID)
        self.full_name = self.__get_str_value(
            self.__get_valid_value(full_name, db_row, self.MYSQL_KEY_FULL_NAME)
        )
        self.end_hs_year = db_row.get(self.MYSQL_KEY_END_HS_YEAR)

    def __get_valid_athlete_id(self, athlete_id, db_row):
        valid_athlete_id = athlete_id
        if valid_athlete_id is None:
            valid_athlete_id = db_row.get(self.MYSQL_KEY_ATHLETE_ID_LC)
            if valid_athlete_id is None:
                valid_athlete_id = db_row.get(self.MYSQL_KEY_ATHLETE_ID)
        return valid_athlete_id

    def __get_valid_value(self, value, db_row, key):
        return value if value else db_row.get(key)

    def __get_str_value(self, value):
        return str(value) if value else value

    def get_json(self):
        return {
            self.JSON_KEY_ATHLETE_ID: self.athlete_id,
            self.JSON_KEY_RUNNER_ID: self.athlete_id,
            self.JSON_KEY_FIRST_NAME: self.first_name,
            self.JSON_KEY_LAST_NAME: self.last_name,
            self.JSON_KEY_YEARS: self.years,
            self.JSON_KEY_GENDER: self.gender,
            self.JSON_KEY_GENDER_ID: self.gender_id,
            self.JSON_KEY_FULL_NAME: self.full_name,
            self.JSON_KEY_END_HS_YEAR: self.end_hs_year,
        }
