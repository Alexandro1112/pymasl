# pymasl
Pymasl - Python Mac Alert System Library. Has more features than other libraries such as add icons, widgets, scrollbars to alert.
<h1>installation</h1> <br>
  
```git clone https://github.com/Alexandro1112/pymasl/```


<h2>Consider main methods.</h2>
Create object instance pymasl so easy.
Bellow we create Alert object, and create alert with 
  
  
> title -> str
  
> message -> str
  
> icon -> pymasl.constants | image-file
  
> buttons -> list | tuple | str
  
> width -> int
  
> height -> int
  
```from pymasl.basealert import Alert
from pymasl.constants import WARNING_ICON

sender = Alert()

title = 'My new alert'
message = 'I added to this alert icon'
icon = WARNING_ICON
buttons = ('OK', 'EXIT')
sender.create_alert(title=title, message=message, icon=icon, buttons=buttons, width=30, height=100)
```

And to this alert radio button
> radio_button_width -> int

> radio_button_height -> int

> radio_button_color -> str

> radio_button_border -> int

> radio_button_font -> str ( font name )

> radio_button_title -> str 

> radio_button_font_size -> int

> radio_button_text_rotation -> int

> radio_button_state -> int ( state of button )
```
sender.add_radio_button(radio_button_width=150, radio_button_height=40,
                        radio_button_color='black',
                        radio_button_border=10, radio_button_font='Arial Black',
                        radio_button_title='RadioButton', radio_button_font_size=17,
                        radio_button_text_rotation=0, radio_button_state=0)
```

And send alert.
```
sender.send()
```
