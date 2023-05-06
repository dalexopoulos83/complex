
""" Simply Python implementation to support complex numbers
    and the basic mathematical operations """
import numbers


class ComplexNum:

    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag
        if not isinstance(self.real, numbers.Number) or not isinstance(self.imag, numbers.Number):
            print("Only numerical types supported")
            raise ValueError

    def __str__(self):
        if self.imag < 0:
            if isinstance(self.real, float):
                return "%f%fj" % (self.real, self.imag)
            else:
                return "%d%dj" % (self.real, self.imag)
        else:
            if isinstance(self.real, float):
                return "%f+%fj" % (self.real, self.imag)
            else:
                return "%d+%dj" % (self.real, self.imag)

    def __eq__(self, other):
        if self.real == other.real and self.imag == other.imag:
            return

    def __add__(self, complex_b):
        if isinstance(complex_b, int) or isinstance(complex_b, float):
            complex_b = ComplexNum(complex_b)
        real = self.real + complex_b.real
        imaginary = self.imag + complex_b.imag
        return ComplexNum(real, imaginary)

    def __sub__(self, complex_b):
        if isinstance(complex_b, int) or isinstance(complex_b, float):
            complex_b = ComplexNum(complex_b)
        real = self.real - complex_b.real
        imaginary = self.imag - complex_b.imag
        return ComplexNum(real, imaginary)

    def __mul__(self, complex_b):
        if isinstance(complex_b, int) or isinstance(complex_b, float):
            complex_b = ComplexNum(complex_b)
        real = self.real * complex_b.real - self.imag * complex_b.imag
        imaginary = self.real * complex_b.imag + complex_b.real * self.imag
        return ComplexNum(real, imaginary)

    def __truediv__(self, complex_b):
        if isinstance(complex_b, int) or isinstance(complex_b, float):
            complex_b = ComplexNum(complex_b)
        real_t = self.real * complex_b.real + self.imag * complex_b.imag
        real = real_t / (complex_b.real ** 2 + complex_b.imag ** 2)
        imaginary_t = self.imag * complex_b.real - self.real * complex_b.imag
        imaginary = imaginary_t / (complex_b.real ** 2 + complex_b.imag ** 2)
        return ComplexNum(real, imaginary)

    def __pow__(self, my_pow):
        res_real = self.real
        res_img = self.imag
        if my_pow > 1:
            for index in range(my_pow - 1):
                res_real, res_img = self.inner_multiply_complex(res_real, res_img, self.real, self.imag)
        return ComplexNum(res_real, res_img)

    # this is a function for internal use when we calculate the complex exponential
    def inner_multiply_complex(self, real_1, imaginary_1, real_2, imaginary_2):
        real = real_1 * real_2 - imaginary_1 * imaginary_2
        imaginary = real_1 * imaginary_2 + real_2 * imaginary_1
        return real, imaginary

    __rtruediv__ = __truediv__
    __rmul__ = __mul__
    __rsub__ = __sub__
    __radd__ = __add__

# TODO: The rest of math operations

# TODO: The ability to handle python natively complex numbers (without creating object etc)
