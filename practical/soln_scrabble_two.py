# scrabble project two
# Using file 113809of.fic identify how many words have:
# 1. two or more vowels
# 2. three or more vowels
# 3. four or more vowels
# 4. five or more vowels
# 5. the most vowels
# 6. no vowels

import pprint
fin = open('113809of.fic').readlines()

vowels = 'aeiou'
vowel_count = dict()
max_count = 0


for line in fin:
    count = 0
    line = line.strip()
    for letter in line:
        if letter in vowels:
            count += 1

    if count > max_count:
        longest = []
        longest.append(line)
        max_count = count
    elif count == max_count:
        longest.append(line)

    vowel_count[count] = vowel_count.get(count, 0) + 1

print('These are the counts:\n')
pprint.pprint(vowel_count)
print('\nThe word(s) with the most vowels, had:', max_count, 'vowels')
print('\nThe words with the most vowels include:', longest)
