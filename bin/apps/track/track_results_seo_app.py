__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


track_results_seo_app = Blueprint(
    'track_results_seo_app', __name__, template_folder='templates', url_prefix='/santa-clara-high-track-and-field/results'
)    


def get_track_race_results(event_id, squad_id, year):
    return render_template('track/results/raceResults.html', eId=event_id, sId=squad_id, yr=year)

def get_track_field_results(event_id, squad_id, year):
    return render_template('track/results/fieldResults.html', eId=event_id, sId=squad_id, yr=year)

def get_track_relay_results(event_id, squad_id, year):
    return render_template('track/results/relayResults.html', eId=event_id, sId=squad_id, yr=year)


@track_results_seo_app.route('/<int:event_id>/<int:squad_id>/<int:year>/',methods=['GET'])
def track_results(event_id, squad_id, year):
    if event_id == 1:
        if squad_id == 1:
            return redirect('/santa-clara-high-track-and-field/results/varsity-girls-100m-dash/{0}/'.format(year))
        if squad_id == 2:
            return redirect('/santa-clara-high-track-and-field/results/varsity-boys-100m-dash/{0}/'.format(year))
        if squad_id == 3:
            return redirect('/santa-clara-high-track-and-field/results/junior-varsity-girls-100m-dash/{0}/'.format(year))
        if squad_id == 4:
            return redirect('/santa-clara-high-track-and-field/results/frosh-soph-boys-100m-dash/{0}/'.format(year))
    if event_id == 2:
        if squad_id == 1:
            return redirect('/santa-clara-high-track-and-field/results/varsity-girls-200m-dash/{0}/'.format(year))
        if squad_id == 2:
            return redirect('/santa-clara-high-track-and-field/results/varsity-boys-200m-dash/{0}/'.format(year))
        if squad_id == 3:
            return redirect('/santa-clara-high-track-and-field/results/junior-varsity-girls-200m-dash/{0}/'.format(year))
        if squad_id == 4:
            return redirect('/santa-clara-high-track-and-field/results/frosh-soph-boys-200m-dash/{0}/'.format(year))
    if event_id == 3:
        if squad_id == 1:
            return redirect('/santa-clara-high-track-and-field/results/varsity-girls-400m-dash/{0}/'.format(year))
        if squad_id == 2:
            return redirect('/santa-clara-high-track-and-field/results/varsity-boys-400m-dash/{0}/'.format(year))
        if squad_id == 3:
            return redirect('/santa-clara-high-track-and-field/results/junior-varsity-girls-400m-dash/{0}/'.format(year))
        if squad_id == 4:
            return redirect('/santa-clara-high-track-and-field/results/frosh-soph-boys-400m-dash/{0}/'.format(year))
    if event_id == 7:
        if squad_id == 1:
            return redirect('/santa-clara-high-track-and-field/results/varsity-girls-800m-run/{0}/'.format(year))
        if squad_id == 2:
            return redirect('/santa-clara-high-track-and-field/results/varsity-boys-800m-run/{0}/'.format(year))
        if squad_id == 3:
            return redirect('/santa-clara-high-track-and-field/results/junior-varsity-girls-800m-run/{0}/'.format(year))
        if squad_id == 4:
            return redirect('/santa-clara-high-track-and-field/results/frosh-soph-boys-800m-run/{0}/'.format(year))
    if event_id == 8:
        if squad_id == 1:
            return redirect('/santa-clara-high-track-and-field/results/varsity-girls-1600m-run/{0}/'.format(year))
        if squad_id == 2:
            return redirect('/santa-clara-high-track-and-field/results/varsity-boys-1600m-run/{0}/'.format(year))
        if squad_id == 3:
            return redirect('/santa-clara-high-track-and-field/results/junior-varsity-girls-1600m-run/{0}/'.format(year))
        if squad_id == 4:
            return redirect('/santa-clara-high-track-and-field/results/frosh-soph-boys-1600m-run/{0}/'.format(year))
    if event_id == 9:
        if squad_id == 1:
            return redirect('/santa-clara-high-track-and-field/results/varsity-girls-3200m-run/{0}/'.format(year))
        if squad_id == 2:
            return redirect('/santa-clara-high-track-and-field/results/varsity-boys-3200m-run/{0}/'.format(year))
        if squad_id == 3:
            return redirect('/santa-clara-high-track-and-field/results/junior-varsity-girls-3200m-run/{0}/'.format(year))
        if squad_id == 4:
            return redirect('/santa-clara-high-track-and-field/results/frosh-soph-boys-3200m-run/{0}/'.format(year))
    if event_id == 17:
        if squad_id == 4:
            return redirect('/santa-clara-high-track-and-field/results/frosh-soph-boys-65m-hurdles-39in/{0}/'.format(year))
    if event_id == 18:
        if squad_id == 1:
            return redirect('/santa-clara-high-track-and-field/results/varsity-girls-100m-hurdles-33in/{0}/'.format(year))
        if squad_id == 3:
            return redirect('/santa-clara-high-track-and-field/results/junior-varsity-girls-100m-hurdles-33in/{0}/'.format(year))
    if event_id == 19:
        if squad_id == 2:
            return redirect('/santa-clara-high-track-and-field/results/varsity-boys-110m-hurdles-39in/{0}/'.format(year))
    if event_id == 20:
        if squad_id == 1:
            return redirect('/santa-clara-high-track-and-field/results/varsity-girls-300m-hurdles-30in/{0}/'.format(year))
        if squad_id == 3:
            return redirect('/santa-clara-high-track-and-field/results/junior-varsity-girls-300m-hurdles-30in/{0}/'.format(year))
    if event_id == 21:
        if squad_id == 2:
            return redirect('/santa-clara-high-track-and-field/results/varsity-boys-300m-hurdles-36in/{0}/'.format(year))
        if squad_id == 4:
            return redirect('/santa-clara-high-track-and-field/results/frosh-soph-boys-300m-hurdles-36in/{0}/'.format(year))
    if event_id == 25:
        if squad_id == 1:
            return redirect('/santa-clara-high-track-and-field/results/varsity-girls-400m-relay/{0}/'.format(year))
        if squad_id == 2:
            return redirect('/santa-clara-high-track-and-field/results/varsity-boys-400m-relay/{0}/'.format(year))
        if squad_id == 3:
            return redirect('/santa-clara-high-track-and-field/results/junior-varsity-girls-400m-relay/{0}/'.format(year))
        if squad_id == 4:
            return redirect('/santa-clara-high-track-and-field/results/frosh-soph-boys-400m-relay/{0}/'.format(year))
    if event_id == 26:
        if squad_id == 1:
            return redirect('/santa-clara-high-track-and-field/results/varsity-girls-1600m-relay/{0}/'.format(year))
        if squad_id == 2:
            return redirect('/santa-clara-high-track-and-field/results/varsity-boys-1600m-relay/{0}/'.format(year))
        if squad_id == 3:
            return redirect('/santa-clara-high-track-and-field/results/junior-varsity-girls-1600m-relay/{0}/'.format(year))
        if squad_id == 4:
            return redirect('/santa-clara-high-track-and-field/results/frosh-soph-boys-1600m-relay/{0}/'.format(year))
    if event_id == 29:
        if squad_id == 1:
            return redirect('/santa-clara-high-track-and-field/results/varsity-girls-high-jump/{0}/'.format(year))
        if squad_id == 2:
            return redirect('/santa-clara-high-track-and-field/results/varsity-boys-high-jump/{0}/'.format(year))
        if squad_id == 3:
            return redirect('/santa-clara-high-track-and-field/results/junior-varsity-girls-high-jump/{0}/'.format(year))
        if squad_id == 4:
            return redirect('/santa-clara-high-track-and-field/results/frosh-soph-boys-high-jump/{0}/'.format(year))
    if event_id == 30:
        if squad_id == 1:
            return redirect('/santa-clara-high-track-and-field/results/varsity-girls-long-jump/{0}/'.format(year))
        if squad_id == 2:
            return redirect('/santa-clara-high-track-and-field/results/varsity-boys-long-jump/{0}/'.format(year))
        if squad_id == 3:
            return redirect('/santa-clara-high-track-and-field/results/junior-varsity-girls-long-jump/{0}/'.format(year))
        if squad_id == 4:
            return redirect('/santa-clara-high-track-and-field/results/frosh-soph-boys-long-jump/{0}/'.format(year))
    if event_id == 31:
        if squad_id == 1:
            return redirect('/santa-clara-high-track-and-field/results/varsity-girls-triple-jump/{0}/'.format(year))
        if squad_id == 2:
            return redirect('/santa-clara-high-track-and-field/results/varsity-boys-triple-jump/{0}/'.format(year))
        if squad_id == 3:
            return redirect('/santa-clara-high-track-and-field/results/junior-varsity-girls-triple-jump/{0}/'.format(year))
        if squad_id == 4:
            return redirect('/santa-clara-high-track-and-field/results/frosh-soph-boys-triple-jump/{0}/'.format(year))
    if event_id == 32:
        if squad_id == 1:
            return redirect('/santa-clara-high-track-and-field/results/varsity-girls-pole-vault/{0}/'.format(year))
        if squad_id == 2:
            return redirect('/santa-clara-high-track-and-field/results/varsity-boys-pole-vault/{0}/'.format(year))
        if squad_id == 3:
            return redirect('/santa-clara-high-track-and-field/results/junior-varsity-girls-pole-vault/{0}/'.format(year))
        if squad_id == 4:
            return redirect('/santa-clara-high-track-and-field/results/frosh-soph-boys-pole-vault/{0}/'.format(year))
    if event_id == 33:
        if squad_id == 1:
            return redirect('/santa-clara-high-track-and-field/results/varsity-girls-shot-put-4kg/{0}/'.format(year))
        if squad_id == 3:
            return redirect('/santa-clara-high-track-and-field/results/junior-varsity-girls-shot-put-4kg/{0}/'.format(year))
    if event_id == 34:
        if squad_id == 4:
            return redirect('/santa-clara-high-track-and-field/results/frosh-soph-boys-shot-put-10lb/{0}/'.format(year))
    if event_id == 35:
        if squad_id == 2:
            return redirect('/santa-clara-high-track-and-field/results/varsity-boys-shot-put-12lb/{0}/'.format(year))
    if event_id == 36:
        if squad_id == 1:
            return redirect('/santa-clara-high-track-and-field/results/varsity-girls-discus-1kg/{0}/'.format(year))
        if squad_id == 3:
            return redirect('/santa-clara-high-track-and-field/results/junior-varsity-girls-discus-1kg/{0}/'.format(year))
    if event_id == 37:
        if squad_id == 2:
            return redirect('/santa-clara-high-track-and-field/results/varsity-boys-discus-1.6kg/{0}/'.format(year))
        if squad_id == 4:
            return redirect('/santa-clara-high-track-and-field/results/frosh-soph-boys-discus-1.6kg/{0}/'.format(year))
    if (event_id >= 1 and event_id <= 24) or (event_id >= 38 and event_id <= 40):
        return get_track_race_results(event_id, squad_id, year)
    elif (event_id >= 25 and event_id <= 28) or (event_id == 41):
        return get_track_relay_results(event_id, squad_id, year)
    elif event_id >= 29 and event_id <= 37:
        return get_track_field_results(event_id, squad_id, year)
    return redirect('/santa-clara-high-track-and-field/season/{0}'.format(year))

