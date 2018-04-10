import Environment

class MultiAgentSystem:
    def __init__(self, scenario, x_lower, y_lower, length, height, number_of_agents, targets_per_agent):

        self.scenarios = ["Competitive", "Compassionate", "Collaborative"]
        self.scenario_type = self.scenarios[scenario]
        self.env = Environment.Environment(x_lower, y_lower, length, height, number_of_agents, targets_per_agent, scenario)
        self.number_of_agents = number_of_agents

    def startSystem(self):
        done = 0
        while done < self.number_of_agents:
            done = 0
            
            for a in self.env.agents:
                if a.controller.stop:
                    done += 1

            for a in self.env.agents:
                a.search()
