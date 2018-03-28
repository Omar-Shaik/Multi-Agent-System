class Object:
    
    #Initialization function initializes function at given position in given environment.
    #Object type 0 denotes a target. Object type 1 denotes a body.
    #Target type associates agents with targets.
    
    def __init__(self, env, x, y, obj_type, tar_type):
        self.position = [x, y]
        self.env = env
        self.object_type = obj_type
        self.target_type = tar_type        


#This class creates an object instance with a value of 1 for the object type.
#Adds move and scan functions to object subclass.
class Body(Object):

    def __init__(self, env, x, y, type):
        Object.__init__(env, x, y, 1, type)

    # Move 1 unit in the given direction, if valid
    def move(self, movement):
        validity = self.env.validPosition(self.position[0] + movement[0], self.position[1] + movement[1])
        if(validity):
            self.position[0] += movement[0]
            self.position[1] += movement[1]
        return validity
    
    #Returns a list of objects within radar range of body
    def scan(self):
        return self.env.scanner(self)

       
#This class just creates an object instance with a value of 0 for the object type.
#Created only because body class was created and the only other object type was target.
#Object class may as well be abstracted.
class Target(Object):

    def __init__(self, env, x, y, type):
        Object.__init__(env, x, y, 0, type)
