__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


track_events_seo_app = Blueprint(
    'track_events_seo_app', __name__, template_folder='templates', url_prefix='/santa-clara-high-track-and-field/events'
)    


@track_events_seo_app.route('/',methods=['GET'])
def track_events_home():
    return render_template('track/events/events.html')

@track_events_seo_app.route('/dropdown-menus',methods=['GET'])
def track_events_dropdown_menus():
    return render_template('track/events/events-dropdown-menus.html')


def get_track_race_results(event_id, gender_id, grade):
    return render_template('track/events/race-results.html', eId=event_id, gId=gender_id, gr=grade)

def get_track_field_results(event_id, gender_id, grade):
    return render_template('track/events/field-results.html', eId=event_id, gId=gender_id, gr=grade)

def get_track_relay_results(event_id, gender_id, squad_id):
    return render_template('track/events/relay-results.html', eId=event_id, gId=gender_id, sId=squad_id)


@track_events_seo_app.route('/<int:event_id>/<int:gender_id>/<int:grade>/',methods=['GET'])
def track_results(event_id, gender_id, grade):
    if event_id == 1:
        if gender_id == 2:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/100m-dash/all-boys/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/100m-dash/senior-boys/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/100m-dash/junior-boys/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/100m-dash/sophomore-boys/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/100m-dash/freshman-boys/')
        if gender_id == 3:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/100m-dash/all-girls/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/100m-dash/senior-girls/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/100m-dash/junior-girls/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/100m-dash/sophomore-girls/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/100m-dash/freshman-girls/')
    if event_id == 2:
        if gender_id == 2:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/200m-dash/all-boys/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/200m-dash/senior-boys/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/200m-dash/junior-boys/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/200m-dash/sophomore-boys/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/200m-dash/freshman-boys/')
        if gender_id == 3:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/200m-dash/all-girls/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/200m-dash/senior-girls/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/200m-dash/junior-girls/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/200m-dash/sophomore-girls/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/200m-dash/freshman-girls/')
    if event_id == 3:
        if gender_id == 2:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/400m-dash/all-boys/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/400m-dash/senior-boys/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/400m-dash/junior-boys/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/400m-dash/sophomore-boys/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/400m-dash/freshman-boys/')
        if gender_id == 3:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/400m-dash/all-girls/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/400m-dash/senior-girls/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/400m-dash/junior-girls/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/400m-dash/sophomore-girls/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/400m-dash/freshman-girls/')
    if event_id == 7:
        if gender_id == 2:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/800m-run/all-boys/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/800m-run/senior-boys/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/800m-run/junior-boys/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/800m-run/sophomore-boys/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/800m-run/freshman-boys/')
        if gender_id == 3:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/800m-run/all-girls/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/800m-run/senior-girls/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/800m-run/junior-girls/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/800m-run/sophomore-girls/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/800m-run/freshman-girls/')
    if event_id == 8:
        if gender_id == 2:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/1600m-run/all-boys/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/1600m-run/senior-boys/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/1600m-run/junior-boys/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/1600m-run/sophomore-boys/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/1600m-run/freshman-boys/')
        if gender_id == 3:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/1600m-run/all-girls/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/1600m-run/senior-girls/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/1600m-run/junior-girls/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/1600m-run/sophomore-girls/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/1600m-run/freshman-girls/')
    if event_id == 9:
        if gender_id == 2:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/3200m-run/all-boys/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/3200m-run/senior-boys/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/3200m-run/junior-boys/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/3200m-run/sophomore-boys/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/3200m-run/freshman-boys/')
        if gender_id == 3:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/3200m-run/all-girls/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/3200m-run/senior-girls/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/3200m-run/junior-girls/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/3200m-run/sophomore-girls/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/3200m-run/freshman-girls/')
    if event_id == 17:
        if gender_id == 2:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/65m-hurdles-39in/all-boys/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/65m-hurdles-39in/sophomore-boys/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/65m-hurdles-39in/freshman-boys/')
    if event_id == 18:
        if gender_id == 3:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/100m-hurdles-33in/all-girls/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/100m-hurdles-33in/senior-girls/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/100m-hurdles-33in/junior-girls/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/100m-hurdles-33in/sophomore-girls/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/100m-hurdles-33in/freshman-girls/')
    if event_id == 19:
        if gender_id == 2:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/110m-hurdles-39in/all-boys/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/110m-hurdles-39in/senior-boys/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/110m-hurdles-39in/junior-boys/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/110m-hurdles-39in/sophomore-boys/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/110m-hurdles-39in/freshman-boys/')
    if event_id == 20:
        if gender_id == 3:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/300m-hurdles-30in/all-girls/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/300m-hurdles-30in/senior-girls/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/300m-hurdles-30in/junior-girls/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/300m-hurdles-30in/sophomore-girls/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/300m-hurdles-30in/freshman-girls/')
    if event_id == 21:
        if gender_id == 2:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/300m-hurdles-36in/all-boys/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/300m-hurdles-36in/senior-boys/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/300m-hurdles-36in/junior-boys/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/300m-hurdles-36in/sophomore-boys/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/300m-hurdles-36in/freshman-boys/')
    if event_id == 25:
        if gender_id == 2:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/400m-relay/all-boys/')
            if grade == 2:  # actually in reference to squad id - varsity boys
                return redirect('/santa-clara-high-track-and-field/events/400m-relay/varsity-boys/')
            if grade == 4:  # actually in reference to squad id - frosh-soph boys
                return redirect('/santa-clara-high-track-and-field/events/400m-relay/frosh-soph-boys/')
        if gender_id == 3:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/400m-relay/all-girls/')
            if grade == 1:  # actually in reference to squad id - varsity girls
                return redirect('/santa-clara-high-track-and-field/events/400m-relay/varsity-girls/')
            if grade == 3:  # actually in reference to squad id - junior varsity girls
                return redirect('/santa-clara-high-track-and-field/events/400m-relay/junior-varsity-girls/')
    if event_id == 26:
        if gender_id == 2:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/1600m-relay/all-boys/')
            if grade == 2:  # actually in reference to squad id - varsity boys
                return redirect('/santa-clara-high-track-and-field/events/1600m-relay/varsity-boys/')
            if grade == 4:  # actually in reference to squad id - frosh-soph boys
                return redirect('/santa-clara-high-track-and-field/events/1600m-relay/frosh-soph-boys/')
        if gender_id == 3:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/1600m-relay/all-girls/')
            if grade == 1:  # actually in reference to squad id - varsity girls
                return redirect('/santa-clara-high-track-and-field/events/1600m-relay/varsity-girls/')
            if grade == 3:  # actually in reference to squad id - junior varsity girls
                return redirect('/santa-clara-high-track-and-field/events/1600m-relay/junior-varsity-girls/')
    if event_id == 29:
        if gender_id == 2:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/high-jump/all-boys/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/high-jump/senior-boys/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/high-jump/junior-boys/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/high-jump/sophomore-boys/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/high-jump/freshman-boys/')
        if gender_id == 3:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/high-jump/all-girls/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/high-jump/senior-girls/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/high-jump/junior-girls/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/high-jump/sophomore-girls/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/high-jump/freshman-girls/')
    if event_id == 30:
        if gender_id == 2:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/long-jump/all-boys/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/long-jump/senior-boys/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/long-jump/junior-boys/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/long-jump/sophomore-boys/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/long-jump/freshman-boys/')
        if gender_id == 3:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/long-jump/all-girls/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/long-jump/senior-girls/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/long-jump/junior-girls/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/long-jump/sophomore-girls/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/long-jump/freshman-girls/')
    if event_id == 31:
        if gender_id == 2:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/triple-jump/all-boys/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/triple-jump/senior-boys/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/triple-jump/junior-boys/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/triple-jump/sophomore-boys/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/triple-jump/freshman-boys/')
        if gender_id == 3:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/triple-jump/all-girls/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/triple-jump/senior-girls/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/triple-jump/junior-girls/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/triple-jump/sophomore-girls/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/triple-jump/freshman-girls/')
    if event_id == 32:
        if gender_id == 2:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/pole-vault/all-boys/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/pole-vault/senior-boys/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/pole-vault/junior-boys/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/pole-vault/sophomore-boys/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/pole-vault/freshman-boys/')
        if gender_id == 3:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/pole-vault/all-girls/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/pole-vault/senior-girls/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/pole-vault/junior-girls/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/pole-vault/sophomore-girls/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/pole-vault/freshman-girls/')
    if event_id == 33:
        if gender_id == 3:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/shot-put-4kg/all-girls/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/shot-put-4kg/senior-girls/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/shot-put-4kg/junior-girls/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/shot-put-4kg/sophomore-girls/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/shot-put-4kg/freshman-girls/')
    if event_id == 34:
        if gender_id == 2:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/shot-put-10lb/all-boys/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/shot-put-10lb/sophomore-boys/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/shot-put-10lb/freshman-boys/')
    if event_id == 35:
        if gender_id == 2:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/shot-put-12lb/all-boys/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/shot-put-12lb/senior-boys/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/shot-put-12lb/junior-boys/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/shot-put-12lb/sophomore-boys/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/shot-put-12lb/freshman-boys/')
    if event_id == 36:
        if gender_id == 3:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/discus-1kg/all-girls/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/discus-1kg/senior-girls/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/discus-1kg/junior-girls/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/discus-1kg/sophomore-girls/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/discus-1kg/freshman-girls/')
    if event_id == 37:
        if gender_id == 2:
            if grade == 0:
                return redirect('/santa-clara-high-track-and-field/events/discus-1.6kg/all-boys/')
            if grade == 12:
                return redirect('/santa-clara-high-track-and-field/events/discus-1.6kg/senior-boys/')
            if grade == 11:
                return redirect('/santa-clara-high-track-and-field/events/discus-1.6kg/junior-boys/')
            if grade == 10:
                return redirect('/santa-clara-high-track-and-field/events/discus-1.6kg/sophomore-boys/')
            if grade == 9:
                return redirect('/santa-clara-high-track-and-field/events/discus-1.6kg/freshman-boys/')
    if (event_id >= 1 and event_id <= 24) or (event_id >= 38 and event_id <= 40):
        return get_track_race_results(event_id, gender_id, grade)
    elif (event_id >= 25 and event_id <= 28) or (event_id == 41):
        return get_track_relay_results(event_id, gender_id, grade)
    elif event_id >= 29 and event_id <= 37:
        return get_track_field_results(event_id, gender_id, grade)
    return redirect('/santa-clara-high-track-and-field/events/')



