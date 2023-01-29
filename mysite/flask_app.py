from flask import Flask, render_template, request, redirect, url_for
import main

app = Flask(__name__)

# --Global Varibles--




# --Fight Screen--
p2s8hp = 1
@app.route("/p1", methods=['GET', 'POST'])
def p1():
    global p2s8hp
    if request.method == 'POST':
        if request.form['1'] == 'Skill':
            p2s8hp += 1
        elif request.form['1'] == 'Rally':
            pass
        elif request.form['1'] == 'Swap':
            pass
        else:
            pass # unknown
    return render_template("fight.html",

    # Player 2 Slot 8
    p2s8name = main.p1[1].name,
    p2s8link = main.p1[1].link,
    p2s8hp = p2s8hp,
    p2s8MAXhp = 3,
    p2s8sp = 3,
    p2s8MAXsp = 3,
    p2s8def = 0,
    p2s8res = 0,
    p2s8spd = 10,
    p2s8eva = 5,
    p2s8token = '[2 Limit]',
    p2s8boost = '[+2 ATK, +3 DEF, +1 RES, \n+2 SPD, +1 EVA, +5 ACC]',
    p2s8drop = '[-1 MAG]',
    p2s8buff = '[Shield 2]',
    p2s8debuff = '[Terror 2]',

    # Player 2 Slot 7
    p2s7name = 'Chen',
    p2s7hp = 3,
    p2s7MAXhp = 3,
    p2s7sp = 3,
    p2s7MAXsp = 3,
    p2s7def = 0,
    p2s7res = 0,
    p2s7spd = 10,
    p2s7eva = 5,
    p2s7token = '',
    p2s7boost = '[+2 ATK, +3 DEF, +1 RES, \n+2 SPD, +1 EVA, +5 ACC]',
    p2s7drop = '',
    p2s7buff = '',
    p2s7debuff = '[Terror 2]',

    # Player 2 Slot 6
    p2s6name = 'Chen',
    p2s6hp = 3,
    p2s6MAXhp = 3,
    p2s6sp = 3,
    p2s6MAXsp = 3,
    p2s6def = 0,
    p2s6res = 0,
    p2s6spd = 10,
    p2s6eva = 5,
    p2s6token = '',
    p2s6boost = '[+2 ATK, +3 DEF, +1 RES, \n+2 SPD, +1 EVA, +5 ACC]',
    p2s6drop = '',
    p2s6buff = '',
    p2s6debuff = '',

    # Player 2 Slot 5
    p2s5name = 'Chen',
    p2s5hp = 3,
    p2s5MAXhp = 3,
    p2s5sp = 3,
    p2s5MAXsp = 3,
    p2s5def = 0,
    p2s5res = 0,
    p2s5spd = 10,
    p2s5eva = 5,
    p2s5token = '',
    p2s5boost = '',
    p2s5drop = '',
    p2s5buff = '',
    p2s5debuff = '',

    # Player 2 Slot 4
    p2s4name = 'Chen',
    p2s4hp = 3,
    p2s4MAXhp = 3,
    p2s4sp = 3,
    p2s4MAXsp = 3,
    p2s4def = 0,
    p2s4res = 0,
    p2s4spd = 10,
    p2s4eva = 5,
    p2s4token = '',
    p2s4boost = '',
    p2s4drop = '',
    p2s4buff = '',
    p2s4debuff = '',

    # Player 2 Slot 3
    p2s3name = 'Chen',
    p2s3hp = 3,
    p2s3MAXhp = 3,
    p2s3sp = 3,
    p2s3MAXsp = 3,
    p2s3def = 0,
    p2s3res = 0,
    p2s3spd = 10,
    p2s3eva = 5,
    p2s3token = '',
    p2s3boost = '',
    p2s3drop = '',
    p2s3buff = '',
    p2s3debuff = '',

    # Player 2 Slot 2
    p2s2name = 'Chen',
    p2s2hp = 3,
    p2s2MAXhp = 3,
    p2s2sp = 3,
    p2s2MAXsp = 3,
    p2s2def = 0,
    p2s2res = 0,
    p2s2spd = 10,
    p2s2eva = 5,
    p2s2token = '',
    p2s2boost = '',
    p2s2drop = '',
    p2s2buff = '',
    p2s2debuff = '',

    # Player 2 Slot 1
    p2s1name = 'Chen',
    p2s1hp = 3,
    p2s1MAXhp = 3,
    p2s1sp = 3,
    p2s1MAXsp = 3,
    p2s1def = 0,
    p2s1res = 0,
    p2s1spd = 10,
    p2s1eva = 5,
    p2s1token = '',
    p2s1boost = '',
    p2s1drop = '',
    p2s1buff = '',
    p2s1debuff = '',

    # Player 1 Slot 1
    p1s1name = main.p1[1].name,
    p1s1hp = main.p1[1].hp,
    p1s1MAXhp = main.p1[1].maxHp,
    p1s1sp = main.p1[1].sp,
    p1s1MAXsp = main.p1[1].maxSp,
    p1s1def = main.p1[1].dfn,
    p1s1res = 0,
    p1s1spd = 10,
    p1s1eva = 5,
    p1s1token = '',
    p1s1boost = '',
    p1s1drop = '',
    p1s1buff = '',
    p1s1debuff = '',

    # Player 1 Slot 2
    p1s2name = 'Chen',
    p1s2hp = 3,
    p1s2MAXhp = 3,
    p1s2sp = 3,
    p1s2MAXsp = 3,
    p1s2def = 0,
    p1s2res = 0,
    p1s2spd = 10,
    p1s2eva = 5,
    p1s2token = '',
    p1s2boost = '',
    p1s2drop = '',
    p1s2buff = '',
    p1s2debuff = '',

    # Player 1 Slot 3
    p1s3name = 'Chen',
    p1s3hp = 3,
    p1s3MAXhp = 3,
    p1s3sp = 3,
    p1s3MAXsp = 3,
    p1s3def = 0,
    p1s3res = 0,
    p1s3spd = 10,
    p1s3eva = 5,
    p1s3token = '',
    p1s3boost = '',
    p1s3drop = '',
    p1s3buff = '',
    p1s3debuff = '',

    # Player 1 Slot 4
    p1s4name = 'Chen',
    p1s4hp = 3,
    p1s4MAXhp = 3,
    p1s4sp = 3,
    p1s4MAXsp = 3,
    p1s4def = 0,
    p1s4res = 0,
    p1s4spd = 10,
    p1s4eva = 5,
    p1s4token = '',
    p1s4boost = '',
    p1s4drop = '',
    p1s4buff = '',
    p1s4debuff = '',

    # Player 1 Slot 5
    p1s5name = 'Chen',
    p1s5hp = 3,
    p1s5MAXhp = 3,
    p1s5sp = 3,
    p1s5MAXsp = 3,
    p1s5def = 0,
    p1s5res = 0,
    p1s5spd = 10,
    p1s5eva = 5,
    p1s5token = '',
    p1s5boost = '',
    p1s5drop = '',
    p1s5buff = '',
    p1s5debuff = '',

    # Player 1 Slot 6
    p1s6name = 'Chen',
    p1s6hp = 3,
    p1s6MAXhp = 3,
    p1s6sp = 3,
    p1s6MAXsp = 3,
    p1s6def = 0,
    p1s6res = 0,
    p1s6spd = 10,
    p1s6eva = 5,
    p1s6token = '',
    p1s6boost = '',
    p1s6drop = '',
    p1s6buff = '',
    p1s6debuff = '',

    # Player 1 Slot 7
    p1s7name = 'Chen',
    p1s7hp = 3,
    p1s7MAXhp = 3,
    p1s7sp = 3,
    p1s7MAXsp = 3,
    p1s7def = 0,
    p1s7res = 0,
    p1s7spd = 10,
    p1s7eva = 5,
    p1s7token = '',
    p1s7boost = '',
    p1s7drop = '',
    p1s7buff = '',
    p1s7debuff = '',

    # Player 1 Slot 8
    p1s8name = 'Chen',
    p1s8hp = 3,
    p1s8MAXhp = 3,
    p1s8sp = 3,
    p1s8MAXsp = 3,
    p1s8def = 0,
    p1s8res = 0,
    p1s8spd = 10,
    p1s8eva = 5,
    p1s8token = '',
    p1s8boost = '',
    p1s8drop = '',
    p1s8buff = '',
    p1s8debuff = '',

    log = main.p2[1].sk1
    )# make a varible called log. Make it a list and add a line for every log event. then have the list revese order and add \n to the end of each line.

