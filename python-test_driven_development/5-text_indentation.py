#!/usr/bin/python3
"""this is a module that prints a text with 2 new \
lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """this function prints a text with 2 new lines \
after each of these characters: ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    for i in range(len(text)):
        new_text += text[i]
        if text[i] in ".?:":
            new_text += "\n\n"
    lines = new_text.split("\n")
    cleaned_lines = [line.strip() for line in lines]

    print("\n".join(cleaned_lines), end="")
