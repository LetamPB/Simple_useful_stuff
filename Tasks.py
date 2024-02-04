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
