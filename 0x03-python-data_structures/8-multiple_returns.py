#!/usr/bin/python3

def multiple_returns(sentence):
    tuple_1 = (len(sentence), sentence[0])
    return tuple_1

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))