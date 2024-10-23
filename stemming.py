from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
 
ps = PorterStemmer()
 
words = ["running", "runner", "ran", "run", "runs"]
 
for w in words:
    print(w, " : ", ps.stem(w))