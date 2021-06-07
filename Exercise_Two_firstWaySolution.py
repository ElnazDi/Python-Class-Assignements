# Assignment 1 - Exercise 2 (First way solution - Main Solution)
# Elnaz Dehkharghani - MatriculationNumber: 11015404
# Last Version For Submission

def function1(value):
    return value


def function2(func):
    return func()


def function3():
    def func():
        return 'from 3'
    return func


print(function1(function2(function3())))
