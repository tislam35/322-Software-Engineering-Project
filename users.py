from system import *

class OU(object):

    __numOfUsers = 0
    
    def __init__(self, username, password, first_name, last_name, email, phoneNumber, interests, score):
        OU.__numOfUsers += 1
        self.id = OU.__numOfUsers
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_Name = last_name
        self.email = email
        self.phoneNumber = phoneNumber
        self.interests = interests
        self.score = score
        self.affiliatedGroups = []
        self.warningsCount = 0
        #adding to WB and BB will be done in invites gui
        self.whiteBox = []
        self.blackBox = []
        self.invites = []
        self.complimentsCount = 0
        self.complaintsCount = 0
        #setting automessage will be done in the ui file
        self.autoMsg = ""

	#gets called on compliment button click
    def compliment(self, username, message):
        targetUser = system.search_by_username(username)
        targetUser.complimentsCount += 1
        if targetUser.complimentsCount > 2:
            system.promote(targetUser)
            #maybe display a message saying they were promoted
        #add targetUser and message to system.compliments
        system.compliments.append([targetUser, message])

    #gets called on complaint button click
    def complaint(self, username, message):
        targetUser = system.search_by_username(username)
        system.complaints.append([targetUser, message])

    #initial score method
    def initialScore(self):
        #

    #invite method called on inviting a user
    #a return of 0 means user was successfully invited to the group
    #a return of 1 means current user is in invitee's BB, display automessage
    def invite(self, username, groupname, message):
        #check if current user is in white box
        targetUser = system.search_by_username(username)
        targetGroup = system.search_by_group(groupname)
        for i in targetUser.whiteBox:
            if system.cur_user.id == i.id:
                #inviting user is in invitee's whitebox
                targetGroup.members.append(targetUser)
                targetUser.affiliatedGroups.append(targetGroup)
                return 0
        for i in targetUser.blackBox:
            if system.cur_user.id == i.id:
                #inviting user is in invitee's blackbox
                #display targetUser.autoMsg if any
                return 1
        #current user isnt in white or black box
        targetUser.invites.append()


    
class VIP(OU):

    def __init__(self, username, password, first_name, last_name, email, phoneNumber, interests, score):
        self.voted = False
        #list of closed groups that the vip needs to score
        self.exEvals = []
        super().__init__(username, password, first_name, last_name, email, phoneNumber, interests, score)

    #group score method
    def groupScore(self):
        #

    #overloaded initial score method for vip user
    def initialScore(self):
        #

    #vote SU method called on vote button clicked
    #accepts the username of voted person
    def voteDSU(self, username):
        if self.voted == False:
            #add the name to list of votes
            system.voted_SU.append[]
            system.DSU_vote_count += 1
            self.voted = True
        #check if number of votes equals number of VIPs
        if system.DSU_vote_count == system.VIP_count:
            #find most voted vip
            newSU = findDSU
            if newSU != None:
                system.promote(newSU)

    #helper method for voteDSU, finds most voted for user
    #only returns if no ties
    def findDSU(self):
        #find and return most frequent user in system.voted_SU

    




class SU(VIP):

    def __init__(self, username, password, first_name, last_name, email, phoneNumber, interests, score):
	    self.voted = True
	    super().__init__(username, password, first_name, last_name, email, phoneNumber, interests, score)

    #assign vip method called on assign click
    #takes groupname and vip username from text fields
    def assignVIP(self, groupname, vipUsername):
        targetUser = system.search_by_username(vipUsername)
        targetGroup = system.search_by_group(groupname)
        targetUser.exEvals.append(targetGroup)

    #wip