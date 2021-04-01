__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

import logging

from flask import Blueprint, render_template, json, request
from bin.utils import Utils
from bin.db.xc.xc_dai import XcDAI
from bin.db.xc.xc_results_dai import XcResultsDAI


xc_db_app = Blueprint('xc_db_app', __name__, template_folder='templates')

xc_dai = XcDAI()
xc_results_dai = XcResultsDAI()


@xc_db_app.route('/getTopCourseResults', methods=['GET'])
def get_top_course_results():
    """
    Get the top race result as a list of json for the given `courseId`, `genderId`, `limit`, 
    and `grade` within the request arguments.  Check the cache prior to querying the DB.  If 
    a DB query is required, then cache the results.
    Usage:
        - /templates/xc/course-results/topCourseResults.html
    :return: list of json from `XcRaceResult` object
    """
    try:
        course_id = request.args.get('courseId', default = 1, type = int)
        gender_id = request.args.get('genderId', default = 2, type = int)
        limit = request.args.get('limit', default = 25, type = int)
        grade = request.args.get('grade', default = 0, type = int)
        top_course_results_cache_key = Utils.get_cache_key_four('get_top_course_results_', course_id, gender_id, grade, limit)
        top_course_results = Utils.cache_get(top_course_results_cache_key)
        if not top_course_results:
            top_results_dict = []
            if grade == 0:
                top_results_dict = xc_results_dai.get_xc_top_individual(course_id, gender_id, limit)
            else:
                top_results_dict = xc_results_dai.get_xc_top_individual_by_grade(course_id, gender_id, grade, limit)
            top_course_results = json.dumps(top_results_dict)
            Utils.cache_set(top_course_results_cache_key, top_course_results)
        return top_course_results
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error = str(e))


@xc_db_app.route('/getCourseInfo', methods=['GET'])
def get_course_info():
    """
    Get the top course info as a list of json for the given `courseId` with the
    request arguments.  Check the cache prior to querying the DB.  If a DB query 
    is required, then cache the results.
    Usage:
        - /templates/xc/course-results/teamCourseResults.html
        - /templates/xc/course-results/topCourseResults.html
    :return: list of json from `XcCourse` object
    """
    try:
        course_id = request.args.get('courseId', default = 1, type = int)
        course_info_cache_key = Utils.get_cache_key_one('get_course_info_', course_id)
        course_info = Utils.cache_get(course_info_cache_key)
        if not course_info:
            course_info = json.dumps(xc_dai.get_course_info(course_id))
            Utils.cache_set(course_info_cache_key, course_info)
        return course_info
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error = str(e))


@xc_db_app.route('/getTopTeamCourseResults', methods=['GET'])
def get_top_team_course_results():
    """
    Get the top team result as a list of json for the given `courseId`, `genderId`, and 
    `limit` within the request arguments.  Check the cache prior to querying the DB.  If 
    a DB query is required, then cache the results.
    Usage:
        - /templates/xc/course-results/teamCourseResults.html
    :return: list of json from `XcTopTeamResult` object
    """
    try:
        course_id = request.args.get('courseId', default = 1, type = int)
        gender_id = request.args.get('genderId', default = 2, type = int)
        limit = request.args.get('limit', default = 15, type = int)
        top_team_course_results_cache_key = Utils.get_cache_key_three('get_top_team_course_results_', course_id, gender_id, limit)
        ret_top_team_course_results = Utils.cache_get(top_team_course_results_cache_key)
        if not ret_top_team_course_results:
            top_team_course_results, top_race_ids, top_competitor_ids = xc_results_dai.get_top_team_course(course_id, gender_id, limit)
            race_competitor_data_dict = xc_results_dai.get_xc_results_by_race_competitor(top_race_ids, top_competitor_ids)
            top_team_course_results_dict = []
            for result in top_team_course_results:
                result.calc_times(race_competitor_data_dict)
                top_team_course_results_dict.append(result.get_json())
            ret_top_team_course_results = json.dumps(top_team_course_results_dict)
            Utils.cache_set(top_team_course_results_cache_key, ret_top_team_course_results)
        return ret_top_team_course_results
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error = str(e))


@xc_db_app.route('/getXcRunners', methods=['GET'])
def get_xc_runners():
    """
    Get the runnners as a list of json for the given `genderId` with the request 
    arguments.  Check the cache prior to querying the DB.  If a DB query is
    required, then cache the results.
    Usage:
        - /templates/xc/runners/runners.html
    :return: list of json from `Athlete` object
    """
    try:
        gender_id = request.args.get('genderId', default = '2,3', type = str)
        xc_runners_cache_key = Utils.get_cache_key_one('get_xc_runners_', gender_id)
        xc_runners = Utils.cache_get(xc_runners_cache_key)
        if not xc_runners:
            xc_runners = json.dumps(xc_dai.get_xc_runners(gender_id))
            Utils.cache_set(xc_runners_cache_key, xc_runners)
        return xc_runners
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error = str(e))


@xc_db_app.route('/getXcRunnerResults', methods=['GET'])
def get_xc_runner_results():
    """
    Get the xc competitor result as a list of json for the given `runnerId` within  
    the request arguments.  Check the cache prior to querying the DB.  If a DB query is 
    required, then cache the results.
    Usage:
        - /templates/xc/runners/runner.html
    :return: list of json from `XcCompetitorResult` object
    """
    try:
        runner_id = request.args.get('runnerId', default = 1, type = int)
        xc_runner_results_cache_key = Utils.get_cache_key_one('get_xc_runner_results_', runner_id)
        xc_runner_results = Utils.cache_get(xc_runner_results_cache_key)
        if not xc_runner_results:
            xc_runner_results = json.dumps(xc_results_dai.get_xc_runner_results(runner_id))
            Utils.cache_set(xc_runner_results_cache_key, xc_runner_results)
        return xc_runner_results
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error = str(e))


