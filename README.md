# FlashCardApp #

## Description ##

This Python application helps you learn a new language by displaying flashcards with the word in one language on the front and its translation in the other language on the back. You can customize the application with your own flashcards stored in a CSV file.

## Features ##

1)Displays flashcards with French words on the front and English translations on the back.

2)Keep track of viewed words to avoid repetition.

3)Allows customization when provided with custom csv.

4)Save the words user could not identify and then read from that csv on subsequent run.

## Prerequisite ##

1)Clone this repo

```bash
   git clone https://github.com/GakuruAlex/FlashCardApp.git
```

or

Fork repo

2)Navigate to the project folder

```bash
       cd FlashCardApp
```

3)Instal a virtual environment for the Project Note: The following create a new virtual environment in current directory.

```bash
       python -m venv myvenv
```

4)Activate the virtual environment.

```bash
   source myvenv/bin/activate
```

## Installing ##

With the virtual env activated, run

   ```markdown
       pip install -r requirements.txt*
   ```

within the project directory.

## Usage ##

From the project directory Run

   ```bash
      python main.py
   ```

When the app launches, click start to begin the sequence. Use the button with red "X" to mark words you didn't identify.They will be saved in words_to_learn.csv for later reference.

## Contributing ##

a)Report bugs: If you encounter any bugs, please let us know. Open up an issue and let me know the problem.

b)Suggestions: If you don't want to code but have some awesome ideas, open up an issue explaining some updates or improvements you would like to see!

## Future updates ##

1.Implementing audio playback for pronunciation.

2.Tracking user progress and displaying statistics.

## License ##

This application is provided under the MIT license. See the LICENSE file for details.
