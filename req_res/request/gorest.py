from common_utilities.common_utils import CommonUtils

class GoRest:
    test_email = CommonUtils.get_unique_email()
    CREATE_USER = {
        "name": "Rohit S",
        "email": test_email,
        "gender": "male",
        "status": "active"
    }

    UPDATE_USER = {
        "name": "Rohit Sharma",
        "status": "active"
    }
