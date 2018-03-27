"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""


def string_splosion(str):
    str_len = len(str)
    final_str = ""
    while str_len > 0:
        str = str[:str_len]
        final_str = str + final_str
        str_len -= 1
    return final_str
