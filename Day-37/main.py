import requests
import datetime

today = datetime.datetime.today()
today_formatted = today.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
pixela_username = "daggy"
pixela_token = "ehfklcnpvnprueiwgibq"

user_params = {
    "token": pixela_token,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"
graph_params = {
    "id": "book101",
    "name": "Book Streak",
    "unit": "pages",
    "type": "int",
    "color": "sora"
}
req_headers = {
    "X-USER-TOKEN": pixela_token
}

# response = requests.post(url=graph_endpoint, json= graph_params, headers=req_headers)
# print(response.text)

pix_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/book101"
pix_params = {
    "date": today_formatted,
    "quantity": "78",
}
# response = requests.post(url=pix_endpoint, json=pix_params, headers=req_headers)

update_pix_endpoint = f"{pix_endpoint}/{today_formatted}"
update_pix_params = {
    "quantity": "15",
}

# response = requests.put(url=update_pix_endpoint, json=update_pix_params, headers=req_headers)

delete_pix_endpoint = f"{pix_endpoint}/{today_formatted}"
response = requests.delete(url=delete_pix_endpoint, headers=req_headers)
