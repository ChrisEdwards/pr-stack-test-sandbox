def auth_middleware(request):
    if not request.get("token"):
        return {"status": 401}
    return None
