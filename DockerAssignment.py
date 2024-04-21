import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punk')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

with open("paragraphs.txt", 'r') as file:
    text = file.read().replace('\n', '')

word_tokens = word_tokenize(text)

filtered_text = [word for word in word_tokens if not word in stop_words]

word_freq = Counter(filtered_text)

for word, count in word_freq.items():
    print(f'Word: {word}, Frequency: {count}')
