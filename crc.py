def xor(a, b):
    # Perform XOR operation
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    # Perform binary division (modulo 2) of dividend by divisor
    pick = len(divisor)
    tmp = dividend[0:pick]
    
    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:   
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    return tmp

def encodeData(data, divisor):
    l_key = len(divisor)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, divisor)
    codeword = data + remainder
    return codeword

def decodeData(data, divisor):
    remainder = mod2div(data, divisor)
    if '1' in remainder:
        return False  # Data is corrupted
    else:
        return True  # Data is correct

# Example Usage
if __name__ == "__main__":
    # (7, 4) code where 7 is the total length of the block and 4 is the number of bits in the data segment
    data = "1101"  # 4-bit data
    divisor = "1011"  # Divisor

    print("Data to be sent: ", data)
    codeword = encodeData(data, divisor)
    print("Encoded data (Data + CRC): ", codeword)

    # Simulate received data
    received_data = codeword  # No error introduced
    # received_data = "1101110"  # Introduce an error for testing

    print("Received data: ", received_data)
    is_correct = decodeData(received_data, divisor)
    
    if is_correct:
        print("No error detected in received data.")
    else:
        print("Error detected in received data.")
