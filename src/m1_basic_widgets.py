import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# Done: 1. (2 pts)
#
#   First, create a tkinter window called window. This is where you will be
#   putting all of your widgets.
#
#   Next, call window's mainloop() method so your window will show up when you
#   run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# Done: 2. (2 pts)
#
#   Now, create a basic label called label with some text in it. You decide
#   what text you want in the label.
#
#   Make sure you use the label's pack() method to add it to your window.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# Done: 3. (2 pts)
#
#   Now, create a basic button called button with some text in it. You decide
#   what text you want in the button.
#
#   Make sure you use the button's pack() method to add it to your window.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# Done: 4. (2 pts)
#
#   Now, create a basic entry box called entry. No need for customization here.
#
#   Make sure you use the entry's pack() method to add it to your window.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
window = tk.Tk()
window.title("Window")
label = tk.Label(window, text="Rock n' Roll!")
label.pack()
button = tk.Button(window, text="Press!")
button.pack()
entry = tk.Entry(window)
entry.pack()
window.mainloop()