@track_events_seo_app.route('/100m-dash/all-boys/',methods=['GET'])
def _100m_dash_all_boys():
    return get_track_race_results(1, 2, 0)

@track_events_seo_app.route('/100m-dash/senior-boys/',methods=['GET'])
def _100m_dash_senior_boys():
    return get_track_race_results(1, 2, 12)

@track_events_seo_app.route('/100m-dash/junior-boys/',methods=['GET'])
def _100m_dash_junior_boys():
    return get_track_race_results(1, 2, 11)

@track_events_seo_app.route('/100m-dash/sophomore-boys/',methods=['GET'])
def _100m_dash_sophomore_boys():
    return get_track_race_results(1, 2, 10)

@track_events_seo_app.route('/100m-dash/freshman-boys/',methods=['GET'])
def _100m_dash_freshman_boys():
    return get_track_race_results(1, 2, 9)

@track_events_seo_app.route('/100m-dash/all-girls/',methods=['GET'])
def _100m_dash_all_girls():
    return get_track_race_results(1, 3, 0)

@track_events_seo_app.route('/100m-dash/senior-girls/',methods=['GET'])
def _100m_dash_senior_girls():
    return get_track_race_results(1, 3, 12)

@track_events_seo_app.route('/100m-dash/junior-girls/',methods=['GET'])
def _100m_dash_junior_girls():
    return get_track_race_results(1, 3, 11)