@xc_db_app.route('/getXcCompetitorsByYear', methods=['GET'])
def get_xc_competitors_by_year():
    """
    Get the competitor as a list of json for the given `year` and `genderId` within 
    the request arguments.  Check the cache prior to querying the DB.  If a DB query 
    is required, then cache the results.
    Usage:
        - /templates/xc/season/season.html
    :return: list of json from `Competitor` object
    """
    try:
        year = request.args.get('year', default = 2003, type = int)
        gender_id = request.args.get('genderId', default = 2, type = int)
        xc_competitors_by_year_cache_key = Utils.get_cache_key_two('get_xc_competitors_by_year_', year, gender_id)
        xc_competitors_by_year = Utils.cache_get(xc_competitors_by_year_cache_key)
        if not xc_competitors_by_year:
            xc_competitors_by_year = json.dumps(xc_dai.get_xc_competitors_by_year(year, gender_id))
            Utils.cache_set(xc_competitors_by_year_cache_key, xc_competitors_by_year)
        return xc_competitors_by_year
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error = str(e))


@xc_db_app.route('/getXcRacesByYear', methods=['GET'])
def get_xc_races_by_year():
    """
    Get the race as a list of json for the given `year` within the request arguments.  
    Check the cache prior to querying the DB.  If a DB query is required, then cache
    the results.
    Usage:
        - /templates/xc/season/season.html
    :return: list of json from `XcRace` object
    """
    try:
        year = request.args.get('year', default = 2003, type = int)
        xc_races_by_year_cache_key = Utils.get_cache_key_one('get_xc_races_by_year_', year)
        xc_races_by_year = Utils.cache_get(xc_races_by_year_cache_key)
        if not xc_races_by_year:
            xc_races_by_year = json.dumps(xc_dai.get_xc_races_by_year(year))
            Utils.cache_set(xc_races_by_year_cache_key, xc_races_by_year)
        return xc_races_by_year
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error = str(e))


@xc_db_app.route('/getXcCompetitorResults', methods=['GET'])
def get_xc_competitor_results():
    """
    Get the xc competitor result as a list of json for the given `competitorId` within  
    the request arguments.  Check the cache prior to querying the DB.  If a DB query is 
    required, then cache the results.
    Usage:
        - /templates/xc/competitors/competitor.html
    :return: list of json from `XcCompetitorResult` object
    """
    try:
        competitor_id = request.args.get('competitorId', default = 1.12, type = str)
        xc_competitor_results_cache_key = Utils.get_cache_key_one('get_xc_competitor_results_', competitor_id)
        xc_competitor_results = Utils.cache_get(xc_competitor_results_cache_key)
        if not xc_competitor_results:
            xc_competitor_results = json.dumps(xc_results_dai.get_xc_competitor_results(competitor_id))
            Utils.cache_set(xc_competitor_results_cache_key, xc_competitor_results)
        return xc_competitor_results
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error = str(e))


@xc_db_app.route('/getXcRaceResults', methods=['GET'])
def get_xc_race_results():
    """
    Get the xc race result as a list of json for the given `raceId` and `genderId` within  
    the request arguments.  Check the cache prior to querying the DB.  If a DB query is 
    required, then cache the results.
    Usage:
        - /templates/xc/race-results/raceResults.html
    :return: list of json from `XcRaceResult` object
    """
    try:
        race_id = request.args.get('raceId', default = 1000132, type = int)
        gender_id = request.args.get('genderId', default = 0, type = int)
        xc_race_results_cache_key = Utils.get_cache_key_two('get_xc_race_results_', race_id, gender_id)
        xc_race_results = Utils.cache_get(xc_race_results_cache_key)
        if not xc_race_results:
            xc_race_results_dict = []
            if gender_id == 0:
                xc_race_results_dict = xc_results_dai.get_all_xc_race_results(race_id)
            else:
                xc_race_results_dict = xc_results_dai.get_xc_race_results(race_id, gender_id)
            xc_race_results = json.dumps(xc_race_results_dict)
            Utils.cache_set(xc_race_results_cache_key, xc_race_results)
        return xc_race_results
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error = str(e))


@xc_db_app.route('/getPastXcAlumniChampions', methods=['GET'])
def get_past_xc_alumni_champions():
    """
    Get the xc competitor result as a list of json for the past xc alumni champions.  
    Check the cache prior to querying the DB.  If a DB query is required, then cache 
    the results.
    Usage:
        - /templates/xc/special-achievements/pastXcAlumniChampions.html
    :return: list of json from `XcCompetitorResult` object
    """
    try:
        past_xc_alumni_champions_cache_key = 'get_past_xc_alumni_champions'
        past_xc_alumni_champions = Utils.cache_get(past_xc_alumni_champions_cache_key)
        if not past_xc_alumni_champions:
            past_xc_alumni_champions = json.dumps(xc_results_dai.get_past_xc_alumni_champions())
            Utils.cache_set(past_xc_alumni_champions_cache_key, past_xc_alumni_champions)
        return past_xc_alumni_champions
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error = str(e))
