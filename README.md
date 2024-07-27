# Python Playground

This repository is a space to explore and share Python projects and code snippets. It serves as a practical example of creating a simple login interface using PySimpleGUI and managing user credentials with a CSV file.

## Project Overview

This project includes:

- `login_interface.py`: A Python script that creates a graphical login interface using PySimpleGUI. It reads user credentials from a CSV file and authenticates user input.
- `sample_users.csv`: A CSV file containing sample user data, including usernames and passwords, used for authentication in the `login_interface.py` script.

## How It Works

- The `login_interface.py` script provides a basic login interface with fields for username and password. Upon clicking the "Enter" button, it checks the provided credentials against the data in `sample_users.csv`.
- If the credentials match, a welcome message is displayed, and the interface closes. If not, an error message prompts the user to try again.

## Getting Started

1. **Clone the Repository**

   ```bash
   git clone https://github.com/R-midolli/PythonPlayground.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd PythonPlayground
   ```

3. **Install Required Packages**
   - Make sure you have the necessary Python packages installed. You can install them using pip:

     ```bash
     pip install PySimpleGUI pandas
     ```

4. **Run the Login Interface**
   - Execute the Python script to launch the login interface:

     ```bash
     python login_interface.py
     ```

## Contributing

Feel free to contribute by creating issues, submitting pull requests, or providing feedback.

## License

This project is licensed under the [MIT License](LICENSE).
