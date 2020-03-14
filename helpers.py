import numpy as np

# Conversion of quantized level to binary
def ADC(numpy_array):
    numpy_array = numpy_array.astype('int64')
    for i in range(0, len(numpy_array)):
        numpy_array[i] = bin(numpy_array[i]).replace('0b', '')
    return numpy_array

# Length normalization of converted binary bits
def lengthNormalizer(numpy_array):
    output_array = []
    for i in range(0, len(numpy_array)):
        output_array.append(format(numpy_array[i], '015d'))
    return output_array

# Converts array of normalized binary numbers into a long string\n",
def binaryAdder(ys_length_normalized):
    result = ""
    for bit in ys_length_normalized:
        result += bit
    return result
