__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

from bin.utils import Utils
from bin.entities.common.misc.competitor import Competitor
from bin.entities.track.event_squad import EventSquad


class TrackRelayResult(object):

    MYSQL_KEY_RANK = "myrank"
    MYSQL_KEY_TIME  = "time"
    MYSQL_KEY_TIME_2  = "result1"
    MYSQL_KEY_RACE_TIME_TYPE_ID = "raceTimeTypeId"
    MYSQL_KEY_RACE_TIME_TYPE_ID_2 = "result2"
    MYSQL_KEY_COMPETITOR_ID_1 = "competitorId1"
    MYSQL_KEY_COMPETITOR_ID_2 = "competitorId2"
    MYSQL_KEY_COMPETITOR_ID_3 = "competitorId3"
    MYSQL_KEY_COMPETITOR_ID_4 = "competitorId4"
    MYSQL_KEY_FULL_NAME_1 = "fullName1"
    MYSQL_KEY_FULL_NAME_2 = "fullName2"
    MYSQL_KEY_FULL_NAME_3 = "fullName3"
    MYSQL_KEY_FULL_NAME_4 = "fullName4"
    MYSQL_KEY_GRADE_1 = "grade1"
    MYSQL_KEY_GRADE_2 = "grade2"
    MYSQL_KEY_GRADE_3 = "grade3"
    MYSQL_KEY_GRADE_4 = "grade4"
    MYSQL_KEY_ATHLETE_ID_1 = "athleteId1"
    MYSQL_KEY_ATHLETE_ID_2 = "athleteId2"
    MYSQL_KEY_ATHLETE_ID_3 = "athleteId3"
    MYSQL_KEY_ATHLETE_ID_4 = "athleteId4"

    JSON_KEY_RANK = "Rank"
    JSON_KEY_TIME = "Time"
    JSON_KEY_RACE_TIME_TYPE_ID = "RaceTimeTypeId"
    JSON_KEY_YEAR = "Year"
    JSON_KEY_RESULT = "Result"
    JSON_KEY_COMPETITOR_ID = "CompetitorId"
    JSON_KEY_COMPETITOR_ID_1 = "CompetitorId1"
    JSON_KEY_COMPETITOR_ID_2 = "CompetitorId2"
    JSON_KEY_COMPETITOR_ID_3 = "CompetitorId3"
    JSON_KEY_COMPETITOR_ID_4 = "CompetitorId4"
    JSON_KEY_FULL_NAME = "FullName"
    JSON_KEY_FULL_NAME_1 = "FullName1"
    JSON_KEY_FULL_NAME_2 = "FullName2"
    JSON_KEY_FULL_NAME_3 = "FullName3"
    JSON_KEY_FULL_NAME_4 = "FullName4"
    JSON_KEY_GRADE = "Grade"
    JSON_KEY_GRADE_1 = "Grade1"
    JSON_KEY_GRADE_2 = "Grade2"
    JSON_KEY_GRADE_3 = "Grade3"
    JSON_KEY_GRADE_4 = "Grade4"
    JSON_KEY_ATHLETE_ID = "AthleteId"
    JSON_KEY_ATHLETE_ID_1 = "AthleteId1"
    JSON_KEY_ATHLETE_ID_2 = "AthleteId2"
    JSON_KEY_ATHLETE_ID_3 = "AthleteId3"
    JSON_KEY_ATHLETE_ID_4 = "AthleteId4"

    def __init__(self, db_row):
        self.rank = db_row.get(self.MYSQL_KEY_RANK)
        self.time = self.__get_time(db_row)
        self.race_time_type_id = self.__get_race_time_type_id(db_row)
        self.result_str = self.__get_result_str(self.time, self.race_time_type_id)
        self.competitor = Competitor(db_row)    # for instances related TrackCompetitorResult
        self.competitor_1 = self.__get_competitor(
            db_row, self.MYSQL_KEY_COMPETITOR_ID_1, self.MYSQL_KEY_GRADE_1, self.MYSQL_KEY_FULL_NAME_1, self.MYSQL_KEY_ATHLETE_ID_1
        )
        self.competitor_2 = self.__get_competitor(
            db_row, self.MYSQL_KEY_COMPETITOR_ID_2, self.MYSQL_KEY_GRADE_2, self.MYSQL_KEY_FULL_NAME_2, self.MYSQL_KEY_ATHLETE_ID_2
        )
        self.competitor_3 = self.__get_competitor(
            db_row, self.MYSQL_KEY_COMPETITOR_ID_3, self.MYSQL_KEY_GRADE_3, self.MYSQL_KEY_FULL_NAME_3, self.MYSQL_KEY_ATHLETE_ID_3
        )
        self.competitor_4 = self.__get_competitor(
            db_row, self.MYSQL_KEY_COMPETITOR_ID_4, self.MYSQL_KEY_GRADE_4, self.MYSQL_KEY_FULL_NAME_4, self.MYSQL_KEY_ATHLETE_ID_4
        )
        self.event_squad = EventSquad(db_row)

    def __get_time(self, db_row):
        time = db_row.get(self.MYSQL_KEY_TIME)
        if time is None:
            time = db_row.get(self.MYSQL_KEY_TIME_2)
        return Utils.format_track_time(time) if time else time

    def __get_race_time_type_id(self, db_row):
        race_time_type_id = db_row.get(self.MYSQL_KEY_RACE_TIME_TYPE_ID)
        if race_time_type_id is None:
            race_time_type_id = db_row.get(self.MYSQL_KEY_RACE_TIME_TYPE_ID_2)
        return str(race_time_type_id) if race_time_type_id else race_time_type_id

    def __get_result_str(self, time, race_time_type_id):
        return '{0}{1}'.format(time, race_time_type_id)

    def __get_competitor(self, db_row, competitor_id_key, grade_key, full_name_key, athlete_id_key):
        return Competitor(
            db_row, competitor_id=db_row.get(competitor_id_key), grade=db_row.get(grade_key), 
            full_name=db_row.get(full_name_key), athlete_id=db_row.get(athlete_id_key)
        )

    def get_measurement(self):
        return self.time

    def get_json(self):
        my_dict = {
            self.JSON_KEY_RANK: self.rank,
            self.JSON_KEY_TIME: self.time,
            self.JSON_KEY_RACE_TIME_TYPE_ID: self.race_time_type_id,
            self.JSON_KEY_YEAR: self.competitor_1.year,
            self.JSON_KEY_RESULT: self.result_str,
            self.JSON_KEY_COMPETITOR_ID: self.competitor.competitor_id,
            self.JSON_KEY_ATHLETE_ID: self.competitor.athlete.athlete_id,
            self.JSON_KEY_FULL_NAME: self.competitor.athlete.full_name,
            self.JSON_KEY_GRADE: self.competitor.grade,
            self.JSON_KEY_COMPETITOR_ID_1: self.competitor_1.competitor_id,
            self.JSON_KEY_ATHLETE_ID_1: self.competitor_1.athlete.athlete_id,
            self.JSON_KEY_FULL_NAME_1: self.competitor_1.athlete.full_name,
            self.JSON_KEY_GRADE_1: self.competitor_1.grade,
            self.JSON_KEY_COMPETITOR_ID_2: self.competitor_2.competitor_id,
            self.JSON_KEY_ATHLETE_ID_2: self.competitor_2.athlete.athlete_id,
            self.JSON_KEY_FULL_NAME_2: self.competitor_2.athlete.full_name,
            self.JSON_KEY_GRADE_2: self.competitor_2.grade,
            self.JSON_KEY_COMPETITOR_ID_3: self.competitor_3.competitor_id,
            self.JSON_KEY_ATHLETE_ID_3: self.competitor_3.athlete.athlete_id,
            self.JSON_KEY_FULL_NAME_3: self.competitor_3.athlete.full_name,
            self.JSON_KEY_GRADE_3: self.competitor_3.grade,
            self.JSON_KEY_COMPETITOR_ID_4: self.competitor_4.competitor_id,
            self.JSON_KEY_ATHLETE_ID_4: self.competitor_4.athlete.athlete_id,
            self.JSON_KEY_FULL_NAME_4: self.competitor_4.athlete.full_name,
            self.JSON_KEY_GRADE_4: self.competitor_4.grade,
        }
        my_dict.update(self.competitor.get_json())
        my_dict.update(self.event_squad.get_json())
        return my_dict
        