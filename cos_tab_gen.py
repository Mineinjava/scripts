from math import pi, cos

DOMAIN_BITS = 12

cos_range = [0, pi]
cos_domain = [0, (1 << DOMAIN_BITS) - 1]

cos_range_delta = cos_range[1] - cos_range[0]
cos_domain_delta = cos_domain[1] - cos_domain[0]

def function(x):
    return cos(x)

numbers = [function((x * cos_range_delta / cos_domain_delta + min(cos_range))) for x in range(cos_domain[1])]

print(numbers)

