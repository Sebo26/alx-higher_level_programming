def text_indentation(text):
    if text in ['.', '?', ':']:
        print('\n')
        print('\n')
    elif not isinstance(text, str):
        raise TypeError("text must be a string")
