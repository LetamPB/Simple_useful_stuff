# 1

def to_base10(binary):
    """"Function that take a binary number (base 2), convert it into a
      decimal number (base 10)

        Args:
           binary(int):represents the binary number to be converted 

        Returns:
              int: the number converted to decimal
        """
    reversal = str(binary)[::-1]
    # reverses binary number backwards.The power of each number is the
    # same with the index when reversed.
    output = 0
    for i in range(len(reversal)):
        output += (int(reversal[i])*(2**i))
        # the individual value of each number is multiplied by the base
        # 2 raised to power of the index.
    return output


print(to_base10(11111111))


def encrypt(message, shifts, alphabet):
    """"Encrypts a plain text message using an improved Caesar cipher encryption method.

    Args:
    - message (str): The plain text message to be encrypted.
    - shifts (list): A list of n positive integers representing the shift values for each character in the message.
    - alphabet (str): A string representing the alphabet used for encryption. Can be any sequence of symbols.

    Returns:
    - str: The encrypted message.

        """
    encryption = ""
    for (letter, shift_value) in zip(message, shifts):
        # to check if size of the shifts is the same as the size of the
        # message

        if len(shifts) != len(message):
            return None

        if shift_value < 0 or shift_value > len(alphabet):
            # to ensure that every individual shift value is not more
            # than the length of the alphabet or a negative number
            return None

        if letter in alphabet:
            sub_index = (alphabet.index(letter)+shift_value) % len(alphabet)

        elif letter not in alphabet:
            # to check that every letter in the message is in the alphabet
            return None

        encryption += alphabet[sub_index]
    return encryption


# print(encrypt(encryption_info, shift_info, alphabet_info))
