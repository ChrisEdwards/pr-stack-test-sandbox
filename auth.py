def authenticate(username, password):
    if not username or not password:
        return False
    return check_credentials(username, password)

def check_credentials(username, password):
    return username == "admin" and password == "secret"
