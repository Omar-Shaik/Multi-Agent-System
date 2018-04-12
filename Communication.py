class CommunicationChannel:
    # Initialization function requires just the channel type.
    # Public channels have type 0. Private channels have type 1.
    # The access list holds all agents that have access to the channel.
    # The message log holds all previous messages.


    def __init__(self, type):
        self.channel_type = type
        self.access_list = []
        self.message_log = []

    # Only public channels can have unlimited accessors in it.
    # Private channels cannot be formed between more than two agents.

    def addAccess(self, accessor):
        if (self.channel_type == 0 or len(self.access_list) < 2):
            self.access_list.append(accessor)

    # A message is sent by specifying the sender and the message.
    # Message is only sent if sender is in the access list.
    # Message is added to the message log.
    # Message is added to the new messages list of every agent in the access list besides the sender.

    def sendMessage(self, sender, message):
        if sender in self.access_list:
            # Adds message to message log
            self.message_log.append(message)
            # Sends message to all controllers in the access list except the sender
            for c in self.access_list:
                if c != sender:
                    c.new_messages.append(message)