@track_events_seo_app.route('/100m-dash/sophomore-girls/',methods=['GET'])
def _100m_dash_sophomore_girls():
    return get_track_race_results(1, 3, 10)

@track_events_seo_app.route('/100m-dash/freshman-girls/',methods=['GET'])
def _100m_dash_freshman_girls():
    return get_track_race_results(1, 3, 9)



@track_events_seo_app.route('/200m-dash/all-boys/',methods=['GET'])
def _200m_dash_all_boys():
    return get_track_race_results(2, 2, 0)

@track_events_seo_app.route('/200m-dash/senior-boys/',methods=['GET'])
def _200m_dash_senior_boys():
    return get_track_race_results(2, 2, 12)

@track_events_seo_app.route('/200m-dash/junior-boys/',methods=['GET'])
def _200m_dash_junior_boys():
    return get_track_race_results(2, 2, 11)

@track_events_seo_app.route('/200m-dash/sophomore-boys/',methods=['GET'])
def _200m_dash_sophomore_boys():
    return get_track_race_results(2, 2, 10)

@track_events_seo_app.route('/200m-dash/freshman-boys/',methods=['GET'])
def _200m_dash_freshman_boys():
    return get_track_race_results(2, 2, 9)

@track_events_seo_app.route('/200m-dash/all-girls/',methods=['GET'])
def _200m_dash_all_girls():
    return get_track_race_results(2, 3, 0)

@track_events_seo_app.route('/200m-dash/senior-girls/',methods=['GET'])
def _200m_dash_senior_girls():
    return get_track_race_results(2, 3, 12)

@track_events_seo_app.route('/200m-dash/junior-girls/',methods=['GET'])
def _200m_dash_junior_girls():
    return get_track_race_results(2, 3, 11)

@track_events_seo_app.route('/200m-dash/sophomore-girls/',methods=['GET'])
def _200m_dash_sophomore_girls():
    return get_track_race_results(2, 3, 10)

@track_events_seo_app.route('/200m-dash/freshman-girls/',methods=['GET'])
def _200m_dash_freshman_girls():
    return get_track_race_results(2, 3, 9)



@track_events_seo_app.route('/400m-dash/all-boys/',methods=['GET'])
def _400m_dash_all_boys():
    return get_track_race_results(3, 2, 0)

@track_events_seo_app.route('/400m-dash/senior-boys/',methods=['GET'])
def _400m_dash_senior_boys():
    return get_track_race_results(3, 2, 12)

@track_events_seo_app.route('/400m-dash/junior-boys/',methods=['GET'])
def _400m_dash_junior_boys():
    return get_track_race_results(3, 2, 11)

