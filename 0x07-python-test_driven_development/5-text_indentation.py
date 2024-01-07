def text_indentation(text):
    if text in ['.', '?', ':']:
        print('\n')
        print('\n')
    if text not in [str]:
        raise TypeError("text must be a string")
