class Object:
    
    '''
    Initialization function initializes function at given position in given environment.
    Object type 0 denotes a target. Object type 1 denotes a body.
    Target type associates agents with targets.
    '''
    def __init__(self, env, x, y, obj_type, tar_type):
        self.position = [x, y]
        self.env = env
        self.object_type = obj_type
        self.target_type = tar_type
        

class Target(Object):

    '''
    This class just creates an object instance with a value of 0 for the object type.
    This class is created more because a body class was created.
    '''
    def __init__(self, env, x, y, type):
        super(Target, self).__init__(env, x, y, 0, type)


class Body(Object):

    '''
    This class creates an object instance with a value of 1 for the object type.
    It also has movement function, which targets don't have. I didn't want to give targets movement.
    '''
    def __init__(self, env, x, y, type):
        super(Body, self).__init__(env, x, y, 1, type)

    # Move 1 unit in the given direction, if valid
    def move(self, movement):
        validity = self.env.validPosition(self.position[0] + movement[0], self.position[1] + movement[1])
        if(validity):
            self.position[0] += movement[0]
            self.position[1] += movement[1]
        return validity
    
    def scan(self):
        return self.env.objectsAround(self)

       
