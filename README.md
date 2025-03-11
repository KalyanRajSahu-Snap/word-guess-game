# Word Guessing Game

A Python-based word guessing game (similar to Hangman) with both console and graphical user interface versions. This project demonstrates Python programming fundamentals while providing an entertaining word game with multiple difficulty levels and interactive features.

![Word Guessing Game Screenshot](https://via.placeholder.com/800x450.png?text=Word+Guessing+Game+Screenshot)

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
   git clone https://github.com/KalyanRajSahu-Snap/word-guessing-game.git
   cd word-guessing-game
   ```

2. No additional packages are required for basic functionality as the game uses Python's built-in libraries.

### Optional Dependencies (for enhanced console version)
For the console version with color support on Windows:
```
pip install colorama
```

## Usage

### Running the Console Version
```
python word_game_console.py
```

Follow the on-screen prompts to:
1. Enter your name
2. Select difficulty level
3. Guess letters to reveal the hidden word
4. Play again or exit when the game ends

### Running the GUI Version
```
python word_game_ui.py
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
word-guessing-game/
├── word_game_console.py   # Terminal-based version with ASCII art
├── word_game_ui.py        # Tkinter GUI version
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


I've created a comprehensive README file for your Word Guessing Game project that you can use on GitHub. Here are the key sections included:

1. **Project Introduction** - A brief description of what the game is and does
2. **Features** - Separate listings for both console and GUI versions
3. **Installation Instructions** - Prerequisites and step-by-step setup guide
4. **Usage Instructions** - How to run both versions of the game
5. **Customization Guide** - How to add new words or adjust difficulty
6. **Project Structure** - Overview of the repository files
7. **Contributing Guidelines** - Instructions for others who might want to contribute
8. **License Information** - Standard MIT license placeholder
9. **Acknowledgments** - Credits and inspirations

The README includes:
- Placeholder for a screenshot image
- Code blocks with proper formatting for commands
- Structured headings and subheadings for easy navigation
- Clear instructions for both technical and non-technical users
- Tips for customizing the game

This README follows GitHub best practices and provides all the information someone would need to understand, install, and use your project. You can simply copy and paste this into a README.md file in your repository root, and replace the placeholder image link with an actual screenshot once you have one.

Would you like me to modify any section or add additional information to the README?