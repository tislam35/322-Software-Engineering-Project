import system
import users

class Group(object):

    __numOfGroups = 0

    def __init__(self, groupName):
        Group.__numOfGroups += 1
        self.groupID = Group.__numOfGroups
        self.groupName = groupName
        self.members = []
        self.meetings = []
        self.meeting_polls=[]
        # member_stat = (memberUsername, missed meeting count, warning count, praise count, commit count)
        self.member_stat = []
        self.meet_poll = None
        self.warn_poll = None
        self.praise_poll = None
        self.remove_member_poll = None
        self.started_close_group=False
        self.close_group_votes = 0
        self.reputation = 0
        self.assigned_vip = ""


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
        return len(self.members) - 1

    def update_reputation(self, amount):
        self.reputation += amount
            
    def assign_vip(self,vip):
        self.assigned_vip = vip
    
    def vote_kick(self, username):
        if(username in self.members):
            print("Vote to kick: " + str(username)) 
            print("y/n?")                           
            counter = 0
            neutral = []
            for member in self.members:
                vote = input()
                if(vote == 'y'):
                    counter += 1
                elif(vote == 'n'):
                    counter -= 1
                else:
                    neutral.append(member)

            if(neutral == True):
                return "Vote is cancelled not everyone voted"
            else:
                if(counter == 0):
                    print("Tie, no decision made")
                elif(counter > 0):
                    print(str(member + " stays"))
                else:
                    remove_member(member)
                    print(str(member) + " has been kicked")
                    system.update_user_score(username, -10)
        else:
            print("Member Not Found")
            
    def vote_praise(self, username, amount):
        if(username in self.members):
            print("Vote to praise: " + str(username))
            print("y/n?")
            counter = 0
            neutral =[]
            for member in self.members:
                vote = input()
                if(vote == 'y'):
                    counter += 1
                elif(vote == 'n'):
                    counter -= 1
                else:
                    neutral.append(member)

            if(neutral == True):
                return "Vote is cancelled not everyone voted"   
            else:     
                if(counter == 0):
                    print("Equal number of votes, No change")
                elif(counter > 0):
                    print(str(username + " complemented"))
                else:
                    print(str(username) + " not complemented")
                    system.update_user_score(username, amount)
        else:
            print("Member Not Found")
    
    def vote_warning(self, username):
        if(username in self.members):
            print("Vote for a Warning: " + str(username))
            print("y/n?")
            counter = 0
            neutral =[]
            for member in self.members:
                vote = input()
                if(vote == 'y'):
                    counter += 1
                elif(vote == 'n'):
                    counter -= 1
                else:
                    neutral.append(member)

            if(neutral == True):
                return "Vote is cancelled not everyone voted"   
            else:     
                if(counter == 0):
                    print("Equal number of votes, No change")
                elif(counter > 0):
                    print(str(username + " got a warning"))
                    user = system.find_user_by_username(username)
                    user.warningCounts += 1
                    if(user.warningCounts >= 3):
                        self.remove_member(username)
                else:
                    print(str(username) + " will not have any warnings")
        else:
            print("Member Not Found")

    def vote_close(self):
        print("Vote to close the group")
        print("y/n?")
        counter = 0
        neutral =[]
        for member in self.members:
            
            vote = input()
            
            if(vote == 'y'):
                counter += 1
            elif(vote == 'n'):
                counter -= 1
            else:
                neutral.append(member)

        if(neutral == True):
             return "Vote is cancelled, not everyone voted."   
        else:     
             if(counter == 0):
                print("Equal number of votes, Group is not closing.")
             elif(counter < 0):
                print("Group stays open")
             else:
                print("Group is closing")
                #self.exit_evaluation
                    


    def response_meeting_poll(self.time):
        # print("Vote for a meeting at " + str(time))
        # print("y/n?")
        counter = 0
        neutral =[]
        for member in self.members:
            vote = input()
            if(vote == 'y'):
                counter += 1
            elif(vote == 'n'):
                counter -= 1
            else:
                neutral.append(member)

        if(neutral == True):
            return "Vote is cancelled, not everyone voted."   
        else:     
            if(counter == 0):
                print("Equal number of votes, meeting not set.")
            elif(counter < 0):
                print("Meeting time is not convenient to majority")
            else:
                print("Meeting is set to " + str(time))
                self.meetings.append(time)
            

    #def exit_evaluation(self):

    #def close_group(self):
    #    self.set_visibiliety(False)
    #    self.exit_evaluation()
    #    self.members.clear()

    
