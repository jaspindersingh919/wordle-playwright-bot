import random

class WordleSolver:
    def __init__(self, word_list):
        self.words = word_list
        self.correct_positions = [None] * 5
        self.present_letters = set()
        self.absent_letters = set()
        self.not_in_position = [set() for _ in range(5)]

    def update_constraints(self, guess, feedback):
        # Update rules based on Wordle feedback
        for i, (letter, state) in enumerate(zip(guess, feedback)):

            if state == "correct":
                # Letter is correct and in the right spot
                self.correct_positions[i] = letter
                self.present_letters.add(letter)

            elif state == "present":
                # Letter is in the word but not in this position
                self.present_letters.add(letter)
                self.not_in_position[i].add(letter)

            elif state == "absent":
                # Only mark absent if it was never seen as present/correct
                if letter not in self.present_letters:
                    self.absent_letters.add(letter)

    def filter_words(self):
        valid = []

        for word in self.words:
            ok = True

            # Check position rules
            for i in range(5):
                if self.correct_positions[i] and word[i] != self.correct_positions[i]:
                    ok = False

                if word[i] in self.not_in_position[i]:
                    ok = False

            # Must include all present letters
            for letter in self.present_letters:
                if letter not in word:
                    ok = False

            # Must NOT include absent letters
            for letter in self.absent_letters:
                if letter in word:
                    ok = False

            if ok:
                valid.append(word)

        self.words = valid
        print("Remaining words:", len(self.words))

    def next_guess(self):
        if not self.words:
            return None

        # First guess: pick a random word
        if len(self.words) > 3000:
            return random.choice(self.words)

        # Later guesses: just take the first remaining word
        return self.words[0]