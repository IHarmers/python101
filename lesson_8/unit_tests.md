# Testing your code

Writing program code is one thing, but how can you be certain that every thing still 
works as intended after you make changes to your program? The answer to this question is 
Unit Tests. Unit Tests consists of code to test your program code. Simply put: code to 
test other code.

Python supports Unit Tests by default. Lets take a look at the following 
example: [counter.py](counter.py). Run the script to see the magic happen.

At first you will have to import the `inittest` modules which contains the `TestCase` class
and the `main` function we need to run our test cases. The goal is to make tests for the
counter class we have created. We define a new class called `TestCounter` and let it
inherit the functionality of the `TestCase` class.

The `setUp` function allows to do some prep work. Here we create a `Counter` object which
can be used by each of our tests. The `setUp` function will be executed before the start
of each test in order to guaranty that each test has a freshly initiated `Counter` object.

Each function named with the "test_" prefix will be seen as a test and automatically
executed by the testing framework. It is important to not only test if your functions
work properly, but also fails properly.

We test the increase and decrease functionality with the `test_increase` and `test_descrease` tests.
And verify that a RuntimeError is raised when the count is decreased below zero with the
`test_decrease_failure` test.
