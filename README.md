# Python CLI Calculator

A simple, interactive Command Line Interface (CLI) calculator built with Python. This project demonstrates basic arithmetic operations and the use of ASCII character encoding for logic handling.

## 🚀 Features

- **Basic Arithmetic**: Performs Addition (`+`), Subtraction (`-`), Multiplication (`*`), and Division (`/`).
- **ASCII Logic**: Uses character encoding (`ord()`) to identify operations, showcasing a unique approach to conditional logic.
- **Continuous Loop**: Allows users to perform multiple calculations without restarting the program.

## 🛠️ How It Works

Instead of direct string comparison, this calculator converts the user's operator input into its corresponding **ASCII value**. 

For example:
- `+` becomes `43`
- `-` becomes `45`
- `*` becomes `42`
- `/` becomes `47`

The program then uses these integer values to execute the correct mathematical operation.

## 📋 Prerequisites

- Python 3.x installed on your system.

## 🏃 Usage

1. Clone this repository or copy the script.
2. Run the script using your terminal:
```bash
   python calculator.py
   
