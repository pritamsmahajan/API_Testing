import random
import logging


class CommonUtils:

    @staticmethod
    def get_custom_header():
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer 143f27542656793184f3d1725dbd457e5c35bf55c14ecb4e3b045d527c4629b7"}
        return header

    @staticmethod
    def get_unique_email():
        random_no = random.randint(1000, 99999)
        email = f"test_automation{random_no}@xyz.com"
        return email


    @staticmethod
    def logger_data():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger