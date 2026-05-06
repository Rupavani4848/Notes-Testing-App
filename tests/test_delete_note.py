from utils.api_client import APIClient
import time

def test_delete_note_api(config):

    api = APIClient(config["api_url"])
    login_res = api.login(config["user"]["email"], config["user"]["password"])
    token = login_res.json().get("token") or login_res.json().get("data", {}).get("token")

    title = f"API_DEL_{int(time.time())}"

    create = api.create_note(token, title, "delete test")

    assert create.status_code in [200, 201]

    note_id = create.json()["data"]["id"]

    delete = api.delete_note(token, note_id)

    assert delete.status_code == 200