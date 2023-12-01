import time


class Tracker:
    __starts = {}
    __counts = {}

    def __init__(self):
        self.__start = time.time()

    def start(self, section):
        self.__starts[section] = time.time()

    def stop(self, section):
        if not section in self.__counts:
            self.__counts[section] = 0
        self.__counts[section] += time.time() - self.__starts[section]
        self.__starts.pop(section, None)

    def done(self):
        print(f'Elapsed time: {self.format(time.time() - self.__start)}ms')
        for key, value in self.__counts.items():
            print(f'\t{key}: {self.format(value)}ms')

    def format(self, t):
        return int((t) * 1000)


tracker = Tracker()
