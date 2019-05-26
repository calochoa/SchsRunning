__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


track_hall_of_fame_seo_app = Blueprint(
    'track_hall_of_fame_seo_app', __name__, template_folder='templates', url_prefix='/santa-clara-high-track-and-field/hall-of-fame'
)    


def get_track_hof_race_results(event_id, gender_id):
    return render_template('track/hall-of-fame/hallOfFameRaceResults.html', eId=event_id, gId=gender_id)

def get_track_hof_relay_results(event_id, gender_id):
    return render_template('track/hall-of-fame/hallOfFameRelayResults.html', eId=event_id, gId=gender_id)

def get_track_hof_field_results(event_id, gender_id):
    return render_template('track/hall-of-fame/hallOfFameFieldResults.html', eId=event_id, gId=gender_id)



@track_hall_of_fame_seo_app.route('/',methods=['GET'])
def track_hof_home():
    return render_template('track/hall-of-fame/hallOfFame.html')

@track_hall_of_fame_seo_app.route('/drop-down-menus',methods=['GET'])
def track_hof_drop_down_menus():
    return render_template('track/hall-of-fame/hallOfFameDropDownMenus.html')

# Sprints
@track_hall_of_fame_seo_app.route('/boys-100m-dash/',methods=['GET'])
def track_boys_100m_dash():
    return get_track_hof_race_results(1, 2)

@track_hall_of_fame_seo_app.route('/boys-200m-dash/',methods=['GET'])
def track_boys_200m_dash():
    return get_track_hof_race_results(2, 2)

@track_hall_of_fame_seo_app.route('/boys-100yd-dash/',methods=['GET'])
def track_boys_100yd_dash():
    return get_track_hof_race_results(4, 2)

@track_hall_of_fame_seo_app.route('/boys-220yd-dash/',methods=['GET'])
def track_boys_220yd_dash():
    return get_track_hof_race_results(5, 2)

@track_hall_of_fame_seo_app.route('/boys-440yd-dash/',methods=['GET'])
def track_boys_440yd_dash():
    return get_track_hof_race_results(6, 2)

@track_hall_of_fame_seo_app.route('/girls-100m-dash/',methods=['GET'])
def track_girls_100m_dash():
    return get_track_hof_race_results(1, 3)

@track_hall_of_fame_seo_app.route('/girls-200m-dash/',methods=['GET'])
def track_girls_200m_dash():
    return get_track_hof_race_results(2, 3)

@track_hall_of_fame_seo_app.route('/girls-400m-dash/',methods=['GET'])
def track_girls_400m_dash():
    return get_track_hof_race_results(3, 3)

@track_hall_of_fame_seo_app.route('/girls-100yd-dash/',methods=['GET'])
def track_girls_100yd_dash():
    return get_track_hof_race_results(4, 3)

@track_hall_of_fame_seo_app.route('/girls-220yd-dash/',methods=['GET'])
def track_girls_220yd_dash():
    return get_track_hof_race_results(5, 3)



# Distance 
@track_hall_of_fame_seo_app.route('/boys-880yd-run/',methods=['GET'])
def track_boys_880yd_run():
    return get_track_hof_race_results(10, 2)

@track_hall_of_fame_seo_app.route('/boys-1600m-run/',methods=['GET'])
def track_boys_1600m_run():
    return get_track_hof_race_results(8, 2)

@track_hall_of_fame_seo_app.route('/boys-2-mile-run/',methods=['GET'])
def track_boys_2_mile_run():
    return get_track_hof_race_results(12, 2)

@track_hall_of_fame_seo_app.route('/girls-880yd-run/',methods=['GET'])
def track_girls_880yd_run():
    return get_track_hof_race_results(10, 3)

@track_hall_of_fame_seo_app.route('/girls-1600m-run/',methods=['GET'])
def track_girls_1600m_run():
    return get_track_hof_race_results(8, 3)

@track_hall_of_fame_seo_app.route('/girls-2-mile-run/',methods=['GET'])
def track_girls_2_mile_run():
    return get_track_hof_race_results(12, 3)



