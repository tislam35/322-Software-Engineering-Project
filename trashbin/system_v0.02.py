from users import *
#datetime library is needed for current time and date
#from datetime import datetime

class system:

    # NOTE: user_taboo_list will be in the OU class
    # NOTE: We might not do online_users or current_time  **added time system is created and current time function
    #but can be removed if there is no use**

    # variables
    curret_user = None
    founder_SU = None
    democratic_SU = None
    OU_count = 0
    OU_list = []
    VIP_count = 0
    VIP_list = []
    registered_users_count = 0
    registered_users = []
    blacklist_count = 0
    blacklist = []
    group_count = 0
    group_list = []
    taboo_list = []
    rejected_visitor_list = []
    rejected_visitor_twice_list = []
    complaints = []
    compliments = []
    #time_created = datetime.now()                  #time system has been instantiated


    #0 find OU by email. RETURN OU id
    def find_OU_by_info(self, first_name, last_name, email):
        for i in range(system.OU_count):
            if system.OU_list[i].email == email:
                if system.OU_list.first_name == first_name:
                    if system.OU_list.last_name == last_name:
                        return i
        return None

    #0b find OU by useranem. RETURN OU object ELSE RETURN None if not found
    def search_by_username(self, username):
        for i in range(system.registered_users_count):
            if system.registered_users[i].username == username:
                return system.registered_users[i]
        return None


    #1 adds approved visitor to OU list
    def add_new_OU(self, approved_visitor):
        system.OU_list.append(approved_visitor)
        system.VIP_count += 1

    #3 changes/updates the reputation of an OU
    def update_score_OU(self, OU_id, amount):
        OU_index = system.check_OU_id(OU_id)
        if OU_index == None:                           #*** EXCEPTIONAL CASE: invalid OU id    ***
           print("error")
           return
        system.OU_list[OU_index].score -= amount
        system.update_OU_status(OU_id)

    #3a checks if OU_id is valid. RETURN: index of OU in OU_list or None
    def check_OU_id(self, OU_id):
        OU = None
        for i in range(system.OU_count):
            if system.OU_list[i].id == OU_id:
                return i
        return None                                   #*** EXCEPTIONAL CASE: OU id not found. RETURNS None


    #3b updates OU status. This is called everything time OU score changes.
    def update_OU_status(self, OU_id):
        OU_index = system.check_OU_id(OU_id)
        if OU_index == None:                            #*** EXCEPTIONAL CASE: invalid OU id    ***
            print("error")
            return
        if system.OU_list[OU_index].score < 0:
            system.blacklist_user(OU_id)
        elif system.OU_list[OU_index].score > 30 and isinstance(system.OU_list[OU_index], OU):
            new_VIP = VIP(system.OU_list[OU_index].id, system.OU_list[OU_index].)
            system.VIP_list.append(new_VIP)
            del system.OU_list[OU_index]
        elif system.OU_list[OU_index].score < 25 and isinstance(system.OU_list[OU_index], VIP):

        # else:
        #     update_ranking()

    #4 puts OU into blacklist (and also removes them from OU_list and registered_list)
    def blacklist_user(self, OU_id):
        OU_index = system.check_OU_id(OU_id)
        if OU_index == None:                            #*** EXCEPTIONAL CASE: OU id not found. RETURNS None
            print("error")
            return
        system.OU_list[OU_index].score = -1
        new_blacklist_user = system.OU_list[OU_index]
        system.blacklist.append(new_blacklist_user)
        system.blacklist_count += 1
        del system.OU_list[OU_index]
        system.OU_count -= 1

    #9 checks to validate user when login, RETURN index if valid ELSE None
    def login(self, username, password):
        print("SYSTEM: method 9")
        for i in range(system.OU_count):
            if system.OU_list[i].username == username and system.OU_list[i].password == password:
                return i
            else:
                return None

    #7 updates the sorted list to be sorted (after score changes or add new user)
    def update_rankings(self, OU_id):
        OU_index = system.check_OU_id(OU_id)
        if OU_index == None:                            #*** EXCEPTIONAL CASE: OU id not found. RETURN None.
            print("error")
            return
        if system.OU_list[OU_index].score < 0:
            system.blacklist_user(system, OU_id)
        elif OU_index == system.OU_count - 1:
            while system.OU_list[OU_index].score > system.OU_list[OU_index - 1].score and OU_index != 0:
                system.OU_list[OU_index], system.OU_list[OU_index -1] = system.OU_list[OU_index -1], system.OU_list[OU_index]
                OU_index -= 1
        elif system.OU_list[OU_index].score > system.OU_list[OU_index + 1].score:
            while system.OU_list[OU_index].score > system.OU_list[OU_index - 1].score and OU_index != 0:
                system.OU_list[OU_index], system.OU_list[OU_index - 1] = system.OU_list[OU_index - 1], system.OU_list[OU_index]
                OU_index -= 1
        elif system.OU_list[OU_index].score < system.OU_list[OU_index + 1].score:
            while system.OU_list[OU_index].score < system.OU_list[OU_index + 1].score:
                system.OU_list[OU_index], system.OU_list[OU_index + 1] = system.OU_list[OU_index + 1], system.OU_list[OU_index]
                OU_index += 1


    #8 updates the sorted list to be sorted (after score change or add new group)
    def update_group_ranking(self, group_id):
        group_index = system.group_count - 1
        while system.group_list[group_index] > system.group_list[group_index - 1] and group_index != 0:
            system.group_list[group_index], system.group_list[group_index - 1] = system.group_list[group_index -1], system.group_lsit[group_index]
        return

    def check_group_id(self, group_id):
        #group = None
        if(group_id in system.group_list):                  #returns true if group_id exist in group_list
            for i in system.group_list:
                if system.group_list[i] == group_id:
                    return i
        else:                                               #if not returns false
            return None                                     #*** Exceptional Cases: Group id not found

    #12 return top 3 user and groups. RETURNS 2-D array
    def top_3(self):
        arr_top_3 = [None] * 2
        for i in range(3):
            arr_top_3[0].append(system.OU_list[i])
            arr_top_3[1].append(system.group_list[i])
        return arr_top_3

    # def current_time():                                    #returns current time in the format YYYY-MM-YY HH:MM:SS.MS
    #     return datetime.now()
