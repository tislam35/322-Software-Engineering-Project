from system import *

class registered_visitor(object):

    def __init__(self, first_name, last_name, email, phone_number, interests, affiliated_classes, reference_first_name, reference_last_name, reference_email):
        self.rejected = None
        self.appealed = False
        self.rejected_twice = None
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.interests = interests
        self.affilated_classes = affiliated_classes
        # we need to check this in register GUI so we don't do it here
        self.reference_OU = system.find_OU_by_info(reference_first_name, reference_last_name, reference_email)
