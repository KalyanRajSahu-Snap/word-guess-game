import tkinter as tk
from tkinter import messagebox, ttk
import random
import time

class WordGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Guessing Game")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        # Word lists by difficulty
        self.EASY_WORDS = ['cat', 'dog', 'sun', 'hat', 'bed', 'fish', 'bird', 'cake', 'tree', 'frog']
        self.MEDIUM_WORDS = ['tiger', 'piano', 'galaxy', 'python', 'castle', 'jungle', 'wizard', 'oxygen']
        self.HARD_WORDS = ['ecosystem', 'boulevard', 'psychology', 'astronaut', 'philosophy', 'chemistry']
        
        self.max_attempts = 6
        self.attempts = 0
        self.secret_word = ""
        self.guessed_letters = set()
        self.game_active = False
        self.difficulty = "medium"
        
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the main user interface elements"""
        # Title
        title_label = tk.Label(self.root, text="Word Guessing Game", font=("Arial", 24, "bold"),
                              bg="#f0f0f0", fg="#333333")
        title_label.pack(pady=20)
        
        # Game container frame
        self.game_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.game_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Left panel for hangman display
        self.left_panel = tk.Frame(self.game_frame, bg="#ffffff", width=300, height=300, 
                                 relief="ridge", bd=2)
        self.left_panel.pack(side="left", padx=10, pady=10, fill="both", expand=True)
        
        # Hangman display
        self.hangman_display = tk.Label(self.left_panel, bg="#ffffff", font=("Courier", 14))
        self.hangman_display.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Right panel for game controls
        self.right_panel = tk.Frame(self.game_frame, bg="#ffffff", relief="ridge", bd=2)
        self.right_panel.pack(side="right", padx=10, pady=10, fill="both", expand=True)
        
        # Difficulty selection
        difficulty_frame = tk.Frame(self.right_panel, bg="#ffffff")
        difficulty_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(difficulty_frame, text="Difficulty:", bg="#ffffff", font=("Arial", 12)).pack(side="left")
        
        self.difficulty_var = tk.StringVar(value="medium")
        easy_rb = tk.Radiobutton(difficulty_frame, text="Easy", variable=self.difficulty_var, 
                               value="easy", bg="#ffffff", command=self.set_difficulty)
        medium_rb = tk.Radiobutton(difficulty_frame, text="Medium", variable=self.difficulty_var, 
                                 value="medium", bg="#ffffff", command=self.set_difficulty)
        hard_rb = tk.Radiobutton(difficulty_frame, text="Hard", variable=self.difficulty_var, 
                               value="hard", bg="#ffffff", command=self.set_difficulty)
        
        easy_rb.pack(side="left", padx=5)
        medium_rb.pack(side="left", padx=5)
        hard_rb.pack(side="left", padx=5)
        
        # Word display
        self.word_display = tk.Label(self.right_panel, text="", font=("Arial", 24, "bold"), 
                                   bg="#ffffff")
        self.word_display.pack(pady=20)
        
        # Used letters display
        self.used_letters_label = tk.Label(self.right_panel, text="Used Letters:", bg="#ffffff",
                                        font=("Arial", 12))
        self.used_letters_label.pack(pady=5)
        
        self.used_letters_display = tk.Label(self.right_panel, text="", bg="#ffffff", 
                                          font=("Arial", 12))
        self.used_letters_display.pack(pady=5)
        
        # Attempts remaining
        self.attempts_label = tk.Label(self.right_panel, text="Attempts: 0/6", bg="#ffffff",
                                     font=("Arial", 12, "bold"))
        self.attempts_label.pack(pady=10)
        
        # Letter input
        input_frame = tk.Frame(self.right_panel, bg="#ffffff")
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Enter a letter:", bg="#ffffff", font=("Arial", 12)).pack(side="left")
        
        self.letter_entry = tk.Entry(input_frame, width=5, font=("Arial", 14), justify="center")
        self.letter_entry.pack(side="left", padx=10)
        self.letter_entry.bind("<Return>", lambda event: self.guess_letter())
        
        self.guess_button = tk.Button(input_frame, text="Guess", command=self.guess_letter,
                                    font=("Arial", 12), bg="#4CAF50", fg="white", width=8)
        self.guess_button.pack(side="left", padx=5)
        
        # Game control buttons
        button_frame = tk.Frame(self.right_panel, bg="#ffffff")
        button_frame.pack(pady=20, fill="x")
        
        self.start_button = tk.Button(button_frame, text="Start Game", command=self.start_game,
                                    font=("Arial", 12), bg="#2196F3", fg="white", width=12)
        self.start_button.pack(side="left", padx=10, expand=True)
        
        self.new_word_button = tk.Button(button_frame, text="New Word", command=self.start_game,
                                       font=("Arial", 12), bg="#FF9800", fg="white", width=12,
                                       state="disabled")
        self.new_word_button.pack(side="right", padx=10, expand=True)
        
        # Status message
        self.status_label = tk.Label(self.root, text="Welcome! Select difficulty and press Start Game",
                                   font=("Arial", 10, "italic"), bg="#f0f0f0", fg="#666666")
        self.status_label.pack(pady=10)
        
        # Initialize the hangman display
        self.update_hangman_display()
    
    def set_difficulty(self):
        """Set the difficulty level based on radio button selection"""
        self.difficulty = self.difficulty_var.get()
        
        if self.difficulty == "easy":
            self.max_attempts = 7
        elif self.difficulty == "medium":
            self.max_attempts = 6
        else:  # hard
            self.max_attempts = 5
            
        self.attempts_label.config(text=f"Attempts: 0/{self.max_attempts}")
        self.status_label.config(text=f"Difficulty set to {self.difficulty.capitalize()}")
    
    def start_game(self):
        """Start a new game"""
        # Select word based on difficulty
        if self.difficulty == "easy":
            self.secret_word = random.choice(self.EASY_WORDS)
        elif self.difficulty == "medium":
            self.secret_word = random.choice(self.MEDIUM_WORDS)
        else:  # hard
            self.secret_word = random.choice(self.HARD_WORDS)
        
        # Reset game state
        self.attempts = 0
        self.guessed_letters = set()
        self.game_active = True
        
        # Update UI
        self.update_word_display()
        self.update_hangman_display()
        self.used_letters_display.config(text="")
        self.attempts_label.config(text=f"Attempts: 0/{self.max_attempts}")
        self.status_label.config(text=f"Game started! Guess a letter.")
        self.letter_entry.config(state="normal")
        self.guess_button.config(state="normal")
        self.start_button.config(state="disabled")
        self.new_word_button.config(state="normal")
        
        # Set focus to the letter entry
        self.letter_entry.delete(0, tk.END)
        self.letter_entry.focus_set()
    
    def guess_letter(self):
        """Process the player's letter guess"""
        if not self.game_active:
            return
        
        # Get the player's guess
        guess = self.letter_entry.get().lower()
        self.letter_entry.delete(0, tk.END)
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            self.status_label.config(text="Please enter a single letter")
            return
            
        # Check if letter was already guessed
        if guess in self.guessed_letters:
            self.status_label.config(text=f"You already guessed '{guess}'")
            return
            
        self.guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in self.secret_word:
            self.status_label.config(text=f"Good guess! '{guess}' is in the word")
        else:
            self.attempts += 1
            self.status_label.config(text=f"Wrong guess! '{guess}' is not in the word")
            
        # Update UI
        self.update_word_display()
        self.update_hangman_display()
        self.update_used_letters()
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")
        
        # Check win/lose conditions
        self.check_game_state()
    
    def update_word_display(self):
        """Update the display of the word being guessed"""
        display = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        self.word_display.config(text=display)
    
    def update_used_letters(self):
        """Update the display of letters that have been guessed"""
        letters = " ".join(sorted(self.guessed_letters))
        self.used_letters_display.config(text=letters)
    
    def update_hangman_display(self):
        """Update the hangman ASCII art based on current attempts"""
        stages = [
            # 0 wrong attempts
            """
            +---+
            |   |
                |
                |
                |
                |
            =========
            """,
            # 1 wrong attempt
            """
            +---+
            |   |
            O   |
                |
                |
                |
            =========
            """,
            # 2 wrong attempts
            """
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========
            """,
            # 3 wrong attempts
            """
            +---+
            |   |
            O   |
           /|   |
                |
                |
            =========
            """,
            # 4 wrong attempts
            """
            +---+
            |   |
            O   |
           /|\\  |
                |
                |
            =========
            """,
            # 5 wrong attempts
            """
            +---+
            |   |
            O   |
           /|\\  |
           /    |
                |
            =========
            """,
            # 6 wrong attempts
            """
            +---+
            |   |
            O   |
           /|\\  |
           / \\  |
                |
            =========
            """
        ]
        
        stage_idx = min(self.attempts, len(stages) - 1)
        self.hangman_display.config(text=stages[stage_idx])
    
    def check_game_state(self):
        """Check if the player has won or lost"""
        # Check if player has won
        if all(letter in self.guessed_letters for letter in self.secret_word):
            self.game_active = False
            messagebox.showinfo("Congratulations!", f"You've guessed the word: {self.secret_word}")
            self.status_label.config(text="You won! Press 'New Word' to play again.")
            self.letter_entry.config(state="disabled")
            self.guess_button.config(state="disabled")
            self.start_button.config(state="normal")
            return
            
        # Check if player has lost
        if self.attempts >= self.max_attempts:
            self.game_active = False
            messagebox.showinfo("Game Over", f"You've run out of attempts. The word was: {self.secret_word}")
            self.status_label.config(text="Game over! Press 'New Word' to play again.")
            self.letter_entry.config(state="disabled")
            self.guess_button.config(state="disabled")
            self.start_button.config(state="normal")
            # Reveal the word
            self.word_display.config(text=" ".join(self.secret_word))
    
    def reveal_word_animation(self):
        """Animate revealing the word one letter at a time"""
        # This is implemented as a visual effect in the GUI
        current_display = ["_"] * len(self.secret_word)
        
        def update_letter(index=0):
            if index < len(self.secret_word):
                current_display[index] = self.secret_word[index]
                self.word_display.config(text=" ".join(current_display))
                self.root.after(300, lambda: update_letter(index + 1))
        
        update_letter()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    game = WordGuessingGame(root)
    root.mainloop()