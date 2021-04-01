__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

from bin.utils import Utils
from bin.entities.xc.xc_competitor_result import XcCompetitorResult


class XcTopTeamResult(object):

    MYSQL_KEY_MY_RANK = "myrank"
    MYSQL_KEY_YEAR = "Year"
    MYSQL_KEY_TEAM_TIME = "Team Time"
    MYSQL_KEY_AVG_IND_TIME = "Avg. Ind. Time"
    MYSQL_KEY_RACE_ID = "Race ID"
    MYSQL_KEY_COMPETITORS = "Competitors"

    JSON_KEY_RANK = "Rank"
    JSON_KEY_YEAR = "Year"
    JSON_KEY_TEAM_TIME = "TeamTime"
    JSON_KEY_TEAM_PACE = "TeamPace"
    JSON_KEY_RACE_ID = "RaceId"
    JSON_KEY_COMPETITOR_IDS = "CompetitorIds"
    JSON_KEY_COMPETITOR_TIMES = "CompetitorTimes"
    JSON_KEY_TEAM_TIME_CALC = "TeamTimeCalc"
    JSON_KEY_TEAM_AVG_IND_TIME_CALC = "TeamAvgIndTimeCalc"
    JSON_KEY_SPREAD = "Spread"

    JSON_KEY_TIME = XcCompetitorResult.JSON_KEY_TIME
    JSON_KEY_DISPLAY = XcCompetitorResult.JSON_KEY_DISPLAY

    def __init__(self, db_row):
        self.my_rank = db_row.get(self.MYSQL_KEY_MY_RANK)
        self.year = db_row.get(self.MYSQL_KEY_YEAR)
        self.team_time = Utils.formatTime(db_row.get(self.MYSQL_KEY_TEAM_TIME))
        self.avg_ind_time = Utils.formatTime(db_row.get(self.MYSQL_KEY_AVG_IND_TIME))
        self.race_id = db_row.get(self.MYSQL_KEY_RACE_ID)
        self.competitors = db_row.get(self.MYSQL_KEY_COMPETITORS)
        self.competitor_times = []
        self.team_time = None
        self.team_avg_ind_time = None
        self.spread = None

    def calc_times(self, race_competitor_data_dict):
        race_id = str(self.race_id)
        team_time_min = 0
        team_time_sec = 0.0
        
        for idx, competitor_id in enumerate(str(self.competitors).split(',')):
            key = race_id + ':' + competitor_id
            competitor_data = race_competitor_data_dict[key]
            self.competitor_times.append(competitor_data[self.JSON_KEY_DISPLAY])
            competitor_time_parts = competitor_data[self.JSON_KEY_TIME].split(':')
            if len(competitor_time_parts) == 2:
                 team_time_min += int(competitor_time_parts[0])
                 team_time_sec += float(competitor_time_parts[1])
            if idx == 0:
                 first_time = competitor_data[self.JSON_KEY_TIME]
            elif idx == 4:
                 fifth_time = competitor_data[self.JSON_KEY_TIME]

        self.team_time = Utils.convertTeamTime(team_time_min,team_time_sec)
        self.team_avg_ind_time = Utils.getTeamAvgIndTime(self.team_time)
        self.spread = Utils.convertTeamTime(0, Utils.getTimeDiff(first_time, fifth_time))

    def get_json(self):
        return {
            self.JSON_KEY_RANK: self.my_rank,
            self.JSON_KEY_YEAR: self.year,
            self.JSON_KEY_TEAM_TIME: self.team_time,
            self.JSON_KEY_TEAM_PACE: self.avg_ind_time,
            self.JSON_KEY_RACE_ID: self.race_id,
            self.JSON_KEY_COMPETITOR_IDS: self.competitors,
            self.JSON_KEY_COMPETITOR_TIMES: self.competitor_times,
            self.JSON_KEY_TEAM_TIME_CALC: self.team_time,
            self.JSON_KEY_TEAM_AVG_IND_TIME_CALC: self.team_avg_ind_time,
            self.JSON_KEY_SPREAD: self.spread,
        }
