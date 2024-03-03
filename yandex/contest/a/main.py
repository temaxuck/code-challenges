from typing import List


def split(text: str) -> List[str]:
    words = []
    word = ""

    for char in text:
        if char == " ":
            if word:
                words.append(word)
                word = ""
        elif char == ",":
            if word:
                words.append(word)
            words.append(",")
            word = ""
        else:
            word += char
    if word:
        words.append(word)

    return words


if __name__ == "__main__":
    text = split(input())
    if not text:
        exit(0)

    line_length = len(max(text, key=len)) * 3
    formatted_text = []
    current_word = ""
    current_line = ""
    i = 0

    while i < len(text):
        if i < len(text) - 1:
            if text[i + 1] == ",":
                current_word = text[i] + text[i + 1]
                i += 1
            else:
                current_word = text[i]
        else:
            current_word = text[i]

        if len(f"{current_line} {current_word}") <= line_length:
            current_line = (
                " ".join([current_line, current_word]) if current_line else current_word
            )
        else:
            formatted_text.append(current_line)
            current_line = current_word

        i += 1

    formatted_text.append(current_line)

    print("\n".join(formatted_text))
