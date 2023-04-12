from pathlib import Path
from json import loads, dumps
from cryptography.fernet import Fernet
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, ttk, NO
from os import chdir, path, listdir
from random import randint
from operator import add, sub, floordiv, mul
from datetime import datetime
from pygame import mixer

chdir(path.dirname(path.abspath(__file__)))
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

windowcolor = "#3556FB"
window = Tk()
window.geometry("800x500")
window.configure(bg = windowcolor)
window.title('Tkinter Math Flash Cards')
window.iconbitmap('main.ico')

startscreen_canvas = Canvas(window, bg = windowcolor, height = 500, width = 800, bd = 0, highlightthickness = 0, relief = "ridge")
mainscreen_canvas = Canvas(window, bg = windowcolor, height = 500, width = 800, bd = 0, highlightthickness = 0, relief = "ridge")
optionsscreen_canvas = Canvas(window, bg = windowcolor, height = 500, width = 800, bd = 0, highlightthickness = 0, relief = "ridge" )
finalscreen_canvas = Canvas( window, bg = windowcolor, height = 500, width = 800, bd = 0, highlightthickness = 0, relief = "ridge" )
historyscreen_canvas = Canvas( window, bg = windowcolor, height = 500, width = 800, bd = 0, highlightthickness = 0, relief = "ridge" )
userscreen_canvas = Canvas( window, bg = windowcolor, height = 500, width = 800, bd = 0, highlightthickness = 0, relief = "ridge" )
profilescreen_canvas = Canvas( window, bg = windowcolor, height = 500, width = 800, bd = 0, highlightthickness = 0, relief = "ridge" )



class sound_class():
    mixer.pre_init(44100, -16, 1, 512)
    mixer.init()
    sound_correct = mixer.Sound("assets/sounds/correct.wav")
    sound_countdown_tick = mixer.Sound("assets/sounds/countdowntick.wav")
    sound_timer_tick = mixer.Sound("assets/sounds/timertick.wav")
    sound_wrong = mixer.Sound("assets/sounds/wrong.wav")
    sound_buttonpress = mixer.Sound("assets/sounds/buttonpress.wav")
    sound_win = mixer.Sound("assets/sounds/win.wav")
    sound_times_up = mixer.Sound("assets/sounds/timesup.wav")
    # sound_countdown_end = mixer.Sound("assets/sounds/countdownend.wav")

    def muted_all_sounds(volume):
        sound_class.sound_correct.set_volume(volume)
        sound_class.sound_countdown_tick.set_volume(volume)
        sound_class.sound_timer_tick.set_volume(volume)
        sound_class.sound_wrong.set_volume(volume)
        sound_class.sound_buttonpress.set_volume(volume)
        sound_class.sound_win.set_volume(volume)
        sound_class.sound_times_up.set_volume(volume)
    
class userscreen_class():
    #Images
    image_bg_image = PhotoImage( file=relative_to_assets("bg_image.png"))
    image_mainbanner = PhotoImage( file=relative_to_assets("userscreen/mainbanner.png"))
    image_usertitle_bg = PhotoImage( file=relative_to_assets("userscreen/usertitle_bg.png"))
    image_usertitle_bg_selected = PhotoImage( file=relative_to_assets("userscreen/usertitle_bg_selected.png"))
    image_usericon_bg = PhotoImage( file=relative_to_assets("userscreen/usericon_bg.png"))
    image_usericon_bg_selected = PhotoImage( file=relative_to_assets("userscreen/usericon_bg_selected.png"))
    image_actionbutton_banner = PhotoImage( file=relative_to_assets("userscreen/actionbutton_banner.png"))
    image_actionbutton_bg = PhotoImage( file=relative_to_assets("userscreen/actionbutton_bg.png"))
    image_actionbutton_bg_selected = PhotoImage( file=relative_to_assets("userscreen/actionbutton_bg_selected.png"))
    image_usericon = PhotoImage( file=relative_to_assets("userscreen/usericon.png"))
    image_useradd = PhotoImage( file=relative_to_assets("userscreen/useradd.png"))
    image_backbutton = PhotoImage( file=relative_to_assets("userscreen/backbutton.png"))
    image_userremove = PhotoImage( file=relative_to_assets("userscreen/userremove.png"))
    image_popup_banner = PhotoImage( file=relative_to_assets("userscreen/popup_banner.png"))
    image_popup_text = PhotoImage( file=relative_to_assets("userscreen/popup_text.png"))
    image_ok_bg = PhotoImage( file=relative_to_assets("userscreen/ok_bg.png"))
    image_ok_bg_selected = PhotoImage( file=relative_to_assets("userscreen/ok_bg_selected.png"))
    image_ok = PhotoImage( file=relative_to_assets("userscreen/ok.png"))
    image_newuser_banner = PhotoImage( file=relative_to_assets("userscreen/newuser_banner.png"))
    image_newuser_text = PhotoImage( file=relative_to_assets("userscreen/newuser_text.png"))
    image_entry_bg = PhotoImage( file=relative_to_assets("userscreen/entry_bg.png"))
    image_verify_bg = PhotoImage( file=relative_to_assets("userscreen/verify_bg.png"))
    image_verify_bg_selected = PhotoImage( file=relative_to_assets("userscreen/verify_bg_selected.png"))
    image_cancel = PhotoImage( file=relative_to_assets("userscreen/cancel.png"))
    image_confirm = PhotoImage( file=relative_to_assets("userscreen/confirm.png"))
    image_delete_confirm_banner = PhotoImage( file=relative_to_assets("userscreen/delete_confirm_banner.png"))
    image_delete_confirm_bg = PhotoImage( file=relative_to_assets("userscreen/delete_confirm_bg.png"))
    image_delete_confirm_bg_selected = PhotoImage( file=relative_to_assets("userscreen/delete_confirm_bg_selected.png"))
    image_del_confirm_yes = PhotoImage( file=relative_to_assets("userscreen/del_confirm_yes.png"))
    image_del_confirm_no = PhotoImage( file=relative_to_assets("userscreen/del_confirm_no.png"))
    #Placed Elements
    bg_image = userscreen_canvas.create_image( 395.0, 255.0, image=image_bg_image)
    mainbanner = userscreen_canvas.create_image( 400.0, 219.0, image=image_mainbanner )
    usertitle0_bg = userscreen_canvas.create_image( 436.0, 99.0, image=image_usertitle_bg )
    usertitle1_bg = userscreen_canvas.create_image( 436.0, 178.0, image=image_usertitle_bg )
    usertitle2_bg = userscreen_canvas.create_image( 436.0, 257.0, image=image_usertitle_bg )
    usertitle3_bg = userscreen_canvas.create_image( 436.0, 336.0, image=image_usertitle_bg )
    usericon0_bg = userscreen_canvas.create_image( 299.0, 99.0, image=image_usericon_bg )
    usericon1_bg = userscreen_canvas.create_image( 299.0, 178.0, image=image_usericon_bg )
    usericon2_bg = userscreen_canvas.create_image( 299.0, 257.0, image=image_usericon_bg )
    usericon3_bg = userscreen_canvas.create_image( 299.0, 336.0, image=image_usericon_bg )
    backbutton_banner = userscreen_canvas.create_image( 288.0, 453.0, image=image_actionbutton_banner )
    backbutton_bg = userscreen_canvas.create_image( 288.0, 452.0, image=image_actionbutton_bg )
    userremove_banner = userscreen_canvas.create_image( 511.0, 453.0, image=image_actionbutton_banner )
    userremove_bg = userscreen_canvas.create_image( 512.0, 452.0, image=image_actionbutton_bg )






    button_usertitle0 = Button(userscreen_canvas, text='', fg="#000000", bg="#D9D9D9", anchor="w", font=("Encode Sans", 27 * -1), borderwidth=0, highlightthickness=0, command=lambda: userscreen_class.log_into_user(0), relief="flat" )
    button_usertitle0.place( x=352.0, y=76.5, width=170.0, height=47.0 )
    button_usertitle0.config(activebackground="#C3C3C3")
    def user0_button_onenter(event): event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(userscreen_class.usertitle0_bg, image=userscreen_class.image_usertitle_bg_selected)
    def user0_button_onleave(event): event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(userscreen_class.usertitle0_bg, image=userscreen_class.image_usertitle_bg)
    button_usertitle0.bind("<Enter>", user0_button_onenter)
    button_usertitle0.bind("<Leave>", user0_button_onleave)


    button_usertitle1 = Button(userscreen_canvas, text='', fg="#000000", bg="#D9D9D9", anchor="w", font=("Encode Sans", 27 * -1), borderwidth=0, highlightthickness=0, command=lambda: userscreen_class.log_into_user(1), relief="flat" )
    button_usertitle1.place( x=352.0, y=155.5, width=170.0, height=47.0 )
    button_usertitle1.config(activebackground="#C3C3C3")
    def user1_button_onenter(event): event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(userscreen_class.usertitle1_bg, image=userscreen_class.image_usertitle_bg_selected)
    def user1_button_onleave(event): event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(userscreen_class.usertitle1_bg, image=userscreen_class.image_usertitle_bg)
    button_usertitle1.bind("<Enter>", user1_button_onenter)
    button_usertitle1.bind("<Leave>", user1_button_onleave)

    # de_button = Button(userscreen_canvas, command=lambda: print(userscreen_class.button_usertitle1.winfo_x(), userscreen_class.button_usertitle1.winfo_y()))
    # de_button.place(x=100, y=100, width= 20, height= 20)



    button_usertitle2 = Button(userscreen_canvas, text='', fg="#000000", bg="#D9D9D9", anchor="w", font=("Encode Sans", 27 * -1), borderwidth=0, highlightthickness=0, command=lambda: userscreen_class.log_into_user(2), relief="flat" )
    button_usertitle2.place( x=352.0, y=233.5, width=170.0, height=47.0 )
    button_usertitle2.config(activebackground="#C3C3C3")
    def user2_button_onenter(event): event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(userscreen_class.usertitle2_bg, image=userscreen_class.image_usertitle_bg_selected)
    def user2_button_onleave(event): event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(userscreen_class.usertitle2_bg, image=userscreen_class.image_usertitle_bg)
    button_usertitle2.bind("<Enter>", user2_button_onenter)
    button_usertitle2.bind("<Leave>", user2_button_onleave)


    button_usertitle3 = Button(userscreen_canvas, text='', fg="#000000", bg="#D9D9D9", anchor="w", font=("Encode Sans", 27 * -1), borderwidth=0, highlightthickness=0, command=lambda: userscreen_class.log_into_user(3), relief="flat" )
    button_usertitle3.place( x=352.0, y=312.5, width=170.0, height=47.0 )
    button_usertitle3.config(activebackground="#C3C3C3")
    def user3_button_onenter(event): event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(userscreen_class.usertitle3_bg, image=userscreen_class.image_usertitle_bg_selected)
    def user3_button_onleave(event): event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(userscreen_class.usertitle3_bg, image=userscreen_class.image_usertitle_bg)
    button_usertitle3.bind("<Enter>", user3_button_onenter)
    button_usertitle3.bind("<Leave>", user3_button_onleave)


    def log_into_user(userlevel):
        sound_class.sound_buttonpress.play()
        data_class.userlevel = userlevel
        data_class.highscore_dict = data_class.user_data[userlevel]['highscore'] 
        optionsscreen_class.reset_settings()
        userscreen_canvas.pack_forget()
        startscreen_canvas.pack()

    temp = None
    def create_user(userlevel):
            sound_class.sound_buttonpress.play()
            userscreen_class.temp = userlevel
            userscreen_class.hide_buttons(1000, 1000)
            newuser_banner = userscreen_canvas.create_image( 400.0, 217.0, image=userscreen_class.image_newuser_banner )
            newuser_text = userscreen_canvas.create_image( 401.0, 188.0, image=userscreen_class.image_newuser_text )
            entry_bg = userscreen_canvas.create_image( 399.0, 239.0, image=userscreen_class.image_entry_bg )
            cancel_bg = userscreen_canvas.create_image( 274.0, 239.0, image=userscreen_class.image_verify_bg )
            confirm_bg = userscreen_canvas.create_image( 524.0, 239.0, image=userscreen_class.image_verify_bg )

            def validate_input(current_input):
                if current_input == "":
                    return True
                current_input
                return len(current_input) <= 10
            validate_cmd = window.register(validate_input)

            def enter_pressed(event):
                newuser_username = username_entry.get()
                exit_create_user()
                data_class.add_user(newuser_username, userscreen_class.temp)

            username_entry = Entry(userscreen_canvas, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, font=("Encode Sans", 20), justify="center", validate='key', validatecommand=(validate_cmd, '%P'))
            username_entry.place( x=313.0, y=218.0, width=173.0, height=41.0 )
            username_entry.bind('<Return>', enter_pressed)


            button_cancel = Button(userscreen_canvas, image=userscreen_class.image_cancel, borderwidth=0, bg="#D9D9D9", highlightthickness=0, command=lambda: exit_create_user(), relief="flat" )
            button_cancel.place( x=252.0, y=220.0, width=45, height=39)
            button_cancel.config(activebackground="#C3C3C3")
            def button_cancel_onenter(event): event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(cancel_bg, image=userscreen_class.image_verify_bg_selected)
            def button_cancel_onleave(event): event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(cancel_bg, image=userscreen_class.image_verify_bg)
            button_cancel.bind("<Enter>", button_cancel_onenter)
            button_cancel.bind("<Leave>", button_cancel_onleave)




            button_confirm = Button(userscreen_canvas,image=userscreen_class.image_confirm, borderwidth=0, bg="#D9D9D9", highlightthickness=0, command=lambda: enter_pressed(None), relief="flat" )
            button_confirm.place( x=502.0, y=220.0, width=45, height=39)
            button_confirm.config(activebackground="#C3C3C3")
            def button_confirm_onenter(event): event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(confirm_bg, image=userscreen_class.image_verify_bg_selected)
            def button_confirm_onleave(event): event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(confirm_bg, image=userscreen_class.image_verify_bg)
            button_confirm.bind("<Enter>", button_confirm_onenter)
            button_confirm.bind("<Leave>", button_confirm_onleave)

            def exit_create_user():
                sound_class.sound_buttonpress.play()
                userscreen_class.hide_buttons(-1000, -1000)
                userscreen_canvas.delete(newuser_banner)
                userscreen_canvas.delete(newuser_text)
                userscreen_canvas.delete(entry_bg)
                userscreen_canvas.delete(cancel_bg)
                userscreen_canvas.delete(confirm_bg)
                button_cancel.destroy()
                button_confirm.destroy()
                username_entry.destroy()

    def show_user_profile(i):
        sound_class.sound_buttonpress.play()
        profilescreen_class.personalize_screen(i)
        userscreen_canvas.pack_forget()
        profilescreen_canvas.pack()


    button_useraction0 = Button(userscreen_canvas, image=image_useradd, bg="#D9D9D9", borderwidth=0, highlightthickness=0, command=lambda: userscreen_class.create_user(0), relief="flat" )
    button_useraction0.place( x=271.0, y=75.0, width=56.0, height=50.0 )
    button_useraction0.config(activebackground="#C3C3C3")
    def useraction0_onenter(event): event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(userscreen_class.usericon0_bg, image=userscreen_class.image_usericon_bg_selected)
    def useraction0_onleave(event): event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(userscreen_class.usericon0_bg, image=userscreen_class.image_usericon_bg)
    button_useraction0.bind("<Enter>", useraction0_onenter)
    button_useraction0.bind("<Leave>", useraction0_onleave)



    button_useraction1 = Button(userscreen_canvas, image=image_useradd, bg="#D9D9D9", borderwidth=0, highlightthickness=0, command=lambda: userscreen_class.create_user(1), relief="flat" )
    button_useraction1.place( x=271.0, y=154.0, width=56.0, height=50.0 )
    button_useraction1.config(activebackground="#C3C3C3")
    def useraction1_onenter(event): event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(userscreen_class.usericon1_bg, image=userscreen_class.image_usericon_bg_selected)
    def useraction1_onleave(event): event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(userscreen_class.usericon1_bg, image=userscreen_class.image_usericon_bg)
    button_useraction1.bind("<Enter>", useraction1_onenter)
    button_useraction1.bind("<Leave>", useraction1_onleave)



    button_useraction2 = Button(userscreen_canvas, image=image_useradd, bg="#D9D9D9", borderwidth=0, highlightthickness=0, command=lambda: userscreen_class.create_user(2), relief="flat" )
    button_useraction2.place( x=271.0, y=233.0, width=56.0, height=50.0 )
    button_useraction2.config(activebackground="#C3C3C3")
    def useraction2_onenter(event): event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(userscreen_class.usericon2_bg, image=userscreen_class.image_usericon_bg_selected)
    def useraction2_onleave(event): event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(userscreen_class.usericon2_bg, image=userscreen_class.image_usericon_bg)
    button_useraction2.bind("<Enter>", useraction2_onenter)
    button_useraction2.bind("<Leave>", useraction2_onleave)



    button_useraction3 = Button(userscreen_canvas, image=image_useradd, bg="#D9D9D9", borderwidth=0, highlightthickness=0, command=lambda: userscreen_class.create_user(3), relief="flat" )
    button_useraction3.place( x=271.0, y=312.0, width=56.0, height=50.0 )
    button_useraction3.config(activebackground="#C3C3C3")
    def useraction3_onenter(event): event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(userscreen_class.usericon3_bg, image=userscreen_class.image_usericon_bg_selected)
    def useraction3_onleave(event): event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(userscreen_class.usericon3_bg, image=userscreen_class.image_usericon_bg)
    button_useraction3.bind("<Enter>", useraction3_onenter)
    button_useraction3.bind("<Leave>", useraction3_onleave)

    
    def confirm_remove_user(i):
        sound_class.sound_buttonpress.play()
        try:
            username = data_class.user_data[i]['displayname']
        except:
            return
        
        userscreen_class.hide_buttons(1000, 1000)
        delete_confirm_banner = userscreen_canvas.create_image( 400.0, 220.0, image=userscreen_class.image_delete_confirm_banner )
        delete_text = userscreen_canvas.create_text( 401.0, 195.0, anchor="center", text=f"Delete {username}?", fill="#000000", font=("Encode Sans", 25 * -1) )
        delete_confirm_bg_yes = userscreen_canvas.create_image( 461.0, 236.0, image=userscreen_class.image_delete_confirm_bg )
        delete_confirm_bg_no = userscreen_canvas.create_image( 341.0, 236.0, image=userscreen_class.image_delete_confirm_bg )


        button_delete_yes = Button(userscreen_canvas, image=userscreen_class.image_del_confirm_yes, borderwidth=0, bg="#D9D9D9", highlightthickness=0, command=lambda: confirm_delete_user(i), relief="flat" )
        button_delete_yes.place( x=422.0, y=221.0, width=80.0, height=32.0 )
        button_delete_yes.config(activebackground="#C3C3C3")
        def button_delete_yes_onenter(event): event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(delete_confirm_bg_yes, image=userscreen_class.image_delete_confirm_bg_selected)
        def button_delete_yes_onleave(event): event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(delete_confirm_bg_yes, image=userscreen_class.image_delete_confirm_bg)
        button_delete_yes.bind("<Enter>", button_delete_yes_onenter)
        button_delete_yes.bind("<Leave>", button_delete_yes_onleave)



        button_delete_no = Button(userscreen_canvas, image=userscreen_class.image_del_confirm_no, borderwidth=0, bg="#D9D9D9", highlightthickness=0, command=lambda: exit_delete_prompt(), relief="flat" )
        button_delete_no.place( x=301.0, y=221.0, width=80.0, height=32.0 )
        button_delete_no.config(activebackground="#C3C3C3")
        def button_delete_no_onenter(event): event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(delete_confirm_bg_no, image=userscreen_class.image_delete_confirm_bg_selected)
        def button_delete_no_onleave(event): event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(delete_confirm_bg_no, image=userscreen_class.image_delete_confirm_bg)
        button_delete_no.bind("<Enter>", button_delete_no_onenter)
        button_delete_no.bind("<Leave>", button_delete_no_onleave)

        def confirm_delete_user(i):
            sound_class.sound_buttonpress.play()
            exit_delete_prompt()
            data_class.remove_user(i)



        def exit_delete_prompt():
            sound_class.sound_buttonpress.play()
            userscreen_class.remove_user_mode()
            userscreen_canvas.delete(delete_confirm_banner)
            userscreen_canvas.delete(delete_text)
            userscreen_canvas.delete(delete_confirm_bg_yes)
            userscreen_canvas.delete(delete_confirm_bg_no)
            button_delete_yes.destroy()
            button_delete_no.destroy()

            userscreen_class.hide_buttons(-1000, -1000)


    
    def remove_user_mode():
        sound_class.sound_buttonpress.play()
        userscreen_class.remove_mode = not userscreen_class.remove_mode
        if userscreen_class.remove_mode:
            for i, element in enumerate(data_class.useraction_buttons):
                element.config(image=userscreen_class.image_userremove, command=lambda userlevel=i: userscreen_class.confirm_remove_user(userlevel))
        else:
            for i, element in enumerate(data_class.useraction_buttons):
                element.config(image=userscreen_class.image_useradd, command=lambda userlevel=i: userscreen_class.create_user(userlevel))
            data_class.check_for_users()

    
    def back_button_pressed():
        sound_class.sound_buttonpress.play()
        if userscreen_class.remove_mode:
            userscreen_class.remove_user_mode()
        if data_class.userlevel == None:
            userscreen_class.login_error()
        else:
            userscreen_canvas.pack_forget()
            startscreen_canvas.pack()
    button_back = Button(userscreen_canvas, image=image_backbutton, bg="#D9D9D9", borderwidth=0, highlightthickness=0, command=lambda: userscreen_class.back_button_pressed(), relief="flat")
    button_back.place( x=256.0, y=441.0, width=65.0, height=23.0 )
    button_back.config(activebackground="#C3C3C3")
    def buttonback_onenter(event): event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(userscreen_class.backbutton_bg, image=userscreen_class.image_actionbutton_bg_selected)
    def buttonback_onleave(event): event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(userscreen_class.backbutton_bg, image=userscreen_class.image_actionbutton_bg)
    button_back.bind("<Enter>", buttonback_onenter)
    button_back.bind("<Leave>", buttonback_onleave)

    remove_mode = False
    button_userremove = Button(userscreen_canvas, image=image_userremove, bg="#D9D9D9", borderwidth=0, highlightthickness=0, command=lambda: userscreen_class.remove_user_mode(), relief="flat" )
    button_userremove.place( x=480.0, y=441.0, width=65.0, height=23.0 )
    button_userremove.config(activebackground="#C3C3C3")
    def userremove_onenter(event): event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(userscreen_class.userremove_bg, image=userscreen_class.image_actionbutton_bg_selected)
    def userremove_onleave(event): event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(userscreen_class.userremove_bg, image=userscreen_class.image_actionbutton_bg)
    button_userremove.bind("<Enter>", userremove_onenter)
    button_userremove.bind("<Leave>", userremove_onleave)


    def login_error():
        userscreen_class.hide_buttons(1000, 1000)
        popup_banner = userscreen_canvas.create_image( 399.0, 210.0, image=userscreen_class.image_popup_banner )
        popup_text = userscreen_canvas.create_image( 399.0, 187.0, image=userscreen_class.image_popup_text )
        ok_bg = userscreen_canvas.create_image( 399.0, 228.0, image=userscreen_class.image_ok_bg )


        button_ok = Button(userscreen_canvas, image=userscreen_class.image_ok, bg="#D9D9D9", activebackground="#C3C3C3", borderwidth=0, highlightthickness=0, command=lambda: hide_error(), relief="flat" )
        button_ok.place( x=358.0, y=213.0, width=82.5, height=31.0 )
        def buttonback_onenter(event): event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(ok_bg, image=userscreen_class.image_ok_bg_selected)
        def buttonback_onleave(event): event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(ok_bg, image=userscreen_class.image_ok_bg)
        button_ok.bind("<Enter>", buttonback_onenter)
        button_ok.bind("<Leave>", buttonback_onleave)
        
        def hide_error():
            sound_class.sound_buttonpress.play()
            userscreen_canvas.delete(popup_banner)
            userscreen_canvas.delete(popup_text)
            userscreen_canvas.delete(ok_bg)
            button_ok.destroy()

            userscreen_class.hide_buttons(-1000, -1000)





    def hide_buttons(x, y):
        try:
            for titlebutton in data_class.usertitle_buttons:
                titlebutton.place_configure(x=titlebutton.winfo_x() + x, y=titlebutton.winfo_y() + y)
        except:
            pass
        for actionbutton in data_class.useraction_buttons:
            actionbutton.place_configure(x=actionbutton.winfo_x() + x, y=actionbutton.winfo_y() + y)


