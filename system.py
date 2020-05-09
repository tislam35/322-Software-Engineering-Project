from users import *

class system:

    # NOTE: user_taboo_list will be in the OU class
    # NOTE: We might not do online_users or current_time

    # variables
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


    #1 adds approved visitor to OU list
    def add_new_OU(self, approved_visitor):
        self.OU_list.append(approved_visitor)
        system.VIP_count += 1

    #3 changes/updates the reputation of an OU
    def update_score_OU(self, OU_id, amount):
        OU_index = self.check_OU_id(OU_id)
        if OU_index == None:                           #*** EXCEPTIONAL CASE: invalid OU id    ***
           print("error")
           return
        self.OU_list[OU_index].score -= amount
        system.update_OU_status(OU_id)

    #3a checks if OU_id is valid. RETURN: index of OU in OU_list or None
    def check_OU_id(self, OU_id):
        OU = None
        for i in range(self.OU_count):
            if self.OU_list[i].id == OU_id:
                return i
        return None                                   #*** EXCEPTIONAL CASE: OU id not found. RETURNS None


    # #3b updates OU status. This is called everything time OU score changes.
    # def update_OU_status(self, OU_id):
    #     OU_index = self.check_OU_id(OU_id)
    #     if OU_index == None:                            #*** EXCEPTIONAL CASE: invalid OU id    ***
    #         print("error")
    #         return
    #     if self.OU_list[OU_index].score < 0:
    #         self.blacklist_user(OU_id)
    #     elif self.OU_list[OU_index].score > 30 and isinstance(self.OU_list[OU_index], OU):
    #         new_VIP = VIP(self.OU_list[OU_index].id, )
    #         self.VIP_list.append(new_VIP)
    #     elif self.OU_list[OU_index].score < 25 and self.OU_list[OU_index].__class__.__name__ == 'VIP':
    #     # else:
    #     #     update_ranking()

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
        group = None
        for i in range(system.group_count):
            if system.group_list[i] == group_id
                return i
        return None                                     #*** Exceptional Cases: Group id not found

    #12 return top 3 user and groups. RETURNS 2-D array
    def top_3(self):
        arr_top_3 = [None] * 2
        for i in range(3):
            arr_top_3[0].append(system.OU_list[i])
            arr_top_3[1].append(system.group_list[i])
        return arr_top_3


