"""
Program: generator.py

Generates and dixplays sentences using simple grammar
and vocabulary.  Words are chosen at random.

"""

import random

# vocabulary: words in 4 different parts of speech
articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")

def sentence():
  # builds and returns a sentence
  return nounPhrase() + ' ' + verbPhrase()

def nounPhrase():
  # builds and returns a noun phrase
  return random.choice(articles) + ' ' + random.choice(nouns)

def verbPhrase():
  # builds and returns a verb phrase
  return random.choice(verbs) + ' ' + nounPhrase() + ' ' + ' ' + prepositionalPhrase()

def prepositionalPhrase():
  # builds and returns a prepositional phrase
  return random.choice(prepositions) + ' ' + nounPhrase()

def main():
  # allows the user to input the number of sentences to generate
  number = int(input('Enter the number of sentences: '))
  for count in range(number):
    print(sentence())

if __name__ == "_main_":
  main()
