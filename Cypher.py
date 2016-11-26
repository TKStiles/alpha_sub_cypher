def key_creation(key):
    print("Key entered as: ", key)
    char_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    itt = 0
    ascii_list = []
    key_red = ""
    for char in key:
        if char not in key_red:
            key_red = key_red + char
    for char in key_red:
        if char not in ascii_list:
            ascii_list.append([char, ord("a") + itt])
            itt += 1
    for char in char_list:
        if char not in key:
            ascii_list.append([char, ord("a") + itt])
            itt += 1
    print("You're key shifts ascii characters as shown below: ")
    print()
    print(ascii_list)
    return ascii_list

def encrypt(key, message):
    cypher_dict = dict()
    new_string = ""
    for item in key:
        cypher_dict[item[0]] = chr(item[1])
    for char in message:
        if char.isalpha():
            string_chr = cypher_dict[char]
            new_string = new_string + string_chr
        else:
            new_string = new_string + char
    return new_string

def decrypt(key, code):
    cypher_dict = dict()
    for item in key:
        cypher_dict[chr(item[1])] = item[0]
    new_string = ""
    for char in code:
        if char.isalpha():
            new_string = new_string + cypher_dict[char]
        else:
            new_string = new_string + char
    return new_string


key_string = input("Please select a key word for your cypher: ")
key_list = key_creation(key_string)
while(True):
    message = input("Please input your message: ")
    resp =  input("Type 'e' if you would like this message encrypted or type 'd' if you would like it decrypted.: ")
    print()
    resp = resp.lower()
    if resp == "e":
        out = encrypt(key_list, message)
        print(out)
        print()
        cont = input("Would you like to continue with your current key word?: ")
        if cont.lower() == "no":
            break
        elif cont.lower() == "yes":
            continue
    elif resp == "d":
        out = decrypt(key_list, message)
        print(out)
        print()
        cont = input("Would you like to continue with your current key word?: ")
        if cont.lower() == "no":
            break
        elif cont.lower() == "yes":
            continue
    else:
        print("Not a valid command. Type 'e' to encrypt, type 'd' to decrypt. Or type 'exit' to quit.: ")
        print()
        continue