@track_results_seo_app.route('/varsity-girls-100m-dash/<int:year>/',methods=['GET'])
def race_results_vg_100m_dash(year):
    return get_track_race_results(1, 1, year)

@track_results_seo_app.route('/varsity-boys-100m-dash/<int:year>/',methods=['GET'])
def race_results_vb_100m_dash(year):
    return get_track_race_results(1, 2, year)

@track_results_seo_app.route('/junior-varsity-girls-100m-dash/<int:year>/',methods=['GET'])
def race_results_jvg_100m_dash(year):
    return get_track_race_results(1, 3, year)

@track_results_seo_app.route('/frosh-soph-boys-100m-dash/<int:year>/',methods=['GET'])
def race_results_fsb_100m_dash(year):
    return get_track_race_results(1, 4, year)



@track_results_seo_app.route('/varsity-girls-200m-dash/<int:year>/',methods=['GET'])
def race_results_vg_200m_dash(year):
    return get_track_race_results(2, 1, year)

@track_results_seo_app.route('/varsity-boys-200m-dash/<int:year>/',methods=['GET'])
def race_results_vb_200m_dash(year):
    return get_track_race_results(2, 2, year)

@track_results_seo_app.route('/junior-varsity-girls-200m-dash/<int:year>/',methods=['GET'])
def race_results_jvg_200m_dash(year):
    return get_track_race_results(2, 3, year)

