# Error handling

Error handling is an important aspect of software development. In my opinion, it
differentiates a bad software developer from a good one.

A bad software developer focuses on functionality only. A good software developer also focuses
on everything that can go wrong.

The first script that I have prepared for this lesson is the [crash](crash.py) script.
If you run the script you will get an output similar to the code block below.

```bash
python3 crash.py 

Traceback (most recent call last):
  File "/Users/valentijnharmers/Projects/python101/lesson_5/crash.py", line 4, in <module>
    sum = number_one + number_two
TypeError: can only concatenate str (not "int") to str
```

As you can see, our program has failed with an error. Python helps us with finding and
resolving the error by displaying helpful information. It tells us that the crash happened
in the crash.py program on line 4. It also displays the exact line where the error occurred
and what the error was.

We tried summing up a number and a string value and this caused a TypeError. These errors
are revered to as exceptions. Python has a collection of builtin exceptions. An overview can be found [here](https://docs.python.org/3/library/exceptions.html).

The trick to properly handling these exceptions is to catch them. Take a look at the
[better_crash](better_crash.py) script. Here we use a try-except block to try and execute
a line of code and catch the TypeError if it is raised from the function.

Note that Python uses the name 'except' instead of 'catch'. I have always found this a bit
strange since other programming languages such as Java or C# do use the word 'catch'. I prefer
the word 'catch' myself, because is better describes what we are doing.

## Creating your own exceptions

Apart from raising the build-in exceptions, you can create and raise your own exceptions.
The [custom_error](custom_error.py) script will show you how to do this. Note that this
script uses a new concept called classes. You will learn everything about classes in the
next lesson, so it might be wise to skip this script for now and revisit it once your are
done with lesson 6.

## Don't overdo it

You might be tempted to create something like this:

```python
try:
    do_stuff()
except BaseException:
    print("Something went wrong!")
```

The goal of error management is to either correct errors or
if this isn't possible, to clearly tell the user what has gone wrong
and how the problem can be fixed.

The code above does tell the user that something went wrong, but
doesn't tell the user what exactly went wrong. Sometimes it's just
better to 'let it rip'.

I know stack traces are not very user friendly, but they are better
than generic error messages which don't help with finding out what
has gone wrong.

## A note about performance

Another thing you have to look out for when working with exceptions
is performance. Raising and exception so now and then is not going to
have a noticeable impact on performance,
but raising a lot of them is going to slow down your program. 
Raising exceptions is resource intensive since a traceback as to 
be generated for every raised exception.

The [performance](preformance.py) script is a modified version of the
[custom_error](custom_error.py) script. The `guess_name` function
now returns a boolean indicator instead of a string.

I have left the ValueError in the code, since I don't expect it will
be raised often.
