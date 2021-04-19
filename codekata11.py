def complex_number_multiply(a, b):
    a = a.replace("i", "j")
    b = b.replace("i", "j")
    a = a.replace("+-", "-")
    b = b.replace("+-", "-")

    a = complex(a)
    b = complex(b)

    z = a * b
    x = z.real
    y = z.imag

    result = str(int(x))+'+'+str(int(y))+'i'

    return result


complex_number_multiply("1+-1i", "1+-1i")
