__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

from bin.entities.common.misc.competitor import Competitor
from bin.entities.track.event import Event


class AthleteResultMetadata(object):

    def __init__(self, db_row):
        self.competitor = Competitor(db_row)
        self.event = Event(db_row)

    def get_competitor_id(self):
        return self.competitor.competitor_id if self.competitor else None

    def get_year(self):
        return self.competitor.year if self.competitor else None

    def get_event_id(self):
        return self.event.event_id if self.event else None

    def get_personal_record_key(self):
        personal_record_key = None
        if self.event:
            event_sub_type_id = self.event.event_sub_type_id
            event_id = self.event.event_id
            event_id_str = '0{0}'.format(event_id) if event_id < 10 else event_id
            personal_record_key = '{0}.{1}'.format(event_sub_type_id, event_id_str)
        return personal_record_key
