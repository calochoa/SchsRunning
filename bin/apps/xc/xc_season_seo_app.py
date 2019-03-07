__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template


xc_season_seo_app = Blueprint(
    'xc_season_seo_app', __name__, template_folder='templates', url_prefix='/santa-clara-high-cross-country/season'
)    


@xc_season_seo_app.route('/<year>',methods=['GET'])
def xcSeasonDNE(year=None):
    return render_template('error.html', error='No data for {0} season'.format(year))

@xc_season_seo_app.route('/2018',methods=['GET'])
def xcSeason2018():
    return render_template('xc/season/season.html', yr=2018)

@xc_season_seo_app.route('/2017',methods=['GET'])
def xcSeason2017():
    return render_template('xc/season/season.html', yr=2017)

@xc_season_seo_app.route('/2016',methods=['GET'])
def xcSeason2016():
    return render_template('xc/season/season.html', yr=2016)

@xc_season_seo_app.route('/2015',methods=['GET'])
def xcSeason2015():
    return render_template('xc/season/season.html', yr=2015)

@xc_season_seo_app.route('/2014',methods=['GET'])
def xcSeason2014():
    return render_template('xc/season/season.html', yr=2014)

@xc_season_seo_app.route('/2013',methods=['GET'])
def xcSeason2013():
    return render_template('xc/season/season.html', yr=2013)

@xc_season_seo_app.route('/2012',methods=['GET'])
def xcSeason2012():
    return render_template('xc/season/season.html', yr=2012)

@xc_season_seo_app.route('/2011',methods=['GET'])
def xcSeason2011():
    return render_template('xc/season/season.html', yr=2011)

@xc_season_seo_app.route('/2010',methods=['GET'])
def xcSeason2010():
    return render_template('xc/season/season.html', yr=2010)

@xc_season_seo_app.route('/2009',methods=['GET'])
def xcSeason2009():
    return render_template('xc/season/season.html', yr=2009)

@xc_season_seo_app.route('/2008',methods=['GET'])
def xcSeason2008():
    return render_template('xc/season/season.html', yr=2008)

@xc_season_seo_app.route('/2007',methods=['GET'])
def xcSeason2007():
    return render_template('xc/season/season.html', yr=2007)

@xc_season_seo_app.route('/2006',methods=['GET'])
def xcSeason2006():
    return render_template('xc/season/season.html', yr=2006)

@xc_season_seo_app.route('/2005',methods=['GET'])
def xcSeason2005():
    return render_template('xc/season/season.html', yr=2005)

@xc_season_seo_app.route('/2004',methods=['GET'])
def xcSeason2004():
    return render_template('xc/season/season.html', yr=2004)

@xc_season_seo_app.route('/2003',methods=['GET'])
def xcSeason2003():
    return render_template('xc/season/season.html', yr=2003)

@xc_season_seo_app.route('/2002',methods=['GET'])
def xcSeason2002():
    return render_template('xc/season/season.html', yr=2002)

@xc_season_seo_app.route('/2001',methods=['GET'])
def xcSeason2001():
    return render_template('xc/season/season.html', yr=2001)

@xc_season_seo_app.route('/2000',methods=['GET'])
def xcSeason2000():
    return render_template('xc/season/season.html', yr=2000)

@xc_season_seo_app.route('/1999',methods=['GET'])
def xcSeason1999():
    return render_template('xc/season/season.html', yr=1999)

@xc_season_seo_app.route('/1998',methods=['GET'])
def xcSeason1998():
    return render_template('xc/season/season.html', yr=1998)

@xc_season_seo_app.route('/1997',methods=['GET'])
def xcSeason1997():
    return render_template('xc/season/season.html', yr=1997)

@xc_season_seo_app.route('/1996',methods=['GET'])
def xcSeason1996():
    return render_template('xc/season/season.html', yr=1996)

@xc_season_seo_app.route('/1995',methods=['GET'])
def xcSeason1995():
    return render_template('xc/season/season.html', yr=1995)

@xc_season_seo_app.route('/1994',methods=['GET'])
def xcSeason1994():
    return render_template('xc/season/season.html', yr=1994)

@xc_season_seo_app.route('/1993',methods=['GET'])
def xcSeason1993():
    return render_template('xc/season/season.html', yr=1993)

@xc_season_seo_app.route('/1992',methods=['GET'])
def xcSeason1992():
    return render_template('xc/season/season.html', yr=1992)

@xc_season_seo_app.route('/1991',methods=['GET'])
def xcSeason1991():
    return render_template('xc/season/season.html', yr=1991)

@xc_season_seo_app.route('/1988',methods=['GET'])
def xcSeason1988():
    return render_template('xc/season/season.html', yr=1988)

    