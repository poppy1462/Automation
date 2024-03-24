import requests

APIKEY = "cf38d0bc0c21cdcf6c3a4391fdba87ab"
TOKEN = "ATTA79f1047258170bd27b97b89eae0da8e25c174f39062b2a3d82afaa125e6fae7996455A6E"

URL = "https://api.trello.com/"


def get_user_boards():
    endpoint = "1/members/me/boards"
    params = {
        'key': APIKEY,
        'token': TOKEN
    }

    response = requests.get(url=URL+endpoint, params=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    responseJson = response.json()
    return(responseJson)


def get_board_id(name):
    id = None
    response = get_user_boards()
    for board in response:
        if board['name'] == name:
            id = board['id']
            break
    if id is None:
        print("No board found with the name: {}".format(name))
    return id


def update_board(name, **kwargs):
    board_id = get_board_id(name)

    endpoint = "{}1/boards/{}".format(URL, board_id)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': name
    }
    for key, value in kwargs.items():
        params[key] = value

    response = requests.request(
        "PUT",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def delete_board(name):
    board_id = get_board_id(name)

    endpoint = "{}1/boards/{}".format(URL, board_id)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': name
    }

    response = requests.request(
        "DELETE",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def create_new_board(name):
    endpoint = "1/boards/"
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': name
    }
    response = requests.post(url=URL+endpoint, json=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def create_list_on_board(name, list_name):
    board_id = get_board_id(name)

    endpoint = "{}1/boards/{}/lists?{}".format(URL, board_id, list_name)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': list_name
    }

    response = requests.request(
        "POST",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def get_lists_on_board(name):
    response = get_board_id(name)

    endpoint = "1/boards/{}/lists".format(response)
    params = {
        'key': APIKEY,
        'token': TOKEN
    }

    response = requests.get(url=URL+endpoint, params=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    responseJson = response.json()
    return(responseJson)


def get_list_id(name, list_name):
    list_id = None
    response = get_lists_on_board(name)
    for list in response:
        if list['name'] == list_name:
            list_id = list['id']
            break
    if list_id is None:
        print("No list found with the name: {}".format(name))

    return list_id


def archive_list(name, list_name):
    list_id = get_list_id(name, list_name)

    endpoint = "{}1/lists/{}/closed".format(URL, list_id)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'value': 'true'
    }

    response = requests.request(
        "PUT",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def create_new_card_in_list(name, list_name, card_name):
    list_id = get_list_id(name, list_name)

    endpoint = "{}1/cards".format(URL)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': card_name,
        'idList': list_id
    }

    response = requests.request(
        "POST",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def get_cards_on_list(name, list_name):
    response = get_list_id(name, list_name)

    endpoint = "1/lists/{}/cards".format(response)
    params = {
        'key': APIKEY,
        'token': TOKEN
    }

    response = requests.get(url=URL+endpoint, params=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    responseJson = response.json()
    return(responseJson)


def get_card_id(name, list_name, card_name):
    card_id = None
    response = get_cards_on_list(name, list_name)
    for card in response:
        if card['name'] == card_name:
            card_id = card['id']
            break
    if card_id is None:
        print("No card found with the name: {}".format(card_name))

    return card_id


def update_card(name, list_name, card_name, **kwargs):
    card_id = get_card_id(name, list_name, card_name)

    endpoint = "{}1/cards/{}".format(URL, card_id)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': card_name
    }
    for key, value in kwargs.items():
        params[key] = value

    response = requests.request(
        "PUT",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def delete_card(name, list_name, card_name):
    card_id = get_card_id(name, list_name, card_name)

    endpoint = "{}1/cards/{}".format(URL, card_id)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': card_name
    }

    response = requests.request(
        "DELETE",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)



if __name__ == "__main__":
    #get_user_boards()
    #create_new_board("Test Automation")
    #update_board("Test Automation", desc="Add items to finish automation")
    #delete_board("Test Automation")
    #create_list_on_board("Test Automation", "New list")
    #create_new_card_in_list("Test Automation", "New list", "New card")
    #update_card("Test Automation", "New list", "New card", desc="This is a test card")
    #delete_card("Test Automation", "New list", "New card")
    archive_list("Test Automation", "New list")