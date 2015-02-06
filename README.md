# buztest
Experiment with pub-sub architecture (goal: refactor pytddmon)

Example of code that implements a simple producer-consumer scenario:

  import buz
  
  # The producer publishes 10 messages of kind 'item', then a 'done' when done.
  # Then it stops (thread of execution), by returning from run() function.
  
  
  # The consumer (subscribes to messages of kind 'item' and 
