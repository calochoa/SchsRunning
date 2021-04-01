__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


class Award(object):

    MYSQL_KEY_FIRST_NAME = "firstName"
    MYSQL_KEY_LAST_NAME = "lastName"
    MYSQL_KEY_AWARD_ID = "awardId"
    MYSQL_KEY_AWARD_NAME = "awardName"
    MYSQL_KEY_AWARD_SHORT_NAME = "awardShortName"
    MYSQL_KEY_SQUAD_ID = "squadId"
    MYSQL_KEY_SQUAD_NAME = "squadName"
    MYSQL_KEY_SQUAD_ABBR = "squadAbbr"
    MYSQL_KEY_YEAR = "year"
    MYSQL_KEY_ATHLETE_ID = "athleteId"

    JSON_KEY_FIRST_NAME = "FirstName"
    JSON_KEY_LAST_NAME = "LastName"
    JSON_KEY_AWARD_ID = "AwardId"
    JSON_KEY_AWARD_NAME = "AwardName"
    JSON_KEY_AWARD_SHORT_NAME = "AwardShortName"
    JSON_KEY_SQUAD_ID = "SquadId"
    JSON_KEY_SQUAD_NAME = "SquadName"
    JSON_KEY_SQUAD_ABBR = "SquadAbbr"
    JSON_KEY_YEAR = "Year"
    JSON_KEY_AWARD = "Award"
    JSON_KEY_SQUAD = "Squad"
    JSON_KEY_RUNNER_ID = "RunnerId"

    def __init__(self, db_row):
        self.first_name = db_row.get(self.MYSQL_KEY_FIRST_NAME)
        self.last_name = db_row.get(self.MYSQL_KEY_LAST_NAME)
        self.award_id = db_row.get(self.MYSQL_KEY_AWARD_ID)
        self.award_name = db_row.get(self.MYSQL_KEY_AWARD_NAME)
        self.award_short_name = db_row.get(self.MYSQL_KEY_AWARD_SHORT_NAME)
        self.squad_id = db_row.get(self.MYSQL_KEY_SQUAD_ID)
        self.squad_name = db_row.get(self.MYSQL_KEY_SQUAD_NAME)
        self.squad_abbr = db_row.get(self.MYSQL_KEY_SQUAD_ABBR)
        self.year = db_row.get(self.MYSQL_KEY_YEAR)
        self.athlete_id = db_row.get(self.MYSQL_KEY_ATHLETE_ID)

    def get_json(self):
        return {
            self.JSON_KEY_FIRST_NAME: self.first_name,
            self.JSON_KEY_LAST_NAME: self.last_name,
            self.JSON_KEY_AWARD_ID: self.award_id,
            self.JSON_KEY_AWARD_NAME: self.award_name,
            self.JSON_KEY_AWARD_SHORT_NAME: self.award_short_name,
            self.JSON_KEY_SQUAD_ID: self.squad_id,
            self.JSON_KEY_SQUAD_NAME: self.squad_name,
            self.JSON_KEY_SQUAD_ABBR: self.squad_abbr,
            self.JSON_KEY_YEAR: self.year,
            self.JSON_KEY_AWARD: self.award_name,
            self.JSON_KEY_SQUAD: self.squad_name,
            self.JSON_KEY_RUNNER_ID: self.athlete_id,
        }
