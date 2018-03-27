import math
import Communication as com
class Environment:

    #Create new environment with the given bounds
    def __init__(self, x_upper, x_lower, y_upper, y_lower):
        self.x_lower = x_lower
        self.x_upper = x_upper
        self.y_lower = y_lower
        self.y_upper = y_upper
        self.objects = []
        self.public_channel = com.CommunicationChannel(0)

    '''
    Registers an object in the environment.
    Uses the validPosition function.
    Returns True if registration is successful.
    Returns False if registration is unsuccessful.
    '''
    def registerObject(self, object):
        if self.validPosition(object.position[0], object.position[1]):
            self.objects.append(object)
            return True
        else:
            return False
    
    '''
    Function checks if proposed position is valid.
    Validity variable holds the validity of the position. Only changes if position is invalid.
    Loop variable controls the entry of the loop for secondary verification.
    Avoids unneccessary entry if first condition makes the position invalid.
    First if statement checks if the position is in the bounds of the envrionment.
    Second if statement is a loop that compares the position of every object currently in the environment with the proposed position.
    Third if statement within second checks if that position is currently occupied.
    Third if statement also makes sure that two agents don't get too close to one another. Their radars cannot overlap, meaning 20cm.
    '''
    def validPosition(self, object):
        validity = True
        loop = True
        if self.x_upper <= object.position[0] <= self.x_lower:
            if self.y_upper <= object.position[1] <= self.y_lower:
                validity = False
                loop = False
        if (loop):
            for obj in self.objects: 
                if (obj.postion[0] == object.position[0] and obj.position[1] == object.position[1]) or (obj.object_type == 1 and math.sqrt((obj.pos[0] - object.position[0])**2 + (obj.pos[1] - object.position[1])**2)) < 20:
                    validity = False
        return validity
    
    '''
    Returns a list of elements visible to the body.
    Removes targets that have the same target type as the body from the environment.
    '''
    def scanner(self, body):
        visible = []
        for object in self.objects:
            if math.sqrt((body.position[0] - object.position[0])**2 + (body.position[1] - object.position[1])**2 ) <= 10 and object.object_type == 0:
                visible.append(object)
            if object.target_type == body.target_type: 
                self.objects.remove(target)
        return visible
