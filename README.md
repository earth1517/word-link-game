# Word Link Game 🔗

This project is inspired by a YouTube game show called **"คำต้องเชื่อม"** ("Words Must Connect"). In this game, players take turns saying words while ensuring that no syllables are repeated within the round. For example, if someone says **"rectangle",** the next person can't say **"triangle" ** because both words share the syllable **"gle".**

On the show, repeated syllables are manually 📝 checked by assistants or judges, which can be slow and sometimes inaccurate. This project was created to automate that process, making the game more efficient and fair.


## Overview

This project is built using Python 🐍 and Tkinter 🖥️ for the graphical user interface. It also leverages the pythainlp library for accurate Thai syllable tokenization.

🔧 **How It Works:**

🏗️ Syllable Extraction: When a word is entered, the app uses pythainlp.tokenize.syllable_tokenize() to break it into syllables.

🔄 Comparison Logic: The syllables are stored in a set, and each new word's syllables are checked against existing ones to detect repetitions.

🎨 Visual Feedback: If a word contains a repeated syllable, it is highlighted in red for easy detection.

🖱️ User Interaction: The interface allows users to add or remove words and resets the game when needed.


## Features

This tool makes it easier to track repeated syllables during the game, ensuring accuracy and a smoother gameplay experience.

- 📝 **Add Words**: Input words and have their syllables automatically extracted.
- 🔎 **Detect Repetitions**: Instantly see if any syllables have been repeated within the round.
- 🎨 **User-Friendly Interface**: A simple and intuitive design to keep the game flowing smoothly.


## How to Use

1. ▶️ **Run the Application**: Launch the app using Python 🐍.
2. ⌨️ **Enter Words**: Type in words as they are said during the game.
3. 🚨 **Monitor Syllables**: The app will highlight 🔴 any repeated syllables in red, making it easy for players to spot and avoid mistakes.

---


🎉 Have fun playing "คำต้องเชื่อม"!

