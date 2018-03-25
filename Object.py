class Object:

    #Create new object at given position.
    def __init__(self, env, x, y, obj_type, tar_type):
        self.x_pos = x
        self.y_pos = y
        self.env = env
            
        #Object type 0 denotes a target. Object type of 1 denotes a body
        self.object_type = obj_type

        #Example of a target type can be A, as in Agent A tries to collect targets A
        self.target_type = tar_type

    def getObjecType(self):
        return self.object_type

    def getTargetType(self):
        return self.target_type


class Target(Object):

    #Assign target type to the target, i.e., the target that's trying to get it.
    def __init__(self, env, x, y, type):

        super(Target, self).__init__(env, x, y, 0, type)



class Body(Object):

    #Assign controller to the body
    def __init__(self, env, x, y, type, controller):
        self.controller = controller
        super(Body, self).__init__(env, x, y, 1, type)

    def getController(self):
        return self.controller

    # Move 1 unit in the given direction, if valid
    def move(self, movement, x_dif, y_dif):
        validity = self.env.validPosition(self.x_pos + movement[0], self.y_pos + movement[1])

        if(validity):
            self.x_pos += movement[0]
            self.y_pos += movement[1]

        return validity
