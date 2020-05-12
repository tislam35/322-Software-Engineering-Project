import system

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
        user = system.find_user_by_username()
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

    def increase_reputation(self, amount):
        self.reputation += amount

    def decrease_reputation(self, amount):
        self.reputation -= amount

    def set_visibiliety(self, val):
        if((val != True) or (val != False)):
            return "Invalid Parameter"
        else:
            self.visable = val
    
    def vote_kick(self, username, amount):
        if(username in self.members):
            print("Vote to kick: " + str(username)) #or setting the text in the gui
            print("y/n?")                           #gui button for yes/no? for each user
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
                    #score change for kicked user needs to be added
                    #check for negative score and blacklist
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
                    #score change will be added
                    #check for VIP promotion
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
                    #warning will increased to user
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
                    exit_evaluation
                    
    def meeting_poll(self, time):
        print("Vote for a meeting at " + str(time))
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
                    print("Equal number of votes, meeting not set.")
                elif(counter < 0):
                    print("Meeting time is not convenient to majority")
                else:
                    print("Meeting is set to " + str(time))
            

    #def exit_evaluation(self):

    def close_group(self):
        set_visibiliety(False)
        exit_evaluation()
        self.members.clear()

    
