from nltk import word_tokenize, sent_tokenize                      #seperate word and sentence
sent = "GeeksforGeeks is a great learning platform.\
It is one of the best for Computer Science students."
print(word_tokenize(sent))
print(sent_tokenize(sent))


from nltk.stem import PorterStemmer                                 #To make root form of word (meaningless)
porter = PorterStemmer()
print(porter.stem("play"))
print(porter.stem("playing"))
print(porter.stem("plays"))
print(porter.stem("played"))

print(porter.stem("Communication"))



from nltk.stem import WordNetLemmatizer                              #To make root form of word (meaningfull)
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("plays", 'v'))
print(lemmatizer.lemmatize("played", 'v'))
print(lemmatizer.lemmatize("play", 'v'))
print(lemmatizer.lemmatize("playing", 'v'))

print(lemmatizer.lemmatize("Communication", 'v'))


from nltk import pos_tag                                              #To find out part of speech
from nltk import word_tokenize

text = "GeeksforGeeks is a Computer Science platform."
tokenized_text = word_tokenize(text)
tags = tokens_tag = pos_tag(tokenized_text)
print(tags) 


from nltk.corpus import stopwords


nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


filtered_words = [word for word in words if word.lower() not in stop_words]
print(filtered_words)