@track_events_seo_app.route('/400m-dash/sophomore-boys/',methods=['GET'])
def _400m_dash_sophomore_boys():
    return get_track_race_results(3, 2, 10)

@track_events_seo_app.route('/400m-dash/freshman-boys/',methods=['GET'])
def _400m_dash_freshman_boys():
    return get_track_race_results(3, 2, 9)

@track_events_seo_app.route('/400m-dash/all-girls/',methods=['GET'])
def _400m_dash_all_girls():
    return get_track_race_results(3, 3, 0)

@track_events_seo_app.route('/400m-dash/senior-girls/',methods=['GET'])
def _400m_dash_senior_girls():
    return get_track_race_results(3, 3, 12)

@track_events_seo_app.route('/400m-dash/junior-girls/',methods=['GET'])
def _400m_dash_junior_girls():
    return get_track_race_results(3, 3, 11)

@track_events_seo_app.route('/400m-dash/sophomore-girls/',methods=['GET'])
def _400m_dash_sophomore_girls():
    return get_track_race_results(3, 3, 10)

@track_events_seo_app.route('/400m-dash/freshman-girls/',methods=['GET'])
def _400m_dash_freshman_girls():
    return get_track_race_results(3, 3, 9)



@track_events_seo_app.route('/800m-run/all-boys/',methods=['GET'])
def _800m_run_all_boys():
    return get_track_race_results(7, 2, 0)

@track_events_seo_app.route('/800m-run/senior-boys/',methods=['GET'])
def _800m_run_senior_boys():
    return get_track_race_results(7, 2, 12)

@track_events_seo_app.route('/800m-run/junior-boys/',methods=['GET'])
def _800m_run_junior_boys():
    return get_track_race_results(7, 2, 11)

@track_events_seo_app.route('/800m-run/sophomore-boys/',methods=['GET'])
def _800m_run_sophomore_boys():
    return get_track_race_results(7, 2, 10)

@track_events_seo_app.route('/800m-run/freshman-boys/',methods=['GET'])
def _800m_run_freshman_boys():
    return get_track_race_results(7, 2, 9)

@track_events_seo_app.route('/800m-run/all-girls/',methods=['GET'])
def _800m_run_all_girls():
    return get_track_race_results(7, 3, 0)

@track_events_seo_app.route('/800m-run/senior-girls/',methods=['GET'])
def _800m_run_senior_girls():
    return get_track_race_results(7, 3, 12)

@track_events_seo_app.route('/800m-run/junior-girls/',methods=['GET'])
def _800m_run_junior_girls():
    return get_track_race_results(7, 3, 11)

@track_events_seo_app.route('/800m-run/sophomore-girls/',methods=['GET'])
def _800m_run_sophomore_girls():
    return get_track_race_results(7, 3, 10)

@track_events_seo_app.route('/800m-run/freshman-girls/',methods=['GET'])
def _800m_run_freshman_girls():
    return get_track_race_results(7, 3, 9)



@track_events_seo_app.route('/1600m-run/all-boys/',methods=['GET'])
def _1600m_run_all_boys():
    return get_track_race_results(8, 2, 0)

@track_events_seo_app.route('/1600m-run/senior-boys/',methods=['GET'])
def _1600m_run_senior_boys():
    return get_track_race_results(8, 2, 12)

@track_events_seo_app.route('/1600m-run/junior-boys/',methods=['GET'])
def _1600m_run_junior_boys():
    return get_track_race_results(8, 2, 11)

@track_events_seo_app.route('/1600m-run/sophomore-boys/',methods=['GET'])
def _1600m_run_sophomore_boys():
    return get_track_race_results(8, 2, 10)

@track_events_seo_app.route('/1600m-run/freshman-boys/',methods=['GET'])
def _1600m_run_freshman_boys():
    return get_track_race_results(8, 2, 9)

@track_events_seo_app.route('/1600m-run/all-girls/',methods=['GET'])
def _1600m_run_all_girls():
    return get_track_race_results(8, 3, 0)

@track_events_seo_app.route('/1600m-run/senior-girls/',methods=['GET'])
def _1600m_run_senior_girls():
    return get_track_race_results(8, 3, 12)

@track_events_seo_app.route('/1600m-run/junior-girls/',methods=['GET'])
def _1600m_run_junior_girls():
    return get_track_race_results(8, 3, 11)

@track_events_seo_app.route('/1600m-run/sophomore-girls/',methods=['GET'])
def _1600m_run_sophomore_girls():
    return get_track_race_results(8, 3, 10)

@track_events_seo_app.route('/1600m-run/freshman-girls/',methods=['GET'])
def _1600m_run_freshman_girls():
    return get_track_race_results(8, 3, 9)



@track_events_seo_app.route('/3200m-run/all-boys/',methods=['GET'])
def _3200m_run_all_boys():
    return get_track_race_results(9, 2, 0)

