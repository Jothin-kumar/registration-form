from guizero import App, Text, TextBox, PushButton
from datetime import datetime

fileName = datetime.now()

app = App(height=287, layout='grid', title='Registration form')

def register():
    with open(fileName.strftime('%d %B %Y %H %M %S') + '.txt', 'w') as registry:
        registry.write('First name: ' + firstNameTextBox.value + ' ')
        registry.write('Last name: ' + lastNameTextBox.value + ' ')
        registry.write('Phone number: ' +phoneNumberTextBox.value + ' ')
        registry.write('E-mail: ' + emailTextBox.value + ' ')
        registry.write('Address: ' + addressTextBox.value + ' ')
        app.info('Registration successful!', 'Congratulations! Your have been successfully registered!')

firstNameText = Text(app, grid=[0,1], text= 'First name')
lastNameText = Text(app, grid=[0,2], text= 'Last name')
phoneNumberText = Text(app, grid=[0,3], text= 'Phone number')
emailText = Text(app, grid=[0,4], text= 'E-mail')
addressText = Text(app, grid=[0,5], text= 'Address')

firstNameTextBox = TextBox(app, grid=[1,1], width=20)
lastNameTextBox = TextBox(app, grid=[1,2], width=20)
phoneNumberTextBox = TextBox(app, grid=[1,3], width=20)
emailTextBox = TextBox(app, grid=[1,4], width=20)
addressTextBox = TextBox(app, grid=[1,5], width=20)

registerButton = PushButton(app, command=register, grid=[1,6], text='Register')
registerButton.bg = 'green'
registerButton.text_color = 'white'

app.display()