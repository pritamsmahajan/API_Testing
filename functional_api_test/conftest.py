import json
import pytest
import requests

def get_api_call(req_method,
                 req_url=None,
                 req_params=None,
                 req_headers=None,
                 req_json=None,
                 expected_status_code=200
                 ):
    response = requests.request(method=req_method,
                                url=req_url,
                                params=req_params,
                                headers=req_headers,
                                json=req_json
                                )
    fail_message = (f"API Call failed. Expected status code: {expected_status_code}\n"
                    f"Response Status Code: {response.status_code}")
    try:
       assert response.status_code == expected_status_code, fail_message
       return response

    except:
        pytest.fail(fail_message)


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="prod")


def update_env(config):
    env_var = config.getoption("--env")
    with open(r"C:\Users\HP\PycharmProjects\PythonProject\PythonProject\API_Testing_Framework\config\endpoints.json", "r+") as json_file:
        data = json.load(json_file)
        data['environment']['env'] = env_var.lower()
        json_file.truncate(0)
        json_file.seek(0)
        json.dump(data, json_file, indent=4)
        json_file.close()


@pytest.hookimpl()
def pytest_configure(config):
    update_env(config)