@app.route("/p2", methods=['GET', 'POST'])
def p2():
    return render_template("fight.html")


# --Character Wiki--

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['1'] == 'Chen':
            return redirect(url_for('chen'))
        elif request.form['1'] == 'Cirno':
            return redirect(url_for('cirno'))
        elif request.form['1'] == 'Emilie':
            return redirect(url_for('emilie'))
        elif request.form['1'] == 'Gaius':
            return redirect(url_for('gaius'))
        elif request.form['1'] == 'Keine':
            return redirect(url_for('keine'))
        elif request.form['1'] == 'Kogasa':
            return redirect(url_for('kogasa'))
        elif request.form['1'] == 'Komachi':
            return redirect(url_for('komachi'))
        elif request.form['1'] == 'Marisa':
            return redirect(url_for('marisa'))
        elif request.form['1'] == 'Minoriko':
            return redirect(url_for('minoriko'))
        elif request.form['1'] == 'Momiji':
            return redirect(url_for('momiji'))
        elif request.form['1'] == 'Nitori':
            return redirect(url_for('nitori'))
        elif request.form['1'] == 'Olberic':
            return redirect(url_for('olberic'))
        elif request.form['1'] == 'Ophilia':
            return redirect(url_for('ophilia'))
        elif request.form['1'] == 'Parsee':
            return redirect(url_for('parsee'))
        elif request.form['1'] == 'Reimu':
            return redirect(url_for('reimu'))
        elif request.form['1'] == 'Rinnosuke':
            return redirect(url_for('rinnosuke'))
        elif request.form['1'] == 'Rumia':
            return redirect(url_for('rumia'))
        elif request.form['1'] == 'Stahl':
            return redirect(url_for('stahl'))
        elif request.form['1'] == 'Sully':
            return redirect(url_for('sully'))
        elif request.form['1'] == 'Therion':
            return redirect(url_for('therion'))
        elif request.form['1'] == 'Vaike':
            return redirect(url_for('vaike'))
        elif request.form['1'] == 'Will':
            return redirect(url_for('will'))
        elif request.form['1'] == 'Wobuffet':
            return redirect(url_for('wobuffet'))
        elif request.form['1'] == 'Youmu':
            return redirect(url_for('youmu'))
        elif request.form['1'] == 'Start p1':
            return redirect(url_for('p1'))
        elif request.form['1'] == 'Start p2':
            return redirect(url_for('p2'))
        else:
            pass # unknown
    return render_template("index.html")



