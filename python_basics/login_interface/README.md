# Login Interface

This project provides a simple login interface using Python and PySimpleGUI.

## Overview

The `login_interface.py` script creates a graphical user interface (GUI) for logging in. It reads user credentials from a CSV file and validates them.

## Files

- `login_interface.py`: The main script that runs the login interface.
- `requirements.txt`: Lists the required Python packages.

## How It Works

1. **Load Data**: The script loads user credentials from `sample_users.csv` into a pandas DataFrame.
2. **Create GUI**: It sets up a window with fields for username, password, and a checkbox to remember the login.
3. **Handle Events**:
   - When the "Login" button is clicked, it checks if the provided username and password match any entry in the CSV file.
   - If the credentials are correct, it displays a welcome message and closes the window.
   - If the credentials are incorrect, it shows an error message.

## Running the Script

To run the login interface, execute the following command in your terminal:

```bash
python login_interface.py
