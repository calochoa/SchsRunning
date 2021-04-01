__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

from bin.entities.common.coaches.coach import Coach


class Coaches(object):

    MYSQL_KEY_NUM_SEASONS = "numSeasons"
    MYSQL_KEY_YEARS = "years"

    JSON_KEY_NUM_SEASONS = "NumSeasons"
    JSON_KEY_YEARS = "Years"

    def __init__(self, db_row):
        self.num_seasons = db_row.get(self.MYSQL_KEY_NUM_SEASONS)
        self.years = db_row.get(self.MYSQL_KEY_YEARS)
        self.coach = Coach(db_row)

    def get_json(self):
        my_dict = {
            self.JSON_KEY_NUM_SEASONS: self.num_seasons,
            self.JSON_KEY_YEARS: self.years,
        }
        my_dict.update(self.coach.get_json())
        return my_dict
