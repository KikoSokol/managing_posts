import requests
from requests import RequestException

BASE_URL = 'https://jsonplaceholder.typicode.com/'


def exists_user_with_id(id):
    url = BASE_URL + "users/" + str(id)

    try:
        request_data = requests.get(url)

        if request_data.status_code == 200:
            return True, "User with user_id " + str(id) + " exists.", 200
        elif request_data.status_code == 404:
            return False, "User with user_id " + str(id) + "does not exist.", 404
    except RequestException:
        return False, "Error in communication with external database.", 503


def get_post_by_id(id):
    url = BASE_URL + "posts/" + str(id)

    try:
        request_data = requests.get(url)

        if request_data.status_code == 200:
            data = request_data.json()
            return True, {"user_id": data["userId"],
                          "id": data["id"],
                          "title": data["title"],
                          "body": data["body"]}, 200
        elif request_data.status_code == 404:
            return False, None, 404
    except RequestException:
        return False, "Error in communication with external database.", 503
