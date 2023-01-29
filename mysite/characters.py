class Char:
    def __init__(self):
        self.name = "I AM ERROR."
        self.link = 'http://tbscrossoverarena.pythonanywhere.com/p1'
        self.hp = 10
        self.sp = 10
        self.atk = 0
        self.mag = 0
        self.dfn = 0
        self.res = 0
        self.spd = 0
        self.eva = 0
        self.acc = 0
        self.maxHp = self.hp
        self.maxSp = self.sp
        self.atkC = 0
        self.magC = 0
        self.dfnC = 0
        self.resC = 0
        self.spdC = 0
        self.evaC = 0
        self.accC = 0
        self.atkT = 0
        self.magT = 0
        self.dfnT = 0
        self.resT = 0
        self.spdT = 0
        self.evaT = 0
        self.accT = 0
        self.action = False
        self.KO = False
        self.passives = 0
        self.skills = 1
        self.ps1 = 'HELLO. I AM ERROR PASSIVE 1.'
        self.ps2 = 'HELLO. I AM ERROR PASSIVE 2.'
        self.ps3 = 'HELLO. I AM ERROR PASSIVE 3.'
        self.sk1 = 'HELLO. I AM ERROR SKILL 1.'
        self.sk2 = 'HELLO. I AM ERROR SKILL 2.'
        self.sk3 = 'HELLO. I AM ERROR SKILL 3.'
        self.sk4 = 'HELLO. I AM ERROR SKILL 4.'
        self.sk5 = 'HELLO. I AM ERROR SKILL 5.'


def base(self):
    self.maxHp = self.hp
    self.maxSp = self.sp
    self.atkB = 0
    self.magB = 0
    self.dfnB = self.dfn
    self.resB = self.res
    self.spdB = self.spd
    self.evaB = self.eva
    self.accB = 0


class Template(Char):
    def __init__(self):
        super().__init__()
        self.name = "I AM ERROR."
        self.hp = 10
        self.sp = 10
        self.dfn = 0
        self.res = 0
        self.spd = 0
        self.eva = 0
        self.passives = 0
        self.skills = 0
        base(self)

class Chen(Char):
    def __init__(self):
        super().__init__()
        self.name = "Chen"
        self.hp = 3
        self.sp = 3
        self.dfn = 0
        self.res = 0
        self.spd = 10
        self.eva = 5
        self.passives = 1
        self.skills = 3
        self.sk1 = 'Flight of Idaten\n[ATK] Cost 1 SP\nOne Enemy : [Pierce 3]'
        base(self)

class Aya(Char):
    def __init__(self):
        super().__init__()
        self.name = "Aya"
        self.hp = 5
        self.sp = 6
        self.dfn = 1
        self.res = 0
        self.spd = 9
        self.eva = 6
        base(self)

class Saitama(Char):
    def __init__(self):
        super().__init__()
        self.name = "Saitama"
        self.hp = 99
        self.sp = 99
        self.dfn = 30
        self.res = 30
        self.spd = 20
        self.eva = 20
        base(self)

class Momiji(Char):
    def __init__(self):
        super().__init__()
        self.name = "Momiji"
        self.hp = 8
        self.sp = 4
        self.dfn = 4
        self.res = 2
        self.spd = 6
        self.eva = 2
        self.passives = 1
        self.skills = 2
        base(self)

class Cirno(Char):
    def __init__(self):
        super().__init__()
        self.name = 'Cirno'
        self.link = "http://tbscrossoverarena.pythonanywhere.com/cirno"
        self.hp = 4
        self.sp = 7
        self.dfn = 2
        self.res = 2
        self.spd = 7
        self.eva = 3
        self.passives = 1
        self.skills = 4
        base(self)

class Emilie(Char):
    def __init__(self):
        super().__init__()
        self.name = "Emilie"
        self.hp = 6
        self.sp = 8
        self.dfn = 1
        self.res = 0
        self.spd = 7
        self.eva = 4
        self.passives = 1
        self.skills = 4
        base(self)

class Gaius(Char):
    def __init__(self):
        super().__init__()
        self.name = "Gaius"
        self.hp = 8
        self.sp = 7
        self.dfn = 1
        self.res = 0
        self.spd = 7
        self.eva = 4
        self.passives = 1
        self.skills = 3
        base(self)

class Keine(Char):
    def __init__(self):
        super().__init__()
        self.name = "Keine"
        self.hp = 6
        self.sp = 12
        self.dfn = 3
        self.res = 2
        self.spd = 4
        self.eva = 1
        self.passives = 1
        self.skills = 4
        base(self)

class Kogasa(Char):
    def __init__(self):
        super().__init__()
        self.name = "Kogasa Tatara"
        self.hp = 5
        self.sp = 8
        self.dfn = 3
        self.res = 1
        self.spd = 3
        self.eva = 0
        self.passives = 1
        self.skills = 4
        base(self)

