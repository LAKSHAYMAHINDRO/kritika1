def count_vowels(sentence):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    for char in sentence:
        if char in vowels:
            vowel_count += 1
    return vowel_count

# Sentence is defined here
sentence = "This is a sample sentence containing vowels."

# Count vowels in the sentence
print("Number of vowels:", count_vowels(sentence))
