import math
class Environment:

    #Create new environment with the given bounds
    def __init__(self, x_upper, x_lower, y_upper, y_lower):
        self.x_lower = x_lower
        self.x_upper = x_upper
        self.y_lower = y_lower
        self.y_upper = y_upper
        self.objects = []
        self.public_channel = CommunicationChannel(0) #for some reason this isn't working



    #Registers an object in the environment
    #Uses the validPosition function
    def registerObject(self, object):
        if self.validPosition(object.x_pos, object.y_pos):
            self.objects.append(object)
            return True
        else:
            return False

    #Function checks if given position is unoccupied and within bounds
    #validity variable holds the validity of the position. Only changes if position is invalid
    #loop variable controls the entry of the loop for secondary verification. Avoids unneccessary entry if first condition makes the position invalid
    def validPosition(self, x, y):
        validity = True
        loop = True

        if self.x_upper <= x <= self.x_lower: #Check in bounds
            if self.y_upper <= y <= self.y_lower:
                validity = False
                loop = False

        if (loop):
            for object in self.objects: #Check unoccupied
                if object.x_pos == x and object.y_pos == y:
                    validity = False

        return validity


    #Get a list of elements visible from the given coordinates
    def objectsAround(self, controller):
        visible = []

        #Euclidean distance: distance^2 = xdiff^2 + ydiff^2
        for object in self.objects:
            #If agent not at scan position AND Euclidean distance less than/equal to 10
            if math.sqrt((controller.body.x_pos - object.x_pos)**2 + (controller.body.y_pos - object.y_pos)**2 ) <= 10 and object.getObjecType() == 0:
                visible.append(object)

        return visible

    def pickUp(self, controller, target):
        if target in self.objects and controller.body.target_type == target.target_type:
            self.objects.remove(target)
