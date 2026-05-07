import time
from utils.api_client import APIClient

def test_api_response_time(config):
    api = APIClient(config["api_url"])

    login_res = api.login(config["user"]["email"], config["user"]["password"])
    token = login_res.json().get("token") or login_res.json().get("data", {}).get("token")

    start = time.time()
    response = api.get_notes(token)
    end = time.time()

    duration = end - start

    print("Response Time:", duration)

    assert response.status_code == 200
    assert duration < 8