# Hurdles 
@track_hall_of_fame_seo_app.route('/boys-120yd-hurdles/',methods=['GET'])
def track_boys_120yd_hurdles():
    return get_track_hof_race_results(23, 2)

@track_hall_of_fame_seo_app.route('/boys-330yd-hurdles/',methods=['GET'])
def track_boys_330yd_hurdles():
    return get_track_hof_race_results(24, 2)

@track_hall_of_fame_seo_app.route('/girls-100m-hurdles-30in/',methods=['GET'])
def track_girls_100m_hurdles_30in():
    return get_track_hof_race_results(22, 3)

@track_hall_of_fame_seo_app.route('/girls-100m-hurdles-33in/',methods=['GET'])
def track_girls_100m_hurdles_33in():
    return get_track_hof_race_results(18, 3)

@track_hall_of_fame_seo_app.route('/girls-300m-hurdles-30in/',methods=['GET'])
def track_girls_300m_hurdles_30in():
    return get_track_hof_race_results(20, 3)



# Relays
@track_hall_of_fame_seo_app.route('/boys-400m-relay/',methods=['GET'])
def track_boys_400m_relay():
    return get_track_hof_relay_results(25, 2)

@track_hall_of_fame_seo_app.route('/boys-mile-relay/',methods=['GET'])
def track_boys_mile_relay():
    return get_track_hof_relay_results(28, 2)

@track_hall_of_fame_seo_app.route('/girls-440yd-relay/',methods=['GET'])
def track_girls_440yd_relay():
    return get_track_hof_relay_results(27, 3)

@track_hall_of_fame_seo_app.route('/girls-400m-relay/',methods=['GET'])
def track_girls_400m_relay():
    return get_track_hof_relay_results(25, 3)

@track_hall_of_fame_seo_app.route('/girls-1600m-relay/',methods=['GET'])
def track_girls_1600m_relay():
    return get_track_hof_relay_results(26, 3)



# Jumps
@track_hall_of_fame_seo_app.route('/boys-high-jump/',methods=['GET'])
def track_boys_high_jump():
    return get_track_hof_field_results(29, 2)

@track_hall_of_fame_seo_app.route('/boys-long-jump/',methods=['GET'])
def track_boys_long_jump():
    return get_track_hof_field_results(30, 2)

@track_hall_of_fame_seo_app.route('/boys-triple-jump/',methods=['GET'])
def track_boys_triple_jump():
    return get_track_hof_field_results(31, 2)

@track_hall_of_fame_seo_app.route('/boys-pole-vault/',methods=['GET'])
def track_boys_pole_vault():
    return get_track_hof_field_results(32, 2)

@track_hall_of_fame_seo_app.route('/girls-high-jump/',methods=['GET'])
def track_girls_high_jump():
    return get_track_hof_field_results(29, 3)

@track_hall_of_fame_seo_app.route('/girls-long-jump/',methods=['GET'])
def track_girls_long_jump():
    return get_track_hof_field_results(30, 3)

@track_hall_of_fame_seo_app.route('/girls-triple-jump/',methods=['GET'])
def track_girls_triple_jump():
    return get_track_hof_field_results(31, 3)

@track_hall_of_fame_seo_app.route('/girls-pole-vault/',methods=['GET'])
def track_girls_pole_vault():
    return get_track_hof_field_results(32, 3)



# Throws
@track_hall_of_fame_seo_app.route('/boys-shot-put-12lb/',methods=['GET'])
def track_boys_shot_put_12lb():
    return get_track_hof_field_results(35, 2)

@track_hall_of_fame_seo_app.route('/boys-discus-1.6kg/',methods=['GET'])
def track_boys_discus_1_6kg():
    return get_track_hof_field_results(37, 2)

@track_hall_of_fame_seo_app.route('/girls-shot-put-4kg/',methods=['GET'])
def track_girls_shot_put_4kg():
    return get_track_hof_field_results(33, 3)

@track_hall_of_fame_seo_app.route('/girls-discus-1kg/',methods=['GET'])
def track_girls_discus_1kg():
    return get_track_hof_field_results(36, 3)


