# Print and Input Functions

## 1. HelloWorldName

Write some code that prints `hello, world` to the terminal using the `print` function.

Then upgrade the code so that it greets the user. First, prompt them to enter their name. Then, capture their input using the `input` function. Finally, print `Hello, <user's name>` to the terminal. Demonstrate: 

* printing on two separate lines
* printing on one line by providing the `print` function an `end` argument
* printing on one line by joining the strings
* printing on one line by providing two string arguments to the `print` function

# String Methods

## 2. HelloFullName

Prompt the user three times: for their first name, their last name, and their nickname. Then greet them with a terminal message like: 

```Hello <firstname> <lastname>, or should I say, <nickname>.```

Then upgrade the code using [string methods](https://docs.python.org/3/library/stdtypes.html#string-methods]) so that:
* it removes any leading or trailing spaces from the user's input
* it capitalizes each of the user's names when printing them

## 3. WelcomeBanner

Prompt the user for their given name. Then greet them with a banner that looks like:
```
--------------------------------------------------------------------------------
|                              Welcome <username>                              |
--------------------------------------------------------------------------------
```
where the text is centered on a terminal of width 80. Use [string methods](https://docs.python.org/3/library/stdtypes.html#string-methods]) to center the text and generate the banner.