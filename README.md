# buztest
Experiment with pub-sub architecture (goal: refactor pytddmon).

The goal is to increase testability and elegance/understandability of pytddmon, NOT higher performance (which is likely to occur anyway but that is a side-effect).

Example of code that implements a simple producer-consumer scenario:

```
import threading
import buz

# The producer publishes 10 messages of kind 'item', then a 'done' when done.
# Then it stops (thread of execution), by returning from run() function.
# The consumer (subscribes to messages of kind 'item' and 
... TODO

# The consumer subscribes to 'item' and 'done' messages.
# Items are printed to console.
# The done message quits the thread.
... TODO

# TODO: write unit tests first...?

producer = Producer()
consumer = Consumer()
producer.start()
consumer.start()

```