class profilescreen_class():
    current_user = None
    image_profile_banner = PhotoImage( file=relative_to_assets("profilescreen/profile_banner.png"))
    image_username_bg = PhotoImage( file=relative_to_assets("profilescreen/username_bg.png"))
    image_stats = PhotoImage( file=relative_to_assets("profilescreen/stats.png"))
    image_action_banner = PhotoImage( file=relative_to_assets("profilescreen/action_banner.png"))
    image_action_bg = PhotoImage( file=relative_to_assets("profilescreen/action_bg.png"))
    image_action_bg_selected = PhotoImage( file=relative_to_assets("profilescreen/action_bg_selected.png"))
    image_back = PhotoImage( file=relative_to_assets("profilescreen/back.png"))
    image_edit = PhotoImage( file=relative_to_assets("profilescreen/edit.png"))
    image_history = PhotoImage( file=relative_to_assets("profilescreen/history.png"))


    bg_image = profilescreen_canvas.create_image( 395.0, 255.0, image=userscreen_class.image_bg_image)
    profile_banner = profilescreen_canvas.create_image( 398.0, 211.0, image=image_profile_banner )
    username_bg = profilescreen_canvas.create_image(403.0, 101.0, image=image_username_bg )
    stats = profilescreen_canvas.create_image(302.0, 221.0, image=image_stats )
    back_banner = profilescreen_canvas.create_image( 197.0, 452.0, image=image_action_banner )
    history_banner = profilescreen_canvas.create_image( 399.0, 452.0, image=image_action_banner )
    edit_banner = profilescreen_canvas.create_image( 601.0, 452.0, image=image_action_banner )
    back_bg = profilescreen_canvas.create_image( 197.0, 451.0, image=image_action_bg )
    history_bg = profilescreen_canvas.create_image( 399.0, 451.0, image=image_action_bg )
    edit_bg = profilescreen_canvas.create_image( 601.0, 451.0, image=image_action_bg )

    def personalize_screen(userlevel):
        profilescreen_class.current_user = userlevel
        username = data_class.user_data[userlevel]['displayname']
        gamesplayed = len(data_class.user_data[userlevel]['gamehistory'])
        grade_to_percentage = {'A+': 97, 'A': 93, 'A-': 90, 'B+': 87, 'B': 83, 'B-': 80, 'C+': 77, 'C': 73, 'C-': 70, 'D+': 67, 'D': 63, 'D-': 60, 'F': 0}
        highestscore = 0
        highestscoremode = 'None'
        mostplayed = {'None' : 0}
        total_percent = 0
        for game in data_class.user_data[userlevel]['gamehistory']:
            if game['correct'] > highestscore:
                highestscore = game['correct']
                highestscoremode = game['mode']
            if game['mode'] not in mostplayed:
                mostplayed[game['mode']] = 1
            else:
                mostplayed[game['mode']] += 1
            gamepercent = game['correct'] / (game['incorrect'] + game['correct'])
            total_percent = total_percent + gamepercent
        try:
            average_percent = total_percent / gamesplayed
        except:
            average_percent = 0

        for grade in sorted(grade_to_percentage.keys()):
            if round(average_percent * 100, 2) >= grade_to_percentage[grade]:
                grade = grade
                if gamesplayed == 0:
                    grade = 'None'
                break


        profilescreen_canvas.itemconfig(profilescreen_class.grade_text, text=grade)
        profilescreen_canvas.itemconfig(profilescreen_class.favorite_mode, text=max(mostplayed, key=mostplayed.get))
        profilescreen_canvas.itemconfig(profilescreen_class.average_percent, text=f"{round(average_percent * 100, 2)}%")
        profilescreen_canvas.itemconfig(profilescreen_class.highest_score_mode, text=highestscoremode)
        profilescreen_canvas.itemconfig(profilescreen_class.highest_score, text=highestscore)
        profilescreen_canvas.itemconfig(profilescreen_class.games_played, text=gamesplayed)
        profilescreen_canvas.itemconfig(profilescreen_class.username_text, text=username)



    username_text = profilescreen_canvas.create_text( 405.0, 81.0, anchor="center", text="Ezra Weaver", fill="#000000", font=("Encode Sans", 28 * -1) )
    grade_text = profilescreen_canvas.create_text( 291.0, 117.0, anchor="nw", text="A+", fill="#000000", font=("Encode Sans", 17 * -1) )
    average_percent = profilescreen_canvas.create_text( 326.0, 154.0, anchor="nw", text="95", fill="#000000", font=("Encode Sans", 17 * -1) )
    highest_score = profilescreen_canvas.create_text( 346.0, 192.0, anchor="nw", text="63", fill="#000000", font=("Encode Sans", 17 * -1) )
    highest_score_mode = profilescreen_canvas.create_text( 394.0, 228.0, anchor="nw", text="*-easy-2:00", fill="#000000", font=("Encode Sans", 17 * -1) )
    favorite_mode = profilescreen_canvas.create_text( 354.0, 265.0, anchor="nw", text="*-easy-2:00", fill="#000000", font=("Encode Sans", 17 * -1) )
    games_played = profilescreen_canvas.create_text( 354.0, 302.0, anchor="nw", text="", fill="#000000", font=("Encode Sans", 17 * -1) )






    def button_back_pressed():
        sound_class.sound_buttonpress.play()
        profilescreen_canvas.pack_forget()
        userscreen_canvas.pack()
    button_back = Button(profilescreen_canvas, image=image_back, borderwidth=0, bg="#D9D9D9", highlightthickness=0, command=lambda: profilescreen_class.button_back_pressed(), relief="flat" )
    button_back.place( x=164.0, y=437.0, width=66.0, height=28.0 )
    button_back.config(activebackground="#C3C3C3")
    def button_back_onenter(event): event.widget.config(bg="#C3C3C3"), profilescreen_canvas.itemconfigure(profilescreen_class.back_bg, image=profilescreen_class.image_action_bg_selected),
    def button_back_onleave(event): event.widget.config(bg="#D9D9D9"), profilescreen_canvas.itemconfigure(profilescreen_class.back_bg, image=profilescreen_class.image_action_bg)
    button_back.bind("<Enter>", button_back_onenter)
    button_back.bind("<Leave>", button_back_onleave)




    def button_edit_pressed():
        sound_class.sound_buttonpress.play()
        profilescreen_class.button_back.config(command=lambda: None)
        profilescreen_class.button_edit.config(command=lambda: None)
        profilescreen_class.button_history.config(command=lambda: None)
        newuser_banner = profilescreen_canvas.create_image( 400.0, 217.0, image=userscreen_class.image_newuser_banner )
        newuser_text = profilescreen_canvas.create_image( 401.0, 188.0, image=userscreen_class.image_newuser_text )
        entry_bg = profilescreen_canvas.create_image( 399.0, 239.0, image=userscreen_class.image_entry_bg )
        cancel_bg = profilescreen_canvas.create_image( 274.0, 239.0, image=userscreen_class.image_verify_bg )
        confirm_bg = profilescreen_canvas.create_image( 524.0, 239.0, image=userscreen_class.image_verify_bg )

        def validate_input(current_input):
            if current_input == "":
                return True
            current_input
            return len(current_input) <= 10
        validate_cmd = window.register(validate_input)

        def enter_pressed(event):
            new_username = username_entry.get()
            data_class.rename_user(profilescreen_class.current_user, new_username)
            profilescreen_canvas.itemconfig(profilescreen_class.username_text, text=new_username)
            exit_rename()



        username_entry = Entry(profilescreen_canvas, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, font=("Encode Sans", 20), justify="center", validate='key', validatecommand=(validate_cmd, '%P'))
        username_entry.place( x=313.0, y=218.0, width=173.0, height=41.0 )
        username_entry.bind('<Return>', enter_pressed)


        button_cancel = Button(profilescreen_canvas, image=userscreen_class.image_cancel, borderwidth=0, bg="#D9D9D9", highlightthickness=0, command=lambda: exit_rename(), relief="flat" )
        button_cancel.place( x=252.0, y=220.0, width=45, height=39)
        button_cancel.config(activebackground="#C3C3C3")
        def button_cancel_onenter(event): event.widget.config(bg="#C3C3C3"), profilescreen_canvas.itemconfigure(cancel_bg, image=userscreen_class.image_verify_bg_selected)
        def button_cancel_onleave(event): event.widget.config(bg="#D9D9D9"), profilescreen_canvas.itemconfigure(cancel_bg, image=userscreen_class.image_verify_bg)
        button_cancel.bind("<Enter>", button_cancel_onenter)
        button_cancel.bind("<Leave>", button_cancel_onleave)


        button_confirm = Button(profilescreen_canvas,image=userscreen_class.image_confirm, borderwidth=0, bg="#D9D9D9", highlightthickness=0, command=lambda: enter_pressed(None), relief="flat" )
        button_confirm.place( x=502.0, y=220.0, width=45, height=39)
        button_confirm.config(activebackground="#C3C3C3")
        def button_confirm_onenter(event): event.widget.config(bg="#C3C3C3"), profilescreen_canvas.itemconfigure(confirm_bg, image=userscreen_class.image_verify_bg_selected)
        def button_confirm_onleave(event): event.widget.config(bg="#D9D9D9"), profilescreen_canvas.itemconfigure(confirm_bg, image=userscreen_class.image_verify_bg)
        button_confirm.bind("<Enter>", button_confirm_onenter)
        button_confirm.bind("<Leave>", button_confirm_onleave)
        
        def exit_rename():
            sound_class.sound_buttonpress.play()
            profilescreen_class.button_back.config(command=lambda: profilescreen_class.button_back_pressed())
            profilescreen_class.button_edit.config(command=lambda: profilescreen_class.button_edit_pressed())
            profilescreen_class.button_history.config(command=lambda: profilescreen_class.button_history_pressed())
            profilescreen_canvas.delete(newuser_banner)
            profilescreen_canvas.delete(newuser_text)
            profilescreen_canvas.delete(entry_bg)
            profilescreen_canvas.delete(cancel_bg)
            profilescreen_canvas.delete(confirm_bg)
            button_cancel.destroy()
            button_confirm.destroy()
            username_entry.destroy()








    button_edit = Button(profilescreen_canvas, image=image_edit, borderwidth=0, bg="#D9D9D9", highlightthickness=0, command=lambda: profilescreen_class.button_edit_pressed(), relief="flat" )
    button_edit.place( x=568.0, y=437.0, width=66.0, height=28.0 )
    button_edit.config(activebackground="#C3C3C3")
    def button_edit_onenter(event): event.widget.config(bg="#C3C3C3"), profilescreen_canvas.itemconfigure(profilescreen_class.edit_bg, image=profilescreen_class.image_action_bg_selected),
    def button_edit_onleave(event): event.widget.config(bg="#D9D9D9"), profilescreen_canvas.itemconfigure(profilescreen_class.edit_bg, image=profilescreen_class.image_action_bg)
    button_edit.bind("<Enter>", button_edit_onenter)
    button_edit.bind("<Leave>", button_edit_onleave)


    def button_history_pressed():
        sound_class.sound_buttonpress.play()
        historyscreen_class.display_data(profilescreen_class.current_user)
        historyscreen_class.back_button.config(command=lambda: profilescreen_class.changed_back_button_pressed())

        historyscreen_canvas.coords(historyscreen_class.buttonbanner_2, 1000, 1000)
        historyscreen_canvas.coords(historyscreen_class.actionbuttonbg_2, 1000, 1000)
        historyscreen_class.info_button.place_configure(x=1000, y=1000)

        profilescreen_canvas.pack_forget()
        historyscreen_canvas.pack()
    def changed_back_button_pressed():
        sound_class.sound_buttonpress.play()
        historyscreen_canvas.pack_forget()
        profilescreen_canvas.pack()

        historyscreen_canvas.coords(historyscreen_class.buttonbanner_2, 710.0, 453.0,)
        historyscreen_canvas.coords(historyscreen_class.actionbuttonbg_2, 710.0, 453.0)
        historyscreen_class.info_button.place_configure(x=663.0, y=438.0)

        historyscreen_class.back_button.config(command=lambda: historyscreen_class.back_button_pressed())
    button_history = Button(profilescreen_canvas, image=image_history, borderwidth=0, bg="#D9D9D9", highlightthickness=0, command=lambda: profilescreen_class.button_history_pressed(), relief="flat" )
    button_history.place( x=366.0, y=437.0, width=66.0, height=28.0 )
    button_history.config(activebackground="#C3C3C3")
    def button_history_onenter(event): event.widget.config(bg="#C3C3C3"), profilescreen_canvas.itemconfigure(profilescreen_class.history_bg, image=profilescreen_class.image_action_bg_selected),
    def button_history_onleave(event): event.widget.config(bg="#D9D9D9"), profilescreen_canvas.itemconfigure(profilescreen_class.history_bg, image=profilescreen_class.image_action_bg)
    button_history.bind("<Enter>", button_history_onenter)
    button_history.bind("<Leave>", button_history_onleave)





