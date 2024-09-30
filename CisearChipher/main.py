from CClogo import logo,alphabet
print(logo)
cipher = True


def ceaser():
    text = input("Input your message: ")
    shift = int(input("Type your shift number: "))
    method = input("Type 'decode' for decryption or 'encode' for encryption: ").lower()
    new_msg = ""
    for i in text:
        if i not in alphabet:
            new_msg += i
        else:
            og_index = alphabet.index(i)
            if method == "encode":
                new_ind = og_index + shift
                new_ind %= len(alphabet)
                new_msg += alphabet[new_ind]
            elif method == "decode":
                new_ind = og_index - shift
                new_ind %= len(alphabet)
                new_msg += alphabet[new_ind]
            else:
                print("please try again and write correctly your desired method.")
    print(f"Your {method}ed message is: {new_msg}")


while cipher:
    ceaser()
    continue_cipher = input("do you want to continues? type y/n: ").lower()
    if continue_cipher == 'y':
        cipher = True
    else:
        print("Goodbye.")
        cipher = False