@track_results_seo_app.route('/frosh-soph-boys-200m-dash/<int:year>/',methods=['GET'])
def race_results_fsb_200m_dash(year):
    return get_track_race_results(2, 4, year)



@track_results_seo_app.route('/varsity-girls-400m-dash/<int:year>/',methods=['GET'])
def race_results_vg_400m_dash(year):
    return get_track_race_results(3, 1, year)

@track_results_seo_app.route('/varsity-boys-400m-dash/<int:year>/',methods=['GET'])
def race_results_vb_400m_dash(year):
    return get_track_race_results(3, 2, year)

@track_results_seo_app.route('/junior-varsity-girls-400m-dash/<int:year>/',methods=['GET'])
def race_results_jvg_400m_dash(year):
    return get_track_race_results(3, 3, year)

@track_results_seo_app.route('/frosh-soph-boys-400m-dash/<int:year>/',methods=['GET'])
def race_results_fsb_400m_dash(year):
    return get_track_race_results(3, 4, year)



@track_results_seo_app.route('/varsity-girls-800m-run/<int:year>/',methods=['GET'])
def race_results_vg_800m_run(year):
    return get_track_race_results(7, 1, year)

@track_results_seo_app.route('/varsity-boys-800m-run/<int:year>/',methods=['GET'])
def race_results_vb_800m_run(year):
    return get_track_race_results(7, 2, year)

