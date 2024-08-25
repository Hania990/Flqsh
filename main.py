from flet import *
def main(page:Page):
    page.title = 'Flash Light'
    page.window.width = 390
    page.window.height = 740
    page.theme_mode = ThemeMode.DARK
    page.scroll = 'auto'
    page.add(
        AppBar(
            bgcolor= colors.BLACK87,
            title= Text('Flash Light' ),
            color= colors.WHITE,
            center_title= True,
            actions=(
                IconButton(icons.SETTINGS , on_click= PermissionHandler.open_app_settings),
            ),
        ),
        Row([
            Text("\n شغل النور يا شطور" , size= 30 , color= colors.BLUE_100  ),
        ],alignment=MainAxisAlignment.CENTER),
        
        Row([
            Image(src='flashlight.png' , width= 250)
        ],alignment=MainAxisAlignment.CENTER),

        Row([
            ElevatedButton('On' , width= 150 , style= ButtonStyle(bgcolor= colors.BLACK , padding= 15 , shape= ContinuousRectangleBorder(radius=100)),
                           on_click= Flashlight.turn_on),
            ElevatedButton('Off' , width= 150 , style= ButtonStyle(bgcolor= colors.BLACK , padding= 15 , shape= ContinuousRectangleBorder(radius=100)),
                           on_click= Flashlight.turn_off)
        ],alignment=MainAxisAlignment.CENTER)
        
    )
    page.update()
app(main)