class Komachi(Char):
    def __init__(self):
        super().__init__()
        self.name = "Komachi Onozuka"
        self.hp = 17
        self.sp = 7
        self.dfn = 0
        self.res = 1
        self.spd = 3
        self.eva = 0
        self.passives = 1
        self.skills = 4
        base(self)

class Marisa(Char):
    def __init__(self):
        super().__init__()
        self.name = "Marisa"
        self.hp = 3
        self.sp = 18
        self.dfn = 0
        self.res = 1
        self.spd = 7
        self.eva = 3
        self.passives = 1
        self.skills = 4
        base(self)

class Minoriko(Char):
    def __init__(self):
        super().__init__()
        self.name = "Minoriko Aki"
        self.hp = 7
        self.sp = 12
        self.dfn = 0
        self.res = 4
        self.spd = 6
        self.eva = 1
        self.passives = 1
        self.skills = 4
        base(self)

class Nitori(Char):
    def __init__(self):
        super().__init__()
        self.name = "Nitori Kawashiro"
        self.hp = 5
        self.sp = 10
        self.dfn = 1
        self.res = 1
        self.spd = 5
        self.eva = 2
        self.passives = 1
        self.skills = 4
        base(self)

class Olberic(Char):
    def __init__(self):
        super().__init__()
        self.name = "Olberic"
        self.hp = 14
        self.sp = 5
        self.dfn = 3
        self.res = 0
        self.spd = 4
        self.eva = 2
        self.passives = 1
        self.skills = 4
        base(self)

class Ophilia(Char):
    def __init__(self):
        super().__init__()
        self.name = "Ophilia"
        self.hp = 8
        self.sp = 15
        self.dfn = 0
        self.res = 3
        self.spd = 4
        self.eva = 0
        self.passives = 1
        self.skills = 4
        base(self)

class Parsee(Char):
    def __init__(self):
        super().__init__()
        self.name = "Parsee Mizuhashi"
        self.hp = 4
        self.sp = 7
        self.dfn = 2
        self.res = 4
        self.spd = 5
        self.eva = 2
        self.passives = 1
        self.skills = 4
        base(self)

class Reimu(Char):
    def __init__(self):
        super().__init__()
        self.name = "Reimu Hakurei"
        self.hp = 5
        self.sp = 9
        self.dfn = 1
        self.res = 1
        self.spd = 5
        self.eva = 5
        self.passives = 1
        self.skills = 4
        base(self)

class Rinnosuke(Char):
    def __init__(self):
        super().__init__()
        self.name = "Rinnosuke Morichika"
        self.hp = 8
        self.sp = 6
        self.dfn = 2
        self.res = 1
        self.spd = 0
        self.eva = 1
        self.passives = 2
        self.skills = 2
        base(self)


class Rumia(Char):
    def __init__(self):
        super().__init__()
        self.name = "Rumia"
        self.hp = 3
        self.sp = 9
        self.dfn = 0
        self.res = 2
        self.spd = 3
        self.eva = 0
        self.passives = 1
        self.skills = 3
        base(self)

class Stahl(Char):
    def __init__(self):
        super().__init__()
        self.name = "Stahl"
        self.hp = 8
        self.sp = 8
        self.dfn = 2
        self.res = 2
        self.spd = 5
        self.eva = 1
        self.passives = 1
        self.skills = 3
        base(self)

class Sully(Char):
    def __init__(self):
        super().__init__()
        self.name = "Sully"
        self.hp = 7
        self.sp = 8
        self.dfn = 1
        self.res = 2
        self.spd = 6
        self.eva = 2
        self.passives = 0
        self.skills = 0
        base(self)


class Therion(Char):
    def __init__(self):
        super().__init__()
        self.name = "Therion"
        self.hp = 8
        self.sp = 10
        self.dfn = 1
        self.res = 1
        self.spd = 7
        self.eva = 3
        self.passives = 1
        self.skills = 4
        base(self)

class Vaike(Char):
    def __init__(self):
        super().__init__()
        self.name = "Vaike"
        self.hp = 14
        self.sp = 10
        self.dfn = 1
        self.res = 0
        self.spd = 5
        self.eva = 1
        self.passives = 1
        self.skills = 3
        base(self)

class Will(Char):
    def __init__(self):
        super().__init__()
        self.name = "I AM ERROR."
        self.hp = 7
        self.sp = 8
        self.dfn = 1
        self.res = 0
        self.spd = 7
        self.eva = 3
        self.passives = 1
        self.skills = 4
        base(self)

class Wobbuffet(Char):
    def __init__(self):
        super().__init__()
        self.name = "Wobbuffet"
        self.hp = 30
        self.sp = 6
        self.dfn = 0
        self.res = 0
        self.spd = 0
        self.eva = 0
        self.passives = 3
        self.skills = 1
        base(self)


class Youmu(Char):
    def __init__(self):
        super().__init__()
        self.name = "Youmu Konpaku"
        self.hp = 6
        self.sp = 12
        self.dfn = 3
        self.res = 1
        self.spd = 4
        self.eva = 1
        self.passives = 2
        self.skills = 4
        base(self)