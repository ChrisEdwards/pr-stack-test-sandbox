def truncate(text, max_len=100):
    if len(text) <= max_len:
        return text
    return text[:max_len-3] + "..."
