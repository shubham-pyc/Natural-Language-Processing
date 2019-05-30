from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
example_sentence = "Hello world this is my first nltk program. This is word tokenization in which the we will seperate all the words"
stop_words = set(stopwords.words("english"))  # This will print some of the stop words in english lanaguage
words = word_tokenize(example_sentence)
useful_words = []                             # All the words which are not stop words in our sentence
for w in words:
    if w not in stop_words:
        useful_words.append(w)
print(useful_words)