@track_results_seo_app.route('/junior-varsity-girls-800m-run/<int:year>/',methods=['GET'])
def race_results_jvg_800m_run(year):
    return get_track_race_results(7, 3, year)

@track_results_seo_app.route('/frosh-soph-boys-800m-run/<int:year>/',methods=['GET'])
def race_results_fsb_800m_run(year):
    return get_track_race_results(7, 4, year)



@track_results_seo_app.route('/varsity-girls-1600m-run/<int:year>/',methods=['GET'])
def race_results_vg_1600m_run(year):
    return get_track_race_results(8, 1, year)

@track_results_seo_app.route('/varsity-boys-1600m-run/<int:year>/',methods=['GET'])
def race_results_vb_1600m_run(year):
    return get_track_race_results(8, 2, year)

@track_results_seo_app.route('/junior-varsity-girls-1600m-run/<int:year>/',methods=['GET'])
def race_results_jvg_1600m_run(year):
    return get_track_race_results(8, 3, year)

@track_results_seo_app.route('/frosh-soph-boys-1600m-run/<int:year>/',methods=['GET'])
def race_results_fsb_1600m_run(year):
    return get_track_race_results(8, 4, year)



@track_results_seo_app.route('/varsity-girls-3200m-run/<int:year>/',methods=['GET'])
def race_results_vg_3200m_run(year):
    return get_track_race_results(9, 1, year)

@track_results_seo_app.route('/varsity-boys-3200m-run/<int:year>/',methods=['GET'])
def race_results_vb_3200m_run(year):
    return get_track_race_results(9, 2, year)

@track_results_seo_app.route('/junior-varsity-girls-3200m-run/<int:year>/',methods=['GET'])
def race_results_jvg_3200m_run(year):
    return get_track_race_results(9, 3, year)

@track_results_seo_app.route('/frosh-soph-boys-3200m-run/<int:year>/',methods=['GET'])
def race_results_fsb_3200m_run(year):
    return get_track_race_results(9, 4, year)



