from system import *

class Group(object):

    __numOfGroups = 0

    def __init__(self, groupName):
        Group.__numOfGroups += 1
        self.groupID = Group.__numOfGroups
        self.groupName = groupName
        self.members = []
        self.meetings = []
        self.visable = True
        self.voteCount = 0
        self.reputation = 0

   def add_member(self, username):
        user = system.find_user_by_username(username)
        if(user != None):
            self.members.append(user)
        else:
            return "User not found"

    def remove_member(self, username):
        if(username in self.members):
            self.members.remove(username)
        else:
            return "User not Found"
    
    def group_size(self):
        return len(self.members)

    def increase_reputation(self, amount):
        self.reputation += amount

    def decrease_reputation(self, amount):
        self.reputation -= amount
       
    #Still figuring out voting and meetings
    
