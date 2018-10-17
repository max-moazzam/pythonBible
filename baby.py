from random import choice

questions = ["Why is the sky blue?: ", "Why do dogs bark?: ", "Why is blue your favorite color?: "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why? :").strip().lower()

print("Oh...Okay")