@track_results_seo_app.route('/frosh-soph-boys-65m-hurdles-39in/<int:year>/',methods=['GET'])
def race_results_fsb_65m_hurdles_39in(year):
    return get_track_race_results(17, 4, year)

@track_results_seo_app.route('/varsity-girls-100m-hurdles-33in/<int:year>/',methods=['GET'])
def race_results_vg_100m_hurdles_33in(year):
    return get_track_race_results(18, 1, year)

@track_results_seo_app.route('/junior-varsity-girls-100m-hurdles-33in/<int:year>/',methods=['GET'])
def race_results_jvg_100m_hurdles_33in(year):
    return get_track_race_results(18, 3, year)

@track_results_seo_app.route('/varsity-boys-110m-hurdles-39in/<int:year>/',methods=['GET'])
def race_results_vb_110m_hurdles_39in(year):
    return get_track_race_results(19, 2, year)



@track_results_seo_app.route('/varsity-girls-300m-hurdles-30in/<int:year>/',methods=['GET'])
def race_results_vg_300m_hurdles_30in(year):
    return get_track_race_results(20, 1, year)

@track_results_seo_app.route('/junior-varsity-girls-300m-hurdles-30in/<int:year>/',methods=['GET'])
def race_results_jvg_300m_hurdles_30in(year):
    return get_track_race_results(20, 3, year)

@track_results_seo_app.route('/varsity-boys-300m-hurdles-36in/<int:year>/',methods=['GET'])
def race_results_vb_300m_hurdles_36in(year):
    return get_track_race_results(21, 2, year)

@track_results_seo_app.route('/frosh-soph-boys-300m-hurdles-36in/<int:year>/',methods=['GET'])
def race_results_fsb_300m_hurdles_36in(year):
    return get_track_race_results(21, 4, year)



@track_results_seo_app.route('/varsity-girls-400m-relay/<int:year>/',methods=['GET'])
def relay_results_vg_400m_relay(year):
    return get_track_relay_results(25, 1, year)

@track_results_seo_app.route('/varsity-boys-400m-relay/<int:year>/',methods=['GET'])
def relay_results_vb_400m_relay(year):
    return get_track_relay_results(25, 2, year)

@track_results_seo_app.route('/junior-varsity-girls-400m-relay/<int:year>/',methods=['GET'])
def relay_results_jvg_400m_relay(year):
    return get_track_relay_results(25, 3, year)

@track_results_seo_app.route('/frosh-soph-boys-400m-relay/<int:year>/',methods=['GET'])
def relay_results_fsb_400m_relay(year):
    return get_track_relay_results(25, 4, year)



@track_results_seo_app.route('/varsity-girls-1600m-relay/<int:year>/',methods=['GET'])
def relay_results_vg_1600m_relay(year):
    return get_track_relay_results(26, 1, year)

@track_results_seo_app.route('/varsity-boys-1600m-relay/<int:year>/',methods=['GET'])
def relay_results_vb_1600m_relay(year):
    return get_track_relay_results(26, 2, year)

@track_results_seo_app.route('/junior-varsity-girls-1600m-relay/<int:year>/',methods=['GET'])
def relay_results_jvg_1600m_relay(year):
    return get_track_relay_results(26, 3, year)

@track_results_seo_app.route('/frosh-soph-boys-1600m-relay/<int:year>/',methods=['GET'])
def relay_results_fsb_1600m_relay(year):
    return get_track_relay_results(26, 4, year)



@track_results_seo_app.route('/varsity-girls-high-jump/<int:year>/',methods=['GET'])
def field_results_vg_high_jump(year):
    return get_track_field_results(29, 1, year)

@track_results_seo_app.route('/varsity-boys-high-jump/<int:year>/',methods=['GET'])
def field_results_vb_high_jump(year):
    return get_track_field_results(29, 2, year)

@track_results_seo_app.route('/junior-varsity-girls-high-jump/<int:year>/',methods=['GET'])
def field_results_jvg_high_jump(year):
    return get_track_field_results(29, 3, year)

@track_results_seo_app.route('/frosh-soph-boys-high-jump/<int:year>/',methods=['GET'])
def field_results_fsb_high_jump(year):
    return get_track_field_results(29, 4, year)