@track_events_seo_app.route('/3200m-run/senior-boys/',methods=['GET'])
def _3200m_run_senior_boys():
    return get_track_race_results(9, 2, 12)

@track_events_seo_app.route('/3200m-run/junior-boys/',methods=['GET'])
def _3200m_run_junior_boys():
    return get_track_race_results(9, 2, 11)

@track_events_seo_app.route('/3200m-run/sophomore-boys/',methods=['GET'])
def _3200m_run_sophomore_boys():
    return get_track_race_results(9, 2, 10)

@track_events_seo_app.route('/3200m-run/freshman-boys/',methods=['GET'])
def _3200m_run_freshman_boys():
    return get_track_race_results(9, 2, 9)

@track_events_seo_app.route('/3200m-run/all-girls/',methods=['GET'])
def _3200m_run_all_girls():
    return get_track_race_results(9, 3, 0)

@track_events_seo_app.route('/3200m-run/senior-girls/',methods=['GET'])
def _3200m_run_senior_girls():
    return get_track_race_results(9, 3, 12)

@track_events_seo_app.route('/3200m-run/junior-girls/',methods=['GET'])
def _3200m_run_junior_girls():
    return get_track_race_results(9, 3, 11)

@track_events_seo_app.route('/3200m-run/sophomore-girls/',methods=['GET'])
def _3200m_run_sophomore_girls():
    return get_track_race_results(9, 3, 10)

@track_events_seo_app.route('/3200m-run/freshman-girls/',methods=['GET'])
def _3200m_run_freshman_girls():
    return get_track_race_results(9, 3, 9)



@track_events_seo_app.route('/65m-hurdles-39in/all-boys/',methods=['GET'])
def _65m_hurdles_39in_all_boys():
    return get_track_race_results(17, 2, 0)

@track_events_seo_app.route('/65m-hurdles-39in/sophomore-boys/',methods=['GET'])
def _65m_hurdles_39in_sophomore_boys():
    return get_track_race_results(17, 2, 10)

@track_events_seo_app.route('/65m-hurdles-39in/freshman-boys/',methods=['GET'])
def _65m_hurdles_39in_freshman_boys():
    return get_track_race_results(17, 2, 9)



@track_events_seo_app.route('/100m-hurdles-33in/all-girls/',methods=['GET'])
def _100m_hurdles_33in_all_girls():
    return get_track_race_results(18, 3, 0)

@track_events_seo_app.route('/100m-hurdles-33in/senior-girls/',methods=['GET'])
def _100m_hurdles_33in_senior_girls():
    return get_track_race_results(18, 3, 12)

@track_events_seo_app.route('/100m-hurdles-33in/junior-girls/',methods=['GET'])
def _100m_hurdles_33in_junior_girls():
    return get_track_race_results(18, 3, 11)

@track_events_seo_app.route('/100m-hurdles-33in/sophomore-girls/',methods=['GET'])
def _100m_hurdles_33in_sophomore_girls():
    return get_track_race_results(18, 3, 10)

@track_events_seo_app.route('/100m-hurdles-33in/freshman-girls/',methods=['GET'])
def _100m_hurdles_33in_freshman_girls():
    return get_track_race_results(18, 3, 9)



@track_events_seo_app.route('/110m-hurdles-39in/all-boys/',methods=['GET'])
def _110m_hurdles_39in_all_boys():
    return get_track_race_results(19, 2, 0)

@track_events_seo_app.route('/110m-hurdles-39in/senior-boys/',methods=['GET'])
def _110m_hurdles_39in_senior_boys():
    return get_track_race_results(19, 2, 12)

@track_events_seo_app.route('/110m-hurdles-39in/junior-boys/',methods=['GET'])
def _110m_hurdles_39in_junior_boys():
    return get_track_race_results(19, 2, 11)

@track_events_seo_app.route('/110m-hurdles-39in/sophomore-boys/',methods=['GET'])
def _110m_hurdles_39in_sophomore_boys():
    return get_track_race_results(19, 2, 10)

@track_events_seo_app.route('/110m-hurdles-39in/freshman-boys/',methods=['GET'])
def _110m_hurdles_39in_freshman_boys():
    return get_track_race_results(19, 2, 9)



@track_events_seo_app.route('/300m-hurdles-30in/all-girls/',methods=['GET'])
def _300m_hurdles_30in_all_girls():
    return get_track_race_results(20, 3, 0)

@track_events_seo_app.route('/300m-hurdles-30in/senior-girls/',methods=['GET'])
def _300m_hurdles_30in_senior_girls():
    return get_track_race_results(20, 3, 12)

@track_events_seo_app.route('/300m-hurdles-30in/junior-girls/',methods=['GET'])
def _300m_hurdles_30in_junior_girls():
    return get_track_race_results(20, 3, 11)

@track_events_seo_app.route('/300m-hurdles-30in/sophomore-girls/',methods=['GET'])
def _300m_hurdles_30in_sophomore_girls():
    return get_track_race_results(20, 3, 10)

