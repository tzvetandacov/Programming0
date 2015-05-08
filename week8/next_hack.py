def dec_to_bin(x):
    return bin(x)[2:]

def reverse_str(string):
    result = ""
    for ch in string:
        result = ch + result
    return result


def is_palindrome(str):
    return str == reverse_str(str)


def char_histogram(string):
    result = {}

    for ch in string:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1


    return result


def hack_number(n):
    bin_n = dec_to_bin(n)
    histogram = char_histogram(bin_n)

    return is_palindrome(bin_n) and histogram['1'] % 2 == 1


def next_hack(n):
    n += 1

    while not hack_number(n):
        n += 1

    return n


print(hack_number(8191))


