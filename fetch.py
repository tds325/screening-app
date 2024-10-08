import requests

def main():
    target_uri = "https://services.cancerimagingarchive.net/nbia-api/"
    token_response = get_oauth_token(target_uri)
    print(token_response)

    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJkZGFhMGY3YS1kZTBmLTRkYWQtYjM1ZS05MjljYjBiMTY3YjgifQ.eyJleHAiOjE3Mjg0Mjk1NzIsImlhdCI6MTcyODQyMjM3MiwianRpIjoiMDExZjkxNGUtNDkwNi00ZTIxLThhZDUtMzhiNWEzOTU2MWFkIiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay1zdGcuZGJtaS5jbG91ZC9hdXRoL3JlYWxtcy9UQ0lBIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImY6MDE5YjU2MzQtZGFiZC00MjExLWE0MWQtNzIzYzQ0YWZjZmZkOm5iaWFfZ3Vlc3QiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJuYmlhIiwic2Vzc2lvbl9zdGF0ZSI6ImU1N2ZhYWExLTJjNDktNDYxNy04NzA5LTUyZWFiZWViZDVmYSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cHM6Ly93d3cuY2FuY2VyaW1hZ2luZ2FyY2hpdmUubmV0IiwiaHR0cHM6Ly9jYW5jZXJpbWFnaW5nYXJjaGl2ZS5uZXQiLCJodHRwczovL3NlcnZpY2VzLmNhbmNlcmltYWdpbmdhcmNoaXZlLm5ldCIsImh0dHBzOi8vbmJpYS5jYW5jZXJpbWFnaW5nYXJjaGl2ZS5uZXQiLCIqIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsImRlZmF1bHQtcm9sZXMtdGNpYSIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInNpZCI6ImU1N2ZhYWExLTJjNDktNDYxNy04NzA5LTUyZWFiZWViZDVmYSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiTkJJQSBHdWVzdCIsInByZWZlcnJlZF91c2VybmFtZSI6Im5iaWFfZ3Vlc3QiLCJnaXZlbl9uYW1lIjoiTkJJQSIsImZhbWlseV9uYW1lIjoiR3Vlc3QiLCJlbWFpbCI6Im5iaWFfZ3Vlc3RAY2FuY2VyaW1hZ2luZ2FyY2hpdmUubmV0In0.AIZa2hQFnwcoLNDQgMmHXC1kVWs7OTlS_pJfcgQm17s"
    headers = { "Authorization": f"Bearer {access_token}" }
    print(headers)

def get_oauth_token(target_uri:str):
    request_data = { "username":"nbia_guest", "password":"", \
                     "client_id":"NBIA", "grant_type":"password" }
    headers = { "Accept": "application/json" }
    target_uri = "https://services.cancerimagingarchive.net/nbia-api/oauth/token"
    resp = requests.post(target_uri+"oauth/token", data=request_data, headers=headers)
    return resp

def renew_oauth_token(target_uri:str):
    pass

if __name__ == '__main__':
    main()
