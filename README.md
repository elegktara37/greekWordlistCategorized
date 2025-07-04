# Greek categorized wordlist
This wordlist has Greek words, written in lowercase and with tonos. Also there is a category next to each word

# Usage
The wordlist is ideal to use for games where you need greek words depending on different categories.

# Categories
There are 15 diffent categories (for example months, colors, buildings, fruits etc)

# How to use the wordlist

from word_loader import load_words_with_categories, get_words_by_category, get_all_categories

word_list = load_words_with_categories()

# Get all categories
categories = get_all_categories(word_list)

# Get words only from specific categories
selected_categories = ["Ζώα", "Φρούτα"]
filtered_words = [entry for entry in word_list if entry[1] in selected_categories]

# Or use the helper:
words_in_ζώα = get_words_by_category("Ζώα", word_list)
