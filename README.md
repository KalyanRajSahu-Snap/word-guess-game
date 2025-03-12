# Word Guessing Game

A Python-based word guessing game (similar to Hangman) with both console and graphical user interface versions. This project demonstrates Python programming fundamentals while providing an entertaining word game with multiple difficulty levels and interactive features.

## Features

### Console Version
- Three difficulty levels with varying word lengths and attempt limits
- ASCII art visualization that updates with each wrong guess
- Sound effects for correct and incorrect guesses
- Color-coded feedback for improved user experience
- Word reveal animation when the player loses
- Player name personalization

### GUI Version (Tkinter)
- Clean, user-friendly graphical interface
- Visual hangman display that updates progressively
- Difficulty selection via radio buttons
- Real-time feedback on guesses and game state
- Tracking of used letters and remaining attempts
- Pop-up notifications for game outcomes

## Installation

### Prerequisites
- Python 3.6 or higher

### Basic Installation
1. Clone the repository:
   ```
   git clone https://github.com/KalyanRajSahu-Snap/word-guess-game.git
   cd word-guess-game
   ```

2. No additional packages are required for basic functionality as the game uses Python's built-in libraries.

### Optional Dependencies (for enhanced console version)
For the console version with color support on Windows:
```
pip install colorama
```

## Usage

### Running the GUI Version
```
python wgg.py
```

In the graphical interface:
1. Select your preferred difficulty level
2. Click "Start Game"
3. Enter letters in the text field and click "Guess" (or press Enter)
4. Monitor your progress with the hangman display and word reveal
5. Start a new game with the "New Word" button when finished

## Customization

### Adding New Words
To add more words to the game:

1. Open either game file in a text editor
2. Locate the word lists near the beginning of the file:
   ```python
   EASY_WORDS = ['cat', 'dog', 'sun', ...]
   MEDIUM_WORDS = ['tiger', 'piano', 'galaxy', ...]
   HARD_WORDS = ['ecosystem', 'boulevard', 'psychology', ...]
   ```
3. Add your own words to the appropriate difficulty level

### Adjusting Difficulty
You can customize the difficulty levels by:
- Changing the number of allowed attempts for each level
- Modifying the word lists to include easier or harder words
- Adjusting the word reveal mechanics

## Project Structure

```
word-guess-game/
├── wgg.py                 # Tkinter GUI version
├── README.md              # This file
└── LICENSE                # License information
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by the classic Hangman game
- ASCII art adapted from traditional hangman visualizations
- Special thanks to the Python community for their excellent documentation and libraries
