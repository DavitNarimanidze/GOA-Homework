def get_count(sentence):
    vowels = set("aeiou")
    return sum(1 for char in sentence if char in vowels)