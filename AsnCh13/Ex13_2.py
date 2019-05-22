# Programming Exercise 13 - 2
# Latin Translator
# Author: Randall Fishwick

import tkinter


class TransLatinGUI:
    def __init__(self):
        # Create the main window widget
        self.main_window = tkinter.Tk()

        # Create two frames to group widgets.
        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Create the button widgets for the top frame.
        # The the Latin words should appear
        # on the face of the Buttons.
        # The appropriate translate method should be executed when
        # the user clicks the Button.

        self.sinister_button = tkinter.Button(self.top_frame,
                                              text='sinister',
                                              command=self.translate_sinister)

        self.medium_button = tkinter.Button(self.top_frame,
                                            text='medium',
                                            command=self.translate_medium)

        self.dexter_button = tkinter.Button(self.top_frame,
                                            text='dexter',
                                            command=self.translate_dexter)

        self.quit_button = tkinter.Button(self.top_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        # Create the description label widget for the bottom frame.
        self.desc_label = tkinter.Label(self.bottom_frame, text='English Translation: ')

        # We need a StringVar object to associate with
        # the translate label. Use the object's set method
        # to store a string of blank characters.
        self.value = tkinter.StringVar()

        # Create the translation label
        self.translate_label = tkinter.Label(self.bottom_frame, textvariable=self.value)

        # Pack the Buttons.
        self.sinister_button.pack(side='left')
        self.medium_button.pack(side='left')
        self.dexter_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the labels
        self.desc_label.pack(side='left')
        self.translate_label.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The translate methods are callback functions for
    # the each translate button.

    def translate_sinister(self):
        self.value.set('left')

    def translate_medium(self):
        self.value.set('center')

    def translate_dexter(self):
        self.value.set('right')


# Create an instance of TransLatinGUI class
show_info = TransLatinGUI()
