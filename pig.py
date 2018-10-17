#Get sentence from user
original = input("Give a sentence to translate into Pig Latin: ").strip().lower()

#Split sentence into words
words = original.split()

#Loop through words and convert to pig latin
newWords = []

#If starts with vowel, just add "yay"
for word in words:
    if word[0] in "aeiou":
        newWord = word + "yay"
        newWords.append(newWord)

#Otherwise, move the first consonant cluster to end, and add "yay"
    else:
        vowelPos = 0
        for letter in word:
            if letter not in "aeiou":
                vowelPos = vowelPos + 1
            else:
                break
        cons = word[:vowelPos]
        theRest = word[vowelPos:]
        newWord = theRest + cons + "ay"
        newWords.append(newWord)

#Stick words back together into a sentence
output = " ".join(newWords)

#Output the final string
print(output)
