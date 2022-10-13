def check_message_contain(message_check):
    if message_check.startswith('kigali') or message_check.startswith('eastern') or message_check.startswith('western') or message_check.startswith('southern'):
        return True
    else:
        return False
