

import affliction
from affliction import Affliction
import priority as prio


venomlock = ['slickness', 'asthma', 'anorexia']
hardlock = ['slickness', 'asthma', 'anorexia', 'curare']
truelock = ['slickness', 'asthma', 'anorexia', 'curare', 'impatience']


class Target:
    def __init__(self):
        self.affs = []
        self.eat_time = 1.5
        self.smoke_time = 1.5
        self.apply_time = 1.5
        self.sip_time = 1.5
        self.focus_time = 5

        self.eat_timer = self.eat_time
        self.smoke_timer = self.smoke_time
        self.apply_timer = self.apply_time
        self.sip_timer = self.sip_time
        self.focus_timer = self.focus_time

    def afflict(self, affliction):
        aff = Affliction(affliction)
        if not aff in self.affs:
            self.affs.append(Affliction(affliction))

    def dstab(self, venom1, venom2):
        aff1 = Affliction(venom1)
        aff2 = Affliction(venom2)
        if not aff1 in self.affs:
            self.affs.append(Affliction(venom1))
        if not aff2 in self.affs:
            self.affs.append(Affliction(venom2))

    def is_afflicted(self, aff_name):
        for i in self.affs:
            if i.get_name() == aff_name:
                return True
        return False

    def can_eat(self):
        return not self.is_afflicted("anorexia")

    def can_smoke(self):
        return not self.is_afflicted("asthma")

    def can_apply(self):
        return not self.is_afflicted("slickness")

    def can_sip(self):
        return not self.is_afflicted("anorexia")

    def can_focus(self):
        return not self.is_afflicted("impatience")

    def can_other(self):
        return True

    def can_cure(self, method):
        switcher = {
            "eat": self.can_eat(),
            "smoke": self.can_smoke(),
            "apply": self.can_apply(),
            "sip": self.can_sip(),
            "other": self.can_other()
        }
        return switcher[method]

    def eat(self, curative):
        if isinstance(curative, list):
            curative = curative[0]
        if self.can_cure("eat"):
            tmp_affs = []
            for i in self.affs:
                if i.is_cured(["eat", curative]):
                    tmp_affs.append(i)
            if len(tmp_affs) > 1:
                for k in range(0,len(tmp_affs)):
                    print(str(k)+": "+tmp_affs[k].get_name())
                to_cure = input("select which affliction to cure:\n")
                tmp_affs[0]=tmp_affs[int(to_cure)]
            if len(tmp_affs) == 0:
                print("Using thing will not cure")
            elif self.eat_timer >= self.eat_time:
                print("Curing " + tmp_affs[0].get_name() + " with " +curative)
                self.eat_timer = 0
                self.affs.remove(tmp_affs[0])
            else:
                print("ate outside of timer...")
        else:
            print("Cannot use "+curative+" due to another affliction")

    def smoke(self, curative):
        if isinstance(curative, list):
            curative = curative[0]
        if self.can_cure("smoke"):
            tmp_affs = []
            for i in self.affs:
                if i.is_cured(["smoke", curative]):
                    tmp_affs.append(i)
            if len(tmp_affs) > 1:
                for k in range(0,len(tmp_affs)):
                    print(str(k)+": "+tmp_affs[k].get_name())
                to_cure = input("select which affliction to cure:\n")
                tmp_affs[0]=tmp_affs[int(to_cure)]
            elif len(tmp_affs) == 0:
                print("Using thing will not cure")
                return
            if self.smoke_timer >= self.smoke_time:
                print("Curing " + tmp_affs[0].get_name() + " with " +curative)
                self.smoke_timer = 0
                self.affs.remove(tmp_affs[0])
            else:
                print("smoked outside of timer...")
        else:
            print("cannot use "+curative+" due to another affliction")

    def apply(self, curative):
        if isinstance(curative, list):
            curative = curative[0]
        if self.can_cure("apply"):
            tmp_affs = []
            for i in self.affs:
                if i.is_cured(["apply", curative]):
                    tmp_affs.append(i)
            if len(tmp_affs) > 1:
                for k in range(0,len(tmp_affs)):
                    print(str(k)+": "+tmp_affs[k].get_name())
                to_cure = input("select which affliction to cure:\n")
                tmp_affs[0]=tmp_affs[int(to_cure)]
            elif len(tmp_affs) == 0:
                print("Using thing will not cure")
                return
            if self.apply_timer >= self.apply_time:
                print("Curing " + tmp_affs[0].get_name() + " with " +curative)
                self.apply_timer = 0
                self.affs.remove(tmp_affs[0])
            else:
                print("applied outside of timer...")
        else:
            print("cannot use "+curative+" due to another affliction")

    def sip(self, curative):
        if isinstance(curative, list):
            curative = curative[0]
        if self.can_cure("sip"):
            tmp_affs = []
            for i in self.affs:
                if i.is_cured(["sip", curative]):
                    tmp_affs.append(i)
            if len(tmp_affs) > 1:
                for k in range(0,len(tmp_affs)):
                    print(str(k)+": "+tmp_affs[k].get_name())
                to_cure = input("select which affliction to cure:\n")
                tmp_affs[0]=tmp_affs[int(to_cure)]
            elif len(tmp_affs) == 0:
                print("Using thing will not cure")
                return
            if self.sip_timer >= self.sip_time:
                print("Curing " + tmp_affs[0].get_name() + " with " +curative)
                self.sip_timer = 0
                self.affs.remove(tmp_affs[0])
            else:
                print("sipped outside of timer...")
        else:
            print("cannot use "+curative+" due to another affliction")

    def focus(self):
        if self.can_focus():
            tmp_affs = []
            for i in self.affs:
                if i.is_cured(["focus", "focus"]):
                    tmp_affs.append(i)
            if len(tmp_affs) > 1:
                for k in range(0, len(tmp_affs)):
                    print(str(k)+": "+tmp_affs[k].get_namte())
                to_cure = input("select which affliction to cure:\n")
                tmp_affs[0]=tmp_affs[int(to_cure)]
            elif len(tmp_affs) == 0:
                print("Using thing will not cure")
                return
            if self.focus_timer >= self.focus_time:
                print("Curing " + tmp_affs[0].get_name() + " with focus")
                self.focus_timer = 0
                self.affs.remove(tmp_affs[0])
            else:
                print("focused outside of timer...")

    def should_eat(self):
        return self.can_eat() and self.eat_timer>=self.eat_time

    def should_smoke(self):
        return self.can_smoke() and self.smoke_timer>=self.smoke_time

    def should_apply(self):
        return self.can_apply() and self.apply_timer>=self.apply_time

    def should_sip(self):
        return self.can_sip() and self.sip_timer>=self.sip_time

    def should_focus(self):
        return self.can_focus() and self.focus_timer>=self.focus_time

    def inc_time(self, time_inc):
        self.eat_timer+=time_inc
        self.smoke_timer+=time_inc
        self.apply_timer+=time_inc
        self.sip_timer+=time_inc

        if self.should_eat():
            return True
        if self.should_smoke():
            return True
        if self.should_apply():
            return True
        if self.should_sip():
            return True
        return False

    def afflicted(self, aff):
        for i in self.affs:
            if i.get_name() == aff:
                return True
        return False

    def next_eat(self):
        for i in prio.eat_prio:
            if self.afflicted(i):
                return affliction.cures_eat[i]
        return 'none'

    def next_apply(self):
        for i in prio.apply_prio:
            if self.afflicted(i):
                return affliction.cures_apply[i]
        return 'none'

    def next_smoke(self):
        for i in prio.smoke_prio:
            if self.afflicted(i):
                return affliction.cures_smoke[i]
        return 'none'

    def next_sip(self):
        for i in prio.sip_prio:
            if self.afflicted(i):
                return affliction.cures_sip[i]
        return 'none'

    def next_focus(self):
        for i in prio.focus_prio:
            if self.afflicted(i):
                return True
        return 'none'


    def handle_eat(self):
        new_curative = self.next_eat()
        if not new_curative == 'none':
            self.eat(new_curative)

    def handle_smoke(self):
        new_curative = self.next_smoke()
        if not new_curative == 'none':
            self.smoke(new_curative)

    def handle_apply(self):
        new_curative = self.next_apply()
        if not new_curative == 'none':
            self.apply(new_curative)

    def handle_sip(self):
        new_curative = self.next_sip()
        if not new_curative == 'none':
            self.sip(new_curative)

    def handle_focus(self):
        new_curative = self.next_focus()
        if not new_curative == 'none':
            self.focus()

    def get_aff_name_list(self):
        tmp_name = []
        for i in self.affs:
            tmp_name.append(i.get_name())
        return tmp_name

    def intersection(self, a1, a2):
        return list(set(a1) & set(a2))

    def check_lock(self):
        tmp_name_list = self.get_aff_name_list()
        if self.intersection(tmp_name_list, truelock) == truelock:
            print("Truelock achieved")
            return
        if self.intersection(tmp_name_list, hardlock) == hardlock:
            print("Hardlock achieved")
            return
        if self.intersection(tmp_name_list, venomlock) == venomlock:
            print("venomlock achieved")
            return

    def handle_cure(self):
        self.check_lock()
        if self.should_focus():
            self.handle_focus()
        if self.should_eat():
            self.handle_eat()
        if self.should_smoke():
            self.handle_smoke()
        if self.should_apply():
            self.handle_apply()
        if self.should_sip():
            self.handle_sip()

    def print_afflictions(self):
        print("Afflictions:")
        for i in self.affs:
            print('\t'+i.get_name())
