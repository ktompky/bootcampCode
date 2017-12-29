import random

name = input("Enter a name: ")
color = input("Enter a color: ")
noun = input("Enter a noun: ")
adjective = input("Enter an adjective: ")

wordPlay = ["Hi my name is " + name + "." + " I like the color " + color + " and eating " + noun + "(s)" " which makes me a " + adjective + " person."], ["When did being a " + adjective + " small " + noun + " mean that you could just take on the name " + name + " and claim the sky was the color " + color + "."],[Buck is the best]

randPhrase = (random.choice(wordPlay))


print(randPhrase[0])