#----------------------------------------------------------------------------------------------- StartScreen
class startscreen_class():
    muted = False
    #startScreen Images
    image_banner1 = PhotoImage(file=relative_to_assets("startscreen/banner1.png"))
    image_banner2 = PhotoImage(file=relative_to_assets("startscreen/banner2.png"))
    image_banner3 = PhotoImage(file=relative_to_assets("startscreen/banner3.png"))
    image_banner4 = PhotoImage(file=relative_to_assets("startscreen/banner4.png"))
    image_banner4_selected = PhotoImage(file=relative_to_assets("startscreen/banner4_selected.png"))
    image_banner5 = PhotoImage(file=relative_to_assets("startscreen/banner5.png"))
    image_banner5_selected = PhotoImage(file=relative_to_assets("startscreen/banner5_selected.png"))
    image_launchbutton = PhotoImage(file=relative_to_assets("startscreen/launchbutton.png"))
    image_title = PhotoImage(file=relative_to_assets("startscreen/title.png"))
    image_subtitle = PhotoImage(file=relative_to_assets("startscreen/subtitle.png"))
    image_volumeunmuted = PhotoImage(file=relative_to_assets("startscreen/volumeunmuted.png"))
    image_volumemuted = PhotoImage(file=relative_to_assets("startscreen/volumemuted.png"))
    image_usersmenu = PhotoImage(file=relative_to_assets("startscreen/usersmenu.png"))
    #Placed Elements
    bg_image = startscreen_canvas.create_image( 395.0, 255.0, image=userscreen_class.image_bg_image)
    banner1 = startscreen_canvas.create_image(400.0, 106.0, image=image_banner1)
    banner2_1 = startscreen_canvas.create_image(89.0, 460.0, image=image_banner2)
    banner2_2 = startscreen_canvas.create_image(714.0, 460.0, image=image_banner2)
    banner3 = startscreen_canvas.create_image(400.0, 327.0, image=image_banner3)
    banner4 = startscreen_canvas.create_image(400.0, 327.0, image=image_banner4)
    banner5_1 = startscreen_canvas.create_image(89.0, 460.0, image=image_banner5)
    banner5_2 = startscreen_canvas.create_image(715.0, 460.0, image=image_banner5)
    subtitle = startscreen_canvas.create_image(400.0, 135.0, image=image_subtitle)
    title = startscreen_canvas.create_image(406.0, 81.0, image=image_title)

    #Volume Button
    def volume_button_pressed():
        if startscreen_class.muted == False:
            startscreen_class.volume_button.configure(image=startscreen_class.image_volumemuted)
            sound_class.muted_all_sounds(0.0)
        else:
            startscreen_class.volume_button.configure(image=startscreen_class.image_volumeunmuted)
            sound_class.muted_all_sounds(1.0)
            sound_class.sound_buttonpress.play()
        startscreen_class.muted = not startscreen_class.muted


    volume_button = Button(startscreen_canvas, image=image_volumeunmuted, borderwidth=0, highlightthickness=0, bg="#D9D9D9", command=lambda: startscreen_class.volume_button_pressed(), relief="flat")
    volume_button.place(x=63, y=449.0, width=52.0, height=22.0)
    volume_button.config(activebackground="#C3C3C3")
    def volumebutton_onenter(event): event.widget.config(bg="#C3C3C3"), startscreen_canvas.itemconfigure(startscreen_class.banner5_1, image=startscreen_class.image_banner5_selected),
    def volumebutton_onleave(event): event.widget.config(bg="#D9D9D9"), startscreen_canvas.itemconfigure(startscreen_class.banner5_1, image=startscreen_class.image_banner5)
    volume_button.bind("<Enter>", volumebutton_onenter)
    volume_button.bind("<Leave>", volumebutton_onleave)

    #User Button
    def user_button_pressed():
        sound_class.sound_buttonpress.play()
        startscreen_canvas.pack_forget()
        userscreen_canvas.pack()
    users_button = Button(startscreen_canvas, image=image_usersmenu, borderwidth=0, highlightthickness=0, bg="#D9D9D9", command=lambda: startscreen_class.user_button_pressed(), relief="flat")
    users_button.place(x=690, y=449.5, width=52.0, height=22.0)
    users_button.config(activebackground="#C3C3C3")
    def usersbutton_onenter(event): event.widget.config(bg="#C3C3C3"), startscreen_canvas.itemconfigure(startscreen_class.banner5_2, image=startscreen_class.image_banner5_selected),
    def usersbutton_onleave(event): event.widget.config(bg="#D9D9D9"), startscreen_canvas.itemconfigure(startscreen_class.banner5_2, image=startscreen_class.image_banner5)
    users_button.bind("<Enter>", usersbutton_onenter)
    users_button.bind("<Leave>", usersbutton_onleave)

    #Launch Button
    def launch_button_pressed():
        sound_class.sound_buttonpress.play()
        startscreen_canvas.pack_forget()
        mainscreen_canvas.pack()
    launch_button = Button(startscreen_canvas, image=image_launchbutton, borderwidth=0, highlightthickness=0, bg="#D9D9D9", command=lambda: startscreen_class.launch_button_pressed(),relief="flat")
    launch_button.place(x=358.0, y=310.0, width=84.0, height=35.0)
    launch_button.config(activebackground="#C3C3C3")
    def launchbutton_onenter(event): event.widget.config(bg="#C3C3C3"), startscreen_canvas.itemconfigure(startscreen_class.banner4, image=startscreen_class.image_banner4_selected),
    def launchbutton_onleave(event): event.widget.config(bg="#D9D9D9"), startscreen_canvas.itemconfigure(startscreen_class.banner4, image=startscreen_class.image_banner4)
    launch_button.bind("<Enter>", launchbutton_onenter)
    launch_button.bind("<Leave>", launchbutton_onleave)


#-----------------------------------------------------------------

