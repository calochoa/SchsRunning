__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template


track_app = Blueprint('track_app', __name__, template_folder='templates')


@track_app.route('/santa-clara-high-track-and-field')
@track_app.route('/track')
def main_track():
    return render_template('track/index.html')

