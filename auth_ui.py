from auth import authenticate

def login_form():
    return "<form><input name='user'/><input name='pass' type='password'/></form>"

def handle_login(username, password):
    if authenticate(username, password):
        return "Welcome!"
    return "Invalid credentials."
