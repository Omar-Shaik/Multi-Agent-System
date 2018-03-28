import Environment as env
import Agent as agt

class System:

    def __int__(self, scenario, x_upper, x_lower, y_upper, y_lower, agents):

        self.scenarios = ["Competitive", "Compassionate", "Collaborative"]
        self.scenario_type = self.scenarios.index(scenario)
        self.environment = env.Environment(x_upper, x_lower, y_upper, y_lower)
