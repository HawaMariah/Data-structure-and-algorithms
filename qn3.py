import string
def word_frequency(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency

#test
sentence = "This is a test sentence. This is a test sentence."
result = word_frequency(sentence)
print(result)
