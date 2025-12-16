a = '3' 
b = '5'
k = 2
number_str = str(number)

has_a = a in number_str

no_b = b not in number_str

count_a = number_str.count(a)
more_than_k = count_a > k

has_both = (a in number_str) and (b in number_str)
