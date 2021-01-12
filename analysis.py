import pronouncing

with open('words.txt', 'r') as input_file:
    data = input_file.readlines()

cleaned_words = [word.strip() for word in data]

def get_pronunciation(word):
    return pronouncing.phones_for_word(word)

def get_stresses(word):
    return list(set(pronouncing.stresses_for_word(word)))

with open('stress-set.txt', 'w') as output_file:

    for item in cleaned_words:
        output_file.write('{}  :  {}'.format(item, get_stresses(item)))
        output_file.write('\n')
