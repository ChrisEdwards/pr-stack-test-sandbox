_sessions = {}

def create_session(user_id):
    import uuid
    session_id = str(uuid.uuid4())
    _sessions[session_id] = user_id
    return session_id
