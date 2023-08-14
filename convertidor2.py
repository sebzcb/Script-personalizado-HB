def decrypt_hex(hex_string):
    str_out = ""
    for x in range(0, len(hex_string), 2):
        str_out += chr(int(hex_string[x:x+2], 16))
    return str_out

input_hex = input("Ingresa la cadena hexadecimal: ")
decrypted_text = decrypt_hex(input_hex)
print("Texto descifrado:", decrypted_text)
