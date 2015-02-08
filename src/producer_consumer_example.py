"""Example of a producer-consumer of 10 items, then shutdown both"""
import threading
import Queue
import time
import logging
from buz import Buz

msgbus = Buz()

fmt = '%(asctime)s %(threadName)s.%(funcName)s: %(message)s'
logging.basicConfig(filename=__file__ + '.log',
                    format=fmt,
                    level=logging.INFO)


def produce():
    for i in range(10):
        msgbus.publish('item', i)
        logging.info('Just produced %d, I will sleep a little.', i)
        time.sleep(2)
    msgbus.publish('done')
    logging.info("I'm done producing, exiting thread.")


def consume():
    queue = msgbus.subscribe('item', 'done')
    while True:
        # Pretend this is a UI thread (e.g. Tkinter window),
        # we do not want to block waiting for a message.
        # Instead, we check for messages on a regular interval
        # via a timeout event handler.
        # Yes, this is polling, but it's low-frequency
        # and will not affect performancy. Only
        # downside is latency, which is livable
        # most of the time (we do not need realtime
        # UI updates).
        logging.info("Checking for new messages.")
        (msg, arg) = queue.check()
        if msg == 'item':
            logging.info('Got Item=%d', arg)
        elif msg == 'done':
            logging.info('Got Done, ending thread.')
            return
        else:
            logging.info('No message found, sleeping awhile.')
            time.sleep(3)

producer_thread = threading.Thread(name='p', target=produce)
consumer_thread = threading.Thread(name='c', target=consume)
consumer_thread.start()
producer_thread.start()
