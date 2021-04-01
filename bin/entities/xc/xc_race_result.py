__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

from bin.entities.xc.xc_competitor_result import XcCompetitorResult


class XcRaceResult(object):

    MYSQL_KEY_RANK = "myrank"

    JSON_KEY_RANK = "Rank"

    def __init__(self, db_row):
        self.rank = db_row.get(self.MYSQL_KEY_RANK)
        self.xc_competitor_result = XcCompetitorResult(db_row)

    def get_json(self):
        my_dict = {
            self.JSON_KEY_RANK: self.rank,
        }
        my_dict.update(self.xc_competitor_result.get_json())
        return my_dict
