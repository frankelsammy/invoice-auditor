import requests

# ====== CONFIG ======
WM_TOKEN = "eyJraWQiOiJ4VjZNTGE1ZzBVdlhGejFzZkFtQXdpMUFTOExrbUlCTzBtZHllZHhUaHlZIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULi1oTXl3VU1BRk01MGNPVjUwWVFuQzAtajVFRGxkMUtkeEFYZmxVUXNMZ1kiLCJpc3MiOiJodHRwczovL3Nzb2xvZ2luLndtLmNvbS9vYXV0aDIvYXVzMTcwbWluanRRT1JlNHUycDciLCJhdWQiOiJodHRwczovL3d3dy53bS5jb20iLCJpYXQiOjE3NzE3OTUzMjEsImV4cCI6MTc3MTc5ODkyMSwiY2lkIjoiMG9hNDRiajEwclZMRTJuczQycDciLCJ1aWQiOiIwMHU0NHVtd2tsbFBxZ3M5MTJwNyIsInNjcCI6WyJvcGVuaWQiLCJlbWFpbCJdLCJhdXRoX3RpbWUiOjE3NzE3OTUzMjEsInN1YiI6ImRhbm55ZnJhbmtlbEBjb21jYXN0Lm5ldCJ9.FZ1O6tVQEyNzk6dGCDyhoHtTG65_8yA4VXbt76B4KQdfdqutp-WwOvd_UMmBsJazj91Ys9aWVTaK69RP9t9_UIX6d6_Ru4V4c1gbSb4-zgJEWFsFCilXOUEws2_u01WzTZ3toLjjLi6J76aWQ_WCfBfZQWDsz8BcheX5KMHUJJoYopJHrvUEtwamZMz1Nm6ZiuFvvbGQSiBirreedgCAb7IGXPlYzctUJLAr7FcB-rh8rxHX1OYtUarDohQ3Yt7Y_yenMWNclO1rQNHN-NpxTHAoiVn2NbZGnZD__YGvBxvHlc0P8hJhaN7pkxzDax1A2L0x_sXA2Yt0nrEFv8XA9Q"
WM_API_KEY = "615F2EFC82FF8BB2F864"

# ====== PARAMETERS ======
ACCOUNT_ID = "000331193013001"
USER_ID = "00u44umwkllPqgs912p7"
BASE_URL = "https://rest-api.wm.com"

# Date range parameters
params = {
    "lang": "en_US",
    "fromDate": "2025-02-22",
    "toDate": "2026-03-22",
    "userId": USER_ID
}

# ====== BUILD URL ======
url = f"{BASE_URL}/account/{ACCOUNT_ID}/invoice"

# ====== HEADERS ======
headers = {
    "Authorization": f"Bearer {WM_TOKEN}",
    "Apikey": WM_API_KEY,
    "Accept": "application/json"
}

# ====== REQUEST ======
response = requests.get(url, headers=headers, params=params)

# ====== OUTPUT ======
print("Status Code:", response.status_code)
print("Response Body:")
print(response.text)