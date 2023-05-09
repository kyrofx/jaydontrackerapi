import requests

response = requests.get("wapwapwaphost/check_jaydon")

if response.status_code == 200:
    data = response.json()
    if data['jaydon']:
        print("Jaydon is in the hours list!")

    else:
        print("Jaydon is not in the hours list.")

else:
    print("Error:", response.status_code)