@track_results_seo_app.route('/varsity-girls-long-jump/<int:year>/',methods=['GET'])
def field_results_vg_long_jump(year):
    return get_track_field_results(30, 1, year)

@track_results_seo_app.route('/varsity-boys-long-jump/<int:year>/',methods=['GET'])
def field_results_vb_long_jump(year):
    return get_track_field_results(30, 2, year)

@track_results_seo_app.route('/junior-varsity-girls-long-jump/<int:year>/',methods=['GET'])
def field_results_jvg_long_jump(year):
    return get_track_field_results(30, 3, year)

@track_results_seo_app.route('/frosh-soph-boys-long-jump/<int:year>/',methods=['GET'])
def field_results_fsb_long_jump(year):
    return get_track_field_results(30, 4, year)



@track_results_seo_app.route('/varsity-girls-triple-jump/<int:year>/',methods=['GET'])
def field_results_vg_triple_jump(year):
    return get_track_field_results(31, 1, year)

@track_results_seo_app.route('/varsity-boys-triple-jump/<int:year>/',methods=['GET'])
def field_results_vb_triple_jump(year):
    return get_track_field_results(31, 2, year)

@track_results_seo_app.route('/junior-varsity-girls-triple-jump/<int:year>/',methods=['GET'])
def field_results_jvg_triple_jump(year):
    return get_track_field_results(31, 3, year)

@track_results_seo_app.route('/frosh-soph-boys-triple-jump/<int:year>/',methods=['GET'])
def field_results_fsb_triple_jump(year):
    return get_track_field_results(31, 4, year)



@track_results_seo_app.route('/varsity-girls-pole-vault/<int:year>/',methods=['GET'])
def field_results_vg_pole_vault(year):
    return get_track_field_results(32, 1, year)

@track_results_seo_app.route('/varsity-boys-pole-vault/<int:year>/',methods=['GET'])
def field_results_vb_pole_vault(year):
    return get_track_field_results(32, 2, year)

@track_results_seo_app.route('/junior-varsity-girls-pole-vault/<int:year>/',methods=['GET'])
def field_results_jvg_pole_vault(year):
    return get_track_field_results(32, 3, year)

@track_results_seo_app.route('/frosh-soph-boys-pole-vault/<int:year>/',methods=['GET'])
def field_results_fsb_pole_vault(year):
    return get_track_field_results(32, 4, year)



@track_results_seo_app.route('/varsity-girls-shot-put-4kg/<int:year>/',methods=['GET'])
def field_results_vg_shot_put_4kg(year):
    return get_track_field_results(33, 1, year)

@track_results_seo_app.route('/junior-varsity-girls-shot-put-4kg/<int:year>/',methods=['GET'])
def field_results_jvg_shot_put4kg(year):
    return get_track_field_results(33, 3, year)

@track_results_seo_app.route('/frosh-soph-boys-shot-put-10lb/<int:year>/',methods=['GET'])
def field_results_fsb_shot_put_10lb(year):
    return get_track_field_results(34, 4, year)

@track_results_seo_app.route('/varsity-boys-shot-put-12lb/<int:year>/',methods=['GET'])
def field_results_vb_shot_put_12lb(year):
    return get_track_field_results(35, 2, year)



@track_results_seo_app.route('/varsity-girls-discus-1kg/<int:year>/',methods=['GET'])
def field_results_vg_discus_1kg(year):
    return get_track_field_results(36, 1, year)

@track_results_seo_app.route('/junior-varsity-girls-discus-1kg/<int:year>/',methods=['GET'])
def field_results_jvg_discus_1kg(year):
    return get_track_field_results(36, 3, year)

@track_results_seo_app.route('/varsity-boys-discus-1.6kg/<int:year>/',methods=['GET'])
def field_results_vb_discus_1_6kg(year):
    return get_track_field_results(37, 2, year)

@track_results_seo_app.route('/frosh-soph-boys-discus-1.6kg/<int:year>/',methods=['GET'])
def field_results_fsb_discus_1_6kg(year):
    return get_track_field_results(37, 4, year)


