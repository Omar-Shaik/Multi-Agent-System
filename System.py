import Environment
import matplotlib.pyplot as plt

class MultiAgentSystem:
    def __init__(self, scenario, x_lower, y_lower, length, height, number_of_agents, targets_per_agent):

        self.scenarios = ["Competitive", "Compassionate", "Collaborative"]
        self.scenario_type = self.scenarios[scenario]
        self.env = Environment.Environment(x_lower, y_lower, length, height, number_of_agents, targets_per_agent, scenario)
        self.number_of_agents = number_of_agents

    def startSystem(self):
        done = 0
        while done < self.number_of_agents:

            self.showEnvironment()
            
            for a in self.env.agents:
                a.search()
                self.showEnvironment()

            done = 0
            for a in self.env.agents:
                if a.controller.stop:
                    done += 1
            i = 0

    def showEnvironment(self):
        agent_x = []
        agent_y = []
        target_x = []
        target_y = []

        for a in self.env.agents:
            agent_x.append(a.body.position[0])
            agent_y.append(a.body.position[1])

        for t in self.env.targets:
            target_x.append(t.position[0])
            target_y.append(t.position[1])
            
        plt.plot(agent_x, agent_y, 'bo', target_x, target_y, 'ro')
