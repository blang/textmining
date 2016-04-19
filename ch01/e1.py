#!env python

from nltk.book import text1


# Every occurrence with context
print text1.concordance("monstrous")

print text1.similar("monstrous")

# S5
