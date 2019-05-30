from nltk.tokenize import sent_tokenize, word_tokenize

text = """
This is python and it is awesome. I really like this lanaugae and we will be working on this and everything is going Greate Mr. Shubham is my name.
Hi How are you doing? I am doing find
"""
print(sent_tokenize(text))
print(word_tokenize(text))

