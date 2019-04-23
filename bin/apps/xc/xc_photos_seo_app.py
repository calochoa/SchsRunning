__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


xc_photos_seo_app = Blueprint(
    'xc_photos_seo_app', __name__, template_folder='templates', url_prefix='/santa-clara-high-cross-country/photos'
)    


@xc_photos_seo_app.route('/',methods=['GET'])
def xc_photos_home():
    return render_template('xc/photos/photos.html')

@xc_photos_seo_app.route('/team-timeline/',methods=['GET'])
def getXcTeamTimelinePhotos():
    return render_template('xc/photos/photosTeamTimeline.html')

@xc_photos_seo_app.route('/crystal-springs-alumni-race/',methods=['GET'])
def getXcCrystalSpringsAlumniRace():
    return render_template('xc/photos/photosCsAlumniRace.html')

