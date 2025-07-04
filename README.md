# Greek categorized wordlist
This wordlist has Greek words, written in lowercase and with tonos. Also there is a category next to each word

# Usage
The wordlist is ideal to use for games where you need greek words depending on different categories.

# Categories
There are 15 diffent categories (for example months, colors, buildings, fruits etc)

# How to use the wordlist
In the main file type folowing:

`from word_loader import load_words_with_categories, get_words_by_category, get_all_categories`  
`word_list = load_words_with_categories()`

To Get all categories  

`categories = get_all_categories(word_list)`  

To Get words only from specific categories  

`selected_categories = ["Ζώο", "Φρούτο"]`  
`filtered_words = [entry for entry in word_list if entry[1] in selected_categories]`  

Or use the helper:  

`words_in_animal = get_words_by_category("Ζώο", word_list)`