@track_events_seo_app.route('/300m-hurdles-30in/freshman-girls/',methods=['GET'])
def _300m_hurdles_30in_freshman_girls():
    return get_track_race_results(20, 3, 9)



@track_events_seo_app.route('/300m-hurdles-36in/all-boys/',methods=['GET'])
def _300m_hurdles_36in_all_boys():
    return get_track_race_results(21, 2, 0)

@track_events_seo_app.route('/300m-hurdles-36in/senior-boys/',methods=['GET'])
def _300m_hurdles_36in_senior_boys():
    return get_track_race_results(21, 2, 12)

@track_events_seo_app.route('/300m-hurdles-36in/junior-boys/',methods=['GET'])
def _300m_hurdles_36in_junior_boys():
    return get_track_race_results(21, 2, 11)

@track_events_seo_app.route('/300m-hurdles-36in/sophomore-boys/',methods=['GET'])
def _300m_hurdles_36in_sophomore_boys():
    return get_track_race_results(21, 2, 10)

@track_events_seo_app.route('/300m-hurdles-36in/freshman-boys/',methods=['GET'])
def _300m_hurdles_36in_freshman_boys():
    return get_track_race_results(21, 2, 9)



@track_events_seo_app.route('/400m-relay/all-boys/',methods=['GET'])
def _400m_relay_all_boys():
    return get_track_relay_results(25, 2, 0)

@track_events_seo_app.route('/400m-relay/varsity-boys/',methods=['GET'])
def _400m_relay_varsity_boys():
    return get_track_relay_results(25, 2, 2)

@track_events_seo_app.route('/400m-relay/frosh-soph-boys/',methods=['GET'])
def _400m_relay_frosh_soph_boys():
    return get_track_relay_results(25, 2, 4)


@track_events_seo_app.route('/400m-relay/all-girls/',methods=['GET'])
def _400m_relay_all_girls():
    return get_track_relay_results(25, 3, 0)

@track_events_seo_app.route('/400m-relay/varsity-girls/',methods=['GET'])
def _400m_relay_varsity_girls():
    return get_track_relay_results(25, 3, 1)

@track_events_seo_app.route('/400m-relay/junior-varsity-girls/',methods=['GET'])
def _400m_relay_junior_varsity_girls():
    return get_track_relay_results(25, 3, 3)



@track_events_seo_app.route('/1600m-relay/all-boys/',methods=['GET'])
def _1600m_relay_all_boys():
    return get_track_relay_results(26, 2, 0)

@track_events_seo_app.route('/1600m-relay/varsity-boys/',methods=['GET'])
def _1600m_relay_varsity_boys():
    return get_track_relay_results(26, 2, 2)

@track_events_seo_app.route('/1600m-relay/frosh-soph-boys/',methods=['GET'])
def _1600m_relay_frosh_soph_boys():
    return get_track_relay_results(26, 2, 4)


@track_events_seo_app.route('/1600m-relay/all-girls/',methods=['GET'])
def _1600m_relay_all_girls():
    return get_track_relay_results(26, 3, 0)

@track_events_seo_app.route('/1600m-relay/varsity-girls/',methods=['GET'])
def _1600m_relay_varsity_girls():
    return get_track_relay_results(26, 3, 1)

@track_events_seo_app.route('/1600m-relay/junior-varsity-girls/',methods=['GET'])
def _1600m_relay_junior_varsity_girls():
    return get_track_relay_results(26, 3, 3)



@track_events_seo_app.route('/high-jump/all-boys/',methods=['GET'])
def _high_jump_all_boys():
    return get_track_field_results(29, 2, 0)

@track_events_seo_app.route('/high-jump/senior-boys/',methods=['GET'])
def _high_jump_senior_boys():
    return get_track_field_results(29, 2, 12)

@track_events_seo_app.route('/high-jump/junior-boys/',methods=['GET'])
def _high_jump_junior_boys():
    return get_track_field_results(29, 2, 11)

@track_events_seo_app.route('/high-jump/sophomore-boys/',methods=['GET'])
def _high_jump_sophomore_boys():
    return get_track_field_results(29, 2, 10)

@track_events_seo_app.route('/high-jump/freshman-boys/',methods=['GET'])
def _high_jump_freshman_boys():
    return get_track_field_results(29, 2, 9)

@track_events_seo_app.route('/high-jump/all-girls/',methods=['GET'])
def _high_jump_all_girls():
    return get_track_field_results(29, 3, 0)

@track_events_seo_app.route('/high-jump/senior-girls/',methods=['GET'])
def _high_jump_senior_girls():
    return get_track_field_results(29, 3, 12)

@track_events_seo_app.route('/high-jump/junior-girls/',methods=['GET'])
def _high_jump_junior_girls():
    return get_track_field_results(29, 3, 11)

@track_events_seo_app.route('/high-jump/sophomore-girls/',methods=['GET'])
def _high_jump_sophomore_girls():
    return get_track_field_results(29, 3, 10)

