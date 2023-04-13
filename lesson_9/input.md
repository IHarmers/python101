# Input Handling

There is going to be a time where your application needs to process input from the outside world.
Your application can ingest user input in many different ways. Lets take a look at some
common examples.

## Asking questions

The [ask_questions](ask_questions.py) script demonstrates the most simple usage of the *input* function.
This function allows you to ask a question to the user. The user is then given the opportunity to type
their answer. The function will block the further execution of your script until it receives
the user's answer. Whatever the user typed will be returned by the function and can be
saved in a variable.

Try to run the script by yourself with `python3 ./ask_credentials.py`. Introduce another question
and ask for the users age or favorite food.

## Asking credentials

Handling sensitive user input (like passwords) is a bit different than regular input.
The [ask_credentials](ask_credentials.py) script demonstrates how it's done.

Your can run the script like this `python3 ask_credentials.py`. The script will then
prompt you for a password. Access will be denied when you enter the wrong password and it
will be granted if you enter the right one.

The asking of the password happens in the *ask_pass* function:

```python

import hashlib
from getpass import getpass

def ask_pass():
    clear_password = getpass()
    hashed_password = hashlib.sha256(clear_password.encode())
    return hashed_password.hexdigest()

```

First we import the *getpass* function from the *getpass* module. This function will
prompt the user for their password. The function will not print the typed characters
on the screen like the *input* function does.

From there on, we hash the retrieved password by using the *sha256* function from
the *hashlib* module. A hashing algorithm takes any data as input and gives a
unique fixed length string as output.

Hashing is only one way. You can never turn the output string back into the data which
was used as input.

You can play around with the different hashing algorithms
[on this website](https://cyberchef.org/#recipe=SHA2('256',64,160)). Try to input
different values and see what the output is. Maybe you can even guess what the
right password is.

## Taking command line arguments

Python has a builtin module for handling command line arguments. This allows you to create
programs which will behave differently depending on the arguments supplied by the user.

The [program_args](program_args.py) script demonstrates the use of command line arguments.
The script simply shows the contents of supplied file name. I have included a text file called
[input.txt](input.txt) in the lesson folder. You can use this file to test the script.

You can run the script with the following command `python3 program_args.py input.txt`. The script
can also display line numbers if you want. Just append ` --line_numbers` to the end of the previous
command.

Let's break this script down:

```python
1. import argparse
```
Here we import the argparse module. The module is part of Python and will parse
all the input the user has provided and makes it accessible in a structured
way.

```python
4.    parser = argparse.ArgumentParser(description="Show contents of a file")
5.    parser.add_argument("file", help="The file which needs to be shown", type=str)
6.    parser.add_argument("-l", "--line_numbers", help="Show line numbers", action="store_true", default=False)
7.    parser_args = parser.parse_args()
```
Here we create the parser object and provide description of our script (line 4). Then
we define two arguments for our program. The first one on line 5 is a positional
argument called 'file'. Positional arguments are mandatory and should be supplied
on the command line in the order they are defined. Optional arguments are not
mandatory and you need to use their name.

These arguments have short and long names. The short name starts with a single hyphen ('-') and
the long name starts with two hyphens ('--'). At line 6 we use '-l' as the short name and
'--line_numbers' as the long name. So running `python3 program_args.py input.txt -l`
and `python3 program_args.py input.txt --line_numbers` will have the same effect.

On the last line (7) we use the `parse_args()` function to parse the supplied user arguments
and store them in the `parser_args` variable.

The rest of the code reads and prints the given file:

```python
9.     try:
10.        with open(parser_args.file, mode="r") as file:
11.            if parser_args.line_numbers:
12.                line_count = 1
13.                for line in file:
14.                    print("{} {}".format(line_count, line))
15.                    line_count = line_count + 1
16.            else:
17.                for line in file:
18.                    print(line)
19.    except FileNotFoundError:
20.        print("Given file was not found")
21.    except PermissionError:
22.        print("No permissions to read file")
```

A with statement is used to safely open and close the file. The file will be automatically closed
for us when the with block ends. The [open](https://docs.python.org/3/library/functions.html#open)
function can be used to open a file, allowing you read from or write to it. In this chase we are
only opening the file in read mode.

You can also see how we access the user supplied arguments on line 9 and 10. You can access
positional arguments by using their name and optional arguments by using their long name.

## Using configuration files

As your program grows using argparse for all user configuration becomes too complex.
Users don't like it when they have to supply a bazillion arguments on the command line
in order to use you program.

The solution in this case is to store all these arguments in a configuration file and let the
program read the file and retrieve all the options it needs.

Configuration files can take on different formats. Some are written in XML and others in JSON.
We are going to make use of Python's [ConfigParser](https://docs.python.org/3/library/configparser.html)
module. Take a look at the [program_config](program_config.py) script. It's a modified version of the
[program_args](program_args.py) script.

This is the most important difference:

```python
10.    config = ConfigParser()
11.    config.read(parser_args.config)
12.    line_numbers = config["DEFAULT"].getboolean("show_line_numbers")
```

The argparse module has been configured to ask for a file to display the contents of, and a
configuration file to read all the options from. The path of the configuration file
will be fed to the ConfigParser. The parser will then read the file and make
the options available to us.

Use the following command to run the program:

```python
python3 program_config.py input.txt input.config
```

The [input.config](input.config) file contains a section called 'DEFAULT'. This section has
one option called 'show_line_numbers' which has the value of 'no'. Try changing it to 'yes'
and run the program again.

You can create multiple sections in one configuration file. These sections allow you to group
related options together. You could create sections like 'video', 'audio' and 'subtitles' when
you are creating a video player for example.
