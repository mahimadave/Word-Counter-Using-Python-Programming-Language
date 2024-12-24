import tkinter as tk
from tkinter import messagebox
import re

# Function to calculate text statistics
def text_statistics(text):
    words = text.split()
    num_words = len(words)
    num_characters = len(text)
    sentences = re.split(r'[.!?]+', text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    num_sentences = len(sentences)
    average_word_length = sum(len(word) for word in words) / num_words if num_words > 0 else 0
    return num_words, num_characters, num_sentences, round(average_word_length, 2)

# Function to update the statistics in the UI
def update_statistics():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Error", "Please enter some text to analyze.")
        return

    num_words, num_characters, num_sentences, avg_word_length = text_statistics(text)
    
    word_count_label.config(text=f"Total Words: {num_words}")
    char_count_label.config(text=f"Total Characters: {num_characters}")
    sentence_count_label.config(text=f"Total Sentences: {num_sentences}")
    avg_word_length_label.config(text=f"Average Word Length: {avg_word_length}")

# Set up the main window
root = tk.Tk()
root.title("Text Statistics Tool")
root.geometry("400x300")
root.config(bg="#f0f0f0")

# Add a title label
title_label = tk.Label(root, text="Text Statistics Tool", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Create a text input area with a scrollbar
text_input_frame = tk.Frame(root, bg="#f0f0f0")
text_input_frame.pack(pady=10)

scrollbar = tk.Scrollbar(text_input_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_input = tk.Text(text_input_frame, wrap=tk.WORD, height=6, width=40, font=("Arial", 12))
text_input.pack(side=tk.LEFT, padx=10)
scrollbar.config(command=text_input.yview)
text_input.config(yscrollcommand=scrollbar.set)

# Create buttons and labels for statistics
button = tk.Button(root, text="Analyze Text", font=("Arial", 12), command=update_statistics, bg="#4CAF50", fg="white")
button.pack(pady=10)

word_count_label = tk.Label(root, text="Total Words: 0", font=("Arial", 12), bg="#f0f0f0")
word_count_label.pack()

char_count_label = tk.Label(root, text="Total Characters: 0", font=("Arial", 12), bg="#f0f0f0")
char_count_label.pack()

sentence_count_label = tk.Label(root, text="Total Sentences: 0", font=("Arial", 12), bg="#f0f0f0")
sentence_count_label.pack()

avg_word_length_label = tk.Label(root, text="Average Word Length: 0.00", font=("Arial", 12), bg="#f0f0f0")
avg_word_length_label.pack()

# Run the GUI
root.mainloop()
