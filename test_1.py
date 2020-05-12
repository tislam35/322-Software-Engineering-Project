import system
import users
from pprint import pprint

print("1.  " + str(system.system.OU_list))
print("2. " + str(system.system.OU_count))
user1 = users.OU("JohnCruz1", "pass123", "John", "Cruz", "John.123@gmail.com", "718-234-2341", "vollyball, chess")
user1.score = 20
system.system.OU_list.append(user1)
system.system.OU_count += 1
print("3. " + str(system.system.OU_list))
print("4. " + str(system.system.OU_count))
print("5. ")
pprint(vars(user1))

print("6." + str(system.system.FSU))
system.system.FSU = users.SU("FSU", "pass123", "Group", "S", "FSU@gmail.com", "718-123-567", "coding, teamwork")
system.system.FSU.score = 100
system.system.FSU.referenceInfo = ("kim.456@gmail.com", 20)
print("7." )
pprint(vars(system.system.FSU))

# get info  from GUI
entered_first_name = "Kim"
entered_last_name = "Zhang"
entered_email = "kim.456@gmail.com"
entered_phone_number = "718-234-6543"
entered_interests = "chess, basketball"
entered_reference_username = "FSU"



isSuccess = system.system.register(entered_first_name, entered_last_name,
                                   entered_email, entered_phone_number,
                                   entered_interests, entered_reference_username)
print("7.8. " + str(system.system.registered_visitor_list))
print("7.9. " + str(system.system.OU_list))
print("8. " + str(isSuccess))
system.system.add_visitor_to_OU(entered_email)
print("8.1. " + str(system.system.registered_visitor_list))
print("8.2. " + str(system.system.OU_list))







