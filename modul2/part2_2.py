#String Format

#method format

my_str="text {}"
print(my_str.format('''example'''))
my_str="text {1} {0}"
print(my_str.format('example1', 'example2'))
my_str="text {ex1} {ex2}"
print(my_str.format(ex1='example1', ex2='example2'))

#formated string

ex1='example1'
ex2='example2'
print(f"text {ex1}")
print(f"text {2}")
print(f"text {ex1} {ex2} {ex1}")

#len function

ex1='example1'
print(len(ex1))