class data_class():
    userlevel = None
    key = b"Kcq-tBBR5XbbOyH15njkMwKsO41l4J_diMGNerJQsKU="
    fernet_key = Fernet(key)
    highscore_dict = {'*-classical-twominute': 0}
    directory_path = 'users'
    user_data = []
    usertitle_buttons = [userscreen_class.button_usertitle0, userscreen_class.button_usertitle1, userscreen_class.button_usertitle2, userscreen_class.button_usertitle3]
    useraction_buttons = [userscreen_class.button_useraction0, userscreen_class.button_useraction1, userscreen_class.button_useraction2, userscreen_class.button_useraction3]
    usertitle_button_positions = [76.5, 155.5, 233.5, 312.5]
    logged_in_users = []

    def check_for_users():
        data_class.user_data = []
        user_name_and_level = {}
        usercount = -1
        for filename in listdir(data_class.directory_path):
            if filename.endswith('.json'): 
                file_path = path.join(data_class.directory_path, filename)
                with open(file_path) as file:
                    decrypted_data = data_class.fernet_key.decrypt(file.read())
                    data = loads(decrypted_data)
                    usercount += 1
                    data_class.user_data.append(data)
                    try:
                        user_name_and_level[data_class.user_data[usercount]['displayname']] = data_class.user_data[usercount]['userlevel']
                    except:
                        pass
        for name, userlevel in user_name_and_level.items():
            try:
                data_class.usertitle_buttons[userlevel].config(text=name)
            except:
                pass
            data_class.useraction_buttons[userlevel].config(image=userscreen_class.image_usericon, command=lambda userlevel=userlevel: userscreen_class.show_user_profile(userlevel))
        for i, element in enumerate(data_class.usertitle_buttons):
            try:
                if element.cget("text") == '':
                    element.place(x=2000, y=2000)
                else:
                    data_class.logged_in_users.append(i)
                    element.place_configure(x=352.0, y=data_class.usertitle_button_positions[i], width=170.0, height=47.0)
            except:
                pass
       

    def clean_users():
        for element in data_class.usertitle_buttons:
            element.config(text='')
        for i, element in enumerate(data_class.useraction_buttons):
            element.config(image=userscreen_class.image_useradd ,command=lambda userlevel=i: userscreen_class.create_user(userlevel))

    def add_user(username, userlevel):
        newuser_dictionary = {"userlevel" : userlevel, "displayname" : username, "highscore" : {'*-classical-twominute': 0}, "gamehistory" : []}
        userfile = f"users/user{userlevel}.json"
        jsondump = dumps(newuser_dictionary)
        encrypted_jsondump = data_class.fernet_key.encrypt(jsondump.encode())
        with open(userfile, 'w') as file:
            file.write(encrypted_jsondump.decode())
        data_class.check_for_users()

    def rename_user(userlevel, name):
        data_class.user_data[userlevel]['displayname'] = name
        userfile = f"users/user{userlevel}.json"
        jsondump = dumps(data_class.user_data[userlevel])
        encrypted_jsondump = data_class.fernet_key.encrypt(jsondump.encode())
        with open(userfile, 'w') as file:
            file.write(encrypted_jsondump.decode())
        data_class.check_for_users()

    def remove_user(i):
        empty_dictionary = {}
        userfile = f"users/user{i}.json"
        jsondump = dumps(empty_dictionary)
        encrypted_jsondump = data_class.fernet_key.encrypt(jsondump.encode())
        with open(userfile, 'w') as file:
            file.write(encrypted_jsondump.decode())
        data_class.userlevel = None
        data_class.clean_users()
        data_class.check_for_users()


    def dump_highscore():
        data_class.user_data[data_class.userlevel]['highscore'] = data_class.highscore_dict
        usercount = -1
        for dictionary in data_class.user_data:
            usercount += 1
            userfile = f"users/user{usercount}.json"
            jsondump = dumps(dictionary)
            encrypted_jsondump = data_class.fernet_key.encrypt(jsondump.encode())
            with open(userfile, 'w') as file:
                file.write(encrypted_jsondump.decode())


    def does_score_exist():
        if data_class.highscore_dict.get(f"{optionsscreen_class.flashcardtype}-{optionsscreen_class.flashcarddifficulty}-{optionsscreen_class.flashcardtime}") is None:
            data_class.highscore_dict[f"{optionsscreen_class.flashcardtype}-{optionsscreen_class.flashcarddifficulty}-{optionsscreen_class.flashcardtime}"] = '0'
data_class.check_for_users()





