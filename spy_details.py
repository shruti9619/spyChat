from datetime import datetime

#class to maintain records of a spy
class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = "Hey there I am using spyChat!"

#class to maintain records of the chatmessages from all sides
class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.is_sent_by_me = sent_by_me

spy = Spy('Shru', 'Ms.', 23, 4.0)

frnd_one = Spy('Sanjay', 'Mr.', 4.0, 27)
frnd_two = Spy('Pooja', 'Ms.', 4.2, 21)
frnd_three = Spy('Shakti', 'Mr.', 4.35, 37)


friends_list = [frnd_one, frnd_two, frnd_three]