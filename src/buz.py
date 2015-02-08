import Queue
import logging


class Buz(object):

    def publish(self, msg, arg=None):
        logging.debug('Publishing: %s, %s', msg, arg)
        self.q.put((msg, arg))

    def subscribe(self, *msgnames):
        logging.debug('Subscribing to: %s', msgnames)
        self.q = Queue.Queue()

        def check():
            try:
                return self.q.get_nowait()
            except Queue.Empty:
                return (None, None)
        self.q.check = check
        return self.q
