__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


class SpecialAchievers(object):

    MYSQL_KEY_SPECIAL_ACHIEVEMENT_NAME = "specialAchievementName"
    MYSQL_KEY_ATHLETE_ID = "athleteId"
    MYSQL_KEY_FIRST_NAME = "firstName"
    MYSQL_KEY_LAST_NAME = "lastName"
    MYSQL_KEY_GRADE = "grade"
    MYSQL_KEY_YEAR = "year"
    MYSQL_KEY_NOTES = "notes"

    JSON_KEY_SPECIAL_ACHIEVEMENT_NAME = "SpecialAchievementName"
    JSON_KEY_RUNNER_ID = "RunnerId"
    JSON_KEY_FIRST_NAME = "FirstName"
    JSON_KEY_LAST_NAME = "LastName"
    JSON_KEY_GRADE = "Grade"
    JSON_KEY_YEAR = "Year"
    JSON_KEY_NOTES = "Notes"

    def __init__(self, db_row):
        self.special_achievement_name = db_row.get(self.MYSQL_KEY_SPECIAL_ACHIEVEMENT_NAME)
        self.athlete_id = db_row.get(self.MYSQL_KEY_ATHLETE_ID)
        self.first_name = db_row.get(self.MYSQL_KEY_FIRST_NAME)
        self.last_name = db_row.get(self.MYSQL_KEY_LAST_NAME)
        self.grade = db_row.get(self.MYSQL_KEY_GRADE)
        self.year = db_row.get(self.MYSQL_KEY_YEAR)
        self.notes = db_row.get(self.MYSQL_KEY_NOTES)

    def get_json(self):
        return {
            self.JSON_KEY_SPECIAL_ACHIEVEMENT_NAME: self.special_achievement_name,
            self.JSON_KEY_RUNNER_ID: self.athlete_id,
            self.JSON_KEY_FIRST_NAME: self.first_name,
            self.JSON_KEY_LAST_NAME: self.last_name,
            self.JSON_KEY_GRADE: self.grade,
            self.JSON_KEY_YEAR: self.year,
            self.JSON_KEY_NOTES: self.notes,
        }
