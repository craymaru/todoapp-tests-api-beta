import requests
import json
from const import API_URL

endpoint = f"{API_URL}/todos"

headers_dic = {'content-type': 'application/json'}

expected_dic = {
    "title": "ネコちゃんにごはんをあげる",
    "memo": "neko",
    "priority": 3
}


def test_create_todoで新規作成できる():
    actual = requests.post(
        endpoint,
        data=json.dumps(expected_dic),
        headers=headers_dic
    )
    actual_json = actual.json()

    assert actual_json["id"]
    assert actual_json["title"] == expected_dic["title"]
    assert actual_json["memo"] == expected_dic["memo"]
    assert actual_json["priority"] == expected_dic["priority"]
