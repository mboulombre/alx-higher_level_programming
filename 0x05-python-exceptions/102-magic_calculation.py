def magic_calculation(a, b):
    result = 0
    try:
        for i in range(1, 4):
            if a > i:
                raise Exception('Too far')
            result += b // i if type(b) is int and b % i == 0 else a ** i
        result += a + b
    except:
        pass
    return result
