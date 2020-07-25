import random

while True:
    statement = input("Am I the greatest(answer truthfully)? ")
    answers = ["yes", "sure", "David rules over all", "poof"]
    answers2 = ["Yar", "LIES", "yoink"]
    lies = ["LIES", "Anardur One", "Anudur Run", "slander", "Ur my sun Luke *audible gasp*"]
    if statement.lower() in answers:
        print("Yar")
    elif statement in answers2:
        print("yoink")
    else:
        print(lies[random.randint(0,len(lies)-1)])