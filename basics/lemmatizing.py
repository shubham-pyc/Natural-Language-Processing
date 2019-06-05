from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("better")) # prints better
print(lemmatizer.lemmatize("better", pos="a")) # prints good