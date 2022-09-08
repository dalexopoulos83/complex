
""" Simply Python implementation to support complex numbers
    and the basic mathematical operations """


class ComplexNum:

    def __init__(self, real, imag=0):
        if not isinstance(real+imag, (float, int)):
            raise ValueError("Only int and float are supported")
        self.real = real
        self.imag = imag

    def __add__(self, complex_b):
        real_2, imaginary_2 = complex_b.readComplex()
        real = self.real + real_2
        imaginary = self.imag + imaginary_2
        return self.displayComplex(real, imaginary)

    def __sub__(self, complex_b):
        real_2, imaginary_2 = complex_b.readComplex()
        real = self.real - real_2
        imaginary = self.imag - imaginary_2
        return self.displayComplex(real, imaginary)

    def __mul__(self, complex_b):
        real_2, imaginary_2 = complex_b.readComplex()
        real = self.real * real_2 - self.imag * imaginary_2
        imaginary = self.real * imaginary_2 + real_2 * self.imag
        return self.displayComplex(real, imaginary)

    def __truediv__(self, complex_b):
        real_2, imaginary_2 = complex_b.readComplex()
        real_t = self.real * real_2 + self.imag * imaginary_2
        real = real_t / (real_2 ** 2 + imaginary_2 ** 2)
        imaginary_t = self.real * imaginary_2 - self.imag
        imaginary = imaginary_t / (real_2 ** 2 + imaginary_2 ** 2)
        return self.displayComplex(real, imaginary)

    def __pow__(self, my_pow):
        res_real = self.real
        res_img = self.imag
        if my_pow > 1:
            for index in range(my_pow - 1):
                res_real, res_img = self.InnerMultiplyComplex(res_real, res_img, self.real, self.imag)
        return self.displayComplex(res_real, res_img)

    # this is a function for internal use when we calculate the complex exponential
    def InnerMultiplyComplex(self, real_1, imaginary_1, real_2, imaginary_2):
        real = real_1 * real_2 - imaginary_1 * imaginary_2
        imaginary = real_1 * imaginary_2 + real_2 * imaginary_1
        return real, imaginary

    def readComplex(self):
        return self.real, self.imag

    # This function is used to display complex numbers
    def displayComplex(self, rel, img):
        if img >= 0:
            res = str(round(rel)) + "+" + str(round(img)) + "j"
            print(res)
            return res
        else:
            res = str(round(rel)) + str(round(img)) + "j"
            print(res)
            return res

# TODO: The math operations should be able to accept more than one value

# TODO: The ability to do sequential meth operations e.g. add 3 complex numbers

# TODO: The rest of math operations

# TODO: The ability to make operations with other numerical types

# TODO: The ability to handle python natively complex numbers (without creating object etc)
