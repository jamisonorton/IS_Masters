# week 10 - code along 1
import requests

url = "https://safeut.test.med.utah.edu/apidemo/RestService/Quote"
req = requests.get(url)
print("Status code: ", req.status_code)

return_value = req.json()
print(return_value)

"""
(.venv) jorton4@jorton4-macmini IS_6495_Python % /Users/jorton4/Documents/personal-repos/IS_Masters/IS_6495_Python/.venv/bin/python /Users/jorton4/Documents/personal-repos/IS_Masters/IS_6495_Python/week10/code_along_1.p
y
Status code:  200
War is God’s way of teaching Americans geography
"""
