import string 

def is_pangram(st):
    st = st.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in st:
            return False
    return True
# 6kyu