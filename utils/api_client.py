import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def login(self, email, password):
        payload = {
            "email": email,
            "password": password
        }

        response = requests.post(
            f"{self.base_url}/users/login",
            json=payload
        )

        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)

        return response

    def get_notes(self, token):
        headers = {
            "x-auth-token": token
        }

        response = requests.get(
            f"{self.base_url}/notes",
            headers=headers
        )

        return response

    def create_note(self, token, title, description):
        headers = {
            "x-auth-token": token
        }
        payload = {
            "title": title,
            "description": description,
            "category": "Personal"
        }

        response = requests.post(
            f"{self.base_url}/notes",
            json=payload,
            headers=headers
        )

        return response

    def delete_note(self, token, note_id):
        headers = {
            "x-auth-token": token
        }

        response = requests.delete(
            f"{self.base_url}/notes/{note_id}",
            headers=headers
        )

        return response