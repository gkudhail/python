pip3 install spacy
import spacy

nlp = spacy.load('en_core_web_md')
#nlp = spacy.load('en_core_web_sm')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("bannana")

print(word1.similarity(word2))
print(word2.similarity(word2))
print(word3.similarity(word1))

#main modue is not found :/opt/homebrew/opt/python@3.12/bin/python3.12: can't find '__main__' module 

tokens = nlp('cat apple monkey bannana ')
for token1 in tokens:
	for token2 in tokens:
		print(token1.text, token2.text, token1.similarity(token2))


sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go", "Hello, there is my car", "I\ve lost my car in my car", "I\'d like my boat back", "I\'d like my boat back", "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
	similarity = nlp(sentence).similarity(model_sentence)
print(sentence + "-" + similarity)
