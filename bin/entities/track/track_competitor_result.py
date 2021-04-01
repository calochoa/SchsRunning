__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

from bin.utils import Utils
from bin.entities.track.track_race_result import TrackRaceResult
from bin.entities.track.track_field_result import TrackFieldResult
from bin.entities.track.track_relay_result import TrackRelayResult


class TrackCompetitorResult(object):


    JSON_KEY_ALL_RANK = "AllRank"
    JSON_KEY_ALL_TOTAL = "AllTotal"
    JSON_KEY_GRADE_RANK = "GradeRank"
    JSON_KEY_GRADE_TOTAL = "GradeRankTotal"
    JSON_KEY_YEAR_SQUAD_RANK = "YearSquadRank"
    JSON_KEY_YEAR_SQUAD_TOTAL = "YearSquadRankTotal"
    JSON_KEY_PERSONAL_RECORD = "PR"

    def __init__(self, db_row):
        self.event_id = db_row.get('eventId')
        self.track_and_field_result = self.__get_track_and_field_result(db_row, self.event_id)
        self.all_rank = 0
        self.all_total = 0
        self.grade_rank = 0
        self.grade_total = 0
        self.year_squad_rank = 0
        self.year_squad_total = 0
        self.personal_record = False

    def __get_track_and_field_result(self, db_row, event_id):
        """
        Get the track and field object result (TrackRaceResult, TrackFieldResult, 
        or TrackRelayResult) given the mysql db row and the event id.
        :param db_row: mysql db row
        :param event_id: event it
        :return: TrackRaceResult, TrackFieldResult, or TrackRelayResult
        """
        track_and_field_result = None
        if event_id:
            if self.__is_field_event(event_id):
                track_and_field_result = TrackFieldResult(db_row)
            elif self.__is_track_event(event_id):
                if self.__is_relay_event(event_id):
                    track_and_field_result = TrackRelayResult(db_row)
                else:
                    track_and_field_result = TrackRaceResult(db_row)
        return track_and_field_result

    def __is_track_event(self, event_id):
        return (event_id >= 1 and event_id <= 28) or (event_id >= 38 and event_id <= 41)

    def __is_field_event(self, event_id):
        return event_id >= 29 and event_id <= 37

    def __is_relay_event(self, event_id):
        return (event_id >= 25 and event_id <= 28) or (event_id == 41)

    def has_data(self):
        return self.track_and_field_result is not None

    def get_competitor_id(self):
        return self.track_and_field_result.competitor.competitor_id if self.has_data() else None

    def get_gender_id(self):
        return self.track_and_field_result.competitor.athlete.gender_id if self.has_data() else None

    def get_rank(self):
        return self.track_and_field_result.rank if self.has_data() else None

    def get_measurement(self):
        return self.track_and_field_result.get_measurement() if self.has_data() else None

    def get_event_id(self):
        return self.track_and_field_result.event_squad.event.event_id if self.has_data() else None

    def get_grade(self):
        return self.track_and_field_result.competitor.grade if self.has_data() else None

    def get_year(self):
        return self.track_and_field_result.competitor.year if self.has_data() else None

    def get_squad_id(self):
        return self.track_and_field_result.event_squad.squad.squad_id if self.has_data() else None

    def set_all_rank(self, all_rank):
        self.all_rank = self.__get_rank(all_rank)

    def set_all_total(self, all_total):
        self.all_total = self.__get_total(all_total)

    def set_grade_rank(self, grade_rank):
        self.grade_rank = self.__get_rank(grade_rank)

    def set_grade_total(self, grade_total):
        self.grade_total = self.__get_total(grade_total)

    def set_year_squad_rank(self, year_squad_rank):
        self.year_squad_rank = self.__get_rank(year_squad_rank)

    def set_year_squad_total(self, year_squad_total):
        self.year_squad_total = self.__get_total(year_squad_total)

    def __get_rank(self, rank):
        return ((rank + 3) / 4) if self.__is_relay_event(self.event_id) else rank

    def __get_total(self, total):
        # need to divide the total by 4 for relay events because there are 4 people with the same results
        return (total / 4) if self.__is_relay_event(self.event_id) else total

    def get_json(self):
        my_dict = {
            self.JSON_KEY_ALL_RANK: self.all_rank,
            self.JSON_KEY_ALL_TOTAL: self.all_total,
            self.JSON_KEY_GRADE_RANK: self.grade_rank,
            self.JSON_KEY_GRADE_TOTAL: self.grade_total,
            self.JSON_KEY_YEAR_SQUAD_RANK: self.year_squad_rank,
            self.JSON_KEY_YEAR_SQUAD_TOTAL: self.year_squad_total,
            self.JSON_KEY_PERSONAL_RECORD: self.personal_record,
        }
        my_dict.update(self.track_and_field_result.get_json())
        return my_dict
