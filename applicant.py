class Applicant():
    def __init__(self, raw_data):
        self.id = raw_data[0]
        self.first_name = raw_data[1]
        self.last_name = raw_data[2]
        self.phone_number = raw_data[3]
        self.email = raw_data[4]
        self.application_code = raw_data[5]

    @staticmethod
    def get_all():
        from db import Database
        return Database.get_applicants()

    # Return the full name, as a full_name property of all the applicants, whose name is Carol
    # returns: list of dictionaries
    # example: [{
    #    full_name: 'Carol James'
    # }, ...]
    @classmethod
    def _4_specific_applicant_by_first_name(cls):
        applicants = Applicant.get_all()
        full_names = []
        for applicant in applicants:
            if applicant.first_name == "Carol":
                full_name = {}
                full_name["full_name"] = applicant.first_name + " " + applicant.last_name
                full_names.append(full_name)
        return full_names
            
    # Return the full name, as a full_name property of all the applicants, whose email ends with '@adipiscingenimmi.edu'
    # returns: list of dictionaries
    # example: [{
    #    full_name: 'Ipis Blud'
    # }, ...]
    @classmethod
    def _5_specific_applicant_by_email_domain(cls):
        applicants = Applicant.get_all()
        full_names = []
        for applicant in applicants:
            if "dipiscingenimmi.edu" in applicant.email:
                full_name = {}
                full_name["full_name"] = applicant.first_name + " " + applicant.last_name
                full_names.append(full_name)
        return full_names

    # Insert a the Applicant into Database.applicants_data,
    # and return a filtered list, where we only add the data of Markus.
    # The data of the new applicant:
    #   id: 11
    #   first_name: 'Markus'
    #   last_name: 'Schaffarzyk'
    #   phone_number: '003620/725-2666'
    #   email: 'djnovus@groovecoverage.com'
    #   application_code: 54823
    # returns: list of dictionaries (one dictionary, as the list should be filtered)
    # example return value: [{
    #    id: 500
    #    first_name: 'Bill',
    #    last_name: 'Wilkinson',
    #    phone_number: '003670/123-4567'
    #    email: 'bill@wilkins.on'
    #    application_code: 54823
    # }]
    @classmethod
    def _6_inserting_a_new_applicant(cls):
        new_applicant = [11, 'Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823]
        from db import Database
        Database.applicants_data.append(new_applicant)
        insert_data = [cls.get_all()[10].__dict__]
        return insert_data

    # Update an Applicant in the applicants_data, and returns a filtered dictionary list for checking.
    # Story: Jemima Foreman, an applicant called us, that her phone number changed to: 003670/223-7459
    # example return value: [{
    #    phone_number: '003670/223-7459'
    # }]
    @classmethod
    def _7_updating_data(cls):
        applicant_data = Applicant.get_all()
        for applicant in applicant_data:
            if applicant.first_name == "Jemima" and applicant.last_name == "Foreman": 
                applicant.phone_number = "003670/223-7459"
                filtered_list = [{"phone_number": applicant.phone_number}]
                return filtered_list

    # Delete lines from the applicants_data, based on a filter condition
    # Story: Arsenio, an applicant called us, that he and his friend applied to Codecool.
    # They both want to cancel the process, because they got an investor for the site they run: mauriseu.net
    # Logic: remove all the applicants, who applied with emails for this domain.
    #       (e-mail address has this domain after the @ sign)
    # returns: integer (number of occurences of the @mauriseu.net e-mail domains)
    # example: 2
    @classmethod
    def _8_deleting_applicants(cls):
        from db import Database
        applicant_data = Applicant.get_all()
        number_of_occurences = 0
        for applicant in applicant_data:
            if "mauriseau.net" in applicant.email:
                number_of_occurences += 1
                del Database.applicants_data
        return number_of_occurences
