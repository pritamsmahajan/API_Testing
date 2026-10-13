from functional_api_test.functional_param import FunctionalParam


class APIurls:

    get_user_url = FunctionalParam.get_base_end_point() + "/public/v2/users"

    def get_url_by_user_id(self, user_id):
        get_user_id_url = FunctionalParam.get_base_end_point() + f"/public/v2/users/{user_id}"
        return get_user_id_url