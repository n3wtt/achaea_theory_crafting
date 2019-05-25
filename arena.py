from target import Target

class Arena:
    def __init__(self):
        self.reset = False
        self.quit = False
        self.time_inc = .1
        self.time=0
        self.bal = 0
        self.target = Target()
        self.cmd_list = ["dstab", "wait", "quit", "reset"]

    def inc_time(self):
        self.bal-=self.time_inc
        self.time+=self.time_inc
        self.bal = round(self.bal, 1)
        self.time = round(self.time, 1)
        if self.target.inc_time(self.time_inc):
            self.target.handle_cure()

    def afflict(self, aff):
        tmp_split = aff.split(' ')
        print(tmp_split)
        while (tmp_split[0] == 'affs'):
            self.affliction_list()
            tmp_split = input("\n").split(' ')

        while len(tmp_split) == 1 and not tmp_split[0] in self.cmd_list:
            self.target.afflict(tmp_split[0])
            self.affliction_list()
            tmp_split = input("").split(' ')
        if (tmp_split[0] == 'quit'):
            self.quit = True
            return
        if (tmp_split[0] == 'reset'):
            self.reset = True
            return
        if (tmp_split[0] == 'dstab' or tmp_split[0] == 'ds'):
            self.target.dstab(tmp_split[1], tmp_split[2])
            self.bal = 2.1
        elif (tmp_split[0] == 'wait'):
            self.bal = 1
        elif (len(tmp_split) > 1):
            self.target.dstab(tmp_split[0], tmp_split[1])
            self.bal = 2.1
        else:
            self.target.afflict(aff)


    def affliction_list(self):
        self.target.print_afflictions()

    def prompt(self):
        self.affliction_list()
        next = input(str(self.time)+": What should I do next?\n")
        self.afflict(next)
        if self.quit or self.reset:
            return
        self.target.handle_cure()

    def can_action(self):
        if self.bal <= 0:
            self.prompt()

    def fight(self):
        while not self.can_action():
            if self.reset:
                self.__init__()
                print("reset all afflictions")
                continue
            if self.quit:
                return
            self.inc_time()
