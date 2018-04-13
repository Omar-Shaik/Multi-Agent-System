import math
import random
import string
import Communication
import Agent
import Object


class Environment:
    # Create new environment with the given bounds
    # Populates an environment with the number of agents and number of targets per agent specified.
    # Found space variable makes sure it's safe to add the randomly generated agent. Only becomes true when position is valid.

    def __init__(self, x_lower, y_lower, width, height, number_of_agents, targets_per_agent, controller_type):
        self.x_lower = x_lower
        self.y_lower = y_lower
        self.x_upper = x_lower + width
        self.y_upper = y_lower + height
        self.target_types = list(string.ascii_uppercase)
        self.number_of_agents = number_of_agents
        self.targets_per_agent = targets_per_agent
        self.number_of_targets = number_of_agents * targets_per_agent
        self.agents = []
        self.targets = []
        self.public_channel = Communication.CommunicationChannel(0)

        for i in range(number_of_agents):
            found_space = False

            while not found_space:
                position = [random.randint(self.x_lower, self.x_upper), random.randint(self.y_lower, self.y_upper)]
                found_space = self.validPosition(position, True)
            agent = Agent.Agent(self, position[0], position[1], self.target_types[i], controller_type)
            self.public_channel.addAccess(agent.controller)
            agent.controller.channels["Public"] = self.public_channel
            self.agents.append(agent)

            for j in range(targets_per_agent):
                found_space = False
                while not found_space:
                    position = [random.randint(self.x_lower, self.x_upper), random.randint(self.y_lower, self.y_upper)]
                    found_space = self.validPosition(position, False)
                target = Object.Target(position[0], position[1], self.target_types[i])
                self.targets.append(target)
        i = 0
        while i < len(self.agents) - 1:
            j = i + 1
            while j < len(self.agents):
                channel = Communication.CommunicationChannel(1)
                agent1 = self.agents[i]
                agent2 = self.agents[j]
                channel.addAccess(agent1.controller)
                agent1.controller.channels[agent2.body.target_type] = channel
                channel.addAccess(agent2.controller)
                agent2.controller.channels[agent1.body.target_type] = channel
                j += 1
            i += 1


            # Function checks if proposed position is valid.
            # Validity variable holds the validity of the position. Only changes if position is invalid.
            # Avoids unnecessary entry if first condition makes the position invalid.
            # First if statement checks if the position is in the bounds of the environment.
            # Second if statement is a loop that compares the position of every object currently in the environment with the proposed position.
            # Third if statement within second checks if that position is currently occupied.
            # Third if statement also makes sure that two agents don't get too close to one another. Their radars cannot overlap, meaning 20cm.

    def validPosition(self, position, if_controller):
        validity = True

        if position[0] >= self.x_upper or position[0] <= self.x_lower or position[1] >= self.y_upper or position[
            1] <= self.y_lower:
            validity = False

        """if validity:
            i = 0
            while validity and i < len(self.targets):
                if self.targets[i].position[0] == position[0] and self.targets[i].position[1] == position[1]:
                    validity = False
                i += 1"""

        """if if_controller and validity:
            i = 0
            while validity and i < len(self.agents):
                if self.distance(self.agents[i].body.position, position) < 20 and self.distance(self.agents[i].body.position, position)  > math.sqrt(2):
                    validity = False
                i += 1"""

        return validity

        # Returns a list of elements visible to the body.
        # Removes targets that have the same target type as the body from the environment if they are within radar range.

    def objectsAround(self, body, need_visible):
        visible = []

        i = len(self.targets) - 1
        while i >= 0:
            if self.distance(body.position, self.targets[i].position) <= 10:
                if body.target_type == self.targets[i].target_type:
                    del self.targets[i]
                    body.controller.d += 1
                else:
                    visible.append(self.targets[i])
            i -= 1

        if need_visible:
            return visible
        else:
            return []

            # Returns euclidean distance between two objects: o1 and o2

    def distance(self, pos1, pos2):
        return math.hypot(pos2[0] - pos1[0], pos2[1] - pos1[1])
