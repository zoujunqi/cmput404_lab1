import requests
response = requests.get("http://www.google.com/")
print(response)
my_url = 'https://github.com/zoujunqi/cmput404_lab1/blob/main/request.py'
content = requests.get(my_url)
print(content.text)
