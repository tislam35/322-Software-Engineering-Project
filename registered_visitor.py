

class registered_visitor(object):

    def __init__(self, first_name, last_name, email, phone_number, interests, score):
        from system import  system
        self.rejected = None
        self.appealed = False
        self.rejected_twice = None
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.interests = interests
        # we need to check this in register GUI so we don't do it here
        # self.referenceUser = system.find_user_by_username(referenceUsername)
        self.score = score
