__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


xc_runners_seo_app = Blueprint(
    'xc_runners_seo_app', __name__, template_folder='templates', url_prefix='/santa-clara-high-cross-country/runners'
)    


@xc_runners_seo_app.route('/boys',methods=['GET'])
def xcBoyRunners():
    return render_template('xc/runners/runners.html', gId=2)

@xc_runners_seo_app.route('/girls',methods=['GET'])
def xcGirlRunners():
    return render_template('xc/runners/runners.html', gId=3)

def getXcRunnerData(runner_id):
    return render_template('xc/runners/runner.html', rId=runner_id)

@xc_runners_seo_app.route('/<int:runner_id>',methods=['GET'])
def xcRunner(runner_id):
    if runner_id == 1:
        return redirect('/santa-clara-high-cross-country/runners/cal-ochoa')
    elif runner_id == 1000261:
        return redirect('/santa-clara-high-cross-country/runners/girmay-guangul')
    elif runner_id == 1000259:
        return redirect('/santa-clara-high-cross-country/runners/vince-rodriguez')
    elif runner_id == 1000179:
        return redirect('/santa-clara-high-cross-country/runners/kindu-ejigu')
    elif runner_id == 1000193:
        return redirect('/santa-clara-high-cross-country/runners/lenin-zapata')
    elif runner_id == 1000300:
        return redirect('/santa-clara-high-cross-country/runners/rick-duenas')
    elif runner_id == 1000154:
        return redirect('/santa-clara-high-cross-country/runners/bita-manesh')
    elif runner_id == 1000247:
        return redirect('/santa-clara-high-cross-country/runners/rachel-newman')
    elif runner_id == 1000254:
        return redirect('/santa-clara-high-cross-country/runners/sophia-kennedy')
    elif runner_id == 1000182:
        return redirect('/santa-clara-high-cross-country/runners/regan-dyer')
    elif runner_id == 1000316:
        return redirect('/santa-clara-high-cross-country/runners/ingrid-lacy')
    elif runner_id == 1000166:
        return redirect('/santa-clara-high-cross-country/runners/abby-olsen')
    return getXcRunnerData(runner_id)

@xc_runners_seo_app.route('/cal-ochoa',methods=['GET'])
def xcRunnerCalOchoa():
    return getXcRunnerData(1)

@xc_runners_seo_app.route('/girmay-guangul',methods=['GET'])
def xcRunnerGirmayGuangul():
    return getXcRunnerData(1000261)

@xc_runners_seo_app.route('/vince-rodriguez',methods=['GET'])
def xcRunnerVinceRodriguez():
    return getXcRunnerData(1000259)

@xc_runners_seo_app.route('/kindu-ejigu',methods=['GET'])
def xcRunnerKinduEjigu():
    return getXcRunnerData(1000179)

@xc_runners_seo_app.route('/lenin-zapata',methods=['GET'])
def xcRunnerLeninZapata():
    return getXcRunnerData(1000193)

@xc_runners_seo_app.route('/rick-duenas',methods=['GET'])
def xcRunnerRickDuenas():
    return getXcRunnerData(1000300)

@xc_runners_seo_app.route('/bita-manesh',methods=['GET'])
def xcRunnerBitaManesh():
    return getXcRunnerData(1000154)

@xc_runners_seo_app.route('/rachel-newman',methods=['GET'])
def xcRunnerRachelNewman():
    return getXcRunnerData(1000247)

@xc_runners_seo_app.route('/sophia-kennedy',methods=['GET'])
def xcRunnerSophiaKennedy():
    return getXcRunnerData(1000254)

@xc_runners_seo_app.route('/regan-dyer',methods=['GET'])
def xcRunnerReganDyer():
    return getXcRunnerData(1000182)

@xc_runners_seo_app.route('/ingrid-lacy',methods=['GET'])
def xcRunnerIngridLacy():
    return getXcRunnerData(1000316)

@xc_runners_seo_app.route('/abby-olsen',methods=['GET'])
def xcRunnerAbbyOlsen():
    return getXcRunnerData(1000166)

