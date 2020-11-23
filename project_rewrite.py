def min(x, y):
    if x <= y:
        return x
    else:
        return y
  

def max(values_list):
    if len(values_list) == 0:
        return 0
    max = values_list[0]
    for elem in values_list:
        if elem > max:
            max = elem
    return max


def len(values_list):
    count = 0
    for elem in values_list:
        count += 1
    return count


def multiply(x, y):
    result = 0
    for i in range(y):
        result += x
    return result


def pow(x, y):
    result = 1
    for i in range(y):
        result *= x
    return result


def divmod(x, y):
    quotient = 0
    remainder = 0
    mylist = [0, 0]
    if y == 0:
        return None
    while x-y >= 0:
        quotient += 1
        x -= y
    remainder = x
    mylist[0] = quotient
    mylist[1] = remainder
    return mylist


if __name__ == '__main__':
    print(divmod(12, 5))