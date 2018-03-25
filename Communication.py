class CommunicationChannel:

    def __init__(self, type):
        #Public channels are type 0. Private channels are type 1.
        self.channel_type = type
        self.access_list = []
        self.message_log = []

    #Only the public channel can have unlimited accesssors added to it
    #Private channels between two agents can't have more accessors added to them
    def add_access(self, accessor):
        if (self.channel_type == 0 or len(self.access_list) < 2):
            self.access_list.append(accessor)

    #Each controller has a list of new messages
    def send_message(self, sender, message):
        if sender in self.access_list:
            # Adds message to message log
            self.message_log.append(message)
            # Sends message to all controllers in the access list except the sender
            for controller in self.access_list:
                if controller != sender:
                    controller.new_messages.append(message)
