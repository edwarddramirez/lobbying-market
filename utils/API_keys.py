def get_opensecrets_key():
    user_key = "[add id here]"
    if user_key == "[add id here]":
        raise ValueError("You need to add your OpenSecrets API key in the API_keys.py file")
    else:
        return user_key