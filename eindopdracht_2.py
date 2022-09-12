
import random

punct = (".", ";", "!", "?", ",")
count = 0
new_word = ""

with open("myfile.txt", 'r') as fin:
    for line in fin.readlines():  # Lees elke regel in het txt bestand
        for word in line.split():  # per regel: lees elk woord in deze regel
            if len(word) > 3:  # If woord grotte >3

                # todo verbeter deze code. Momenteel doet dit niets.
                new_word += word + " "

                # todo
                '''If word ends with punctuation
                      Remove firstletter, lastletter and punctuation
                      Shuffle the words
                      Add the removed letters (first letter)
                      Add the removed letters (last letter)
                      Add the removed letters (punctuation mark)'''

                # todo

                '''If there is no punctuation mark
                    Remove first letter and last letter
                    Shuffle the word
                    Add the removed letters (first letter)
                    Add the removed letters (last letter)
                    Append the word and " " to the previous words'''

                # todo

            '''If word length <3 just append the word and " " to the previous words'''

        else:
            new_word = new_word + word + " "

with open(("myfile-Scrambled.txt"), 'a+') as fout:
    fout.write(new_word + "\n")

new_word = ""