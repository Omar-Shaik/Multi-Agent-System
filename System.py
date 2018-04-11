import Environment
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


class MultiAgentSystem:
    def __init__(self, scenario, x_lower, y_lower, length, height, number_of_agents, targets_per_agent):

        self.scenarios = ["Competitive", "Compassionate", "Collaborative"]
        self.scenario_type = self.scenarios[scenario]
        self.env = Environment.Environment(x_lower, y_lower, length, height, number_of_agents, targets_per_agent, scenario)
        self.number_of_agents = number_of_agents

    def startSystem(self):
        done = 0

        agent_x = []
        agent_y = []
        target_x = []
        target_y = []

        '''for a in self.env.agents:
            agent_x.append(a.body.position[0])
            agent_y.append(a.body.position[1])

        for t in self.env.targets:
            target_x.append(t.position[0])
            target_y.append(t.position[1])'''

        fig = plt.figure()
        '''ax = fig.add_subplot(111, xlim=(0, 100), ylim=(0, 100))

        line, = ax.plot(agent_x, agent_y, 'bo')
        line2, = ax.plot(target_x, target_y, 'ro')

        def animate(i):
            thisx = agent_x
            thisy = agent_y
            tx = target_x
            ty = target_y

            line.set_data(thisx, thisy)
            line2.set_data(tx, ty)
            return line, line2'''

        while done < self.number_of_agents:


            for a in self.env.agents:
                a.controller.scan()
                a.controller.readMessages()
                a.search()
                a.controller.scan()
                #self.showEnvironment()


            done = 0
            for a in self.env.agents:
                if a.controller.stop:
                    done += 1
                    print (done)
     
            target_x = []
            target_y = []
            for a in self.env.agents:
                agent_x.append(a.body.position[0])
                agent_y.append(a.body.position[1])

            for t in self.env.targets:
                target_x.append(t.position[0])
                target_y.append(t.position[1])

            ax = fig.add_subplot(111, xlim=(0, 100), ylim=(0, 100))
            #ax.set_facecolor('black')

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


    '''def showEnvironment(self):
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

        fig = plt.figure()
        ax = fig.add_subplot(111, xlim=(0, 100), ylim=(0, 100))

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
        plt.pause(0.1)'''
