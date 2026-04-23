from sessions import _sessions

def expire_session(session_id):
    _sessions.pop(session_id, None)
