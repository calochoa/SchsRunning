__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

from bin.entities.common.misc.competitor import Competitor
from bin.entities.track.event_squad import EventSquad


class TrackFieldResult(object):

    MYSQL_KEY_RANK = "myrank"
    MYSQL_KEY_FOOT_PART_OF_DISTANCE  = "footPartOfDistance"
    MYSQL_KEY_FOOT_PART_OF_DISTANCE_2  = "result1"
    MYSQL_KEY_INCH_PART_OF_DISTANCE = "inchPartOfDistance"
    MYSQL_KEY_INCH_PART_OF_DISTANCE_2 = "result2"

    JSON_KEY_RANK = "Rank"
    JSON_KEY_FOOT_PART_OF_DISTANCE = "FootPartOfDistance"
    JSON_KEY_INCH_PART_OF_DISTANCE = "InchPartOfDistance"
    JSON_KEY_RESULT = "Result"

    def __init__(self, db_row):
        self.rank = db_row.get(self.MYSQL_KEY_RANK)
        self.foot_part_of_distance = self.__get_foot_part_of_distance(db_row)
        self.inch_part_of_distance = self.__get_inch_part_of_distance(db_row)
        self.distance_in_inches = self.__get_distance_in_inches(self.foot_part_of_distance, self.inch_part_of_distance)
        self.result_str = self.__get_result_str(self.foot_part_of_distance, self.inch_part_of_distance)
        self.competitor = Competitor(db_row)
        self.event_squad = EventSquad(db_row)

    def __get_foot_part_of_distance(self, db_row):
        foot_part_of_distance = db_row.get(self.MYSQL_KEY_FOOT_PART_OF_DISTANCE)
        if foot_part_of_distance is None:
            foot_part_of_distance = db_row.get(self.MYSQL_KEY_FOOT_PART_OF_DISTANCE_2)
        return int(foot_part_of_distance) if foot_part_of_distance is not None else foot_part_of_distance

    def __get_inch_part_of_distance(self, db_row):
        inch_part_of_distance = db_row.get(self.MYSQL_KEY_INCH_PART_OF_DISTANCE)
        if inch_part_of_distance is None:
            inch_part_of_distance = db_row.get(self.MYSQL_KEY_INCH_PART_OF_DISTANCE_2)
        return float(inch_part_of_distance) if inch_part_of_distance is not None else inch_part_of_distance

    def __get_distance_in_inches(self, foot_part_of_distance, inch_part_of_distance):
        return (12 * foot_part_of_distance) + inch_part_of_distance

    def __get_result_str(self, foot_part_of_distance, inch_part_of_distance):
        if str(inch_part_of_distance).endswith('.0'):
            inch_part_of_distance = int(inch_part_of_distance)
        return '{0}\' {1}"'.format(foot_part_of_distance, inch_part_of_distance)

    def get_measurement(self):
        return self.distance_in_inches

    def get_json(self):
        my_dict = {
            self.JSON_KEY_RANK: self.rank,
            self.JSON_KEY_FOOT_PART_OF_DISTANCE: self.foot_part_of_distance,
            self.JSON_KEY_INCH_PART_OF_DISTANCE: self.inch_part_of_distance,
            self.JSON_KEY_RESULT: self.result_str,
        }
        my_dict.update(self.competitor.get_json())
        my_dict.update(self.event_squad.get_json())
        return my_dict
