from auth import authenticate, check_credentials
from auth_ui import handle_login

def test_valid_login():
    assert authenticate("admin", "secret") is True

def test_invalid_login():
    assert authenticate("user", "wrong") is False

def test_empty_credentials():
    assert authenticate("", "") is False

def test_ui_valid():
    assert handle_login("admin", "secret") == "Welcome!"

def test_ui_invalid():
    assert handle_login("bad", "creds") == "Invalid credentials."
