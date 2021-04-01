__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

from bin.entities.track.event import Event
from bin.entities.common.misc.squad import Squad


class EventSquad(object):

    MYSQL_KEY_EVENT_BY_SQUAD = "eventBySquad"
    MYSQL_KEY_NUM_RESULTS = "numResults"

    JSON_KEY_EVENT_BY_SQUAD = "EventBySquad"
    JSON_KEY_NUM_RESULTS = "NumResults"

    def __init__(self, db_row):
        self.event_by_squad = str(db_row.get(self.MYSQL_KEY_EVENT_BY_SQUAD))
        self.num_results = db_row.get(self.MYSQL_KEY_NUM_RESULTS)
        self.event = Event(db_row)
        self.squad = Squad(db_row)

    def get_json(self):
        my_dict = {
            self.JSON_KEY_EVENT_BY_SQUAD: self.event_by_squad,
            self.JSON_KEY_NUM_RESULTS: self.num_results,
        }
        my_dict.update(self.event.get_json())
        my_dict.update(self.squad.get_json())
        return my_dict
        