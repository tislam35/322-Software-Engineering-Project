import users
import system
import registered_visitor
from pprint import pprint

# TEST: PASSED
# set up scenario

# create OU user
user1 = users.OU("JohnCruz1", "pass123", "John", "Cruz", "John.123@gmail.com", "718-234-2341", "vollyball, chess")
user1.score = 20
# create user's reference to a potential visitor
user1.referenceInfo = ("kim.456@gmail.com", 10)
# add user to system OU list
system.system.OU_list.append(user1)
system.system.OU_count += 1

# get info  from GUI
entered_first_name = "Kim"
entered_last_name = "Zhang"
entered_email = "kim.456@gmail.com"
entered_phone_number = "718-234-6543"
entered_interests = "chess, basketball"
entered_reference_username = "JohnCruz1"

# entered info to system register method. It create a registered_visiter object and adds to list
isSuccess = system.system.register(entered_first_name, entered_last_name, entered_email, entered_phone_number, entered_interests, entered_reference_username)

# make registered visitor an OU (removes from register_visitor list, make OU object, and add to OU list
system.system.add_visitor_to_OU(entered_email)












# YOU CAN SEE THE CHANGES BY PRINT THE LIST AND CONTENTS OF EVERY OBJECT CREATED
# # set up scenario
#
# # create OU user
# user1 = users.OU("JohnCruz1", "pass123", "John", "Cruz", "John.123@gmail.com", "718-234-2341", "vollyball, chess")
# # create user's reference to a potential visitor
# user1.referenceInfo = ("kim.456@gmail.com", 10)
# # add user to system OU list
# system.system.OU_list.append(user1)
# system.system.OU_count += 1
# print(pprint(vars(system.system.OU_list[system.system.OU_count - 1])))
# print("number of OU in system list: " + str(system.system.OU_count))
#
#
# visitor1 = registered_visitor.registered_visitor("Kim", "Zhang", "kim.456@gmail.com", "718-234-6543", "chess, basketball", 10)
# # pprint(vars(visitor1))
# # visitor2 = registered_visitor.registered_visitor("Victor", "Jefferson", "v.mail@gmail.com", "718-123-345", "programming, walking", 5)
# # pprint(vars(visitor2))
#
# # print(system.system.registered_visitor_list)
# print("number of register_visitor: " + str(len(system.system.registered_visitor_list)))
# isSuccess = system.system.register(visitor1.first_name, visitor1.last_name, visitor1.email, visitor1.phone_number, visitor1.interests, "JohnCruz1")
# print(isSuccess)
# pprint(vars(system.system.registered_visitor_list[0]))
# print("number of register_visitor: " + str(len(system.system.registered_visitor_list)))
# print("number of OU unser: " + str(len(system.system.OU_list)))
# system.system.add_visitor_to_OU(visitor1.email)
# print(system.system.OU_list)
# print("number of OU user: " + str(len(system.system.OU_list)))
# print("number of register_visitor: " + str(len(system.system.registered_visitor_list)))
# # pprint(vars(system.system.registered_visitor_list[0]))
# print(system.system.registered_visitor_list)
# print("END")

