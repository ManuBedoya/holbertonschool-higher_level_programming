#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError('text must be a string')
    st = True
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(end='\n\n')
            st = False
        else:
            if st:
                print(text[i], end='')
            else:
                st = True
