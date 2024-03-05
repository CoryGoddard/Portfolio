This program is essentially a version of the hangman game

I created this program during spring of 2024 (the current semester) for our first project. I went above and beyond the project requirements because I wanted to learn the material at a faster pace than the class covers.

Original Project Requirements:

- You'll create a simple word guessing game website where the user gets infinite tries to guess the word (like Hangman without the hangman, or like Wheel of Fortune without the wheel and fortune).

- Create two global arrays: one to hold the letters of the word (e.g. 'F', 'O', 'X'), and one to hold the current guessed letters (e.g. it would start with '_', '_', '\_' and end with 'F', 'O', 'X'). You must select a word with at least 5 letters.
- Have 1 input textbox where a user can enter in a single character.
- Have 1 button called guess that calls the function guessLetter.
- The web page will always display the current guessed letters.
- In addition, you need to keep track of the number of guesses the user has made and display this number on the website.
- Write a function called guessLetter that will:
  - Take one argument, the guessed letter.
  - Iterate through the word letters and see if the guessed letter is in there.
  - If the guessed letter matches a word letter, changed the guessed letters array to reflect that.
  - When it's done iterating, it should log the current guessed letters ('F\_\_') and congratulate the user if they found a new letter.
  - It should also figure out if there are any more letters that need to be guessed, and if not, it should congratulate the user for winning the game. Then you need to create 5 different ranges and based upon the number of guesses tell the user how well they did. Example (if the number of guesses is > 20 then display to the user " You are an amateur." otherwise if the number of guesses is > 15 but < 20 the display to the user "You are an ok guesser." ...)
