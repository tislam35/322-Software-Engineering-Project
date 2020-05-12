#methods are static for testing, change if required
#try except not yet added

class OU(object):

    def __init__(self, username, password, first_name, last_name, email, phoneNumber, interests):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phoneNumber = phoneNumber
        self.interests = interests
        self.score = 0
        self.languages = ""
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
        self.first_login = True
        self.referenceInfo = None
        self.first_time_logging_in = False

	# #gets called on compliment button click
    # @staticmethod
    # def compliment(username, message):
    #     targetUser = system.find_user_by_username()
    #     targetUser.complimentsCount += 1
    #     if targetUser.complimentsCount > 2:
    #         system.promote(targetUser)
    #         #maybe display a message saying they were promoted
    #     #add targetUser and message to system.compliments
    #     system.compliments.append([targetUser, message])
    #
    # #gets called on complaint button click
    # @staticmethod
    # def complaint(username, message):
    #     targetUser = system.find_user_by_username()
    #     system.complaints.append([targetUser, message])
    #
    # #ou version of initial score
    # #refer to initialScore method to use this
    # @staticmethod
    # def initScore(username, score):
    #     if(score > 10 or score < 0):
    #         return -1
    #     targetUser = system.find_user_by_username()
    #     targetUser.score = score
    #     return 0
    #
    # #initial score method, obtains parameters from gui
    # #while this function returns -1 display "invalid score"
    # @staticmethod
    # def initialScore(cls, username, score):
    #     return cls.initScore(username, score)
    #
    # #invite method called on inviting a user
    # #a return of 0 means user was successfully invited to the group
    # #a return of 1 means current user is in invitee's BB, display automessage
    # @staticmethod
    # def invite(username, groupname, message):
    #     #check if current user is in white box
    #     targetUser = system.find_user_by_username(username)
    #     targetGroup = system.find_group(groupname)
    #     for i in targetUser.whiteBox:
    #         if system.cur_user.id == i.id:
    #             #inviting user is in invitee's whitebox
    #             targetGroup.members.append(targetUser)
    #             targetUser.affiliatedGroups.append(targetGroup)
    #             return 0
    #     for i in targetUser.blackBox:
    #         if system.cur_user.id == i.id:
    #             #inviting user is in invitee's blackbox
    #             #display targetUser.autoMsg if any
    #             return 1
    #     #current user isnt in white or black box
    #     targetUser.invites.append()
    #     return 0



class VIP(OU):

    def __init__(self, username, password, first_name, last_name, email, phoneNumber, interests):
        self.voted = False
        #list of closed groups that the vip needs to score
        self.exEvals = []
        super().__init__(username, password, first_name, last_name, email, phoneNumber, interests)

    # #group score method, might need to change based on how we connect GUIs
    # @staticmethod
    # def groupScore(score, groupname):
    #     targetGroup = system.find_group(groupname)
    #     targetGroup.reputation = score
    #
    # #vip version of initial score
    # #refer to initialScore method to use this
    # @staticmethod
    # def initScore(username, score):
    #     if(score > 20 or score < 0):
    #         return -1
    #     targetUser = system.find_user_by_username()
    #     targetUser.score = score
    #     return 0
    #
    # #vote SU method called on vote button clicked
    # #accepts the username of voted person
    # def voteDSU(self, username):
    #     if self.voted == False:
    #         #add the name to list of votes
    #         if system.voted_DSU.has_key(username):
    #             system.voted_DSU[username] = system.voted_DSU[username] + 1
    #         else:
    #             system.voted_DSU[username] = 1
    #         system.DSU_vote_count += 1
    #         self.voted = True
    #     #check if number of votes equals number of VIPs
    #     if system.DSU_vote_count == system.VIP_count:
    #         #find most voted vip
    #         newSU = VIP.findDSU()
    #         if newSU != None:
    #             system.promote(newSU)
    #
    # #helper method for voteDSU, finds most voted for user
    # #doesnt handle ties
    # @staticmethod
    # def findDSU():
    #     #find and return most frequent user in system.voted_DSU
    #     max = 0
    #     newSU = None
    #     for i in system.voted_DSU:
    #         if system.voted_DSU[i] > max:
    #             max = system.voted_DSU[i]
    #             newSU = i
    #     return system.find_user_by_username()



class SU(VIP):

    def __init__(self, username, password, first_name, last_name, email, phoneNumber, interests):
	    self.voted = True
	    super().__init__(username, password, first_name, last_name, email, phoneNumber, interests)

   # #assign vip method called on assign click
# #takes groupname and vip username from text fields
# @staticmethod
# def assignVIP(groupname, vipUsername):
#     targetUser = system.find_user_by_username()
#     targetGroup = system.find_group(groupname)
#     targetUser.exEvals.append(targetGroup)
#
# #kick method called on kick click
# #make sure we close all windows and go back to starting home page UI
# @staticmethod
# def kick(username):
#     targetUser = system.find_user_by_username()
#     system.kicked_list.append(targetUser)
#     system.kicked_count += 1
#     system.current_user = None
#
# #shutdown group method
# @staticmethod
# def shutdownGroup(groupname):
#     targetGroup = system.find_group(groupname)
#     for i in targetGroup.members:
#         i.affiliatedGroups.remove(targetGroup)
#     system.group_list.remove(targetGroup)
#
# #approve registration method
# #new user is of type registered_visitor
# @staticmethod
# def approveRegist(newUser):
#     #create new username
#     name = None
#     for i in len(system.OU_list):
#         name = newUser.first_name + newUser.last_name + i
#         if system.find_user_by_username() is None:
#             break
#     #create new password
#     pswrd = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
#     #create new OU
#     newOU = OU(name, pswrd, newUser.first_name, newUser.last_name, newUser.email, newUser.phoneNumber, newUser.interests)
#     #add this user to reference user list of scores to be initialized
#     newUser.referenceUser.initialScoresNeeded.append(newOU)
#     #remove from registered visitor list and add to OU list
#     system.registered_visitor_list.remove(newUser)
#     system.OU_list.append(newOU)
#     system.OU_count += 1
#     #email the new user
#
# #reject registration method
# #new user is of type registered_visitor
# @staticmethod
# def rejectRegist(registUser):
#     if registUser.rejected == False:
#         registUser.rejected = True
#         #email visitor of rejection
#     #visitor was already rejected once
#     else:
#         system.blacklist.append(registUser)
#         system.blacklist_count += 1