@track_events_seo_app.route('/high-jump/freshman-girls/',methods=['GET'])
def _high_jump_freshman_girls():
    return get_track_field_results(29, 3, 9)



@track_events_seo_app.route('/long-jump/all-boys/',methods=['GET'])
def _long_jump_all_boys():
    return get_track_field_results(30, 2, 0)

@track_events_seo_app.route('/long-jump/senior-boys/',methods=['GET'])
def _long_jump_senior_boys():
    return get_track_field_results(30, 2, 12)

@track_events_seo_app.route('/long-jump/junior-boys/',methods=['GET'])
def _long_jump_junior_boys():
    return get_track_field_results(30, 2, 11)

@track_events_seo_app.route('/long-jump/sophomore-boys/',methods=['GET'])
def _long_jump_sophomore_boys():
    return get_track_field_results(30, 2, 10)

@track_events_seo_app.route('/long-jump/freshman-boys/',methods=['GET'])
def _long_jump_freshman_boys():
    return get_track_field_results(30, 2, 9)

@track_events_seo_app.route('/long-jump/all-girls/',methods=['GET'])
def _long_jump_all_girls():
    return get_track_field_results(30, 3, 0)

@track_events_seo_app.route('/long-jump/senior-girls/',methods=['GET'])
def _long_jump_senior_girls():
    return get_track_field_results(30, 3, 12)

@track_events_seo_app.route('/long-jump/junior-girls/',methods=['GET'])
def _long_jump_junior_girls():
    return get_track_field_results(30, 3, 11)

@track_events_seo_app.route('/long-jump/sophomore-girls/',methods=['GET'])
def _long_jump_sophomore_girls():
    return get_track_field_results(30, 3, 10)

@track_events_seo_app.route('/long-jump/freshman-girls/',methods=['GET'])
def _long_jump_freshman_girls():
    return get_track_field_results(30, 3, 9)



@track_events_seo_app.route('/triple-jump/all-boys/',methods=['GET'])
def _triple_jump_all_boys():
    return get_track_field_results(31, 2, 0)

@track_events_seo_app.route('/triple-jump/senior-boys/',methods=['GET'])
def _triple_jump_senior_boys():
    return get_track_field_results(31, 2, 12)

@track_events_seo_app.route('/triple-jump/junior-boys/',methods=['GET'])
def _triple_jump_junior_boys():
    return get_track_field_results(31, 2, 11)

@track_events_seo_app.route('/triple-jump/sophomore-boys/',methods=['GET'])
def _triple_jump_sophomore_boys():
    return get_track_field_results(31, 2, 10)

@track_events_seo_app.route('/triple-jump/freshman-boys/',methods=['GET'])
def _triple_jump_freshman_boys():
    return get_track_field_results(31, 2, 9)

@track_events_seo_app.route('/triple-jump/all-girls/',methods=['GET'])
def _triple_jump_all_girls():
    return get_track_field_results(31, 3, 0)

@track_events_seo_app.route('/triple-jump/senior-girls/',methods=['GET'])
def _triple_jump_senior_girls():
    return get_track_field_results(31, 3, 12)

@track_events_seo_app.route('/triple-jump/junior-girls/',methods=['GET'])
def _triple_jump_junior_girls():
    return get_track_field_results(31, 3, 11)

@track_events_seo_app.route('/triple-jump/sophomore-girls/',methods=['GET'])
def _triple_jump_sophomore_girls():
    return get_track_field_results(31, 3, 10)

@track_events_seo_app.route('/triple-jump/freshman-girls/',methods=['GET'])
def _triple_jump_freshman_girls():
    return get_track_field_results(31, 3, 9)



@track_events_seo_app.route('/pole-vault/all-boys/',methods=['GET'])
def _pole_vault_all_boys():
    return get_track_field_results(32, 2, 0)

@track_events_seo_app.route('/pole-vault/senior-boys/',methods=['GET'])
def _pole_vault_senior_boys():
    return get_track_field_results(32, 2, 12)

@track_events_seo_app.route('/pole-vault/junior-boys/',methods=['GET'])
def _pole_vault_junior_boys():
    return get_track_field_results(32, 2, 11)

@track_events_seo_app.route('/pole-vault/sophomore-boys/',methods=['GET'])
def _pole_vault_sophomore_boys():
    return get_track_field_results(32, 2, 10)

@track_events_seo_app.route('/pole-vault/freshman-boys/',methods=['GET'])
def _pole_vault_freshman_boys():
    return get_track_field_results(32, 2, 9)

@track_events_seo_app.route('/pole-vault/all-girls/',methods=['GET'])
def _pole_vault_all_girls():
    return get_track_field_results(32, 3, 0)

@track_events_seo_app.route('/pole-vault/senior-girls/',methods=['GET'])
def _pole_vault_senior_girls():
    return get_track_field_results(32, 3, 12)

