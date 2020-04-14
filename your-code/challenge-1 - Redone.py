print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')

# Place words / numbers into dictionary so that when a word form of a number is referenced it returns the numeric version.
num_words = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10}

# I take the 'a' variable, iterate over the items of the num_words dictionary and extract the corresponding value

val_one = 0
for key, value in num_words.items():
    if key == a:
        val_one += value

# I take the 'b' variable, iterate over the items of the num_words dictionary and extract the corresponding value

val_two = 0
for key, value in num_words.items():
    if key == c:
        val_two += value

# I take the 'b' variable, iterate over the items of the num_words dictionary and extract the corresponding value
num_value = 0
    
if b == 'plus':
    result = val_one + val_two
    num_value = num_value + result

if b == 'minus':
    result = val_one - val_two
    num_value = num_value + result

final_value = ''
for key, value in num_words.items():
    if num_value == value:
        final_value = final_value + key

if num_value >= 0:
    print(a,b,c,'equals',final_value)
elif num_value < 0:
    print(a,b,c,'equals negative',final_value)