#----------------------------------------------------------------------------------------------- MainScreen
class mainscreen_class():
    currentscore = 0
    high_score = 0
    flashcard1 = ''
    flashcard2 = ''
    last_flashcard1 = 20000000
    last_flashcard2 = 1
    correctanswer = ''
    feedback = ''
    final_feedback = ''
    incorrect = 0
    countdown_initialized = False
    game_started = False
    #mainScreen Images
    image_flashbg = PhotoImage(file=relative_to_assets("mainscreen/flashbg.png"))
    image_banner6 = PhotoImage(file=relative_to_assets("mainscreen/banner6.png"))
    image_banner7 = PhotoImage(file=relative_to_assets("mainscreen/banner7.png"))
    image_banner8 = PhotoImage(file=relative_to_assets("mainscreen/banner8.png"))
    image_line1 = PhotoImage(file=relative_to_assets("mainscreen/line1.png"))
    image_mathoperator_multiplication = PhotoImage(file=relative_to_assets("mainscreen/mathoperatorX.png"))
    image_mathoperator_minus = PhotoImage(file=relative_to_assets("mainscreen/mathoperator-.png"))
    image_mathoperator_plus = PhotoImage(file=relative_to_assets("mainscreen/mathoperator+.png"))
    image_mathoperator_divide = PhotoImage(file=relative_to_assets("mainscreen/mathoperatord.png"))
    image_entryboxbg = PhotoImage(file=relative_to_assets("mainscreen/entryboxbg.png"))
    image_timerbg = PhotoImage(file=relative_to_assets("mainscreen/timerbg.png"))
    image_scoreboxbg = PhotoImage(file=relative_to_assets("mainscreen/scoreboxbg.png"))
    image_line2 = PhotoImage(file=relative_to_assets("mainscreen/line2.png"))
    image_scorebg = PhotoImage(file=relative_to_assets("mainscreen/scorebg.png"))
    image_startbuttonbg = PhotoImage(file=relative_to_assets("mainscreen/startbuttonbg.png"))
    image_startbuttonbg_selected = PhotoImage(file=relative_to_assets("mainscreen/startbuttonbg_selected.png"))
    image_startbutton = PhotoImage(file=relative_to_assets("mainscreen/startbutton.png"))
    image_entrybox = PhotoImage(file=relative_to_assets("mainscreen/entrybox.png"))
    image_buttonbox = PhotoImage(file=relative_to_assets("mainscreen/buttonbox.png"))
    image_buttonboxbg = PhotoImage(file=relative_to_assets("mainscreen/buttonboxbg.png"))
    image_buttonboxbg_selected = PhotoImage(file=relative_to_assets("mainscreen/buttonboxbg_selected.png"))
    image_backbutton = PhotoImage(file=relative_to_assets("mainscreen/backbutton.png"))
    image_settingsbutton = PhotoImage(file=relative_to_assets("mainscreen/settingsbutton.png"))
    image_historybutton = PhotoImage(file=relative_to_assets("mainscreen/historybutton.png"))
    image_countdownbox = PhotoImage( file=relative_to_assets("mainscreen/countdownbox.png"))
    image_cancel_countdown_bg = PhotoImage( file=relative_to_assets("mainscreen/cancel_countdown_bg.png"))
    image_cancel_countdown_bg_selected = PhotoImage( file=relative_to_assets("mainscreen/cancel_countdown_bg_selected.png"))
    image_cancel_countdown_button = PhotoImage( file=relative_to_assets("mainscreen/cancel_countdown_button.png"))
    image_quit_banner = PhotoImage( file=relative_to_assets("mainscreen/quit_banner.png"))
    image_quit_buttonbg = PhotoImage( file=relative_to_assets("mainscreen/quit_buttonbg.png"))
    image_quit_buttonbg_selected = PhotoImage( file=relative_to_assets("mainscreen/quit_buttonbg_selected.png"))
    image_no_quit_button = PhotoImage( file=relative_to_assets("mainscreen/no_quit_button.png"))
    image_yes_quit_button = PhotoImage( file=relative_to_assets("mainscreen/yes_quit_button.png"))
    #Placed Elements
    bg_image = mainscreen_canvas.create_image( 395.0, 255.0, image=userscreen_class.image_bg_image)
    flashbg = mainscreen_canvas.create_image(408.0, 218.0, image=image_flashbg)
    banner6 = mainscreen_canvas.create_image(640.0, 134.0, image=image_banner6)
    correctanswerbgbox = mainscreen_canvas.create_image(641.0, 221.0, image=image_banner7)
    startbuttonbgbox = mainscreen_canvas.create_image(641.0, 302.0, image=image_banner7)
    banner8 = mainscreen_canvas.create_image(410.0, 378.0, image=image_banner8)
    line1 = mainscreen_canvas.create_image(413.0, 262.0, image=image_line1)
    mathoperator = mainscreen_canvas.create_image(462.0, 236.0, image=image_mathoperator_multiplication)
    entryboxbg = mainscreen_canvas.create_image(386.0, 289.0, image=image_entryboxbg)
    timerbg = mainscreen_canvas.create_image(642.0, 135.0, image=image_timerbg)
    scoreboxbg = mainscreen_canvas.create_image(163.0, 187.0, image=image_scoreboxbg)
    line2_1 = mainscreen_canvas.create_image(161.0, 137.0, image=image_line2)
    line2_2 = mainscreen_canvas.create_image(161.0, 222.0, image=image_line2)
    scorebg_1 = mainscreen_canvas.create_image(161.0, 249.0, image=image_scorebg)
    scorebg_2 = mainscreen_canvas.create_image(161.0, 163.0, image=image_scorebg)
    startbuttonbg = mainscreen_canvas.create_image(641.0, 301.5, image=image_startbuttonbg)
    buttonbox_1 = mainscreen_canvas.create_image(161.0, 320.0, image=image_buttonbox)
    buttonbox_2 = mainscreen_canvas.create_image(161.0, 381.0, image=image_buttonbox)
    buttonbox_3 = mainscreen_canvas.create_image(64.0, 34.0, image=image_buttonbox)
    buttonboxbg_1 = mainscreen_canvas.create_image(64.0, 34.0, image=image_buttonboxbg)
    buttonboxbg_2 = mainscreen_canvas.create_image(161.0, 320.0, image=image_buttonboxbg)
    buttonboxbg_3 = mainscreen_canvas.create_image(161.0, 381.0, image=image_buttonboxbg)
    


    #Back Button
    def back_button_pressed():
        sound_class.sound_buttonpress.play()
        if mainscreen_class.game_started == True:
            mainscreen_class.confirm_quit()
        else:
            mainscreen_canvas.pack_forget()
            startscreen_canvas.pack()
    back_button = Button(mainscreen_canvas, image=image_backbutton, bg="#D9D9D9", borderwidth=0, highlightthickness=0, command=lambda: mainscreen_class.back_button_pressed(), relief="flat")
    back_button.place(x=34.0, y=23.5, width=59.0, height=22.0)
    back_button.config(activebackground="#C3C3C3")
    def backbutton_onenter(event): event.widget.config(bg="#C3C3C3"), mainscreen_canvas.itemconfigure(mainscreen_class.buttonboxbg_1, image=mainscreen_class.image_buttonboxbg_selected),
    def backbutton_onleave(event): event.widget.config(bg="#D9D9D9"), mainscreen_canvas.itemconfigure(mainscreen_class.buttonboxbg_1, image=mainscreen_class.image_buttonboxbg)
    back_button.bind("<Enter>", backbutton_onenter)
    back_button.bind("<Leave>", backbutton_onleave)


    #Settings Button
    def settings_button_pressed():
        sound_class.sound_buttonpress.play()
        optionsscreen_canvas.itemconfig(optionsscreen_class.specific_highscore_text, text=data_class.highscore_dict[f"{optionsscreen_class.flashcardtype}-{optionsscreen_class.flashcarddifficulty}-{optionsscreen_class.flashcardtime}"])
        mainscreen_canvas.pack_forget()
        optionsscreen_canvas.pack()
    settings_button = Button(mainscreen_canvas, image=image_settingsbutton, bg="#D9D9D9", borderwidth=0, highlightthickness=0, command=lambda: mainscreen_class.settings_button_pressed(), relief="flat")
    settings_button.place(x=131, y=310, width=59.0, height=22.0)
    settings_button.config(activebackground="#C3C3C3")
    def settingsbutton_onenter(event): event.widget.config(bg="#C3C3C3"), mainscreen_canvas.itemconfigure(mainscreen_class.buttonboxbg_2, image=mainscreen_class.image_buttonboxbg_selected),
    def settingsbutton_onleave(event): event.widget.config(bg="#D9D9D9"), mainscreen_canvas.itemconfigure(mainscreen_class.buttonboxbg_2, image=mainscreen_class.image_buttonboxbg)
    settings_button.bind("<Enter>", settingsbutton_onenter)
    settings_button.bind("<Leave>", settingsbutton_onleave)


    #History Button
    def history_button_pressed():
        sound_class.sound_buttonpress.play()
        historyscreen_class.display_data(data_class.userlevel)
        mainscreen_canvas.pack_forget()
        historyscreen_canvas.pack()
    history_button = Button(mainscreen_canvas, image=image_historybutton, bg="#D9D9D9", borderwidth=0, highlightthickness=0, command=lambda: mainscreen_class.history_button_pressed(), relief="flat")
    history_button.place(x=131.0, y=370.5, width=59.0, height=22.0)
    history_button.config(activebackground="#C3C3C3")
    def historybutton_onenter(event): event.widget.config(bg="#C3C3C3"), mainscreen_canvas.itemconfigure(mainscreen_class.buttonboxbg_3, image=mainscreen_class.image_buttonboxbg_selected),
    def historybutton_onleave(event): event.widget.config(bg="#D9D9D9"), mainscreen_canvas.itemconfigure(mainscreen_class.buttonboxbg_3, image=mainscreen_class.image_buttonboxbg)
    history_button.bind("<Enter>", historybutton_onenter)
    history_button.bind("<Leave>", historybutton_onleave)


    #Start Button
    def start_button_pressed():
        mainscreen_class.place_countdownscreen()
        sound_class.sound_buttonpress.play()
    start_button = Button(mainscreen_canvas, image=image_startbutton, borderwidth=0, bg="#D9D9D9", highlightthickness=0, command=lambda: mainscreen_class.start_button_pressed(), relief="flat")
    start_button.place(x=604.0, y=290.0, width=72.0, height=25.0)
    start_button.config(activebackground="#C3C3C3")
    def startbutton_onenter(event): event.widget.config(bg="#C3C3C3"), mainscreen_canvas.itemconfigure(mainscreen_class.startbuttonbg, image=mainscreen_class.image_startbuttonbg_selected),
    def startbutton_onleave(event): event.widget.config(bg="#D9D9D9"), mainscreen_canvas.itemconfigure(mainscreen_class.startbuttonbg, image=mainscreen_class.image_startbuttonbg)
    start_button.bind("<Enter>", startbutton_onenter)
    start_button.bind("<Leave>", startbutton_onleave)

    #Place Text
    flashcard2_text = mainscreen_canvas.create_text(359.0, 184.0, anchor="nw", text=flashcard1, fill="#000000", font=("Helvetica", 70 * -1))
    flashcard1_text = mainscreen_canvas.create_text(359.0, 116.0, anchor="nw", text=flashcard2, fill="#000000", font=("Helvetica", 70 * -1))
    time_text = mainscreen_canvas.create_text(591.0, 113.0, anchor="nw", text='', fill="#000000", font=("Encode Sans", 40 * -1))
    feedback_text = mainscreen_canvas.create_text(359.0, 360.0, anchor="nw", text=feedback, fill="#000000", font=("Encode Sans", 30 * -1))
    highscore_text = mainscreen_canvas.create_text(160.0, 250.0, anchor="center", text='', fill="#000000", font=("Encode Sans", 23 * -1))
    currentscore_text = mainscreen_canvas.create_text(160, 163.0, anchor="center", text='', fill="#000000", font=("Encode Sans", 23 * -1))
    correctanswer_text = mainscreen_canvas.create_text(640.0, 222.0, anchor="center", text='', fill="#000000", font=("Encode Sans", 38 * -1))
    mainscreen_canvas.create_text( 103.0, 187.0, anchor="nw", text="High Score", fill="#000000", font=("Encode Sans", 25 * -1))
    mainscreen_canvas.create_text(88.0, 103.0, anchor="nw", text="Current Score", fill="#000000", font=("Encode Sans", 25 * -1))







    def place_countdownscreen():
        #CountDown Elements
        countdownbox = mainscreen_canvas.create_image( 407.0, 211.0, image=mainscreen_class.image_countdownbox )
        cancel_countdown_bg = mainscreen_canvas.create_image( 297.0, 113.0, image=mainscreen_class.image_cancel_countdown_bg )

        countdown_title_text = mainscreen_canvas.create_text( 352.0, 109.0, anchor="nw", text="Starts in...", fill="#000000", font=("Encode Sans", 25 * -1) )
        countdown_counter_text = mainscreen_canvas.create_text( 385.0, 178.0, anchor="nw", text='', fill="#000000", font=("Helvetica", 70 * -1) )

        cancel_countdown_button = Button(mainscreen_canvas, image=mainscreen_class.image_cancel_countdown_button, borderwidth=0, highlightthickness=0, bg="#D9D9D9", command=lambda: cancel_countdown(), relief="flat" )
        cancel_countdown_button.place( x=289.4, y=104.5, width=17.5, height=17.0 )
        cancel_countdown_button.config(activebackground="#C3C3C3")
        def cancelcountdownbutton_onenter(event): event.widget.config(bg="#C3C3C3"), mainscreen_canvas.itemconfigure(cancel_countdown_bg, image=mainscreen_class.image_cancel_countdown_bg_selected),
        def cancelcountdownbutton_onleave(event): event.widget.config(bg="#D9D9D9"), mainscreen_canvas.itemconfigure(cancel_countdown_bg, image=mainscreen_class.image_cancel_countdown_bg)
        cancel_countdown_button.bind("<Enter>", cancelcountdownbutton_onenter)
        cancel_countdown_button.bind("<Leave>", cancelcountdownbutton_onleave)
        mainscreen_class.pre_game_cleanup()
        mainscreen_class.back_button.place(x=34000000.0, y=23.5,)
        def destroy_countdownscreen():
            mainscreen_canvas.delete(countdownbox)
            mainscreen_canvas.delete(countdown_counter_text)
            mainscreen_canvas.delete(countdown_title_text)
            mainscreen_canvas.delete(cancel_countdown_bg)
            cancel_countdown_button.destroy()
            mainscreen_class.back_button.place(x=34.0, y=23.5)

        def initialize_countdown(seconds, callback):
            if seconds == 0:
                callback()
                mainscreen_class.start_game()
                return
            mainscreen_canvas.itemconfig(countdown_counter_text, text=seconds)
            seconds -= 1
            sound_class.sound_countdown_tick.play()
            mainscreen_canvas.countdownloop = mainscreen_canvas.after(1000, initialize_countdown, seconds, callback)


        def cancel_countdown():
            sound_class.sound_buttonpress.play()
            mainscreen_canvas.after_cancel(mainscreen_canvas.countdownloop)
            mainscreen_class.post_game_cleanup()
            destroy_countdownscreen()
        initialize_countdown(3, destroy_countdownscreen)











    def confirm_quit():
        quit_banner = mainscreen_canvas.create_image( 408.0, 215.0, image=mainscreen_class.image_quit_banner )
        quit_buttonbg_1 = mainscreen_canvas.create_image( 348.0, 230.0, image=mainscreen_class.image_quit_buttonbg )
        quit_buttonbg_2 = mainscreen_canvas.create_image( 468.0, 230.0, image=mainscreen_class.image_quit_buttonbg )
        quit_text = mainscreen_canvas.create_text( 294.0, 176.0, anchor="nw", text="Do you want to quit?\n", fill="#000000", font=("Encode Sans", 25 * -1) )

        def yes_quit_button_pressed():
            sound_class.sound_buttonpress.play()
            destroy_quitbox()
            mainscreen_class.game_started = False
            if optionsscreen_class.flashcardtime == "practice":
                mainscreen_class.post_game_cleanup()
                return
            mainscreen_canvas.after_cancel(mainscreen_canvas.maintimerloop)
            mainscreen_class.post_game_cleanup()

            
        yes_quit_button = Button( image=mainscreen_class.image_yes_quit_button, borderwidth=0, highlightthickness=0, bg="#D9D9D9", command=lambda: yes_quit_button_pressed(), relief="flat" )
        yes_quit_button.place( x=429.0, y=217.0, width=80.0, height=26.0 )
        yes_quit_button.config(activebackground="#C3C3C3")
        def yes_quitbutton_onenter(event): event.widget.config(bg="#C3C3C3"), mainscreen_canvas.itemconfigure(quit_buttonbg_2, image=mainscreen_class.image_quit_buttonbg_selected),
        def yes_quitbutton_onleave(event): event.widget.config(bg="#D9D9D9"), mainscreen_canvas.itemconfigure(quit_buttonbg_2, image=mainscreen_class.image_quit_buttonbg)
        yes_quit_button.bind("<Enter>", yes_quitbutton_onenter)
        yes_quit_button.bind("<Leave>", yes_quitbutton_onleave)

        def no_quit_button_pressed():
            sound_class.sound_buttonpress.play()
            destroy_quitbox()
        no_quit_button = Button( image=mainscreen_class.image_no_quit_button, borderwidth=0, highlightthickness=0, bg="#D9D9D9", command=lambda: no_quit_button_pressed(), relief="flat" )
        no_quit_button.place( x=308.0, y=217.0, width=80.0, height=26.0 )
        no_quit_button.config(activebackground="#C3C3C3")
        def no_quitbutton_onenter(event): event.widget.config(bg="#C3C3C3"), mainscreen_canvas.itemconfigure(quit_buttonbg_1, image=mainscreen_class.image_quit_buttonbg_selected),
        def no_quitbutton_onleave(event): event.widget.config(bg="#D9D9D9"), mainscreen_canvas.itemconfigure(quit_buttonbg_1, image=mainscreen_class.image_quit_buttonbg)
        no_quit_button.bind("<Enter>", no_quitbutton_onenter)
        no_quit_button.bind("<Leave>", no_quitbutton_onleave)

        def destroy_quitbox():
            mainscreen_canvas.delete(quit_banner)
            mainscreen_canvas.delete(quit_buttonbg_1)
            mainscreen_canvas.delete(quit_buttonbg_2)
            mainscreen_canvas.delete(quit_text)
            no_quit_button.destroy()
            yes_quit_button.destroy()





















    def start_game():
        # sound_class.sound_countdown_end.play()
        mainscreen_class.game_started = True
        mainscreen_canvas.itemconfig(mainscreen_class.currentscore_text, text=mainscreen_class.currentscore)
        mainscreen_class.entrybox.place(x=364.0, y=278.0, width=44.0, height=21.0)
        mainscreen_class.generate_problem()
        if optionsscreen_class.flashcardtime == "practice":
            mainscreen_canvas.itemconfig(mainscreen_class.highscore_text, text='0')
            return
        mainscreen_canvas.itemconfig(mainscreen_class.highscore_text, text=data_class.highscore_dict[f"{optionsscreen_class.flashcardtype}-{optionsscreen_class.flashcarddifficulty}-{optionsscreen_class.flashcardtime}"])
        mainscreen_class.start_timer(optionsscreen_class.minutes, optionsscreen_class.seconds)



    def generate_problem():
        mainscreen_class.flashcard1 = randint(optionsscreen_class.difficultyint1, optionsscreen_class.difficultyint2)
        mainscreen_class.flashcard2 = randint(optionsscreen_class.difficultyint1, optionsscreen_class.difficultyint2)
        do_math = {'+': add, '-': sub, '/': floordiv, '*': mul}[optionsscreen_class.flashcardtype]
        mainscreen_class.correctanswer = do_math(mainscreen_class.flashcard1, mainscreen_class.flashcard2)
        mainscreen_class.check_problem()
        mainscreen_canvas.itemconfig(mainscreen_class.flashcard2_text, text=mainscreen_class.flashcard2)
        mainscreen_canvas.itemconfig(mainscreen_class.flashcard1_text, text=mainscreen_class.flashcard1)

    def check_problem():
        if mainscreen_class.correctanswer < 0:
            mainscreen_class.generate_problem()
        if (mainscreen_class.flashcard1 == mainscreen_class.last_flashcard1 and mainscreen_class.flashcard2 == mainscreen_class.last_flashcard2) or \
        (mainscreen_class.flashcard1 == mainscreen_class.last_flashcard2 and mainscreen_class.flashcard2 == mainscreen_class.last_flashcard1):
            mainscreen_class.generate_problem()
        if optionsscreen_class.flashcardtype == "/" and not mainscreen_class.flashcard1 % mainscreen_class.flashcard2 == 0:
            mainscreen_class.generate_problem()




    def user_pressed_enter(event):
        user_answer = mainscreen_class.entrybox.get()
        try:
            if int(user_answer) == mainscreen_class.correctanswer:
                mainscreen_class.feedback = "Correct!"
                mainscreen_class.currentscore = mainscreen_class.currentscore + 1
                sound_class.sound_correct.play()
            else:
                mainscreen_class.feedback = "Wrong!"
                mainscreen_class.incorrect = mainscreen_class.incorrect + 1
                sound_class.sound_wrong.play()
                if mainscreen_class.currentscore > 0:
                    mainscreen_class.currentscore = mainscreen_class.currentscore - 1
        except:
            return
        mainscreen_canvas.itemconfig(mainscreen_class.currentscore_text, text=mainscreen_class.currentscore)
        mainscreen_canvas.itemconfig(mainscreen_class.correctanswer_text, text=mainscreen_class.correctanswer)
        mainscreen_canvas.itemconfig(mainscreen_class.feedback_text, text=mainscreen_class.feedback)
        mainscreen_class.last_flashcard1 = mainscreen_class.flashcard1
        mainscreen_class.last_flashcard2 = mainscreen_class.flashcard2
        mainscreen_class.generate_problem()
        mainscreen_class.entrybox.delete(0, 'end')



    def start_timer(minutes, seconds):
        if minutes == 00 and seconds == 1:
            mainscreen_class.end_game()
            return

        if seconds == 00:
            minutes -= 1
            seconds = 60

        seconds -= 1
        sound_class.sound_timer_tick.play()
        mainscreen_canvas.itemconfig(mainscreen_class.time_text, text=f'{minutes:2}:{seconds:02}')

        mainscreen_canvas.maintimerloop = mainscreen_canvas.after(1000, mainscreen_class.start_timer, minutes, seconds)





    def pre_game_cleanup():
        mainscreen_class.start_button.place(x=60400.0, y=290.0, width=72.0, height=25.0)
        mainscreen_class.history_button.place(x=13100.0, y=370.5, width=59.0, height=22.0)
        mainscreen_class.settings_button.place(x=13100, y=310, width=59.0, height=22.0)
        mainscreen_canvas.coords(mainscreen_class.buttonbox_1, 16100.0, 320.0,)
        mainscreen_canvas.coords(mainscreen_class.buttonbox_2, 16100.0, 320.0,)
        mainscreen_canvas.coords(mainscreen_class.buttonboxbg_3, 16100.0, 320.0)
        mainscreen_canvas.coords(mainscreen_class.buttonboxbg_2, 16100.0, 320.0)
        mainscreen_canvas.coords(mainscreen_class.startbuttonbg, 16100.0, 320.0)
        mainscreen_canvas.coords(mainscreen_class.startbuttonbgbox, 16100.0, 320.0)


    def post_game_cleanup():
        mainscreen_class.start_button.place(x=604.0, y=290.0, width=72.0, height=25.0)
        mainscreen_class.history_button.place(x=131.0, y=370.5, width=59.0, height=22.0)
        mainscreen_class.settings_button.place(x=131, y=310, width=59.0, height=22.0)
        mainscreen_canvas.coords(mainscreen_class.buttonbox_1, 161.0, 320.0,)
        mainscreen_canvas.coords(mainscreen_class.buttonbox_2, 161.0, 381.0,)
        mainscreen_canvas.coords(mainscreen_class.buttonboxbg_3, 161.0, 381.0,)
        mainscreen_canvas.coords(mainscreen_class.buttonboxbg_2, 161.0, 320.0,)
        mainscreen_canvas.itemconfig(mainscreen_class.time_text, text='')
        mainscreen_canvas.itemconfig(mainscreen_class.flashcard2_text, text='')
        mainscreen_canvas.itemconfig(mainscreen_class.flashcard1_text, text='')
        mainscreen_canvas.itemconfig(mainscreen_class.currentscore_text, text='')
        mainscreen_canvas.itemconfig(mainscreen_class.highscore_text, text='')
        mainscreen_canvas.itemconfig(mainscreen_class.correctanswer_text, text='')
        mainscreen_canvas.itemconfig(mainscreen_class.feedback_text, text='')
        mainscreen_canvas.coords(mainscreen_class.startbuttonbg, 641.0, 301.5)
        mainscreen_canvas.coords(mainscreen_class.startbuttonbgbox, 641.0, 302)
        mainscreen_class.entrybox.place(x=36400.0, y=278.0)
        mainscreen_class.currentscore = 0
        mainscreen_class.incorrect = 0
        mainscreen_class.game_started = False
        mainscreen_class.entrybox.delete(0, 'end')


    def is_new_highscore():
        if int(mainscreen_class.currentscore) > int(data_class.highscore_dict[f"{optionsscreen_class.flashcardtype}-{optionsscreen_class.flashcarddifficulty}-{optionsscreen_class.flashcardtime}"]):
            finalscreen_class.finalscore_feedback_text = 'New Highscore!'
            sound_class.sound_win.play()
            data_class.highscore_dict[f"{optionsscreen_class.flashcardtype}-{optionsscreen_class.flashcarddifficulty}-{optionsscreen_class.flashcardtime}"] = mainscreen_class.currentscore
        else:
            finalscreen_class.finalscore_feedback_text = 'Better Luck Next TIme!'
            sound_class.sound_times_up.play()

    def log_game():
        if mainscreen_class.currentscore == 0:
            return
        current_datetime = datetime.now()
        current_date = current_datetime.strftime("%m/%d/%Y")
        current_time = current_datetime.strftime("%I:%M %p")
        log_dictionary = {"date" : current_date, "time" : current_time, "correct" : mainscreen_class.currentscore, "incorrect" : mainscreen_class.incorrect, "mode" : f"{optionsscreen_class.flashcardtype}-{optionsscreen_class.flashcarddifficulty}-{optionsscreen_class.flashcardtime}"}
        data_class.user_data[data_class.userlevel]['gamehistory'].append(log_dictionary)


    def end_game():
        mainscreen_canvas.pack_forget()
        finalscreen_canvas.pack()
        finalscreen_canvas.itemconfig(finalscreen_class.yourscore_text, text=mainscreen_class.currentscore)
        finalscreen_canvas.itemconfig(finalscreen_class.highscore_text, text=data_class.highscore_dict[f"{optionsscreen_class.flashcardtype}-{optionsscreen_class.flashcarddifficulty}-{optionsscreen_class.flashcardtime}"])
        finalscreen_canvas.itemconfig(finalscreen_class.incorrect_text, text=mainscreen_class.incorrect)
        mainscreen_class.is_new_highscore()
        finalscreen_canvas.itemconfig(finalscreen_class.feedback_text, text=finalscreen_class.finalscore_feedback_text)
        mainscreen_class.log_game()
        data_class.dump_highscore()
        mainscreen_class.post_game_cleanup()



    def validate_main_input(current_input):
        if current_input == "":
            return True
        try:
            int(current_input)
            return len(current_input) <= 4
        except ValueError:
            return False

    mainscreen_validate_cmd = window.register(validate_main_input)

    #Entry Box
    entryboxbg = mainscreen_canvas.create_image(386.0, 289.5, image=image_entrybox)
    entrybox = Entry(mainscreen_canvas, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, font=("Encode Sans", 13), validate='key', validatecommand=(mainscreen_validate_cmd, '%P'))

    entrybox.bind('<Return>', user_pressed_enter)


