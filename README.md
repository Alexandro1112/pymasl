▎Notification Library - PyMasl

Welcome to the Notification Library, a simple and elegant way to create and manage notifications in your applications. With this library, you can easily display alerts with customizable options, making it perfect for enhancing user interactions.

▎Features

• Create customizable alerts with titles, messages, icons, and buttons.

• Add custom input fields to gather user input.

• Choose from various alert styles and configurations.

• Easy integration with your existing Python applications.

▎Installation

To install the Notification Library, you can use pip:

``git clone https://github.com/Alexandro1112/pymasl/``


▎Quick Start

Here's a simple example of how to create a notification using the library:
```
from pymasl.basealert import Alert
import AppKit

# Initialize the Alert sender
sender = Alert()

# Define the alert parameters

title = 'My new alert'
message = 'I added to this alert icon'
icon = 'warning'  # You can use predefined icons
buttons = ['OK', 'NO']

# Create and configure the alert
sender.create_alert(title=title, message=message, icon=icon, buttons=buttons, width=30, height=100)

# Optionally customize the alert with additional features
sender.custom_method('showsSuppressionButton', None)  # Example of adding a suppression button

# Add an entry field for user input
sender.add_entry(width=100, height=50, border=4, color='white', text_color='black', font='Arial', font_size=15)

# Send the alert to the user
sender.send()

# Output the result of the user's interaction
print(sender.pressed_button, sender.entry_text)
```


▎Explanation of the Script

1. Importing Required Modules: The script imports the Alert class from the pymasl.basealert module and AppKit for macOS GUI support.

2. Initializing the Alert Sender: An instance of Alert is created, which will be used to configure and display the notification.

3. Defining Alert Parameters: The title, message, icon type, and button labels are defined. You can customize these parameters to suit your needs.

4. Creating the Alert: The create_alert method is called on the sender object to set up the alert with the specified parameters, including its dimensions.

5. Customizing the Alert: The custom_method allows you to add additional features to the alert; in this case, a suppression button is added.

6. Adding Input Entry: The add_entry method creates an input field within the alert for user interaction. You can customize its appearance with various parameters.

7. Sending the Alert: The send method displays the alert to the user.

8. Capturing User Interaction: After the alert is closed, you can access which button was pressed and any text entered in the input field through pressed_button and entry_text.

▎Documentation

For more detailed information on all available methods and options, please refer to the Documentation.

▎Contributing

We welcome contributions! If you have suggestions for improvements or new features, please open an issue or submit a pull request.
