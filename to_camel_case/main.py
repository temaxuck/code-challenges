def to_camel_case(text):
    if text == "":
        return ""
    res = []
    i = 0

    while i < len(text):
        if text[i] in ["-", "_"]:
            if i + 1 < len(text):
                res.append(text[i + 1].upper())
            i += 1
        else:
            res.append(text[i])

        i += 1

    return "".join(res)


print(to_camel_case("THe_Stealth_Warrior"))
