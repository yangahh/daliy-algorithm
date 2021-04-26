# solution1
def complex_number_multiply(a, b):
    a = a.replace("i", "j")
    b = b.replace("i", "j")
    a = a.replace("+-", "-")
    b = b.replace("+-", "-")

    z = complex(a) * complex(b)

    real = int(z.real)
    imag = int(z.imag)

    return f'{real}+{imag}i'

#solution2
#def complex_number_multiply(a, b):
#    a_real, a_imag = a.split('+')
#    b_real, b_imag = b.split('+')
#    
#    a_real, b_real = int(a_real), int(b_real)
#    a_imag = int(a_imag[:len(a_imag)-1]) 
#    b_imag = int(b_imag[:len(b_imag)-1])
#
#    result_real = a_real * b_real + a_imag * b_imag * (-1)
#    result_imag = a_real * b_imag + a_imag * b_real
#
#    return str(result_real) + '+' + str(result_imag) + 'i'
