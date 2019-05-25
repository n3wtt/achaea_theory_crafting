import priority as prio


types = ["eat", "sip", "apply", "smoke", "other"]
venom_conversion = {
    "xentio": "clumsiness",
    "oleander": "blindness",
    "eurypteria": "reckless",
    "kalmia": "asthma",
    "digitalis": "shyness",
    "darkshade": "darkshade",
    "curare": "paralysis",
    "epteth": "crippled_arm",
    "prefarar": "sensitivity",
    "monkshood": "disfigured",
    "euphorbia": "nausea",
    "colocasia": "blindness/deafness",
    "vernalius": "weariess",
    "epseth": "crippled_leg",
    "larkspur": "dizziness",
    "slike": "anorexia",
    "voyria": "voyria",
    "delphinium": "sleep",
    "notechis": "haemophilia",
    "vardrax": "addiction",
    "loki": "random",
    "aconite": "stupidity",
    "selarnia": "bondness",
    "gecko": "slickness",
    "scytherus": "relapse",
    "nechamandra": "freezing"
}
can_focus = [
    "stupidity",
    "anorexia",
    "recklessness",
    "vertigo",
    "claustrophobia",
    "generosity",
    "confusion",
    "dizziness",
    "loneliness",
    "shyness",
    "epilepsy",
    "pacifism",
    "agoraphobia",
    "masochism",
    "fear",
    "paranoia",
    "dementia",
    "hallucinations"
]
cures_other = {
    "bleeding": "clot",
    "entangled": "writhe",
    "fear": "compose",
    "transfixed": "writhe",
    "webbed": "writhe"
}
cures_eat = {
    "addiction": ["ginseng", "ferrum"],
    "agoraphobia": ["ginseng", "ferrum"],
    "asthma":["kelp", "aurum"],
    "claustrophobia": ["lobelia", "argentum"],
    "clumsiness": ["kelp", "aurum"],
    "confusion": ["ash","stannum"],
    "darkshade": ["ginseng", "ferrum"],
    "dementia": ["ash", "stannum"],
    "dissonance": ["goldenseal", "plumbum"],
    "dizziness":["goldenseal", "plumbum"],
    "epilepsy":["goldenseal", "plumbum"],
    "generosity":["bellwort", "cuprum"],
    "hallucinations":["ash", "stannum"],
    "haemophilia": ["ginseng", "ferrum"],
    "health_leech":["kelp", "aurum"],
    "hypochondria":["kelp", "aurum"],
    "hypersomnia":["kelp", "aurum"],
    "impatience":["goldenseal", "plumbum"],
    "justice":["bellwort", "cuprum"],
    "lethargy":["ginseng", "ferrum"],
    "loneliness":["lobelia", "argentum"],
    "lovers":["bellwort", "cuprum"],
    "masochism": ["lobelia", "argentum"],
    "nausea": ["ginseng", "ferrum"],
    "pacifism": ["bellwort", "cuprum"],
    "paralysis":["bloodroot", "magnesium"],
    "paranoia":["ash", "stannum"],
    "peace":["bellwort", "cuprum"],
    "recklessness":["lobelia", "argentum"],
    "scytherus":["ginseng", "ferrum"],
    "sensitivity":["kelp", "aurum"],
    "shyness":["goldenseal", "plumbum"],
    "slickness": ["bloodroot", "magnesium"],
    "stupidity":["goldenseal", "plumbum"],
    "vertigo":["lobelia", "argentum"],
    "weariness":["kelp", "aurum"]
}
cures_smoke = {
    "aeon":["elm", "cinnabar"],
    "deadening":["elm", "cinnabar"],
    "disfigurement":["valerian", "realgar"],
    "hellsight":["valerian", "realgar"],
    "mana_leech":["valerian", "realgar"],
    "slickness":["valerian", "realgar"],
}
cures_sip = {
    "voyria": ["immunity"]
}
cures_apply = {
    "ablaze": ["mending"],
    "anorexia": ["epidermal"],
    "blindness": ["epidermal"],
    "concussion": ["restoration"],
    "crippled_leg": ["mending"],
    "crippled_arm": ["mending"],
    "damaged_leg": ["restoration"],
    "damaged_arm": ["restoration"],
    "deafness": ["epidermal"],
    "freezing": ["caloric"],
    "internal_trauma": ["restoration"],
    "mangled_leg": ["restoration"],
    "mangled_arm": ["restoration"],
    "stuttering": ["epidermal"]
}

class Affliction:


    def __init__(self, name):
        self.cure_list = {}
        self.is_focus = False
        if name in venom_conversion:
            self.name = venom_conversion[name]
        else:
            self.name = name
        if self.name in cures_sip:
            self.cure_list["sip"] = cures_sip[self.name]
        if self.name in cures_apply:
            self.cure_list["apply"] = cures_apply[self.name]
        if self.name in cures_eat:
            self.cure_list["eat"] = cures_eat[self.name]
        if self.name in cures_smoke:
            self.cure_list["smoke"] = cures_smoke[self.name]
        if self.name in cures_other:
            self.cure_list["other"] = cures_other[self.name]

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.get_name() == other.get_name()
        else:
            return False

    def can_focus(self, name):
        return name in prio.focus_prio

    def is_cured(self, curative):
        if (curative[0] == 'focus'):
            return self.can_focus(self.name)
        if curative[0] in self.cure_list:
            if curative[1] in self.cure_list[curative[0]]:
                return True
        else:
            return False
        return False

    def get_name(self):
        return self.name

    def get_cure_list(self):
        return self.cure_list
