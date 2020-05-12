# SYSTEM MODULE

# import statments
import users
from users import *

# SYSTEM CLASS
from registered_visitor import *


class system:

    # SYSTEM CLASS VARIABLES

    current_user = None
    current_user_groups = []
    FSU = None
    DSU = None              # democratic super user
    OU_count = 0
    OU_list = []
    VIP_count = 0
    VIP_list = []
    blacklist_count = 0
    blacklist = []
    group_count = 0
    group_list = []
    closed_group_list = []
    taboo_list = ["shit", "fuck"]
    registered_visitor_list = []
    complaints = []
    complaints_group = []
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
                system.update_user_ranking(system.VIP_list[system.VIP_count - 1])
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
        if isinstance(user, VIP):
            try:
                index = system.OU_list.index(user)
            except:
                print("error 02: METHOD: # 5 update_user_ranking: no user found")
                return False
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
        elif isinstance(user, users.OU):
            try:
                index = system.OU_list.index(user)
            except:
                print("error 01: METHOD: # 5 update_user_ranking: no user found")
                return False
            # for i in range(system.OU_count):
            #     if user.username == system.OU_list[i].username:
            #         index = i
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
        print("error 03: METHOD: # 5 update_user_rankings: user not OU or VIP")

    # 6 put OU/VIP into blacklist (and removes them form OU/VIP list)
    # INPUT: OU/VIP username
    @staticmethod
    def blacklist_user(username):
        user = system.find_user_by_username(username)
        if user == None:
            print("error: METHOD: # 9: blacklist_user: no user found")
        if isinstance(user, VIP):
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
        elif isinstance(user, OU):
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
        print("error 04: METHOD: #9 blacklist_user: end of fucntion")


    # 7 vaidates login
    # INPUT: OU/VIP username and password. OUTPUT: index ELSE None. PROCESS: records current user
    @staticmethod
    def login(username, password):
        print("logintest1")
        for user in system.OU_list:
            print("logintest2")
            if user.username == username and user.password == password:
                system.current_user = user
                # return system.OU_list.index(user)
                return True
        for user in system.VIP_list:
            print("logintest3")
            if user.username == username and user.password == password:
                system.current_user = user
                # return system.VIP_list.index(user)
                return True
        print("logintest4")
        return False                                               # EXCEPTIONAL CASE

    # 8 returns maximum of  3 user and groups
    # OUTPUT: 2-D array
    @staticmethod
    def top_3():
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
    @staticmethod
    def find_group(group_id):
        for i in range(system.group_count):
            if system.group_list[i].groupID == group_id:
                return system.group_list[i]
        return None

    # 10 update group rankings
    # INPUT: group name PROCESS: sort
    @staticmethod
    def update_group_rankings(group_name):
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
        if system.FSU.username == reference_username:
            if system.FSU.referenceInfo[0] == email:
                new_registered_visitor = registered_visitor(first_name, last_name, email, phone_number, interests,
                                                            system.FSU.referenceInfo[1])
                system.registered_visitor_list.append(new_registered_visitor)
                system.FSU.referenceInfo = None
                print("visitor registered as registered visitor by FSU reference")
                return True
            print("your FSU reference did not reference you")
            return False
        if system.DSU != None and system.DSU.username == reference_username:
            if system.DSU.referenceInfo[0] == email:
                new_registered_visitor = registered_visitor(first_name, last_name, email, phone_number, interests,
                                                            system.DSU.referenceInfo[1])
                system.registered_visitor_list.append(new_registered_visitor)
                system.DSU.referenceInfo = None
                print("visitor registered as registered visitor by DSU reference")
                return True
            print("your DSU reference did not reference you")
            return False
        for user in valid_user:
            if user.username == reference_username:
                if user.referenceInfo[0] == email:
                    new_registered_visitor = registered_visitor(first_name, last_name, email, phone_number, interests,
                                                                user.referenceInfo[1])
                    system.registered_visitor_list.append(new_registered_visitor)
                    user.referenceInfo = None
                    print("visitor registered as registered visitor")
                    return True
                print("your reference did not reference you")
                return False
        print("reference username was not valid")
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
        for reg_visitor in system.registered_visitor_list:
            if r_visitor_email == reg_visitor.email:
                system.add_visitor_to_OU(reg_visitor.email)
                return True
        return False

    # 15 kick user
    # INPUT: OU/VIP username OUTPUT: True if successful, ELSE False
    @staticmethod
    def kick(username):
        target_user = system.find_user_by_username(username)
        if target_user == None:
            print("error: METHOD: kick: username not found in OU, VIP list")
            return False
        # remove from all groups
        for group in system.group_list:
            for member_username in group.members:
                if member_username == target_user.username:
                    group.members.remove(member_username)
        # take out form OU or VIP list and to kicked_list
        if isinstance(target_user, VIP):
            system.kicked_list.append(target_user)
            system.kicked_count += 1
            system.VIP_list.remove(target_user)
            system.VIP_list.count -= 1
            print("user successfully moved form VIP to kick")
            return True
        elif isinstance(target_user, OU):
            system.kicked_list.append(target_user)
            system.kicked_count += 1
            system.OU_list.remove(target_user)
            system.OU_list.count -= 1
            print("user successfully moved form OU to kick")
            return True

    # 16 assign target VIP to evaluate a target group
    # INPUT: target VIP username, target group id
    @staticmethod
    def assignVIP(username, group_id):
        target_VIP = system.find_user_by_username(username)
        if target_VIP == None:
            print("error: METHOD: assignVIP: no VIP with input username found")
            return False
        target_group = system.find_group(group_id)
        if target_group == None:
            print("error: METHOD: assignVIP: no group with input group id")
            return False
        if isinstance(target_VIP, VIP):
            target_VIP.exEvals.append(target_group.groupID)
            print("VIP successfully assigned to group")
            return True
        else:
            print("error: METHOD: assignVIP: assigned user must be VIP")
            return False

    # 17 shutdown group and kick out all members
    # INPUT: group_id
    @staticmethod
    def shutdown_and_kick_out(group_id):
        target_group = system.find_group(group_id)
        if target_group == None:
            print("error: METHOD: shutdown_and_kick_out: no group with input group id found")
            return False
        for member_username in target_group.members:
            target_member = system.find_user_by_username(member_username)
            if target_member == None:
                print("error: METHOD: shutdown_group_and_kick_out: no member found in list")
                return False
            system.kick(member_username)
        for complained_group in system.complaints_group:
            if target_group.groupID == complained_group[1]:
                system.complaints_group.remove(complained_group)
        system.group_list.remove(target_group)
        system.closed_group_list.append(target_group)
        return True

    # 18 shutdown group and reduce score for each
    @staticmethod
    def shutdown_and_reduce_score(group_id, amount):
        target_group = system.find_group(group_id)
        if target_group == None:
            print("error: METHOD: shutdown_and_kick_out: no group with input group id found")
            return False
        for member_username in target_group.members:
            target_member = system.find_user_by_username(member_username)
            if target_member == None:
                print("error: METHOD: shutdown_group_and_kick_out: no member found in list")
                return False
            system.update_user_score(member_username, amount)
        for complained_group in system.complaints_group:
            if target_group.groupID == complained_group[1]:
                system.complaints_group.remove(complained_group)
        system.group_list.remove(target_group)
        system.closed_group_list.append(target_group)
        return True

    # 19 assign score to evaluated group
    @staticmethod
    def score_group(group_id, score):
        target_group = system.find_group(group_id)
        if target_group == None:
            print("error: METHOD: score_group: no group with input group id found")
            return False
        for member_username in target_group.members:
            target_member = system.find_user_by_username(member_username)
            if target_member == None:
                print("error: METHOD: shutdown_group_and_kick_out: no member found in list")
                return False
            system.update_user_score(member_username, score)
        target_group.reputation = score

    # 20 compliment target user
    @staticmethod
    def compliment(target_username, message):
        target_user = system.find_user_by_username(target_username)
        if target_user == None:
            print("error: METHOD: copliment: no user with username found")
            return False
        system.complaints.append((target_username, message))
        target_user.complimentsCount += 1

    # 21 complaint target user
    @staticmethod
    def complain_user(target_username, message):
        target_user = system.find_user_by_username(target_username)
        if target_user == None:
            print("error: METHOD: # 21: complain_user: no user with input username found")
        system.complaints.append((target_username, message))
        target_user.complaintsCount += 1

    # 22 complaint target group
    @staticmethod
    def complain_group(target_group_id, message):
        target_group = system.find_group(target_group_id)
        if target_group == None:
            print("error: METHOD: #22: complain_group: no group with in group id found")
            return False
        system.complaints_group.append((target_group_id, message))

    # 23 invite group members
    @staticmethod
    def invite(invited_username, group_id):
        target_user = system.find_user_by_username(invited_username)
        if target_user == None:
            print("error: METHOD: #23: invite: no users with input user name found")
            return False
        target_group = system.find_group(group_id)
        if target_group == None:
            print("error: METHOD: #23:invite: no group with input groud id")
            return False
        for white_box_username in target_user.whiteBox:
            if system.current_user.username == white_box_username:
                target_group.members.append(target_user.username)
                print("current_user in invited's whitebox. Invited add to group")
                return True
        for black_box_username in target_user.blackBox:
            if system.current_user.username == black_box_username:
                print("current_user in invited's blackbox. Invited not sent.")
                print(target_user.autoMsg)
                return True
        target_user.invites.append((group_id, system.current_user.username))
        print("invite send to" + str(target_user.username))
        return True

    # 24 reject invite
    @staticmethod
    def reject_invite(group_id):
        target_group = system.find_group(group_id)
        if target_group ==  None:
            print("error: METHOD: reject_invite: group with input group id not found")
        for current_user_invite in system.current_user.invites:
            if target_group.groupID == current_user_invite[0]:
                system.current_user.invites.remove(current_user_invite)
                print("reject invite form group with id " + str(target_group.groupID))
                return True


# initial user: FSU

system.FSU = users.SU("FSU", "pass123", "Group", "S", "FSU@gmail.com", "718-123-567", "coding, teamwork")
system.FSU.score = 100
system.FSU.referenceInfo = ("kim.456@gmail.com", 20)