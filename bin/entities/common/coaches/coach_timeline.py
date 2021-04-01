__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


class CoachTimeline(object):

    MYSQL_KEY_YEAR = "year"
    MYSQL_KEY_COACHES = "coaches"

    JSON_KEY_YEAR = "Year"
    JSON_KEY_COACHES = "Coaches"

    def __init__(self, db_row):
        self.year = db_row[self.MYSQL_KEY_YEAR]
        self.coaches = db_row[self.MYSQL_KEY_COACHES]

    def get_json(self):
        return {
            self.JSON_KEY_YEAR: self.year,
            self.JSON_KEY_COACHES: self.coaches,
        }
