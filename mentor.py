class Mentor():
    def __init__(self, raw_data):
        self.id = raw_data[0]
        self.first_name = raw_data[1]
        self.last_name = raw_data[2]
        self.nick_name = raw_data[3]
        self.phone_number = raw_data[4]
        self.email = raw_data[5]
        self.city = raw_data[6]
        self.favourite_number = raw_data[7]

    @staticmethod
    def get_all():
        from db import Database
        return Database.get_mentors()

    # Return the 2 name property of all the mentors
    # returns: list of dictionaries
    # example: [{
    #    first_name: 'Bill',
    #    last_name: 'Wilkinson'
    # }, ...]
    @classmethod
    def _1_list_mentors(cls):
        mentors = Mentor.get_all()
        mentor_names = []
        for mentor in mentors:
            first_last = {}
            first_last["first_name"] = mentor.first_name
            first_last["last_name"] = mentor.last_name
            mentor_names.append(first_last)
        return mentor_names
    
    # Return the nick_name property of all the mentors located in Miskolc
    # returns: list of dictionaries
    # example: [{
    #    nick_name: 'Billy'
    # }, ...]
    @classmethod
    def _2_list_mentors_from_miskolc(cls):
        mentors = Mentor.get_all()
        nick_names = []
        for mentor in mentors:
            if mentor.city == "Miskolc":
                m_located_mentors = {}
                m_located_mentors["nick_name"] = mentor.nick_name
                nick_names.append(m_located_mentors)
        return nick_names

    # Return the highest favourite number of all mentors
    # returns: integer
    # example: 927
    @classmethod
    def _3_greatest_favourite_number(cls):
        mentors = Mentor.get_all()
        favourite_numbers = []
        for mentor in mentors:
            if mentor.favourite_number != None:
                favourite_numbers.append(mentor.favourite_number)
        return max(favourite_numbers)