student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}


import pandas
student_data_frame = pandas.DataFrame(student_dict)

df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}
print(phonetic_alphabet)

def generate_phonetic():
    try:
        user_input = input("enter your word: ").upper()
        int(user_input)
    except ValueError:
        list1 = [user_input for user_input in user_input]
        final = []
        for i in list1:
            if i in phonetic_alphabet:
                final.append(phonetic_alphabet[i])
        print(final)
    else:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
generate_phonetic()
