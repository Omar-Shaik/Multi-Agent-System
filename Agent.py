import Object
import Controller


class Agent:
    def __init__(self, env, x, y, target_type, controller_type):
        self.body = Object.Body(x, y, target_type)
        if controller_type == 0:
            self.controller = Controller.Competitive_Controller(self.body, env)
        elif controller_type == 1:
            self.controller = Controller.Collaborative_Controller(self.body, env)
        elif controller_type == 2:
            self.controller = Controller.Compassionate_Controller(self.body, env)
        self.body.controller = self.controller

    def search(self):
        self.controller.goToNext()
