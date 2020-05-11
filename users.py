from system import system

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
        #if the list below isnt empty we should display the initial
        #score dialog on user login for each user in the list
        self.initialScoresNeeded = []
        self.complimentsCount = 0
        self.complaintsCount = 0
        #setting automessage will be done in the ui file
        self.autoMsg = ""

	#gets called on compliment button click
    def compliment(self, username, message):
        targetUser = system.find_user_by_username(username)
        targetUser.complimentsCount += 1
        if targetUser.complimentsCount > 2:
            system.promote(targetUser)
            #maybe display a message saying they were promoted
        #add targetUser and message to system.compliments
        system.compliments.append([targetUser, message])

    #gets called on complaint button click
    def complaint(self, username, message):
        targetUser = system.find_user_by_username(username)
        system.complaints.append([targetUser, message])

    #initial score method, obtains parameters from gui
    #while this function returns -1 display "invalid score"
    def initialScore(self, username, score):
        if(score > 10 or score < 0):
            return -1
        targetUser = system.find_user_by_username(username)
        targetUser.score = score
        return 0

    #invite method called on inviting a user
    #a return of 0 means user was successfully invited to the group
    #a return of 1 means current user is in invitee's BB, display automessage
    def invite(self, username, groupname, message):
        #check if current user is in white box
        targetUser = system.find_user_by_username(username)
        targetGroup = system.find_group(groupname)
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
        return 0


    
class VIP(OU):

    def __init__(self, username, password, first_name, last_name, email, phoneNumber, interests, score):
        self.voted = False
        #list of closed groups that the vip needs to score
        self.exEvals = []
        super().__init__(username, password, first_name, last_name, email, phoneNumber, interests, score)

    #group score method, might need to change based on how we connect GUIs
    def groupScore(self, score, groupname):
        targetGroup = system.find_group(groupname)
        targetGroup.reputation = score

    #overloaded initial score method for vip user
    def initialScore(self, username, score):
        if(score > 20 or score < 0):
            return -1
        targetUser = system.find_user_by_username(username)
        targetUser.score = score
        return 0

    #vote SU method called on vote button clicked
    #accepts the username of voted person
    def voteDSU(self, username):
        if self.voted == False:
            #add the name to list of votes
            if system.voted_DSU.has_key(username):
                system.voted_DSU[username] = system.voted_DSU[username] + 1
            else:
                system.voted_DSU[username] = 1
            system.DSU_vote_count += 1
            self.voted = True
        #check if number of votes equals number of VIPs
        if system.DSU_vote_count == system.VIP_count:
            #find most voted vip
            newSU = VIP.findDSU
            if newSU != None:
                system.promote(newSU)

    #helper method for voteDSU, finds most voted for user
    #doesnt handle ties
    def findDSU(self):
        #find and return most frequent user in system.voted_DSU
        max = 0
        newSU = None
        for i in system.voted_DSU:
            if system.voted_DSU[i] > max:
                max = system.voted_DSU[i]
                newSU = i
        return system.find_user_by_username(newSU)

    




class SU(VIP):

    def __init__(self, username, password, first_name, last_name, email, phoneNumber, interests, score):
	    self.voted = True
	    super().__init__(username, password, first_name, last_name, email, phoneNumber, interests, score)

    #assign vip method called on assign click
    #takes groupname and vip username from text fields
    def assignVIP(self, groupname, vipUsername):
        targetUser = system.find_user_by_username(vipUsername)
        targetGroup = system.find_group(groupname)
        targetUser.exEvals.append(targetGroup)

    #wip