from middleware import auth_middleware

def logging_middleware(request):
    print(f"Request: {request['path']}")
    return None
