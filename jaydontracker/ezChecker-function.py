import requests
def ezChecker():
    response = requests.get("https://127.0.0.1:5000/check_jaydon")
    if response.status_code == 200:
        data = response.json()
        if data['jaydon']:
            return True
            print("true")

        else:
            return False
        print("false")

    else:
        print("Error:", response.status_code)
        return False