@track_events_seo_app.route('/pole-vault/junior-girls/',methods=['GET'])
def _pole_vault_junior_girls():
    return get_track_field_results(32, 3, 11)

@track_events_seo_app.route('/pole-vault/sophomore-girls/',methods=['GET'])
def _pole_vault_sophomore_girls():
    return get_track_field_results(32, 3, 10)

@track_events_seo_app.route('/pole-vault/freshman-girls/',methods=['GET'])
def _pole_vault_freshman_girls():
    return get_track_field_results(32, 3, 9)



@track_events_seo_app.route('/shot-put-4kg/all-girls/',methods=['GET'])
def _shot_put_4kg_all_girls():
    return get_track_field_results(33, 3, 0)

@track_events_seo_app.route('/shot-put-4kg/senior-girls/',methods=['GET'])
def _shot_put_4kg_senior_girls():
    return get_track_field_results(33, 3, 12)

@track_events_seo_app.route('/shot-put-4kg/junior-girls/',methods=['GET'])
def _shot_put_4kg_junior_girls():
    return get_track_field_results(33, 3, 11)

@track_events_seo_app.route('/shot-put-4kg/sophomore-girls/',methods=['GET'])
def _shot_put_4kg_sophomore_girls():
    return get_track_field_results(33, 3, 10)

@track_events_seo_app.route('/shot-put-4kg/freshman-girls/',methods=['GET'])
def _shot_put_4kg_freshman_girls():
    return get_track_field_results(33, 3, 9)



@track_events_seo_app.route('/shot-put-10lb/all-boys/',methods=['GET'])
def _shot_put_10lb_all_boys():
    return get_track_field_results(34, 2, 0)

@track_events_seo_app.route('/shot-put-10lb/sophomore-boys/',methods=['GET'])
def _shot_put_10lb_sophomore_boys():
    return get_track_field_results(34, 2, 10)

@track_events_seo_app.route('/shot-put-10lb/freshman-boys/',methods=['GET'])
def _shot_put_10lb_freshman_boys():
    return get_track_field_results(34, 2, 9)



@track_events_seo_app.route('/shot-put-12lb/all-boys/',methods=['GET'])
def _shot_put_12lb_all_boys():
    return get_track_field_results(35, 2, 0)

@track_events_seo_app.route('/shot-put-12lb/senior-boys/',methods=['GET'])
def _shot_put_12lb_senior_boys():
    return get_track_field_results(35, 2, 12)

@track_events_seo_app.route('/shot-put-12lb/junior-boys/',methods=['GET'])
def _shot_put_12lb_junior_boys():
    return get_track_field_results(35, 2, 11)

@track_events_seo_app.route('/shot-put-12lb/sophomore-boys/',methods=['GET'])
def _shot_put_12lb_sophomore_boys():
    return get_track_field_results(35, 2, 10)

@track_events_seo_app.route('/shot-put-12lb/freshman-boys/',methods=['GET'])
def _shot_put_12lb_freshman_boys():
    return get_track_field_results(35, 2, 9)



@track_events_seo_app.route('/discus-1kg/all-girls/',methods=['GET'])
def _discus_1kg_all_girls():
    return get_track_field_results(36, 3, 0)

@track_events_seo_app.route('/discus-1kg/senior-girls/',methods=['GET'])
def _discus_1kg_senior_girls():
    return get_track_field_results(36, 3, 12)

@track_events_seo_app.route('/discus-1kg/junior-girls/',methods=['GET'])
def _discus_1kg_junior_girls():
    return get_track_field_results(36, 3, 11)

@track_events_seo_app.route('/discus-1kg/sophomore-girls/',methods=['GET'])
def _discus_1kg_sophomore_girls():
    return get_track_field_results(36, 3, 10)

@track_events_seo_app.route('/discus-1kg/freshman-girls/',methods=['GET'])
def _discus_1kg_freshman_girls():
    return get_track_field_results(36, 3, 9)



@track_events_seo_app.route('/discus-1.6kg/all-boys/',methods=['GET'])
def _discus_1_6kg_all_boys():
    return get_track_field_results(37, 2, 0)

@track_events_seo_app.route('/discus-1.6kg/senior-boys/',methods=['GET'])
def _discus_1_6kg_senior_boys():
    return get_track_field_results(37, 2, 12)

@track_events_seo_app.route('/discus-1.6kg/junior-boys/',methods=['GET'])
def _discus_1_6kg_junior_boys():
    return get_track_field_results(37, 2, 11)

@track_events_seo_app.route('/discus-1.6kg/sophomore-boys/',methods=['GET'])
def _discus_1_6kg_sophomore_boys():
    return get_track_field_results(37, 2, 10)

@track_events_seo_app.route('/discus-1.6kg/freshman-boys/',methods=['GET'])
def _discus_1_6kg_freshman_boys():
    return get_track_field_results(37, 2, 9)


