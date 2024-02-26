def is_substring(potential_substring, potential_superstring):
    if potential_substring-("!$%&/()=-_'?+*.:,;") in potential_superstring:
        return True
    else:
        return False
    
print(is_substring("rassgat.", "farðu í rassgat og rófu"))