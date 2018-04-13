import Environment
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import csv


class MultiAgentSystem:
    def __init__(self, scenario, x_lower, y_lower, length, height, number_of_agents, targets_per_agent):

        self.scenarios = ["Competitive", "Compassionate", "Collaborative"]
        self.scenario_type = self.scenarios[scenario]
        self.env = Environment.Environment(x_lower, y_lower, length, height, number_of_agents, targets_per_agent, scenario)
        self.number_of_agents = number_of_agents
        self.a = scenario + 1
        self.b = 1
        self.g = 0
        self.h = 0
        self.i = 0
        self.j = 0

    def updateStatVar(self):
        self.updateAgentHappiness()
        self.updateMaxHappiness()
        self.updateMinHappiness()
        self.updateAverageHappiness()
        self.updateStdDevHappiness()
        self.updateAgentCompetitiveness()

    def updateAgentHappiness(self):
        for agt in self.env.agents:
            agt.f = agt.controller.d / (agt.controller.e + 1)

    def updateMaxHappiness(self):
        self.g = 0
        for agt in self.env.agents:
            if agt.controller.f > self.g:
                self.g = agt.controller.f

    def updateMinHappiness(self):
        self.h = self.env.agents[0].controller.f
        for agt in self.env.agents:
            if agt.controller.f < self.h:
                self.h = agt.controller.f

    def updateAverageHappiness(self):
        self.i = 0
        for agt in self.env.agents:
            self.i += agt.controller.f
        self.i /= self.number_of_agents

    def updateStdDevHappiness(self):
        self.j = 0
        for agt in self.env.agents:
            self.j += (agt.controller.f - self.i) ** 2
        self.j = math.sqrt(self.j / self.number_of_agents)

    def updateAgentCompetitiveness(self):
        for agt in self.env.agents:
            agt.controller.k = (agt.controller.f - self.h) / (self.g - self.h)

    def startSystem(self):
        done = 0
        agent_x = []
        agent_y = []
        target_x = []
        target_y = []
        fig = plt.figure()
        csv_row = []
        fig = plt.figure()
        firstFile = open('G21_1.csv', 'w')
        secondFile = open('G21_2.csv', 'w')

        while done < self.number_of_agents:

            for agt in self.env.agents:
                agt.controller.scan()
                agt.controller.readMessages()
                agt.search()
                self.updateStatVar()
                row = [self.a, self.b, agt.controller.c, agt.controller.d, agt.controller.e, agt.controller.f, self.h, self.h, self.i, self.j, agt.controller.k]
                csv_row.append(row)

            done = 0
            for a in self.env.agents:
                if a.controller.stop:
                    done += 1

            self.b +=1

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

            ax = fig.add_subplot(111, xlim=(0, 100), ylim=(0, 100))
            ax.set_facecolor('black')

            line, = ax.plot(agent_x, agent_y, 'bo')
            line2, = ax.plot(target_x, target_y, 'ro')

            def animate(i):
                thisx = agent_x
                thisy = agent_y
                tx = target_x
                ty = target_y

                line.set_data(thisx, thisy)
                line2.set_data(tx, ty)
                return line, line2

            ani = animation.FuncAnimation(fig, animate)
            plt.show(block=False)
            plt.pause(0.01)
            ax.cla()

        with firstFile:
            writer = csv.writer(firstFile)
            writer.writerows(csv_row)
