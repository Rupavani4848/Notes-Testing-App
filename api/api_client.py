import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def login(self, email, password):
        url = f"{self.base_url}/users/login"
        payload = {
            "email": email,
            "password": password
        }
        res = requests.post(url, json=payload)

        print("STATUS:", res.status_code)
        print("RESPONSE:", res.text)

        assert res.status_code == 200
        return res

    def get_notes(self, token):
        url = f"{self.base_url}/notes"
        headers = {
            "Authorization": f"Bearer {token}"
        }
        return requests.get(url, headers=headers)