#-----------------------------------------------------------------


#----------------------------------------------------------------------------------------------- OptionsScreen
class optionsscreen_class():
    flashcardtype = "*"
    flashcarddifficulty = "classical"
    flashcardtime = "twominute"
    difficultyint1 = 1
    difficultyint2 = 15
    explanationtitle = None
    explanation = None
    minutes = 2
    seconds = 1

    #optionsscreen Images
    image_banner9 = PhotoImage(file=relative_to_assets("optionsscreen/banner9.png"))
    image_banner10 = PhotoImage(file=relative_to_assets("optionsscreen/banner10.png"))
    image_descriptionbox = PhotoImage(file=relative_to_assets("optionsscreen/descriptionbox.png"))
    image_buttonbg_outline = PhotoImage(file=relative_to_assets("optionsscreen/buttonbg_outline.png"))
    image_buttonbg_outline_selected = PhotoImage(file=relative_to_assets("optionsscreen/buttonbg_outline_selected.png"))
    image_buttonbg = PhotoImage(file=relative_to_assets("optionsscreen/buttonbg.png"))
    image_buttonbg_selected = PhotoImage(file=relative_to_assets("optionsscreen/buttonbg_selected.png"))
    image_flashcardtype_title = PhotoImage(file=relative_to_assets("optionsscreen/flashcardtype_title.png"))
    image_difficulty_title = PhotoImage(file=relative_to_assets("optionsscreen/difficulty_title.png"))
    image_time_title = PhotoImage( file=relative_to_assets("optionsscreen/time_title.png"))
    image_back_buttonbg = PhotoImage( file=relative_to_assets("optionsscreen/back_buttonbg.png"))
    image_back_buttonbg_selected = PhotoImage( file=relative_to_assets("optionsscreen/back_buttonbg_selected.png"))
    image_addition_button = PhotoImage(file=relative_to_assets("optionsscreen/addition_button.png"))
    image_subtraction_button = PhotoImage(file=relative_to_assets("optionsscreen/subtraction_button.png"))
    image_multiplication_button = PhotoImage(file=relative_to_assets("optionsscreen/multiplication_button.png"))
    image_division_button = PhotoImage(file=relative_to_assets("optionsscreen/division_button.png"))
    image_medium_button = PhotoImage(file=relative_to_assets("optionsscreen/medium_button.png"))
    image_easy_button = PhotoImage(file=relative_to_assets("optionsscreen/easy_button.png"))
    image_practice_button = PhotoImage(file=relative_to_assets("optionsscreen/practice_button.png"))
    image_twominute_button = PhotoImage(file=relative_to_assets("optionsscreen/2minute_button.png"))
    image_oneminute_button = PhotoImage(file=relative_to_assets("optionsscreen/1minute_button.png"))
    image_thirtysecond_button = PhotoImage(file=relative_to_assets("optionsscreen/30second_button.png"))
    image_hard_button = PhotoImage(file=relative_to_assets("optionsscreen/hard_button.png"))
    image_classical_button = PhotoImage(file=relative_to_assets("optionsscreen/classical_button.png"))
    image_back_button = PhotoImage( file=relative_to_assets("optionsscreen/back_button.png"))
    image_highscore_banner = PhotoImage( file=relative_to_assets("optionsscreen/highscore_banner.png"))
    image_highscore_bg = PhotoImage( file=relative_to_assets("optionsscreen/highscore_bg.png"))
    #Place Elements
    bg_image = optionsscreen_canvas.create_image( 395.0, 255.0, image=userscreen_class.image_bg_image)
    banner9_1 = optionsscreen_canvas.create_image(132.0, 163.0, image=image_banner9)
    banner9_2 = optionsscreen_canvas.create_image(399.0, 166.0, image=image_banner9)
    banner9_3 = optionsscreen_canvas.create_image(666.0, 166.0, image=image_banner9)
    banner10 = optionsscreen_canvas.create_image(106.0, 455.0, image=image_banner10)
    descriptionbox = optionsscreen_canvas.create_image(391.0, 403.0, image=image_descriptionbox)
    back_buttonbg = optionsscreen_canvas.create_image( 107.0, 454.0, image=image_back_buttonbg)

    buttonbg_difficulty_classical = optionsscreen_canvas.create_image(400.0, 102.0, image=image_buttonbg_outline)
    buttonbg_difficulty_easy = optionsscreen_canvas.create_image(400.0, 150.0, image=image_buttonbg)
    buttonbg_difficulty_medium = optionsscreen_canvas.create_image( 400.0, 198.0, image=image_buttonbg)
    buttonbg_difficulty_hard = optionsscreen_canvas.create_image(400.0, 246.0, image=image_buttonbg)


    buttonbg_time_twominute = optionsscreen_canvas.create_image(667.0, 102.0, image=image_buttonbg_outline)
    buttonbg_time_oneminute = optionsscreen_canvas.create_image(667.0, 150.0, image=image_buttonbg)
    buttonbg_time_thirtysecond = optionsscreen_canvas.create_image(667.0, 198.0, image=image_buttonbg)
    buttonbg_time_practice = optionsscreen_canvas.create_image(667.0, 246.0, image=image_buttonbg)


    buttonbg_type_multiplication = optionsscreen_canvas.create_image(135.0, 102.0, image=image_buttonbg_outline)
    buttonbg_type_subtraction = optionsscreen_canvas.create_image(135.0, 150.0, image=image_buttonbg)
    buttonbg_type_addition = optionsscreen_canvas.create_image(135.0, 198.0, image=image_buttonbg)
    buttonbg_type_division = optionsscreen_canvas.create_image(135.0, 246.0, image=image_buttonbg)


    flashcardtype_title = optionsscreen_canvas.create_image(134.0, 63.0, image=image_flashcardtype_title)
    difficulty_title = optionsscreen_canvas.create_image(400.0, 63.0, image=image_difficulty_title)
    time_title = optionsscreen_canvas.create_image(666.0, 63.0, image=image_time_title)

    highscore_banner = optionsscreen_canvas.create_image( 691.0, 413.0, image=image_highscore_banner )
    highscore_bg = optionsscreen_canvas.create_image( 691.0, 428.0, image=image_highscore_bg )
    optionsscreen_canvas.create_text( 647.0, 379.0, anchor="nw", text="Highscore:", fill="#000000", font=("Encode Sans", 19 * -1) )
    specific_highscore_text = optionsscreen_canvas.create_text(691.0, 428.0, anchor="center", text=data_class.highscore_dict[f"{flashcardtype}-{flashcarddifficulty}-{flashcardtime}"], fill="#000000", font=("Encode Sans", 19 * -1))


    def reset_settings():
        optionsscreen_class.flashcardtype = "*"
        optionsscreen_class.flashcarddifficulty = "classical"
        optionsscreen_class.flashcardtime = "twominute"
        optionsscreen_class.difficultyint1 = 1
        optionsscreen_class.difficultyint2 = 15
        optionsscreen_class.explanationtitle = None
        optionsscreen_class.explanation = None
        optionsscreen_class.minutes = 2
        optionsscreen_class.seconds = 1
        optionsscreen_canvas.itemconfigure(optionsscreen_class.specific_highscore_text, text=data_class.highscore_dict[f"{optionsscreen_class.flashcardtype}-{optionsscreen_class.flashcarddifficulty}-{optionsscreen_class.flashcardtime}"])
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_multiplication, image=optionsscreen_class.image_buttonbg_outline)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_addition, image=optionsscreen_class.image_buttonbg)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_subtraction, image=optionsscreen_class.image_buttonbg)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_division, image=optionsscreen_class.image_buttonbg)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_classical, image=optionsscreen_class.image_buttonbg_outline)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_hard, image=optionsscreen_class.image_buttonbg)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_medium, image=optionsscreen_class.image_buttonbg)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_easy, image=optionsscreen_class.image_buttonbg)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_thirtysecond, image=optionsscreen_class.image_buttonbg)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_oneminute, image=optionsscreen_class.image_buttonbg)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_practice, image=optionsscreen_class.image_buttonbg)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_twominute, image=optionsscreen_class.image_buttonbg_outline)






    #Buttons

    #Flash Card Type Buttons
    def multiplication_button_pressed():
        optionsscreen_class.flashcardtype = "*"
        optionsscreen_class.explanationtitle, optionsscreen_class.explanation, optionsscreen_class.difficultyint1, optionsscreen_class.difficultyint2 = optionsscreen_class.get_info(
            optionsscreen_class.flashcardtype, optionsscreen_class.flashcarddifficulty)
        optionsscreen_class.explanationtitle = "Multiplication -"
        optionsscreen_class.explanation = "Put your time tables to the test!"
        mainscreen_canvas.itemconfigure(mainscreen_class.mathoperator, image=mainscreen_class.image_mathoperator_multiplication)
        optionsscreen_class.clear_type_outline()
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_multiplication, image=optionsscreen_class.image_buttonbg_outline_selected)
    multiplication_button = Button(optionsscreen_canvas, image=image_multiplication_button, borderwidth=0, highlightthickness=0, bg="#D9D9D9", command=lambda: optionsscreen_class.multiplication_button_pressed(), relief="flat" )
    multiplication_button.place(x=110.0, y=90.5, width=50.0, height=22.0 )
    multiplication_button.config(activebackground="#C3C3C3")
    def multiplicationbutton_onenter(event):
        event.widget.config(bg="#C3C3C3")
        if optionsscreen_class.flashcardtype == "*":
             optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_multiplication, image=optionsscreen_class.image_buttonbg_outline_selected)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_multiplication, image=optionsscreen_class.image_buttonbg_selected)
    def multiplicationbutton_onleave(event):
        event.widget.config(bg="#D9D9D9")
        if optionsscreen_class.flashcardtype == "*":
             optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_multiplication, image=optionsscreen_class.image_buttonbg_outline)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_multiplication, image=optionsscreen_class.image_buttonbg)
    multiplication_button.bind("<Enter>", multiplicationbutton_onenter)
    multiplication_button.bind("<Leave>", multiplicationbutton_onleave)



    def subtraction_button_pressed():
        optionsscreen_class.flashcardtype = "-"
        optionsscreen_class.explanationtitle, optionsscreen_class.explanation, optionsscreen_class.difficultyint1, optionsscreen_class.difficultyint2 = optionsscreen_class.get_info(
            optionsscreen_class.flashcardtype, optionsscreen_class.flashcarddifficulty)
        optionsscreen_class.explanationtitle = "Subtraction -"
        optionsscreen_class.explanation = "Put your subtraction skills to the test!"
        optionsscreen_class.clear_type_outline()
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_subtraction, image=optionsscreen_class.image_buttonbg_outline_selected)
        mainscreen_canvas.itemconfigure(mainscreen_class.mathoperator, image=mainscreen_class.image_mathoperator_minus)
    subtraction_button = Button(optionsscreen_canvas, image=image_subtraction_button, borderwidth=0, highlightthickness=0, bg="#D9D9D9", command=lambda: optionsscreen_class.subtraction_button_pressed(), relief="flat" )
    subtraction_button.place(x=110.0, y=139.0, width=50.0, height=22.0 )
    subtraction_button.config(activebackground="#C3C3C3")
    def subtractionbutton_onenter(event):
        event.widget.config(bg="#C3C3C3")
        if optionsscreen_class.flashcardtype == "-":
             optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_subtraction, image=optionsscreen_class.image_buttonbg_outline_selected)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_subtraction, image=optionsscreen_class.image_buttonbg_selected)
    def subtractionbutton_onleave(event):
        event.widget.config(bg="#D9D9D9")
        if optionsscreen_class.flashcardtype == "-":
             optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_subtraction, image=optionsscreen_class.image_buttonbg_outline)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_subtraction, image=optionsscreen_class.image_buttonbg)
    subtraction_button.bind("<Enter>", subtractionbutton_onenter)
    subtraction_button.bind("<Leave>", subtractionbutton_onleave)



    def addition_button_pressed():
        optionsscreen_class.flashcardtype = "+"
        optionsscreen_class.explanationtitle, optionsscreen_class.explanation, optionsscreen_class.difficultyint1, optionsscreen_class.difficultyint2 = optionsscreen_class.get_info(
            optionsscreen_class.flashcardtype, optionsscreen_class.flashcarddifficulty)
        optionsscreen_class.explanationtitle = "Addition -"
        optionsscreen_class.explanation = "Put your addition skills to the test!"
        optionsscreen_class.clear_type_outline()
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_addition, image=optionsscreen_class.image_buttonbg_outline_selected)
        mainscreen_canvas.itemconfigure(mainscreen_class.mathoperator, image=mainscreen_class.image_mathoperator_plus)
    addition_button = Button(optionsscreen_canvas, image=image_addition_button, borderwidth=0, highlightthickness=0,  bg="#D9D9D9", command=lambda: optionsscreen_class.addition_button_pressed(), relief="flat" )
    addition_button.place(x=110.0, y=187.0, width=50.0, height=22.0 )
    addition_button.config(activebackground="#C3C3C3")
    def additionbutton_onenter(event):
        event.widget.config(bg="#C3C3C3")
        if optionsscreen_class.flashcardtype == "+":
             optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_addition, image=optionsscreen_class.image_buttonbg_outline_selected)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_addition, image=optionsscreen_class.image_buttonbg_selected)
    def additionbutton_onleave(event):
        event.widget.config(bg="#D9D9D9"),
        if optionsscreen_class.flashcardtype == "+":
             optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_addition, image=optionsscreen_class.image_buttonbg_outline)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_addition, image=optionsscreen_class.image_buttonbg)
    addition_button.bind("<Enter>", additionbutton_onenter)
    addition_button.bind("<Leave>", additionbutton_onleave)



    def divison_button_pressed():
        optionsscreen_class.flashcardtype = "/"
        optionsscreen_class.explanationtitle, optionsscreen_class.explanation, optionsscreen_class.difficultyint1, optionsscreen_class.difficultyint2 = optionsscreen_class.get_info(
            optionsscreen_class.flashcardtype, optionsscreen_class.flashcarddifficulty)
        optionsscreen_class.explanationtitle = "Divison -"
        optionsscreen_class.explanation = "Put your division skills to the test!"
        optionsscreen_class.clear_type_outline()
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_division, image=optionsscreen_class.image_buttonbg_outline_selected)
        mainscreen_canvas.itemconfigure(mainscreen_class.mathoperator, image=mainscreen_class.image_mathoperator_divide)
    division_button = Button(optionsscreen_canvas, image=image_division_button, borderwidth=0, highlightthickness=0, bg="#D9D9D9", command=lambda: optionsscreen_class.divison_button_pressed(), relief="flat" )
    division_button.place(x=110.0, y=235.0, width=50.0, height=22.0 )
    division_button.config(activebackground="#C3C3C3")
    def divisionbutton_onenter(event):
        event.widget.config(bg="#C3C3C3"),
        if optionsscreen_class.flashcardtype == "/":
             optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_division, image=optionsscreen_class.image_buttonbg_outline_selected)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_division, image=optionsscreen_class.image_buttonbg_selected)
    def divisionbutton_onleave(event):
        event.widget.config(bg="#D9D9D9"),
        if optionsscreen_class.flashcardtype == "/":
             optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_division, image=optionsscreen_class.image_buttonbg_outline)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_division, image=optionsscreen_class.image_buttonbg)
    division_button.bind("<Enter>", divisionbutton_onenter)
    division_button.bind("<Leave>", divisionbutton_onleave)



    


    def clear_type_outline():
        sound_class.sound_buttonpress.play()
        optionsscreen_canvas.itemconfig(optionsscreen_class.description_title, text=optionsscreen_class.explanationtitle)
        optionsscreen_class.description.config(text=optionsscreen_class.explanation)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_addition, image=optionsscreen_class.image_buttonbg)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_division, image=optionsscreen_class.image_buttonbg)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_multiplication, image=optionsscreen_class.image_buttonbg)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_type_subtraction, image=optionsscreen_class.image_buttonbg)
        data_class.does_score_exist()
        optionsscreen_canvas.itemconfig(optionsscreen_class.specific_highscore_text, text=data_class.highscore_dict[f"{optionsscreen_class.flashcardtype}-{optionsscreen_class.flashcarddifficulty}-{optionsscreen_class.flashcardtime}"])







    #Difficulty Buttons
    def classical_button_pressed():
        optionsscreen_class.flashcarddifficulty = "classical"
        optionsscreen_class.explanationtitle, optionsscreen_class.explanation, optionsscreen_class.difficultyint1, optionsscreen_class.difficultyint2 = optionsscreen_class.get_info(
            optionsscreen_class.flashcardtype, optionsscreen_class.flashcarddifficulty)
        optionsscreen_class.clear_difficulty_outline()
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_classical, image=optionsscreen_class.image_buttonbg_outline_selected)
    classical_button = Button(optionsscreen_canvas, image=image_classical_button, borderwidth=0, highlightthickness=0, bg="#D9D9D9", command=lambda: optionsscreen_class.classical_button_pressed(), relief="flat")
    classical_button.place(x=375.0, y=91.0, width=50.0, height=22.0)
    classical_button.config(activebackground="#C3C3C3")
    def classicalbutton_onenter(event):
        event.widget.config(bg="#C3C3C3")
        if optionsscreen_class.flashcarddifficulty == "classical":
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_classical, image=optionsscreen_class.image_buttonbg_outline_selected)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_classical, image=optionsscreen_class.image_buttonbg_selected)
    def classicalbutton_onleave(event):
        event.widget.config(bg="#D9D9D9"),
        if optionsscreen_class.flashcarddifficulty == "classical":
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_classical, image=optionsscreen_class.image_buttonbg_outline)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_classical, image=optionsscreen_class.image_buttonbg)
    classical_button.bind("<Enter>", classicalbutton_onenter)
    classical_button.bind("<Leave>", classicalbutton_onleave)



    def easy_button_pressed():
        optionsscreen_class.flashcarddifficulty = "easy"
        optionsscreen_class.explanationtitle, optionsscreen_class.explanation, optionsscreen_class.difficultyint1, optionsscreen_class.difficultyint2 = optionsscreen_class.get_info(
            optionsscreen_class.flashcardtype, optionsscreen_class.flashcarddifficulty)
        optionsscreen_class.clear_difficulty_outline()
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_easy, image=optionsscreen_class.image_buttonbg_outline_selected)
        optionsscreen_class.flashcarddifficulty = "easy"
    easy_button = Button(optionsscreen_canvas, image=image_easy_button, borderwidth=0, highlightthickness=0, bg="#D9D9D9", command=lambda: optionsscreen_class.easy_button_pressed(), relief="flat" )
    easy_button.place(x=375.0, y=140.0, width=50.0, height=20.0 )
    easy_button.config(activebackground="#C3C3C3")
    def easybutton_onenter(event):
        event.widget.config(bg="#C3C3C3")
        if optionsscreen_class.flashcarddifficulty == "easy":
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_easy, image=optionsscreen_class.image_buttonbg_outline_selected)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_easy, image=optionsscreen_class.image_buttonbg_selected)
    def easybutton_onleave(event):
        event.widget.config(bg="#D9D9D9")
        if optionsscreen_class.flashcarddifficulty == "easy":
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_easy, image=optionsscreen_class.image_buttonbg_outline)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_easy, image=optionsscreen_class.image_buttonbg)
    easy_button.bind("<Enter>", easybutton_onenter)
    easy_button.bind("<Leave>", easybutton_onleave)


    def medium_button_pressed():
        optionsscreen_class.flashcarddifficulty = "medium"
        optionsscreen_class.explanationtitle, optionsscreen_class.explanation, optionsscreen_class.difficultyint1, optionsscreen_class.difficultyint2 = optionsscreen_class.get_info(
            optionsscreen_class.flashcardtype, optionsscreen_class.flashcarddifficulty)
        optionsscreen_class.clear_difficulty_outline()
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_medium, image=optionsscreen_class.image_buttonbg_outline_selected)
        optionsscreen_class.flashcarddifficulty = "medium"
    medium_button = Button(optionsscreen_canvas, image=image_medium_button, borderwidth=0, highlightthickness=0, bg="#D9D9D9", command=lambda: optionsscreen_class.medium_button_pressed(), relief="flat" )
    medium_button.place(x=374.0, y=187.0, width=52.0, height=22.0 )
    medium_button.config(activebackground="#C3C3C3")
    def mediumbutton_onenter(event):
        event.widget.config(bg="#C3C3C3")
        if optionsscreen_class.flashcarddifficulty == "medium":
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_medium, image=optionsscreen_class.image_buttonbg_outline_selected)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_medium, image=optionsscreen_class.image_buttonbg_selected)
    def mediumbutton_onleave(event):
        event.widget.config(bg="#D9D9D9")
        if optionsscreen_class.flashcarddifficulty == "medium":
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_medium, image=optionsscreen_class.image_buttonbg_outline)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_medium, image=optionsscreen_class.image_buttonbg)
    medium_button.bind("<Enter>", mediumbutton_onenter)
    medium_button.bind("<Leave>", mediumbutton_onleave)


    def hard_button_pressed():
        optionsscreen_class.flashcarddifficulty = "hard"
        optionsscreen_class.explanationtitle, optionsscreen_class.explanation, optionsscreen_class.difficultyint1, optionsscreen_class.difficultyint2 = optionsscreen_class.get_info(
            optionsscreen_class.flashcardtype, optionsscreen_class.flashcarddifficulty)
        optionsscreen_class.clear_difficulty_outline()
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_hard, image=optionsscreen_class.image_buttonbg_outline_selected)
        optionsscreen_class.flashcarddifficulty = "hard"
    hard_button = Button(optionsscreen_canvas, image=image_hard_button, borderwidth=0, highlightthickness=0, bg="#D9D9D9", command=lambda: optionsscreen_class.hard_button_pressed(), relief="flat")
    hard_button.place(x=375.0, y=234.5, width=50.0, height=22.0)
    hard_button.config(activebackground="#C3C3C3")
    def hardbutton_onenter(event):
        event.widget.config(bg="#C3C3C3"),
        if optionsscreen_class.flashcarddifficulty == "hard":
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_hard, image=optionsscreen_class.image_buttonbg_outline_selected)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_hard, image=optionsscreen_class.image_buttonbg_selected)
    def hardbutton_onleave(event):
        event.widget.config(bg="#D9D9D9"),
        if optionsscreen_class.flashcarddifficulty == "hard":
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_hard, image=optionsscreen_class.image_buttonbg_outline)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_hard, image=optionsscreen_class.image_buttonbg)
    hard_button.bind("<Enter>", hardbutton_onenter)
    hard_button.bind("<Leave>", hardbutton_onleave)


    difficulty_info = {
        ("/", "classical"): ("Classical -", "Divide numbers up to 50's! A classical challenge!", 1, 50),
        ("-", "classical"): ("Classical -", "Subtract up to the 70's! A classical challenge!", 1, 79),
        ("*", "classical"): ("Classical -", "Times tables up to the 15's! A classical challenge!",1, 15),
        ("+", "classical"): ("Classical -", "Addition up to the 70's! A classical challenge!", 1, 79),
        ("/", "easy"): ("Easy -", "Divide numbers 15 and below!", 1, 15),
        ("-", "easy"): ("Easy -", "Subtract numbers 30 and below!", 1, 29),
        ("*", "easy"): ("Easy -", "Times tables up to the 10's!",1, 10),
        ("+", "easy"): ("Easy -", "Add numbers 30 and below!", 1, 29),
        ("/", "medium"): ("Medium -", "Divide numbers up to 25!", 1, 25),
        ("-", "medium"): ("Medium -", "Subtract numbers up to 50!", 1, 50),
        ("*", "medium"): ("Medium -", "Times tables up to the 13's!",1, 13),
        ("+", "medium"): ("Medium -", "Add numbers up to 50!", 1, 50),
        ("/", "hard"): ("Hard -", "Divide numbers below the 100's!", 1, 99),
        ("-", "hard"): ("Hard -", "Subtract numbers below the 100's!", 1, 99),
        ("*", "hard"): ("Hard -", "Times tables up to the 20's!",1, 20),
        ("+", "hard"): ("Hard -", "Add numbers below the 100's!", 1, 99),
    }  
    def get_info(card_type, difficulty):
        return optionsscreen_class.difficulty_info.get((card_type, difficulty))

    def clear_difficulty_outline():
        sound_class.sound_buttonpress.play()
        optionsscreen_canvas.itemconfig(optionsscreen_class.description_title, text=optionsscreen_class.explanationtitle)
        optionsscreen_class.description.config(text=optionsscreen_class.explanation)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_hard, image=optionsscreen_class.image_buttonbg)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_medium, image=optionsscreen_class.image_buttonbg)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_easy, image=optionsscreen_class.image_buttonbg)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_difficulty_classical, image=optionsscreen_class.image_buttonbg)
        data_class.does_score_exist()
        optionsscreen_canvas.itemconfig(optionsscreen_class.specific_highscore_text, text=data_class.highscore_dict[f"{optionsscreen_class.flashcardtype}-{optionsscreen_class.flashcarddifficulty}-{optionsscreen_class.flashcardtime}"])


    #Mode Buttons
    def practice_button_pressed():
        optionsscreen_class.explanationtitle = "Practice -"
        optionsscreen_class.flashcardtime = "practice"
        optionsscreen_class.explanation = "No time limit! Tone your math skills! (No results will be stored)"
        optionsscreen_class.clear_time_outline()
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_practice, image=optionsscreen_class.image_buttonbg_outline_selected)
    practice_button = Button(optionsscreen_canvas, image=image_practice_button, borderwidth=0, highlightthickness=0, bg="#D9D9D9", command=lambda: optionsscreen_class.practice_button_pressed(), relief="flat")
    practice_button.place(x=642.0, y=235.0, width=50.0, height=22.0)
    practice_button.config(activebackground="#C3C3C3")
    def practicebutton_onenter(event):
        event.widget.config(bg="#C3C3C3")
        if optionsscreen_class.flashcardtime == "practice":
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_practice, image=optionsscreen_class.image_buttonbg_outline_selected)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_practice, image=optionsscreen_class.image_buttonbg_selected)
    def practicebutton_onleave(event):
        event.widget.config(bg="#D9D9D9")
        if optionsscreen_class.flashcardtime == "practice":
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_practice, image=optionsscreen_class.image_buttonbg_outline)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_practice, image=optionsscreen_class.image_buttonbg)
    practice_button.bind("<Enter>", practicebutton_onenter)
    practice_button.bind("<Leave>", practicebutton_onleave)


    def twominute_button_pressed():
        optionsscreen_class.minutes = 2
        optionsscreen_class.seconds = 1
        optionsscreen_class.explanationtitle = "2:00 -"
        optionsscreen_class.explanation = "A good test of math skill and endurance! This is the standard flash card time!"
        optionsscreen_class.flashcardtime = "twominute"
        optionsscreen_class.clear_time_outline()
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_twominute, image=optionsscreen_class.image_buttonbg_outline_selected)
    twominute_button = Button(optionsscreen_canvas, image=image_twominute_button, borderwidth=0, highlightthickness=0, bg="#D9D9D9", command=lambda: optionsscreen_class.twominute_button_pressed(), relief="flat")
    twominute_button.place(x=644.0, y=92.0, width=47.0, height=20.0)
    twominute_button.config(activebackground="#C3C3C3")
    def twominutebutton_onenter(event):
        event.widget.config(bg="#C3C3C3")
        if optionsscreen_class.flashcardtime == "twominute":
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_twominute, image=optionsscreen_class.image_buttonbg_outline_selected)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_twominute, image=optionsscreen_class.image_buttonbg_selected)
    def twominutebutton_onleave(event):
        event.widget.config(bg="#D9D9D9")
        if optionsscreen_class.flashcardtime == "twominute":
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_twominute, image=optionsscreen_class.image_buttonbg_outline)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_twominute, image=optionsscreen_class.image_buttonbg)
    twominute_button.bind("<Enter>", twominutebutton_onenter)
    twominute_button.bind("<Leave>", twominutebutton_onleave)


    def oneminute_button_pressed():
        optionsscreen_class.minutes = 1
        optionsscreen_class.seconds = 1
        optionsscreen_class.explanationtitle = "1:00 -"
        optionsscreen_class.explanation = "Low on time? how about a minute of pure math!"
        optionsscreen_class.flashcardtime = "oneminute"
        optionsscreen_class.clear_time_outline()
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_oneminute, image=optionsscreen_class.image_buttonbg_outline_selected)
    oneminute_button = Button(optionsscreen_canvas, image=image_oneminute_button, borderwidth=0, highlightthickness=0, bg="#D9D9D9", command=lambda: optionsscreen_class.oneminute_button_pressed(), relief="flat")
    oneminute_button.place(x=642.0, y=139.0, width=50.0, height=22.0)
    oneminute_button.config(activebackground="#C3C3C3")
    def oneminutebutton_onenter(event):
        event.widget.config(bg="#C3C3C3")
        if optionsscreen_class.flashcardtime == "oneminute":
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_oneminute, image=optionsscreen_class.image_buttonbg_outline_selected)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_oneminute, image=optionsscreen_class.image_buttonbg_selected)
    def oneminutebutton_onleave(event):
        event.widget.config(bg="#D9D9D9")
        if optionsscreen_class.flashcardtime == "oneminute":
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_oneminute, image=optionsscreen_class.image_buttonbg_outline)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_oneminute, image=optionsscreen_class.image_buttonbg)
    oneminute_button.bind("<Enter>", oneminutebutton_onenter)
    oneminute_button.bind("<Leave>", oneminutebutton_onleave)



    def thirtysecond_button_pressed():
        optionsscreen_class.minutes = 0
        optionsscreen_class.seconds = 11  #--------------- DEAR GOD PLEASE CHANGE THIS
        optionsscreen_class.explanationtitle = "0:30 -"
        optionsscreen_class.explanation = "Wanna show off? Only thirty seconds to show your true math skills!"
        optionsscreen_class.flashcardtime = "thirtysecond"
        optionsscreen_class.clear_time_outline()
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_thirtysecond, image=optionsscreen_class.image_buttonbg_outline_selected)
    thirtysecond_button = Button(optionsscreen_canvas, image=image_thirtysecond_button, borderwidth=0, highlightthickness=0, bg="#D9D9D9", command=lambda: optionsscreen_class.thirtysecond_button_pressed(), relief="flat")
    thirtysecond_button.place(x=642.0, y=187.0, width=50.0, height=22.0)
    thirtysecond_button.config(activebackground="#C3C3C3")
    def thirtysecondbutton_onenter(event):
        event.widget.config(bg="#C3C3C3")
        if optionsscreen_class.flashcardtime == "thirtysecond":
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_thirtysecond, image=optionsscreen_class.image_buttonbg_outline_selected)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_thirtysecond, image=optionsscreen_class.image_buttonbg_selected)
    def thirtysecondbutton_onleave(event):
        event.widget.config(bg="#D9D9D9")
        if optionsscreen_class.flashcardtime == "thirtysecond":
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_thirtysecond, image=optionsscreen_class.image_buttonbg_outline)
        else:
            optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_thirtysecond, image=optionsscreen_class.image_buttonbg)
    thirtysecond_button.bind("<Enter>", thirtysecondbutton_onenter)
    thirtysecond_button.bind("<Leave>", thirtysecondbutton_onleave)



    def clear_time_outline():
        sound_class.sound_buttonpress.play()
        optionsscreen_canvas.itemconfig(optionsscreen_class.description_title, text=optionsscreen_class.explanationtitle)
        optionsscreen_class.description.config(text=optionsscreen_class.explanation)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_thirtysecond, image=optionsscreen_class.image_buttonbg)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_twominute, image=optionsscreen_class.image_buttonbg)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_oneminute, image=optionsscreen_class.image_buttonbg)
        optionsscreen_canvas.itemconfigure(optionsscreen_class.buttonbg_time_practice, image=optionsscreen_class.image_buttonbg)
        data_class.does_score_exist()
        optionsscreen_canvas.itemconfig(optionsscreen_class.specific_highscore_text, text=data_class.highscore_dict[f"{optionsscreen_class.flashcardtype}-{optionsscreen_class.flashcarddifficulty}-{optionsscreen_class.flashcardtime}"])

    #Back Button
    def back_button_pressed():
        sound_class.sound_buttonpress.play()
        optionsscreen_canvas.pack_forget()
        mainscreen_canvas.pack()
    back_button = Button(optionsscreen_canvas, image=image_back_button, borderwidth=0, highlightthickness=0, bg="#D9D9D9", command=lambda: optionsscreen_class.back_button_pressed(), relief="flat" )
    back_button.place( x=60.0, y=440.0, width=94.0, height=30.0 )
    back_button.config(activebackground="#C3C3C3")
    def backbutton_onenter(event): event.widget.config(bg="#C3C3C3"), optionsscreen_canvas.itemconfigure(optionsscreen_class.back_buttonbg, image=optionsscreen_class.image_back_buttonbg_selected),
    def backbutton_onleave(event): event.widget.config(bg="#D9D9D9"), optionsscreen_canvas.itemconfigure(optionsscreen_class.back_buttonbg, image=optionsscreen_class.image_back_buttonbg)
    back_button.bind("<Enter>", backbutton_onenter)
    back_button.bind("<Leave>", backbutton_onleave)




    #Placed Text
    description_title = optionsscreen_canvas.create_text(215.0, 330.0, anchor="nw", text=explanationtitle, fill="#000000", font=("Encode Sans", 24 * -1) )

    description = Label(optionsscreen_canvas, anchor="nw", text=explanation,
                        font=("Encode Sans", 17 * -1), wraplength=211, fg="#000000", bg="#FFFFFF")
    description.place(x= 296, y= 382)

