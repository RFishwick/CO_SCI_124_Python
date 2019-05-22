# Programming Exercise 13 - 1

import tkinter


class ShowInfoGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create two frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create a blank label in the top frame
        self.value = tkinter.StringVar()
        self.address_label = tkinter.Label(self.top_frame, \
                                           textvariable=self.value)

        # Create the two buttons in the bottom frame
        self.address_button = tkinter.Button(self.bottom_frame, \
                                             text='Show Info', command=self.show_info)
        self.quit_button = tkinter.Button(self.bottom_frame, \
                                          text='Quit', command=self.main_window.destroy)

        # Pack the label
        self.address_label.pack()
        # Pack the buttons
        self.address_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # Define the show_info function
    def show_info(self):
        self.value.set('Steven Marcus\n274 Baily Drive\n' \
                       'Waynesville, NC 27999')


# Create an instance of ShowInfoGUI
show_info = ShowInfoGUI()

