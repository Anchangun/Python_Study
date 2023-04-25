letter='o'
if letter == 'a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
    print(letter,'is a vowel')
else :
    print(letter, 'is not a vowel')


print("===================")

vowels ='aeiou'
letter = 'o'
print("letter in vowels :",letter in vowels)
if letter in vowels :
    print(letter,"is a vowel")

list_data =[1,2,3]
if 1 in list_data:
    print("list_data_true")


print("===================")

letter='o'
vowel_set = {'a','e','i','o','u'}
print(letter in vowel_set)
vowel_list = ['a','e','i','o','u']
print(letter in vowel_list)
vowel_tuple = ('a','e','i','o','u')
print(letter in vowel_tuple)
vowel_string="aeiou"
print(letter in vowel_string)
vowel_dict = {'a':'apple','e':'elephant','o':'ocelot','i':'imala','u':'unicorn'}
print(letter in vowel_dict)
