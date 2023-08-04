def convert_hex_to_decimal(hex_string):
    hex_list = hex_string.split()
    decimal_list = []

    for hex_value in hex_list:
        decimal_value = int(hex_value, 16)
        decimal_list.append(decimal_value)

    return decimal_list

input_hexadecimal = "FFF0F0 FFE1E1 FFCECE FFBFBF FFAFAF FD9F9F FF8F8F FF8080 FF7171 FF6161 FF4F4F FF4040 FF3030 FF2020 FF1212 FF0000"
decimal_list = convert_hex_to_decimal(input_hexadecimal)
print(decimal_list)
