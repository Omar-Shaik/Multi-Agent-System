import Environment 
import Agent 

class MultiAgentSystem:

    def __int__(self, scenario, x_upper, x_lower, y_upper, y_lower, number_of_agents, targets_per_agent):

        self.scenarios = ["Competitive", "Compassionate", "Collaborative"]
        self.scenario_type = self.scenarios.index(scenario) 
        self.environment = Environment.Environment(x_upper, x_lower, y_upper, y_lower)
        self.environment.populate(number_of_agents, targets_per_agent)
        
        
    def startSystem(self):
        #simulate
