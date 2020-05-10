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

    #methods not yet added
    