__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


track_athletes_seo_app = Blueprint(
    'track_athletes_seo_app', __name__, template_folder='templates', url_prefix='/santa-clara-high-track-and-field/athletes'
)    


@track_athletes_seo_app.route('/', methods=['GET'])
def track_athletes():
    return render_template('track/athletes/athletes.html', gId='2,3')

@track_athletes_seo_app.route('/males', methods=['GET'])
def track_male_athletes():
    return render_template('track/athletes/athletes.html', gId='2')

@track_athletes_seo_app.route('/females', methods=['GET'])
def track_female_athletes():
    return render_template('track/athletes/athletes.html', gId='3')

def get_track_athlete_data(athlete_id):
    return render_template('track/athletes/athlete.html', aId=athlete_id)

@track_athletes_seo_app.route('/<int:athlete_id>', methods=['GET'])
def track_athlete(athlete_id):
    if athlete_id == 1:
        return redirect('/santa-clara-high-track-and-field/athletes/cal-ochoa')
    elif athlete_id == 1000197:
        return redirect('/santa-clara-high-track-and-field/athletes/scott-robinson')
    elif athlete_id == 10114:
        return redirect('/santa-clara-high-track-and-field/athletes/dave-wallick')
    elif athlete_id == 10030:
        return redirect('/santa-clara-high-track-and-field/athletes/steve-marcki')
    elif athlete_id == 10031:
        return redirect('/santa-clara-high-track-and-field/athletes/john-siirila')
    elif athlete_id == 1000261:
        return redirect('/santa-clara-high-track-and-field/athletes/girmay-guangul')
    elif athlete_id == 1000435:
        return redirect('/santa-clara-high-track-and-field/athletes/david-zamora')
    elif athlete_id == 1000144:
        return redirect('/santa-clara-high-track-and-field/athletes/billy-chaung')
    elif athlete_id == 10086:
        return redirect('/santa-clara-high-track-and-field/athletes/margaret-demorest')
    elif athlete_id == 10139:
        return redirect('/santa-clara-high-track-and-field/athletes/shana-buchanan')
    elif athlete_id == 1000281:
        return redirect('/santa-clara-high-track-and-field/athletes/emily-gordon')
    elif athlete_id == 1000457:
        return redirect('/santa-clara-high-track-and-field/athletes/cynthia-smith')
    elif athlete_id == 1000465:
        return redirect('/santa-clara-high-track-and-field/athletes/grace-wills')
    elif athlete_id == 1000464:
        return redirect('/santa-clara-high-track-and-field/athletes/olivia-valente')
    elif athlete_id == 10083:
        return redirect('/santa-clara-high-track-and-field/athletes/julie-sumpter')
    return get_track_athlete_data(athlete_id)

@track_athletes_seo_app.route('/cal-ochoa', methods=['GET'])
def track_athlete_cal_ochoa():
    return get_track_athlete_data(1)

@track_athletes_seo_app.route('/scott-robinson', methods=['GET'])
def track_athlete_scott_robinson():
    return get_track_athlete_data(1000197)

@track_athletes_seo_app.route('/dave-wallick', methods=['GET'])
def track_athlete_dave_wallick():
    return get_track_athlete_data(10114)

@track_athletes_seo_app.route('/steve-marcki', methods=['GET'])
def track_athlete_steve_marcki():
    return get_track_athlete_data(10030)

@track_athletes_seo_app.route('/john-siirila', methods=['GET'])
def track_athlete_john_siirila():
    return get_track_athlete_data(10031)

@track_athletes_seo_app.route('/girmay-guangul', methods=['GET'])
def track_athlete_GirmayGuangul():
    return get_track_athlete_data(1000261)

@track_athletes_seo_app.route('/david-zamora', methods=['GET'])
def track_athlete_david_zamora():
    return get_track_athlete_data(1000435)

@track_athletes_seo_app.route('/billy-chaung', methods=['GET'])
def track_athlete_billy_chaung():
    return get_track_athlete_data(1000144)

@track_athletes_seo_app.route('/margaret-demorest', methods=['GET'])
def track_athlete_margaret_demorest():
    return get_track_athlete_data(10086)

@track_athletes_seo_app.route('/shana-buchanan', methods=['GET'])
def track_athlete_shana_buchanan():
    return get_track_athlete_data(10139)

@track_athletes_seo_app.route('/emily-gordon', methods=['GET'])
def track_athlete_emily_gordon():
    return get_track_athlete_data(1000281)

@track_athletes_seo_app.route('/cynthia-smith', methods=['GET'])
def track_athlete_cynthia_smith():
    return get_track_athlete_data(1000457)

@track_athletes_seo_app.route('/grace-wills', methods=['GET'])
def track_athlete_grace_wills():
    return get_track_athlete_data(1000465)

@track_athletes_seo_app.route('/olivia-valente', methods=['GET'])
def track_athlete_olivia_valente():
    return get_track_athlete_data(1000464)

@track_athletes_seo_app.route('/julie-sumpter', methods=['GET'])
def track_athlete_julie_sumpter():
    return get_track_athlete_data(10083)

