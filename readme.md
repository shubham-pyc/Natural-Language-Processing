# Natural Langauge Processing


## Corpora
They are just body of text. Ex: medical journals

---

## Lexicon
Words and their means, i.e it is an dictionary<br>
For example: 
Here is a scinerio of two people speakings one if an invetor and another is a laymay
* __Bull__ for investor is someone who is positive about the market
* __Bull__ for a layman is an animal
---
## Tokenizing
It is the process of grouping things
1. Word tokenizers
```python
    from nltk.tokenize import word_tokenize
    text = "Hello world this is my first nltk program. This is word tokenization in which the we will seperate all the words "
    print(word_tokenize(text))
```
2. Sentence Tokenizers
```python
    from nltk.tokenize import sent_tokenize
    text = "Hello world this is my first nltk program. This is word tokenization in which the we will seperate all the words "
    print(sent_tokenize(text))
```
---
## Stop Words
They are just the filler words which doesn't give any insight about the sentence to the machine like: a, an, the. We as humans need these stop words to understand by for data analysis they are useless
```python
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
example_sentence = "Hello world this is my first nltk program. This is word tokenization in which the we will seperate all the words"
stop_words = set(stopwords.words("english"))  # This will print some of the stop words in english lanaguage
words = word_tokenize(example_sentence)
useful_words = []                             # All the words which are not stop words in our sentence
for w in words:
    if w not in stop_words:
        useful_words.append(w)
```
---
## Steming
Stemming is a process of cutting prefix and suffix from the word which  extracts the root of the word for better understanding

```python
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
example_words = ["python","pythoner","pythoning","pythoned","pythonly"]     
## All of these words are in differnet parts of speech we just want the root which is python

for w in example_words:
    print(ps.stem(w))
```

---
## Part of Speech Tagging
This is the process of tagging a particular word with it's part of speech i.e: Noun, Pronoun, Adjective etc.

```python
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
    except Exception as e:
        print(str(e))

```
|Abbreviation| Part of Speech|
|-------|--------------|
|CC|coordinating conjunction|
|CD|cardinal digit|
|DT|determiner|
|EX|existential there (like: "there is" ... think of it like "there exists")|
|FW|foreign word|
|IN|preposition/subordinating conjunction|
|JJ|adjective	'big'|
|JJR|adjective, comparative	'bigger'|
|JJS|adjective, superlative	'biggest'|
|LS|list marker	1)|
|MD|modal	could, will|
|NN|noun, singular 'desk'|
|NNS|noun plural	'desks'|
|NNP|proper noun, singular	'Harrison'|
|NNPS|proper noun, plural	'Americans'|
|PDT|predeterminer	'all the kids'|
|POS|possessive ending	parent\'s|
|PRP|personal pronoun	I, he, she|
|PRP\$|possessive pronoun	my, his, hers|
|RB|adverb	very, silently,|
|RBR|adverb, comparative	better|
|RBS|adverb, superlative	best|
|RP|particle	give up|
|TO|to	go 'to' the store.|
|UH|interjection	errrrrrrrm|
|VB|verb, base form	take|
|VBD|verb, past tense	took|
|VBG|verb, gerund/present participle	taking|
|VBN|verb, past participle	taken|
|VBP|verb, sing. present, non-3d	take|
|VBZ|verb, 3rd person sing. present	takes|
|WDT|wh-determiner	which|
|WP|wh-pronoun	who, what|
|WP\$|possessive wh-pronoun	whose|
|WRB|wh-abverb	where, when|
---
## Named Entity Recognition
Nltk provides a powerful tool which recognized the named entity from the data set

```python
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEnt = ntlk.ne_chink(tagged)
            namedEnt.draw()
    except Exception as e:
        print(str(e))
```