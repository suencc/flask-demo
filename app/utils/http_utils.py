import requests

def get_json(url, params):
    r = __get_requests(url, params)

    if r:
        return r.json()
    else:
        return None


def post(url, data):
    try:
        r = requests.post(url, data=data, timeout=60)
        print(r.status_code)
        return r.text
    except Exception as e:
        print("ERROR:", e)
        return 404

def put(url, params):
    try:
        r = requests.put(url, params=params)
        return r.text
    except Exception as e:
        print("ERROR:", e)
        return 404

def delete(url, params):
    try:
        r = requests.delete(url, params=params)
        return r.text
    except Exception as e:
        print("ERROR:", e)
        return 404

def get_content(url, params):

    r = __get_requests(url, params)
    if r:
        return r.content
    else:
        return None

def __get_requests(url, params):
    try:
        for i in range(3):
            r = requests.get(url, params=params, timeout=60)

            if r.status_code == 200 or r.status_code == 304:
                return r

    except Exception as e:
        print("HTTP ERROR:", e)
        return None
