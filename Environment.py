import math
import random
import string
import Communication
import Agent
import Object

#Hi
class Environment:
    # Create new environment with the given bounds

   def __init__(self, x_lower, y_lower, length, height):
       self.x_lower = x_lower
       self.y_lower = y_lower
       self.x_upper = x_lower + length
       self.y_upper = y_lower + height
       self.target_types = list(string.ascii_uppercase)
       self.target_type_counter = 0
       self.agents = []
       self.targets = []
       self.public_channel = Communication.CommunicationChannel(0)


    # Populates an environment with the number of agents and number of targets per agent specified.
    # Found space variable makes sure it's safe to add the randomly generated agent. Only becomes true when position is valid.

    def populate(self, number_of_agents, targets_per_agent):
        for i in range(number_of_agents):
            found_space = False
            while (not found_space):
                agent = Agent.Agent(self, random.randint(self.x_lower, self.x_upper),
                                    random.randint(self.y_lower, self.y_upper), self.target_types[i])
                found_space = self.validPosition(agent.body)
            self.objects.append(agent.body)
            for j in range(targets_per_agent):
                found_space = False
                while (not found_space):
                    target = Object.Target(self, random.randint(self.x_lower, self.x_upper),
                                           random.randint(self.y_lower, self.y_upper), self.target_types[i])
                    found_space = self.validPosition(target)
                self.objects.append(target)


# Function checks if proposed position is valid.
# Validity variable holds the validity of the position. Only changes if position is invalid.
# Avoids unneccessary entry if first condition makes the position invalid.
# First if statement checks if the position is in the bounds of the envrionment.
# Second if statement is a loop that makes sure that agents aren't placed too close to other agents.
# Third if statement within second checks if that position is currently occupied.

   def validPosition(self, object):
       validity = True
       if object.pos[0] >= self.x_upper or object.pos[0] <= self.x_lower or object.pos[1] >= self.y_upper or object.pos[1] <= self.y_lower:
           validity = False
       if validity and object.target_type == 1:
           for a in self.agents:
               if (a.pos[0] == object.pos[0] and a.pos[1] == object.pos[1]) or (math.sqrt((a.pos[0] - object.pos[0]) ** 2 + (a.pos[1] - object.pos[1]) ** 2)) < 20:
                   validity = False
       if validity and object.target_type == 0:
               for t in self.targets:
                       if (t.pos[0] == object.pos[0] and t.pos[1] == object.pos[1]):
                               validity = False
       return validity


# Returns a list of elements visible to the body.
# Removes targets that have the same target type as the body from the environment if they are within radar range.

   def objectsAround(self, body):
        visible = []
        for t in self.targets:
            if math.sqrt((body.pos[0] - t.pos[0]) ** 2 + (body.pos[1] - t.pos[1]) ** 2) <= 10:
                if body.target_type == t.target_type:
                    self.targets.remove(t)
                    body.controller.collected += 1 
                visible.append(t)
            if body.target_type == t.target_type:
                self.targets.remove(t)
        return visible
    
#Returns euclidean distance between two objects
    def distance(o1, o2):
        return math.sqrt((o1.pos[0] - o2.pos[0]) ** 2 + (o1.pos[1] - o2.pos[1]) ** 2)
