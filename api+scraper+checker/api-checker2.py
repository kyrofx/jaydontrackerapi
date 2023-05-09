import requests
from tester import check_jaydon

answer = check_jaydon()

if answer:
    print("Jaydon is in the hours list!")
else:
    print("Jaydon is not in the hours list.")

