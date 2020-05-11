# SYSTEM MODULE

# import statments
from users import *

# SYSTEM CLASS
from users import OU, VIP


class system:

    # SYSTEM CLASS VARIABLES

    current_user = None
    FSU = None              # founding super user
    DSU = None              # democratic super user
    OU_count = None
    OU_list = []
    VIP_count = None
    VIP_list = []
    blacklist_count = None
    blacklist = []
    group_count = None
    group_list = []
    taboo_list = []
    registered_visitor_list = []
    rejected_once_visitor_list = []
    complaints = []
    compliments = []
    #added variables for voting
    DSU_vote_count = 0
    voted_DSU = {}
    #added a kicked list
    kicked_count = None
    kicked_list = []

    # SYSTEM CLASS METHODS

    # 1 find OU by username
    # INPUT: OU/VIP username. OUTPUT: OU object ELSE None
    def find_user_by_username(self, username):
        for user in system.OU_list:
            if user.username == username:
                return user
        for user in system.VIP_list:
            if user.username == user:
                return user
        return None                                     # EXCEPTIONAL CASE: not found

    # 2 adds approved visitor to OU list
    # INPUT: registered_visitor object
    def add_visitor_to_OU(self, username):
        visitor = None
        for registered_visitor in system.registered_visitor_list:
            if registered_visitor.username == username:
                visitor = registered_visitor
                break
        if visitor == None:
            for rejected_once_visitor in system.rejected_once_visitor_list:
                if rejected_once_visitor.username == username:
                    visitor = rejected_once_visitor
                    break
        if visitor == None:
            print("error: METHOD: # 2 add_visitor_to_OU: visitor not found")
            return
        new_OU = OU(visitor.username, visitor.password, visitor.first_name, visitor.last_name, visitor.email, visitor.phone_number, visitor.interests, visitor.score)
        system.OU_list.append(new_OU)
        system.OU_count += 1
        system.update_user_rankings(system.OU_list[system.OU_count - 1])

    # 3 changes the the reputation score of OU
    # INPUT: OU/VIP username. PROCESS: update rankings after
    def update_user_score(self, username, amount):
        user = system.find_user_by_username(username)
        if user == None:
            print("error: METHOD: # 3 update_OU_score: no user found")
            return
        user.score += amount
        system.update_user_status(user)

    # 4 update user status
    # INPUT: OU/VIP object
    def update_user_status(self, username):
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
                new_VIP = VIP(user.username, user.password, user.first_name, user.last_Name, user.email,
                              user.phoneNumber, user.interests, user.score)
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
                new_OU = OU(user.username, user.password, user.first_name, user.last_Name, user.email,
                              user.phoneNumber, user.interests, user.score)
                system.OU_list.append(new_OU)
                system.OU_count += 1
                del system.VIP_list[index]
                system.VIP_count -= 1
                system.update_user_ranking(system.OU_list[system.OU_count])
            return
        print("error 04: METHOD: # 4 update_user_status: no user found")


    # 5 sorts OU list or VIP list
    # INPUT: OU/VIP object
    def update_user_ranking(self, user):
        index = None
        if isinstance(user, OU):
            try:
                index = system.OU_list.index(user)
            except:
                print("error 01: METHOD: # 5 update_user_ranking: no user found")
            if system.OU_list[index].score > system.OU_list[index - 1].score and index != 0:
                i = index
                while system.OU_list[i].score > system.OU_list[i - 1].score and i != 0:
                    system.OU_list[i], system.OU_list[i - 1] = system.OU_list[i - 1], system.OU_list[i]
                    i -= 1
            if system.OU_list[index].score < system.OU_list[index + 1].score and index != system.OU_count - 1:
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
        user = system.find_user_by_username(username)
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
        return -1                                               # EXCEPTIONAL CASE

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