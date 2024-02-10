def get_first_character_after_space(input_string):
    words = input_string.split()
    result = ''
    for word in words:
      result += word[0]
    return result
sentence = get_first_character_after_space(input_string)
print(sentence)
