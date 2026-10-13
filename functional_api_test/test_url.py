from logging import Logger

from common_utilities.common_utils import CommonUtils
# from functional_api_test.functional_param import FunctionalParam
from config.APIconfig import APIurls
from req_res.request.gorest import GoRest
import conftest

class TestGoRestAPIs:

    def test_base_url(self):
        self.logger = CommonUtils.logger_data()

        # url = FunctionalParam.get_base_end_point()
        # print("url : ", url)

        # Get the urls from APIConfig
        get_user_url = APIurls().get_user_url
        self.logger.info(f"URL -->  {get_user_url}")
        print("URL : ", get_user_url)
        # print(f"Base user url: {get_user_url}")
        # get_url_by_user_id = APIurls().get_url_by_user_id(543298)
        # print(f"Base URL by user_id {get_url_by_user_id}")

        # get the custom headers
        # print(f"Testing the headers")
        header = CommonUtils.get_custom_header()
        self.logger.info(f"header: {header}")
        # print(headers)

        # # get custom and unique email
        # print("Testing email")
        # email = CommonUtils.get_unique_email()
        # print(email)


        # # Get JsonBody
        # print("Create JSON request")
        create_json_req = GoRest.CREATE_USER
        # print(create_json_req)
        #
        # print("User Update JSON request")
        # user_update_json_req = GoRest.UPDATE_USER
        # print(user_update_json_req)

        # req = conftest.get_api_call("GET",
        #                             get_user_url,
        #                             headers
        #                             )
        # print(req.json())

        # response = conftest.get_api_call(req_method="POST",
        #                             req_url=get_user_url,
        #                             req_headers=header,
        #                             req_json=create_json_req,
        #                             expected_status_code=201
        #                             )
        #
        # user_id = response.json()["id"]

        # url_with_user_id = APIurls().get_url_by_user_id(user_id)
        request = conftest.get_api_call(req_method="GET",
                                        req_url=get_user_url,
                                        req_headers=header,
                                        expected_status_code=200)

        # user_ids = []
        # for user_obj in request.json():
        #     user_ids.append(user_obj["id"])
        # print("Response: ", response.json())
        print("request: ", request.json())
        self.logger.info(f"request: {request.json()}")
        self.logger.info(f"Status code: {request.status_code}")
        # assert response.json() == request.json(), "User ID is not available"
        print("Test execution completed")

