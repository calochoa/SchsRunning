__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


xc_awards_seo_app = Blueprint(
    'xc_awards_seo_app', __name__, template_folder='templates', url_prefix='/santa-clara-high-cross-country/awards'
)    


@xc_awards_seo_app.route('/awards-dropdown-menus',methods=['GET'])
def xc_awards_dropdown_menus():
    return render_template('xc/awards/awards-dropdown-menus.html')


@xc_awards_seo_app.route('/',methods=['GET'])
def xc_awards_home():
    return render_template('xc/awards/awards.html')

def getXcAwardsTimelineData(squad_id):
    return render_template('xc/awards/awardsTimeline.html', squadId=squad_id)

@xc_awards_seo_app.route('/timeline/<int:squad_id>',methods=['GET'])
def xcAwardsTimeline(squad_id):
    if squad_id == 0:
        return redirect('/santa-clara-high-cross-country/awards/timeline/')
    elif squad_id == 1:
        return redirect('/santa-clara-high-cross-country/awards/timeline/varsity-girls')
    elif squad_id == 2:
        return redirect('/santa-clara-high-cross-country/awards/timeline/varsity-boys')
    elif squad_id == 3:
        return redirect('/santa-clara-high-cross-country/awards/timeline/junior-varsity-girls')
    elif squad_id == 4:
        return redirect('/santa-clara-high-cross-country/awards/timeline/frosh-soph-boys')
    return getXcAwardsTimelineData(squad_id)

@xc_awards_seo_app.route('/timeline/',methods=['GET'])
def xcAllAwardsTimeline():
    return getXcAwardsTimelineData(0)

@xc_awards_seo_app.route('/timeline/varsity-girls',methods=['GET'])
def xcVGAwardsTimeline():
    return getXcAwardsTimelineData(1)

@xc_awards_seo_app.route('/timeline/varsity-boys',methods=['GET'])
def xcVBAwardsTimeline():
    return getXcAwardsTimelineData(2)

@xc_awards_seo_app.route('/timeline/junior-varsity-girls',methods=['GET'])
def xcJVGAwardsTimeline():
    return getXcAwardsTimelineData(3)

@xc_awards_seo_app.route('/timeline/frosh-soph-boys',methods=['GET'])
def xcFSBAwardsTimeline():
    return getXcAwardsTimelineData(4)

def getXcAwardsData(award_id, squad_id):
    return render_template('xc/awards/award.html', awardId=award_id, squadId=squad_id)

@xc_awards_seo_app.route('/<int:award_id>/<int:squad_id>',methods=['GET'])
def xcAwards(award_id, squad_id):
    mvp_award_id_list = [0, 1, 2]
    if award_id in mvp_award_id_list and squad_id == 0:
        return redirect('/santa-clara-high-cross-country/awards/most-valuable-runner/')
    elif award_id in mvp_award_id_list and squad_id == 1:
        return redirect('/santa-clara-high-cross-country/awards/varsity-girls-most-valuable-runner')
    elif award_id in mvp_award_id_list and squad_id == 2:
        return redirect('/santa-clara-high-cross-country/awards/varsity-boys-most-valuable-runner')
    elif award_id in mvp_award_id_list and squad_id == 3:
        return redirect('/santa-clara-high-cross-country/awards/junior-varsity-girls-most-valuable-runner')
    elif award_id in mvp_award_id_list and squad_id == 4:
        return redirect('/santa-clara-high-cross-country/awards/frosh-soph-boys-most-valuable-runner')
    elif award_id == 3 and squad_id == 0:
        return redirect('/santa-clara-high-cross-country/awards/most-improved/')
    elif award_id == 3 and squad_id == 1:
        return redirect('/santa-clara-high-cross-country/awards/varsity-girls-most-improved')
    elif award_id == 3 and squad_id == 2:
        return redirect('/santa-clara-high-cross-country/awards/varsity-boys-most-improved')
    elif award_id == 3 and squad_id == 3:
        return redirect('/santa-clara-high-cross-country/awards/junior-varsity-girls-most-improved')
    elif award_id == 3 and squad_id == 4:
        return redirect('/santa-clara-high-cross-country/awards/frosh-soph-boys-most-improved')
    return getXcAwardsData(award_id, squad_id)

@xc_awards_seo_app.route('/most-valuable-runner/',methods=['GET'])
def xcMvpAwards():
    return getXcAwardsData(0, 0)

@xc_awards_seo_app.route('/varsity-girls-most-valuable-runner/',methods=['GET'])
def xcVGMvpAwards():
    return getXcAwardsData(0, 1)

@xc_awards_seo_app.route('/varsity-boys-most-valuable-runner/',methods=['GET'])
def xcVBMvpAwards():
    return getXcAwardsData(0, 2)

@xc_awards_seo_app.route('/junior-varsity-girls-most-valuable-runner/',methods=['GET'])
def xcJVGMvpAwards():
    return getXcAwardsData(0, 3)

@xc_awards_seo_app.route('/frosh-soph-boys-most-valuable-runner/',methods=['GET'])
def xcFSBMvpAwards():
    return getXcAwardsData(0, 4)

@xc_awards_seo_app.route('/most-improved/',methods=['GET'])
def xcMIAwards():
    return getXcAwardsData(3, 0)

@xc_awards_seo_app.route('/varsity-girls-most-improved/',methods=['GET'])
def xcVGMIAwards():
    return getXcAwardsData(3, 1)

@xc_awards_seo_app.route('/varsity-boys-most-improved/',methods=['GET'])
def xcVBMIAwards():
    return getXcAwardsData(3, 2)

@xc_awards_seo_app.route('/junior-varsity-girls-most-improved/',methods=['GET'])
def xcJVGMIAwards():
    return getXcAwardsData(3, 3)

@xc_awards_seo_app.route('/frosh-soph-boys-most-improved/',methods=['GET'])
def xcFSBMIAwards():
    return getXcAwardsData(3, 4)