# --Character Stats and Skills--

@app.route("/chen")
def chen():
    return render_template("chen.html")
@app.route("/cirno")
def cirno():
    return render_template("cirno.html")
@app.route("/emilie")
def emilie():
    return render_template("emilie.html")
@app.route("/gaius")
def gaius():
    return render_template("gaius.html")
@app.route("/keine")
def keine():
    return render_template("keine.html")
@app.route("/kogasa")
def kogasa():
    return render_template("kogasa.html")
@app.route("/komachi")
def komachi():
    return render_template("komachi.html")
@app.route("/marisa")
def marisa():
    return render_template("marisa.html")
@app.route("/minoriko")
def minoriko():
    return render_template("minoriko.html")
@app.route("/momiji")
def momiji():
    return render_template("momiji.html")
@app.route("/nitori")
def nitori():
    return render_template("nitori.html")
@app.route("/olberic")
def olberic():
    return render_template("olberic.html")
@app.route("/ophilia")
def ophilia():
    return render_template("ophilia.html")
@app.route("/parsee")
def parsee():
    return render_template("parsee.html")
@app.route("/reimu")
def reimu():
    return render_template("reimu.html")
@app.route("/rinnosuke")
def rinnosuke():
    return render_template("rinnosuke.html")
@app.route("/rumia")
def rumia():
    return render_template("rumia.html")
@app.route("/stahl")
def stahl():
    return render_template("stahl.html")
@app.route("/sully")
def sully():
    return render_template("sully.html")
@app.route("/therion")
def therion():
    return render_template("therion.html")
@app.route("/vaike")
def vaike():
    return render_template("vaike.html")
@app.route("/will")
def will():
    return render_template("will.html")
@app.route("/wobuffet")
def wobuffet():
    return render_template("wobuffet.html")
@app.route("/youmu")
def youmu():
    return render_template("youmu.html")



# --Test Pages--


@app.route("/ello")
def hello_world():
    return "Hello"

cHp = 1
@app.route("/hp", methods=['GET', 'POST'])
def hp():
    global cHp
    if request.method == 'POST':
        if request.form['1'] == '+1':
            cHp += 1
        else:
            pass # unknown
    return render_template("hp.html",cHp = cHp)


@app.route("/hp2", methods=['GET', 'POST'])
def hp2():
    global cHp
    if request.method == 'POST':
        if request.form['1'] == '+1':
            cHp += 10
        else:
            pass # unknown
    return render_template("hp.html",cHp = cHp)