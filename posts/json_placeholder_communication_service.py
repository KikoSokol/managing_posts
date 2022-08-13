import requests

BASE_URL = 'https://jsonplaceholder.typicode.com/'


def exists_user_with_id(id):
    url = BASE_URL + "users/" + str(id)

    request_data = requests.get(url)

    if request_data.status_code == 200:
        return True
    elif request_data.status_code == 404:
        return False


def get_post_by_id(id):
    url = BASE_URL + "posts/" + str(id)
    request_data = requests.get(url)

    if request_data.status_code == 200:
        data = request_data.json()
        return {"user_id": data["userId"],
                "id": data["id"],
                "title": data["title"],
                "body": data["body"]}
    elif request_data.status_code == 404:
        return None
