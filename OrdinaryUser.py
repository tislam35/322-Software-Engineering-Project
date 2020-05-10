from datetime import datetime

class OrdinaryUser:

    def __init__(self, user_id, username, password, first_name, last_name, email_address, phone_number, interests, 
        reference_user, reference_email):
        
        self.user_id = user_id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.interests = interests
        self.reference_user = reference_user
        self.reference_email = reference_email
        self.score = 0
        self.whitebox = []
        self.blackbox = []
        self.warning_counts = 0
        self.complements_count = 0
        self.time_created = datetime.now()

    def __str__(self):
        return "User ID: " + str(self.user_id) + \
               "\nUsername: " + str(self.username) + \
               "\nPassowrd: " + str(self.password) + \
               "\nFirst Name: " + str(self.first_name) + \
               "\nLast Name: " + str(self.last_name) + \
               "\nEmail: " + str(self.email_address) + \
               "\nPhone No.: " + str(self.phone_number) + \
               "\nInterests: " + str(self.interests) + \
               "\nReference User: " + str(self.reference_user) + \
               "\nReference Email: " +str(self.reference_email) + \
               "\nScore: " + str(self.score) + \
               "\nWhitebox: " + str(self.whitebox) + \
               "\nBlackbox: " + str(self.blackbox) + \
               "\nWarnings: " + str(self.warning_counts) + \
               "\nComplements: " + str(self.complements_count) + \
               "\nTime Created: " + str(self.time_created)
    
