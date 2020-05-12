# SYSTEM MODULE

# import statments
import users
from users import *

# SYSTEM CLASS
from registered_visitor import *


class system:

    # SYSTEM CLASS VARIABLES

    current_user = None
    FSU = None              # founding super user
    DSU = None              # democratic super user
    OU_count = 0
    OU_list = []
    VIP_count = 0
    VIP_list = []
    blacklist_count = 0
    blacklist = []
    group_count = 0
    group_list = []
    taboo_list = ["shit", "fuck"]
    registered_visitor_list = []
    complaints = []
    compliments = []
    appeals = []
    #added variables for voting
    DSU_vote_count = 0
    voted_DSU = {}
    #added a kicked list
    kicked_count = 0
    kicked_list = []

    # SYSTEM CLASS METHODS

    # 1 find OU by username
    # INPUT: OU/VIP username. OUTPUT: OU object ELSE None
    @staticmethod
    def find_user_by_username(username):
        for user in system.OU_list:
            if user.username == username:
                return user
        for user in system.VIP_list:
            if user.username == username:
                return user
        return None                                     # EXCEPTIONAL CASE: not found

    # 2 adds approved visitor to OU list
    # INPUT: registered_visitor object
    @staticmethod
    def add_visitor_to_OU(email):
        for registered_visitor in system.registered_visitor_list:
            if registered_visitor.email == email:
                visitor = registered_visitor
                # get the reference score form OU
                # create OU object and insert into OU_list
                username = str(visitor.first_name) + str(visitor.last_name) + str(1)
                password = str(visitor.first_name) + str(visitor.last_name)
                print("given username: " + str(username))
                print("given password: " + str(password))
                new_OU = users.OU(username, password, visitor.first_name, visitor.last_name,
                                  visitor.email, visitor.phone_number, visitor.interests)
                new_OU.score = visitor.score
                new_OU.first_time_logging_in = True
                system.OU_list.append(new_OU)
                system.OU_count += 1
                system.update_user_ranking(system.OU_list[system.OU_count - 1])
                # delete registered visitor from list
                system.registered_visitor_list.remove(registered_visitor)
                return True
        print("error: METHOD: # 2 add_visitor_to_OU: visitor not found")
        return False


    # 3 changes the the reputation score of OU
    # INPUT: OU/VIP username. PROCESS: update rankings after
    @staticmethod
    def update_user_score(username, amount):
        user = system.find_user_by_username(username)
        if user == None:
            print("error: METHOD: # 3 update_OU_score: no user found")
            return
        user.score += amount
        system.update_user_status(username)

    # 4 update user status
    # INPUT: OU/VIP object
    @staticmethod
    def update_user_status(username):
        user = system.find_user_by_username(username)
        if user == None:
            print("error 01: METHOD: # 4 update_user_status: no user found")
            return
        if isinstance(user, OU):
            index = None
            try:
                index = system.OU_list.index(user)
            except:
                print("error 02: METHOD: # 4 update_user_status: no user found")
                return
            if user.score < 0:
                system.blacklist.append(user)
                system.blacklist_count += 1
                del system.OU_list[index]
                system.OU_count -= 1
                return
            if user.score > 30:
                new_VIP = VIP(user.username, user.password, user.first_name, user.last_name, user.email,
                              user.phoneNumber, user.interests)
                new_VIP.score = user.score
                system.VIP_list.append(new_VIP)
                system.VIP_count += 1
                del system.OU_list[index]
                system.OU_count -= 1
                system.update_user_ranking(system.VIP_list[system.VIP_count])
            return
        elif isinstance(user, VIP):
            index = None
            try:
                index = system.VIP_list.index(user)
            except:
                print("error 03: METHOD: # 4 update_user_status: no user found")
            if user.score < 0:
                system.blacklist.append(user)
                system.blacklist_count += 1
                del system.VIP_list[index]
                system.VIP_count -= 1
                return
            if user.score < 25:
                new_OU = OU(user.username, user.password, user.first_name, user.last_name, user.email,
                                  user.phoneNumber, user.interests)
                new_OU = user.score
                system.OU_list.append(new_OU)
                system.OU_count += 1
                del system.VIP_list[index]
                system.VIP_count -= 1
                system.update_user_ranking(system.OU_list[system.OU_count])
            return
        print("error 04: METHOD: # 4 update_user_status: no user found")


    # 5 sorts OU list or VIP list
    # INPUT: OU/VIP object
    @staticmethod
    def update_user_ranking(user):
        index = None
        if isinstance(user, users.OU):
            try:
                index = system.OU_list.index(user)
            except:
                print("error 01: METHOD: # 5 update_user_ranking: no user found")
            if index != 0 and system.OU_list[index].score > system.OU_list[index - 1].score:
                i = index
                while system.OU_list[i].score > system.OU_list[i - 1].score and i != 0:
                    system.OU_list[i], system.OU_list[i - 1] = system.OU_list[i - 1], system.OU_list[i]
                    i -= 1
            if index != system.OU_count - 1 and system.OU_list[index].score < system.OU_list[index + 1].score:
                i = index
                while system.OU_list[i].score < system.OU_list[i + 1].score and i != system.OU_count - 1:
                    system.OU_list[i], system.OU_list[i + 1] = system.OU_list[i + 1], system.OU_list[i]
                    i += 1
            return
        elif isinstance(user, VIP):
            try:
                index = system.OU_list.index(user)
            except:
                print("error 02: METHOD: # 5 update_user_ranking: no user found")
            if system.VIP_list[index].score > system.VIP_list[index - 1].score and index != 0:
                i = index
                while system.VIP_list[i].score > system.VIP_list[i - 1].score and i != 0:
                    system.VIP_list[i], system.VIP_list[i - 1] = system.VIP_list[i - 1], system.VIP_list[i]
                    i -= 1
            elif system.VIP_list[index].score < system.VIP_list[index + 1].score and index != system.VIP_count - 1:
                i = index
                while system.VIP_list[i].score < system.VIP_list[i + 1].score and i != system.VIP_count - 1:
                    system.VIP_list[i], system.VIP_list[i + 1] = system.VIP_list[i + 1], system.VIP_list[i]
                    i += 1
                return
        print("error 03: METHOD: # 5 update_user_rankings: user not OU or VIP")

    # 6 put OU/VIP into blacklist (and removes them form OU/VIP list)
    # INPUT: OU/VIP username
    def blacklist_user(self, username):
        user = system.find_user_by_username()
        if user == None:
            print("error: METHOD: # 9: blacklist_user: no user found")
        if isinstance(user, OU):
            index = None
            try:
                index = system.OU_list.index(user)
            except:
                print("error 02: METHOD: # 4 update_user_status: no user found")
                return
            system.blacklist.append(user)
            system.blacklist_count += 1
            del system.OU_list[index]
            system.OU_count -= 1
            return
        elif isinstance(user, VIP):
            index = None
            try:
                index = system.VIP_list.index(user)
            except:
                print("error 03: METHOD: # 4 update_user_status: no user found")
                return
            system.blacklist.append(user)
            system.blacklist_count += 1
            del system.VIP_list[index]
            system.VIP_count -= 1
            return
        print("error 04: METHOD: #9 blacklist_user: end of fucntion")


    # 7 vaidates login
    # INPUT: OU/VIP username and password. OUTPUT: index ELSE None. PROCESS: records current user
    def login(self, username, password):
        for user in system.OU_list:
            if user.username == username and user.password == password:
                system.current_user = user
                return system.OU_list.index(user)
        for user in system.VIP_list:
            if user.username == username and user.password == password:
                system.current_user = user
                return system.VIP_list.index(user)
        return None                                               # EXCEPTIONAL CASE

    # 8 returns maximum of  3 user and groups
    # OUTPUT: 2-D array
    def top_3(self):
        arr_top_3 = [None] * 2
        J = 0
        for i in range(3):
            try:
                arr_top_3[0].append(system.VIP_list[i])
            except:
                try:
                    arr_top_3[0].append(system.OU_list[i - J])
                except:
                    print("Less then 3 top probiles (OU)")
                print("Less then 3 top profiles(VIP)")
            try:
                arr_top_3[1].append(system.group_list[i])
            except:
                print("Less then 3 top gropus")
            J += 1
        return arr_top_3

    # 9 check group by group name
    # INPUT: group name. OUTPUT: group object
    def find_group(self, group_name):
        for i in range(system.group_count):
            if system.group_list[i].name == group_name:
                return system.group_list[i]
        return None

    # 10 update group rankings
    # INPUT: group name PROCESS: sort
    def update_group_rankings(self, group_name):
        group = system.find_group(group_name)
        index = None
        try:
            index = system.group_list.index(group)
        except:
            print("error: METHOD: #10: update_group_rankings: group not found")
        system.group_list.sort(key=lambda x: x.score, reverse = True)

    # 11 register registered visitor
    # INPUT: registertion info PROCESS: check and then add info to register_visitor OUTPUT: True if successful ELSE False if same email found
    @staticmethod
    def register(first_name, last_name, email, phone_number, interests, reference_username):
        all_recored_users = system.OU_list + system.VIP_list + system.blacklist + system.kicked_list + system.registered_visitor_list
        for user in all_recored_users:
            if email == user.email:
                print("error: METHOD: # 11: email already in system")
                return False
        valid_user = system.OU_list + system.VIP_list
        for user in valid_user:
            if user.username == reference_username:
                if user.referenceInfo[0] == email:
                    new_registered_visitor = registered_visitor(first_name, last_name, email, phone_number, interests,
                                                                user.referenceInfo[1])
                    system.registered_visitor_list.append(new_registered_visitor)
                    print("visitor registered as registered visitor")
                    return True
                print("your reference did not reference you")
                return False
        print("refernce username was not valid")
        return False

    # 12 reject a registered visitor
    @staticmethod
    def reject_registered_visitor(r_visitor):
        if r_visitor.rejected == False:
            r_visitor.rejected = True
        else:
            r_visitor.rejected_twice = True
            system.registered_visitor_list.remove(r_visitor)
            system.blacklist.append(r_visitor)
            system.blacklist_count += 1

    # 13 visitor appeal if rejected
    # INPUT: reject visitor's email that s/he registered with and the appeal message
    @staticmethod
    def appeal(r_visitor_email, message):
        for registered_visitor in system.registered_visitor_list:
            if r_visitor_email == registered_visitor.email:
                registered_visitor.appealed = True
                system.appeals.append((registered_visitor.email, message))
                return True
        return False                            # EXCEPTIONAL CASE: no email found in list

    # 14 SU approved visitor
    @staticmethod
    def approve(r_visitor_email):
        for registered_visitor in system.registered_visitor_list:
            if r_visitor_email == registered_visitor:
                system.add_visitor_to_OU(registered_visitor.email)
                return True
        return False


