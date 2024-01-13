def create_phone_number(n):
    phone_number = ["("]
    for i in range(len(n)):
        phone_number.append(str(n[i]))
        if i == 2:
            phone_number.append(") ")
        if i == 5:
            phone_number.append("-")

    return "".join(phone_number)
