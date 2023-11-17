# Print and Input Functions, and String Methods

1. `eeyore_birthday_gift.py`
  
    Prompt the user for a gift idea. Print the gift idea, except capitalize each word, so that a user input of
    
    ```
    a very useful pot
    ```
    
    would be printed
    ```
    A Very Useful Pot
    ```
    
    We cannot use `.capitalize()` here because that only converts the first letter of the whole string into uppercase, but there is another [string method](https://docs.python.org/3/library/stdtypes.html#str.title) that can be used.
  
1. `emojify_text_message.py`

    Prompt the user for a text message. Print the text message to the terminal console where any instances of ":)" are [replace](https://docs.python.org/3/library/stdtypes.html#string-methods)d with the [slightly smiling emoji](https://emojipedia.org/slightly-smiling-face), 🙂, and any instances of ":(" are replaced by the [slightly frowning emoji](https://emojipedia.org/slightly-frowning-face), 🙁.

1. `make_username.py`

    Prompt the user for input twice: first for their full name, then for their favorite number between 1 and 99. Print a username for them. Their username should consist of their full name with each part of the name capitalized and any spaces removed (i.e. replaced with a blank string "") followed by their favorite number, zero padded if necessary (i.e. **z**ero **fill**ed to a width of 2).

    For example:

    Full name | Favorite number | username 
    ---|---|---
    sophie emma halifax | 7 | SophieEmmaHalifax07
    Tom Waits | 82 | TomWaits82

1. `voice_level.py`
    
    Ask the user for a message to amplify. Print this message so that it is all uppercase, and any periods are replaced with exclamation points.

    Ask the user for a message to soften. Print this message so that it is all lowercase, and any exclamation points are replaced with periods.
