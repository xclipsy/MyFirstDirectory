# Daily Blocker Tracker

A simple Python CLI tool to help developers document and track their daily blockers before they reach out to their team for support. 

## 📝 Description

This script handles the **persistence** of a user's daily blocker by saving it to a local text file (`database.txt`). Depending on the user's input, it will either safely append the new entry or intentionally **overwrite** the entire database after a confirmation warning. Later, the program can **fetch** the stored blockers to display them, allowing the user to review their documented issues before they **reach out** to their team for help.

## ✨ Features

* **Quick Logging:** Prompts the user to quickly type in their current daily blocker.
* **Safe Appending:** Default route safely adds new blockers to the end of the file without deleting history.
* **Hard Reset (Overwrite):** Allows users to wipe the slate clean and overwrite the file, guarded by a yes/no safety warning.
* **Fetch History:** Includes a `fetch_blocker()` function that reads back all stored blockers if the file is not empty.

## 🚀 How to Use

1. **Clone the repository** or download the Python script to your local machine.
2. **Run the script** via your terminal:
   ```bash
   python blocker_tracker.py
   ```
   *(Note: Replace `blocker_tracker.py` with whatever you named your file).*
3. **Follow the prompts:**
   * Enter your daily blocker.
   * Choose `a` to append to your running list, or `w` to overwrite it.
4. **View your blockers:**
   To see your list of blockers, you can add `fetch_blocker()` to the bottom of your Python script, or import it into another file.

## 📂 File Structure

* `[your_script_name].py`: The main script containing the logic.
* `database.txt`: Automatically generated upon running the script. This is where your blockers are stored. (You may want to add `database.txt` to your `.gitignore` file so you don't accidentally push your personal blockers to a public repository).

---
*Created to keep blockers clear, concise, and courteous.*

## 💻 Author

*Luis Guerrero*

** GITHUB REPOSITORY: https://github.com/xclipsy/MyFirstDirectory/tree/Daily-blocker-tracker**
