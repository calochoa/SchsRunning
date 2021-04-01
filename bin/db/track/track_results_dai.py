__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

import logging

from collections import OrderedDict

from bin.db.common.mysql_controller import MySQLController
from bin.entities.track.track_race_result import TrackRaceResult
from bin.entities.track.track_field_result import TrackFieldResult
from bin.entities.track.track_relay_result import TrackRelayResult
from bin.entities.track.track_competitor_result import TrackCompetitorResult
from bin.entities.track.athlete_result_metadata import AthleteResultMetadata


class TrackResultsDAI(object):

    def __init__(self, config_file='bin/conf/config.ini', section='mysql'):
        self.mysql = MySQLController(config_file=config_file, section=section)

    def get_track_hof_race_results(self, event_id, gender_id, limit=40):
        """
        Call the stored procedure, `GetTopTrackRaceIndividual`, to get the race results 
        as a list of json for the given event id, gender id, and limit.  Limit the hall 
        of fame list to the top 15, which can include ties; therfore, query for a list 
        of at least 40 results.
        Usage:
            - /bin/apps/track/track_db_app.py
        :param event_id: event id (reference `Event` in DB)
        :param gender_id: gender id (reference `Gender` in DB)
        :param limit: limit
        :return: list of json from `TrackRaceResult` object
        """
        query = 'CALL GetTopTrackRaceIndividual({0}, {1}, {2})'.format(event_id, gender_id, limit)
        return self.__get_track_results(self.__get_track_race_result_list(query), max_hof_rank=15)

    def get_track_race_results(self, event_id, squad_id, year):
        """
        Call the stored procedure, `GetTrackRaceResults`, to get the race results as a
        list of json for the given event id, squad id, and year.
        Usage:
            - /bin/apps/track/track_db_app.py
        :param event_id: event id (reference `Event` in DB)
        :param squad_id: squad id (reference `Squad` in DB)
        :param year: year
        :return: list of json from `TrackRaceResult` object
        """
        query = 'CALL GetTrackRaceResults({0}, {1}, {2})'.format(event_id, squad_id, year)
        return self.__get_track_results(self.__get_track_race_result_list(query))

    def get_track_race_results_by_event(self, event_id, gender_id, grade):
        """
        Call the stored procedure, `GetAllTrackRaceResults`, if grade equals 0 or call 
        the stored procedure, `GetTrackRaceResultsByGrade`, to get the race results as 
        a list of json for the given event id, gender id, and grade.
        Usage:
            - /bin/apps/track/track_db_app.py
        :param event_id: event id (reference `Event` in DB)
        :param gender_id: gender id (reference `Gender` in DB)
        :param grade: grade
        :return: list of json from `TrackRaceResult` object
        """
        query = 'CALL GetAllTrackRaceResults({0}, {1})'.format(event_id, gender_id) if grade == 0 \
            else 'CALL GetTrackRaceResultsByGrade({0}, {1}, {2})'.format(event_id, gender_id, grade)
        return self.__get_track_results(self.__get_track_race_result_list(query))

    def __get_track_race_result_list(self, query):
        """
        Get the race results as a list for the given query.
        :param query: mysql query
        :return: list of `TrackRaceResult` object
        """
        try:
            results = self.__get_results(query)
            return [TrackRaceResult(result) for result in results] if results else []
        except Exception as e:
            logging.exception(e)
            raise

    def get_track_hof_relay_results(self, event_id, gender_id, limit=40):
        """
        Call the stored procedure, `GetTopTrackRelayTeam`, to get the relay results 
        as a list of json for the given event id, gender id, and limit.  Limit the 
        hall of fame list to the top 15, which can include ties; therfore, query 
        for a list of at least 40 results.
        Usage:
            - /bin/apps/track/track_db_app.py
        :param event_id: event id (reference `Event` in DB)
        :param gender_id: gender id (reference `Gender` in DB)
        :param limit: limit
        :return: list of json from `TrackRelayResult` object
        """
        query = 'CALL GetTopTrackRelayTeam({0}, {1}, {2})'.format(event_id, gender_id, limit)
        return self.__get_track_results(self.__get_track_relay_result_list(query), max_hof_rank=15)

    def get_track_relay_results(self, event_id, squad_id, year):
        """
        Call the stored procedure, `GetTrackRelayResults`, to get the relay results as a
        list of json for the given event id, squad id, and year.
        Usage:
            - /bin/apps/track/track_db_app.py
        :param event_id: event id (reference `Event` in DB)
        :param squad_id: squad id (reference `Squad` in DB)
        :param year: year
        :return: list of json from `TrackRelayResult` object
        """
        query = 'CALL GetTrackRelayResults({0}, {1}, {2})'.format(event_id, squad_id, year)
        return self.__get_track_results(self.__get_track_relay_result_list(query))

    def get_track_relay_results_by_event(self, event_id, gender_id, squad_id):
        """
        Call the stored procedure, `GetAllTrackRelayResults`, if squad id equals 0 or call 
        the stored procedure, `GetTrackRelayResultsBySquad`, to get the relay results as 
        a list of json for the given event id, gender id, and squad id.
        Usage:
            - /bin/apps/track/track_db_app.py
        :param event_id: event id (reference `Event` in DB)
        :param gender_id: gender id (reference `Gender` in DB)
        :param squad_id: squad id (reference `Squad` in DB)
        :return: list of json from `TrackRelayResult` object
        """
        query = 'CALL GetAllTrackRelayResults({0}, {1})'.format(event_id, gender_id) if squad_id == 0 \
            else 'CALL GetTrackRelayResultsBySquad({0}, {1}, {2})'.format(event_id, gender_id, squad_id)
        return self.__get_track_results(self.__get_track_relay_result_list(query))

    def __get_track_relay_result_list(self, query):
        """
        Get the relay results as a list for the given query.
        :param query: mysql query
        :return: list of `TrackRelayResult` object
        """
        try:
            results = self.__get_results(query)
            return [TrackRelayResult(result) for result in results] if results else []
        except Exception as e:
            logging.exception(e)
            raise

    def __get_track_results(self, query_results, max_hof_rank=None):
        """
        Get the track results as a list of json for the given query results.  If the
        maximum hall of fame rank is provided, then limit the results by that amount.
        :param query_results: query results
        :param max_hof_rank: maximum hall of fame rank
        :return: list of json
        """
        track_results = []
        last_rank = 0
        last_measurement = 0
        for result in query_results:
            current_rank = result.rank
            current_measurement = result.get_measurement()
            current_rank, last_rank, current_measurement, last_measurement = self.__get_rank_measurement_metadata(
                current_rank, last_rank, current_measurement, last_measurement
            )
            if max_hof_rank and last_rank > max_hof_rank:
                break
            result.rank = current_rank
            track_results.append(result.get_json())
        return track_results

    def get_track_hof_field_results(self, event_id, gender_id, limit=40):
        """
        Call the stored procedure, `GetTopFieldIndividual`, to get the field results 
        as a list of json for the given event id, gender id, and limit.  Limit the 
        hall of fame list to the top 15, which can include ties; therfore, query for 
        a list of at least 40 results.
        Usage:
            - /bin/apps/track/track_db_app.py
        :param event_id: event id (reference `Event` in DB)
        :param gender_id: gender id (reference `Gender` in DB)
        :param max_hof_rank: maximum hall of fame rank
        :param limit: limit
        :return: list of json from `TrackFieldResult` object
        """
        query = 'CALL GetTopFieldIndividual({0}, {1}, {2})'.format(event_id, gender_id, limit)
        return self.__get_field_results(self.__get_field_relay_result_list(query), max_hof_rank=15)

    def get_track_field_results(self, event_id, squad_id, year):
        """
        Call the stored procedure, `GetTrackFieldResults`, to get the relay results as a
        list of json for the given event id, squad id, and year.
        Usage:
            - /bin/apps/track/track_db_app.py
        :param event_id: event id (reference `Event` in DB)
        :param squad_id: squad id (reference `Squad` in DB)
        :param year: year
        :return: list of json from `TrackFieldResult` object
        """
        query = 'CALL GetTrackFieldResults({0}, {1}, {2})'.format(event_id, squad_id, year)
        return self.__get_field_results(self.__get_field_relay_result_list(query))

    def get_track_field_results_by_event(self, event_id, gender_id, grade):
        """
        Call the stored procedure, `GetAllTrackFieldResults`, if grade equals 0 or call 
        the stored procedure, `GetTrackFieldResultsByGrade`, to get the field results as 
        a list of json for the given event id, gender id, and grade.
        Usage:
            - /bin/apps/track/track_db_app.py
        :param event_id: event id (reference `Event` in DB)
        :param gender_id: gender id (reference `Gender` in DB)
        :param grade: grade
        :return: list of json from `TrackFieldResult` object
        """
        query = 'CALL GetAllTrackFieldResults({0}, {1})'.format(event_id, gender_id) if grade == 0 \
            else 'CALL GetTrackFieldResultsByGrade({0}, {1}, {2})'.format(event_id, gender_id, grade)
        return self.__get_field_results(self.__get_field_relay_result_list(query))

    def __get_field_relay_result_list(self, query):
        """
        Get the field results as a list for the given query.
        :param query: mysql query
        :return: list of `TrackFieldResult` object
        """
        try:
            results = self.__get_results(query)
            return [TrackFieldResult(result) for result in results] if results else []
        except Exception as e:
            logging.exception(e)
            raise

    def __get_field_results(self, query_results, max_hof_rank=None):
        """
        Get the field results as a list of json for the given query results.  If the
        maximum hall of fame rank is provided, then limit the results by that amount.
        :param query_results: query results
        :param max_hof_rank: maximum hall of fame rank
        :return: list of json
        """
        field_results = []
        last_rank = 0
        last_measurement = 0
        for result in query_results:
            current_rank = result.rank
            current_measurement = result.get_measurement()
            current_rank, last_rank, current_measurement, last_measurement = self.__get_rank_measurement_metadata(
                current_rank, last_rank, current_measurement, last_measurement
            )
            if max_hof_rank and last_rank > max_hof_rank:
                break
            result.rank = current_rank
            field_results.append(result.get_json())
        return field_results

    def get_track_competitor_results(self, competitor_id):
        """
        Call the stored procedure, `GetTrackCompetitorResults`, to get the track competitor 
        results as a list of json for the given competitor id.
        Usage:
            - /bin/apps/track/track_db_app.py
        :param competitor_id: competitor id (reference `Competitor` in DB)
        :return: list of json from `TrackCompetitorResult` object
        """
        
        query = 'CALL GetTrackCompetitorResults("{0}")'.format(competitor_id)
        male_eid_tcr_list_odict, female_eid_tcr_list_odict = self.__get_eid_tcr_list_odicts(query)
        track_competitor_results = self.__get_tcr_from_odict(competitor_id, male_eid_tcr_list_odict)
        if not track_competitor_results:
            track_competitor_results = self.__get_tcr_from_odict(competitor_id, female_eid_tcr_list_odict)
        return track_competitor_results

    def get_track_athlete_results(self, athlete_id):
        """
        Call the stored procedure, `GetTrackCompetitorResults`, to get the track competitor 
        results as a list of json for the given competitor id.
        Usage:
            - /bin/apps/track/track_db_app.py
        :param athlete_id: athlete id (reference `Athlete` in DB)
        :return: list of json from `TrackCompetitorResult` object
        """
        track_athlete_results = []
        personal_record_dict = {}

        query = 'CALL GetTrackAthleteResults("{0}")'.format(athlete_id)
        athlete_result_metadata_list = []
        male_eid_tcr_list_odict, female_eid_tcr_list_odict = self.__get_eid_tcr_list_odicts(query, arm_list=athlete_result_metadata_list)

        # iterate over the metadata
        for athlete_result_metadata in athlete_result_metadata_list:
            event_id = athlete_result_metadata.get_event_id()
            pr_key = athlete_result_metadata.get_personal_record_key()
            competitor_id = athlete_result_metadata.get_competitor_id()

            # calculate the rankings by looking up the competitor id in the event specific results 
            track_competitor_result = self.__get_tcr_and_set_rankings(competitor_id, male_eid_tcr_list_odict.get(event_id))
            if not track_competitor_result:
                track_competitor_result = self.__get_tcr_and_set_rankings(competitor_id, female_eid_tcr_list_odict.get(event_id))
            
            if track_competitor_result:
                track_athlete_results.append(track_competitor_result.get_json())

                # determine which are the personal records
                pr_result = personal_record_dict.get(pr_key)
                if pr_result is None or track_competitor_result.all_rank <= pr_result.all_rank:
                    track_competitor_result.personal_record = True
                    personal_record_dict[pr_key] = track_competitor_result

        # sort and add the personal records
        for pr_key in OrderedDict(sorted(personal_record_dict.items())):
            track_athlete_results.append(personal_record_dict.get(pr_key).get_json())

        return track_athlete_results

    def __get_eid_tcr_list_odicts(self, query, arm_list=None):
        """
        Get 2 ordered dictionaries of event ids to a list of TrackCompetitorResult for males and females.
        If the list of athlete result metadata is passed, then populate the list with AthleteResultMetadata
        where the mysql result has a length of 4 (ie 4 key/values in its dictionary).
        :param query: mysql query
        :param arm_list: list of AthleteResultMetadata
        :return: 2 ordered dictionaries for male and females
        """
        try:
            male_eid_tcr_list_odict = OrderedDict()
            female_eid_tcr_list_odict = OrderedDict()
            for mysql_result in self.__get_results(query):
                if arm_list is not None and len(mysql_result) == 4:
                    arm_list.append(AthleteResultMetadata(mysql_result))
                else:
                    track_competitor_result = TrackCompetitorResult(mysql_result)
                    if track_competitor_result.has_data():
                        event_id = mysql_result.get('eventId')
                        gender_id = mysql_result.get('genderId')
                        if gender_id == 2:
                            self.__add_to_odict(male_eid_tcr_list_odict, event_id, track_competitor_result)
                        elif gender_id == 3:
                            self.__add_to_odict(female_eid_tcr_list_odict, event_id, track_competitor_result)
            return male_eid_tcr_list_odict, female_eid_tcr_list_odict
        except Exception as e:
            logging.exception(e)
            raise

    def __add_to_odict(self, eid_tcr_list_odict, event_id, track_competitor_result):
        """
        Add the TrackCompetitorResult to the ordered dictionary (of event ids to a list of 
        TrackCompetitorResult) for the given event id.
        :param eid_tcr_list_odict: ordered dictionary of event ids to a list of TrackCompetitorResult
        :param event_id: event id (reference `Event` in DB)
        :param track_competitor_result: TrackCompetitorResult
        :return: n/a
        """
        tcr_list = eid_tcr_list_odict.get(event_id)
        if tcr_list is None:
            tcr_list = []
            eid_tcr_list_odict[event_id] = tcr_list
        tcr_list.append(track_competitor_result)

    def __get_tcr_from_odict(self, competitor_id, eid_tcr_list_odict):
        """
        Iterate over the ordered dictionary of event ids to a list of TrackCompetitorResult
        and collect the track competitor results as a list of json for the given competitor id.
        :param competitor_id: competitor id (reference `Competitor` in DB)
        :param eid_tcr_list_odict: ordered dictionary of event ids to a list of TrackCompetitorResult
        :return: list of json from `TrackCompetitorResult` object
        """
        track_competitor_results = []
        for event_id, track_competitor_result_list in eid_tcr_list_odict.items():
            track_competitor_result = self.__get_tcr_and_set_rankings(competitor_id, track_competitor_result_list)
            if track_competitor_result:
                track_competitor_results.append(track_competitor_result.get_json())
        return track_competitor_results

    def __set_rankings(self, competitor_id, track_competitor_result_list, track_competitor_results):
        """
        Attempt to get the TrackCompetitorResult from the competitor id and list of TrackCompetitorResult.
        If found, then set all the rankings and add the json the track_competitor_results.  Return the 
        TrackCompetitorResult that is matched (if any).
        :param competitor_id: competitor id
        :param track_competitor_result_list: list of TrackCompetitorResult
        :param track_competitor_results: list of json from `TrackCompetitorResult` object
        :return: TrackCompetitorResult
        """
        track_competitor_result = self.__get_track_competitor_result(competitor_id, track_competitor_result_list)
        if track_competitor_result:
            self.__set_all_grade_ranking(track_competitor_result, track_competitor_result_list)
            self.__set_year_squad_ranking(track_competitor_result, track_competitor_result_list)
            track_competitor_results.append(track_competitor_result.get_json())
        return track_competitor_result

    def __get_tcr_and_set_rankings(self, competitor_id, track_competitor_result_list):
        """
        Get the TrackCompetitorResult from the given list of TrackCompetitorResult which 
        matches the given competitor id.  Also, set the all rank and all total metadata to 
        the matching TrackCompetitorResult while iterating over the list.  Finally, if the
        TrackCompetitorResult is found, also set the grade and year squad rankings/totals.
        :param competitor_id: competitor id
        :param track_competitor_result_list: list of TrackCompetitorResult
        :return: current rank, last rank, current measurement, last measurement
        """
        track_competitor_result = None
        if track_competitor_result_list:
            last_rank = 0
            last_measurement = 0
            for tcr in track_competitor_result_list:
                current_rank = tcr.get_rank()
                current_measurement = tcr.get_measurement()
                current_rank, last_rank, current_measurement, last_measurement = self.__get_rank_measurement_metadata(
                    current_rank, last_rank, current_measurement, last_measurement
                )
                if competitor_id == tcr.get_competitor_id():
                    tcr.set_all_rank(current_rank)
                    tcr.set_all_total(len(track_competitor_result_list))
                    track_competitor_result = tcr
                    break
            if track_competitor_result:
                self.__set_grade_ranking(track_competitor_result, track_competitor_result_list)
                self.__set_year_squad_ranking(track_competitor_result, track_competitor_result_list)
        return track_competitor_result

    def __set_grade_ranking(self, track_competitor_result, track_competitor_result_list):
        """
        Set the grade rank and grade total metadata to the given TrackCompetitorResult by
        iterating over the give list TrackCompetitorResult and comparing matching grades.
        :param track_competitor_result: TrackCompetitorResult
        :param track_competitor_result_list: list of TrackCompetitorResult
        :return: n/a
        """
        last_rank = 0
        last_measurement = 0
        grade_total = 0
        found_competitor = False
        for tcr in track_competitor_result_list:
            if track_competitor_result.get_grade() == tcr.get_grade():
                grade_total += 1
                if not found_competitor:
                    current_rank = grade_total
                    current_measurement = tcr.get_measurement()
                    current_rank, last_rank, current_measurement, last_measurement = self.__get_rank_measurement_metadata(
                        current_rank, last_rank, current_measurement, last_measurement
                    )
                    if track_competitor_result.get_competitor_id() == tcr.get_competitor_id():
                        found_competitor = True
                        track_competitor_result.set_grade_rank(current_rank)
        track_competitor_result.set_grade_total(grade_total)

    def __set_year_squad_ranking(self, track_competitor_result, track_competitor_result_list):
        """
        Set the year squad rank and year squad total metadata to the given TrackCompetitorResult 
        by iterating over the give list TrackCompetitorResult and comparing matching year squad.
        :param track_competitor_result: TrackCompetitorResult
        :param track_competitor_result_list: list of TrackCompetitorResult
        :return: n/a
        """
        last_rank = 0
        last_measurement = 0
        year_squad_total = 0
        found_competitor = False
        for tcr in track_competitor_result_list:
            if track_competitor_result.get_year() == tcr.get_year() and track_competitor_result.get_squad_id() == tcr.get_squad_id():
                year_squad_total += 1
                if not found_competitor:
                    current_rank = year_squad_total
                    current_measurement = tcr.get_measurement()
                    current_rank, last_rank, current_measurement, last_measurement = self.__get_rank_measurement_metadata(
                        current_rank, last_rank, current_measurement, last_measurement
                    )
                    if track_competitor_result.get_competitor_id() == tcr.get_competitor_id():
                        found_competitor = True
                        track_competitor_result.set_year_squad_rank(current_rank)
        track_competitor_result.set_year_squad_total(year_squad_total)

    def __get_rank_measurement_metadata(self, current_rank, last_rank, current_measurement, last_measurement):
        """
        Get the rank measurement metadata given the current rank, last rank, current
        measurement, and last measurement.
        :param current_rank: current rank
        :param last_rank: last rank
        :param current_measurement: current measurement
        :param last_measurement: last measurement
        :return: current rank, last rank, current measurement, last measurement
        """
        if last_rank > 0:
            if current_measurement == last_measurement:
                current_rank = last_rank
            else:
                last_rank = current_rank
                last_measurement = current_measurement
        else:
            last_rank = current_rank
            last_measurement = current_measurement
        return current_rank, last_rank, current_measurement, last_measurement

    def __get_results(self, query):
        """
        Get the results as a dictionary for the given query.
        :param query: mysql query
        :return: dictionary results
        """
        return self.mysql.query_multi_with_fetchall_as_dict(query)
