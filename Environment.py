import math
import random as ran
import Communication as com
import Agent as agt
import Object as obj
import string as str


class Environment:
    # Create new environment with the given bounds
    def __init__(self, x_upper, x_lower, y_upper, y_lower):
        self.x_lower = x_lower
        self.x_upper = x_upper
        self.y_lower = y_lower
        self.y_upper = y_upper
        self.target_types = list(str.ascii_uppercase)
        self.objects = []
        self.public_channel = com.CommunicationChannel(0)

    #Populates an environment with the number of agents and number of targets per agent specified.
    #Found space variable makes sure it's safe to add the randomly generated agent. Only becomes true when position is valid.
    def populate(self, number_of_agents, targets_per_agent):
        for i in range(number_of_agents):
            found_space = False
            while(not found_space):
                agent = agt.Agent(self, ran.randint(self.x_lower, self.x_upper), ran.randint(self.y_lower, self.y_upper), self.target_types[i])
                found_space = self.validPosition(agent.body)
            self.objects.append(agent.body)
                for j in range(targets_per_agent):
                    found_space = False
                    while(not found_space):
                        target = obj.Target(self, ran.randint(self.x_lower, self.x_upper), ran.randint(self.y_lower, self.y_upper), self.target_types[i])
                        found_space = self.validPosition(target)
                    self.objects.append(target)
        
        
    #Function checks if proposed position is valid.
    #Validity variable holds the validity of the position. Only changes if position is invalid.
    #Avoids unneccessary entry if first condition makes the position invalid.
    #First if statement checks if the position is in the bounds of the envrionment.
    #Second if statement is a loop that compares the position of every object currently in the environment with the proposed position.
    #Third if statement within second checks if that position is currently occupied.
    #Third if statement also makes sure that two agents don't get too close to one another. Their radars cannot overlap, meaning 20cm.
    
    def validPosition(self, object):
        validity = True
        if object.position[0] >= self.x_upper or object.position[0] <= self.x_lower or object.position[1] >= self.y_upper or object.position[1] <= self.y_lower:
            validity = False
        if (validity):
            for obj in self.objects: 
                if (obj.postion[0] == object.position[0] and obj.position[1] == object.position[1]) or (obj.object_type == 1 and math.sqrt((obj.pos[0] - object.position[0])**2 + (obj.pos[1] - object.position[1])**2)) < 20:
                    validity = False
        return validity
    
    
    #Returns a list of elements visible to the body.
    #Removes targets that have the same target type as the body from the environment if they are within radar range.
    
    def scanner(self, body):
        visible = []
        for object in self.objects:
            if math.sqrt((body.position[0] - object.position[0])**2 + (body.position[1] - object.position[1])**2 ) <= 10:
                visible.append(body)
            if body.target_type == object.target_type: 
                self.objects.remove(object)
        return visible
