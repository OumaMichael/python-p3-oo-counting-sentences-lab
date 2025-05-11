#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=""):
        # Use the property setter for validation
        self.value = value

    def __setattr__(self, name, value):
        if name == "value":
            if not isinstance(value, str):
                print("The value must be a string.")
            else:
                super().__setattr__(name, value)
        else:
            super().__setattr__(name, value)

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def is_capitalized(self):
        return bool(self.value) and self.value[0].isupper()

    def count_sentences(self):
        # Split the string into sentences using regex
        sentences = re.split(r'(?<=[.!?]) +', self.value)
        # Filter out empty strings and count the sentences
        return len([s for s in sentences if s.strip()])

# Example usage (for demonstration only):
if __name__ == "__main__":
    string = MyString("Hello world. How are you? I am fine!")
    print(string.count_sentences())  # 3
    print(string.is_sentence())     # False
    print(string.is_question())     # False
    print(string.is_exclamation())  # False
    print(string.is_capitalized())  # True
    # Trigger setter print
    string.value = 123  # Should print: The value must be a string.


