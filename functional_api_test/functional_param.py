
import json

class FunctionalParam:
    filepath = r"C:\Users\HP\PycharmProjects\PythonProject\PythonProject\API_Testing_Framework\config\endpoints.json"

    @staticmethod
    def get_base_end_point():
        with open(file=FunctionalParam.filepath, mode="r") as json_file:
            properties = json.load(json_file)
            env = properties["environment"]["env"]
            url = properties[env]["base_url"]
            return url