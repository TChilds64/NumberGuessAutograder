import numberGuess as ng
import random as r
import contextlib as cl

file = 'NumberAutoGrade.txt'
correct = ng.generateNumber()
guesses = [r.randint(0, 100) for i in range(4)]
guesses.append(correct)
itr = iter(guesses)

with open(file, 'w') as f:
    with cl.redirect_stdout(f):
        ng.autoguessingGame(correct, itr)

f = open(file, 'r')
line = f.readline()

new_itr = iter(guesses)
answers = 0
while line:
    val = next(new_itr)
    if val < correct:
        comp = line.find("low")
    elif val > correct:
        comp = line.find("high")
    else:
        comp = line.find("win")
    
    if comp >= 0:
        answers += 1
    else:
        print("Incorrect for guess: " + str(val) + "\n")

    line = f.readline()
f.close()

print("Final grade is: " + str(answers/5 * 100) + "%")