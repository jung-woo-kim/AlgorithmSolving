import json
import requests

base_url = "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"
x_auth_token = "5cd988931dca345a10e11bfffe09ca8c"
key = ""
start_header ={'Content-Type':'application/json; charset=utf-8',
    'X-Auth-Token' : "5cd988931dca345a10e11bfffe09ca8c" }
headers = {'Content-Type':'application/json; charset=utf-8',
    'Authorization' : key}



def start_api():
    global key
    response = requests.post(base_url+"/start",headers=start_header,params={"problem":1})
    key = response.json()["auth_key"]
    headers['Authorization'] = key


def get_waitingLine():
    response = requests.get(base_url+"/waiting_line",headers=headers)
    if response.status_code == 200:
        waiting_line = response.json()["waiting_line"]
    #     "waiting_line": [
    # { "id": 1, "from": 3 },
    # { "id": 2, "from": 14 },
    # ...
  #]

        



def get_gameResult():
    response = requests.get(base_url+"/game_result",headers=headers)

    if response.status_code == 200:
        game_result = response.json()["game_result"]
# "game_result": [
#     {"win": 10, "lose": 2, "taken": 7 },
#     {"win": 7, "lose": 12, "taken": 33 },
#     ...
#   ]

def get_userInfo():
    response = requests.get(base_url+"/user_info",headers=headers)

    if response.status_code == 200:
        user_info = response.json()["user_info"]
# "user_info": [
#     { "id": 1, "grade": 2100 },
#     { "id": 13, "grade": 1501 },
#     ...
#   ]

def put_match():
    response = requests.put(base_url+"/match",headers=headers,json={"pairs" :[[1, 2], [9, 7], [11, 49]]})

    if response.status_code == 200:
        status = response.json()["status"]
        time = response.json()["time"]
    else:
        print(response.json())

def put_changeGrade():
    response = requests.put(base_url+"/change_grade",headers=headers,json={"commands" :[{ "id": 1, "grade": 1900 }]})

    if response.status_code == 200:
        status = response.json()["status"]
    else:
        print(response.json())
def get_score():
    response = requests.get(base_url+"/score",headers=headers)

    if response.status_code == 200:
        score = response.json()["score"]
    else:
        print(response.json())

if __name__ == "__main__":
    start_api()
    get_waitingLine()
    get_gameResult()
    put_match()
    put_changeGrade()
    get_score()