#-----------------------------------------------------------------


#----------------------------------------------------------------------------------------------- finalScreen
class finalscreen_class():
    finalscore_feedback_text = ''
    #finalScreen Images
    image_scorebanner = PhotoImage( file=relative_to_assets("finalscreen/scorebanner.png"))
    image_scoreseperator = PhotoImage( file=relative_to_assets("finalscreen/scoreseperator.png"))
    image_scorebg = PhotoImage( file=relative_to_assets("finalscreen/scorebg.png"))
    image_buttonbanner = PhotoImage( file=relative_to_assets("finalscreen/buttonbanner.png"))
    image_feedbackbanner = PhotoImage( file=relative_to_assets("finalscreen/feedbackbanner.png"))
    image_buttonbg = PhotoImage( file=relative_to_assets("finalscreen/buttonbg.png"))
    image_buttonbg_selected = PhotoImage( file=relative_to_assets("finalscreen/buttonbg_selected.png"))
    image_continue_button = PhotoImage( file=relative_to_assets("finalscreen/continue_button.png"))
    #Place Elements
    bg_image = finalscreen_canvas.create_image( 395.0, 255.0, image=userscreen_class.image_bg_image)
    scorebanner = finalscreen_canvas.create_image( 391.0, 197.0, image=image_scorebanner )
    scoreseperator_1 = finalscreen_canvas.create_image( 392.0, 90.0, image=image_scoreseperator )
    scoreseperator_2 = finalscreen_canvas.create_image( 392.0, 194.0, image=image_scoreseperator )
    scoreseperator_3 = finalscreen_canvas.create_image( 392.0, 299.0, image=image_scoreseperator )
    scorebg_1 = finalscreen_canvas.create_image( 391.0, 117.0, image=image_scorebg )
    scorebg_2 = finalscreen_canvas.create_image( 391.0, 221.0, image=image_scorebg )
    scorebg_3 = finalscreen_canvas.create_image( 391.0, 332.0, image=image_scorebg )
    buttonbanner = finalscreen_canvas.create_image( 391.0, 436.0, image=image_buttonbanner )
    feedbackbanner = finalscreen_canvas.create_image( 620.0, 436.0, image=image_feedbackbanner )
    buttonbg = finalscreen_canvas.create_image( 620.0, 436.0, image=image_buttonbg )

    #Text
    yourscore_text = finalscreen_canvas.create_text( 390.0, 118.0, anchor="center", text="", fill="#000000", font=("Encode Sans", 33 * -1) )
    incorrect_text = finalscreen_canvas.create_text( 390.0, 222.0, anchor="center", text="", fill="#000000", font=("Encode Sans", 33 * -1) )
    highscore_text = finalscreen_canvas.create_text( 391.0, 332.0, anchor="center", text="", fill="#000000", font=("Encode Sans", 33 * -1) )
    feedback_text = finalscreen_canvas.create_text( 390.0, 435.0, anchor="center", text="", fill="#000000", font=("Encode Sans", 19 * -1, "bold",) )
    finalscreen_canvas.create_text( 308.0, 44.0, anchor="nw", text="You Scored", fill="#000000", font=("Encode Sans", 35 * -1) )
    finalscreen_canvas.create_text( 310.0, 250.0, anchor="nw", text="High Score", fill="#000000", font=("Encode Sans", 35 * -1) )
    finalscreen_canvas.create_text( 325.0, 146.0, anchor="nw", text="Incorrect", fill="#000000", font=("Encode Sans", 35 * -1) )


    #Continue Button
    def continue_button_pressed():
        sound_class.sound_buttonpress.play()
        mainscreen_class.post_game_cleanup()
        finalscreen_canvas.pack_forget()
        mainscreen_canvas.pack()
    continue_button = Button(finalscreen_canvas, image=image_continue_button, borderwidth=0, highlightthickness=0, bg="#D9D9D9", command=lambda: finalscreen_class.continue_button_pressed(), relief="flat" )
    continue_button.place( x=584.0, y=424.0, width=72.0, height=25.0 )
    continue_button.config(activebackground="#C3C3C3")
    def continuebutton_onenter(event): event.widget.config(bg="#C3C3C3"), finalscreen_canvas.itemconfigure(finalscreen_class.buttonbg, image=finalscreen_class.image_buttonbg_selected),
    def continuebutton_onleave(event): event.widget.config(bg="#D9D9D9"), finalscreen_canvas.itemconfigure(finalscreen_class.buttonbg, image=finalscreen_class.image_buttonbg)
    continue_button.bind("<Enter>", continuebutton_onenter)
    continue_button.bind("<Leave>", continuebutton_onleave)

