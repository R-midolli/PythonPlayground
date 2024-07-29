import PySimpleGUI as sg
import pandas as pd

# Path to the CSV file containing login data
csv_file = 'sample_users.csv'  # Name of the CSV file with user credentials

# Load the data from the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)

# Define the theme and layout for the GUI
sg.theme('Reddit')
layout = [
    [sg.Text('Username'), sg.Input(key='username')],
    [sg.Text("Password"), sg.Input(key='password', password_char="*")],
    [sg.Checkbox("Remember me?")],
    [sg.Button("Login")]
]

# Create a window with the title 'Login Screen' and the defined layout
window = sg.Window('Login Screen', layout)

# Main event loop for the GUI to monitor events
while True:
    event, values = window.read()  # Read events and values from the interface
    if event == sg.WIN_CLOSED:  # If the window is closed, exit the loop
        break
    if event == "Login":  # If the 'Login' button is clicked
        username = values["username"]  # Get the value from the 'Username' field
        password = values['password']   # Get the value from the 'Password' field
        
        # Check if the provided username and password match any records in the DataFrame
        if (df['Name'] == username).any() and (df['Password'] == password).any():
            sg.popup(f"Welcome, {username}!")  # Show a welcome message
            window.close()  # Close the window after successful login
            break  # Exit the loop to end the program
        else:
            sg.popup("Incorrect username or password. Please try again.")  # Show an error message

# Close the window when the loop ends
window.close()
