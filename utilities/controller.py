import sys
sys.path.append("..")

from userscreen.user_screen import UserGUI, root
from textscreen.text_screen import EnterTextGUI
from profilescreen.profile_screen import ProfileGUI
from utilities.controller_variables import screen_variables

screens = {"user_screen" : UserGUI(), "text_screen" : EnterTextGUI(), 
           "profile_screen" : ProfileGUI()}

class Controller:

    @staticmethod
    def hide_viewable_canvas():
        for _, screen in screens.items():
            if screen.canvas.winfo_viewable():
                screen.hide_canvas()

    @staticmethod
    def screen_variable_check():
        for screen, boolean in screen_variables.items():
            if boolean:
                screen_variables[screen] = False
                screens[screen].show_canvas()
                Controller.hide_viewable_canvas()
        root.after(1, Controller.screen_variable_check)

Controller.screen_variable_check()