#-----------------------------------------------------------------


#----------------------------------------------------------------------------------------------- historyScreen
class historyscreen_class():
    image_actionbuttonbg = PhotoImage( file=relative_to_assets("historyscreen/actionbuttonbg.png"))
    image_actionbuttonbg_selected = PhotoImage( file=relative_to_assets("historyscreen/actionbuttonbg_selected.png"))
    image_buttonbanner = PhotoImage( file=relative_to_assets("historyscreen/buttonbanner.png"))
    image_back_button = PhotoImage( file=relative_to_assets("historyscreen/back_button.png"))
    image_datasheet_bg = PhotoImage( file=relative_to_assets("historyscreen/datasheet_bg.png"))
    image_info_button = PhotoImage( file=relative_to_assets("historyscreen/info_button.png"))

    bg_image = historyscreen_canvas.create_image( 395.0, 255.0, image=userscreen_class.image_bg_image)
    buttonbanner_1 = historyscreen_canvas.create_image( 89.0, 454.0, image=image_buttonbanner )
    buttonbanner_2 = historyscreen_canvas.create_image( 709.0, 454.0, image=image_buttonbanner )
    actionbuttonbg_1 = historyscreen_canvas.create_image( 89.0, 453.0, image=image_actionbuttonbg )
    actionbuttonbg_2 = historyscreen_canvas.create_image( 710.0, 453.0, image=image_actionbuttonbg )
    datasheet_bg = historyscreen_canvas.create_image( 399.0, 227.0, image=image_datasheet_bg )


    def back_button_pressed():
        sound_class.sound_buttonpress.play()
        historyscreen_canvas.pack_forget()
        mainscreen_canvas.pack()
    back_button = Button(historyscreen_canvas, image=image_back_button, borderwidth=0, highlightthickness=0, bg="#D9D9D9", command=lambda: historyscreen_class.back_button_pressed(), relief="flat" )
    back_button.place( x=42.0, y=438.0, width=93.0, height=30.0 )
    back_button.config(activebackground="#C3C3C3")
    def backbutton_onenter(event): event.widget.config(bg="#C3C3C3"), historyscreen_canvas.itemconfigure(historyscreen_class.actionbuttonbg_1, image=historyscreen_class.image_actionbuttonbg_selected),
    def backbutton_onleave(event): event.widget.config(bg="#D9D9D9"), historyscreen_canvas.itemconfigure(historyscreen_class.actionbuttonbg_1, image=historyscreen_class.image_actionbuttonbg)
    back_button.bind("<Enter>", backbutton_onenter)
    back_button.bind("<Leave>", backbutton_onleave)


    def info_button_pressed():
        sound_class.sound_buttonpress.play()
        profilescreen_canvas.pack()
        historyscreen_canvas.pack_forget()
        profilescreen_class.personalize_screen(data_class.userlevel)
        profilescreen_class.button_back.config(command=lambda: historyscreen_class.changed_back_button_pressed())
        profilescreen_canvas.coords(profilescreen_class.history_bg, 1000, 1000)
        profilescreen_canvas.coords(profilescreen_class.history_banner, 1000, 1000)
        profilescreen_canvas.coords(profilescreen_class.edit_bg, 1000, 1000)
        profilescreen_canvas.coords(profilescreen_class.edit_banner, 1000, 1000)
        profilescreen_class.button_history.place_configure(x=1000, y=1000)
        profilescreen_class.button_edit.place_configure(x=1000, y=1000)
    def changed_back_button_pressed():
        sound_class.sound_buttonpress.play()
        historyscreen_canvas.pack()
        profilescreen_canvas.pack_forget()
        profilescreen_canvas.coords(profilescreen_class.history_bg, 399.0, 451.0)
        profilescreen_canvas.coords(profilescreen_class.history_banner, 399.0, 452.0)
        profilescreen_canvas.coords(profilescreen_class.edit_bg, 601.0, 452.0)
        profilescreen_canvas.coords(profilescreen_class.edit_banner, 601.0, 451.0)
        profilescreen_class.button_history.place_configure(x=366.0, y=437.0)
        profilescreen_class.button_edit.place_configure(x=568.0, y=437.0)
        profilescreen_class.button_back.config(command=lambda: profilescreen_class.button_back_pressed())
    info_button = Button(historyscreen_canvas, image=image_info_button, borderwidth=0, highlightthickness=0, bg="#D9D9D9", command=lambda: historyscreen_class.info_button_pressed(), relief="flat" )
    info_button.place( x=663.0, y=438.0, width=93.0, height=30.0 )
    info_button.config(activebackground="#C3C3C3")
    def infobutton_onenter(event): event.widget.config(bg="#C3C3C3"), historyscreen_canvas.itemconfigure(historyscreen_class.actionbuttonbg_2, image=historyscreen_class.image_actionbuttonbg_selected),
    def infobutton_onleave(event): event.widget.config(bg="#D9D9D9"), historyscreen_canvas.itemconfigure(historyscreen_class.actionbuttonbg_2, image=historyscreen_class.image_actionbuttonbg)
    info_button.bind("<Enter>", infobutton_onenter)
    info_button.bind("<Leave>", infobutton_onleave)


    tree = ttk.Treeview(historyscreen_canvas, columns=('date', 'time', 'correct', 'incorrect', 'mode', '%'), show = 'headings')

    tree.heading('date', text='Date')
    tree.heading('time', text='Time')
    tree.heading('correct', text='Correct')
    tree.heading('incorrect', text='Incorrect')
    tree.heading('mode', text='Mode')
    tree.heading('%', text='%')

    tree.column('date', width=90, stretch=False, anchor='center')
    tree.column('time', width=90, stretch='no', anchor='center')
    tree.column('correct', width=70, stretch='no', anchor='center')
    tree.column('incorrect', width=70, stretch='no', anchor='center')
    tree.column('mode', width=160, stretch='no', anchor='center')
    tree.column('%', width=70, stretch='no', anchor='center')

    def display_data(userlevel):
        from sv_ttk import use_light_theme
        use_light_theme()
        try:
            historyscreen_class.tree.delete(*historyscreen_class.tree.get_children())
        except:
            pass
        for game in data_class.user_data[userlevel]['gamehistory']:
            try:
                game_percentage = game['correct'] / (game['incorrect'] + game['correct'])
                historyscreen_class.tree.insert('', 'end', values=(game['date'], game['time'], game['correct'], game['incorrect'], game['mode'], f"{round(game_percentage * 100, 2)}%"))
            except:
                pass

    scrollbar = ttk.Scrollbar(historyscreen_canvas, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    def disableEvent(event):
        return "break"

    tree.bind("<Button-1>", disableEvent)


    tree.place(x=110, y=67, height=317, width=560)
    scrollbar.place(x=673, y=67, height=317)

    

#-----------------------------------------------------------------









userscreen_canvas.pack()




window.resizable(False, False)
window.mainloop()




