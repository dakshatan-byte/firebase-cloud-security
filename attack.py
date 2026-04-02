import requests

url = "https://firestore.googleapis.com/v1/projects/cloudprojectlabca/databases/(default)/documents/users"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Data:", response.text)