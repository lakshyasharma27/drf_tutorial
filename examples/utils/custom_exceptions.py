from rest_framework.exceptions import APIException

class UniqueConstraintException(APIException):
    '''
        409 if data already exists
    '''
    status_code = 409
    default_detail = "Unable to add/update. Data already exists."
    default_code = "unique_constraint"

    def __init__(self, detail=None, code=None):
        if "UNIQUE constraint" in detail.args[0]:
            print(detail.args[0])
            self.default_detail = detail.args[0].split(".")[1] + " already exists."

        
        # error_detail = detail.args[0].split("Key")[1]
        super().__init__(self.default_detail, code)

class CustomObjectDoesNotExists(APIException):
    status_code = 404
    default_detail = "Data Does not exists."
    default_code = "does_not_exists"

    def __init__(self, detail=None, code=None):
        print(" custom expetion--->")
        # print(detail.args[0])
        key_data = detail.args[0].split(" ")[0]
        print(key_data)
        detail = f'{key_data} does not exists.'
        super().__init__(detail, code)
