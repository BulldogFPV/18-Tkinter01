import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# TODO: 1. (6 pts)
#
#   1) Create a tkinter window with the title "Form".
#
#   2) Add a label and an entry box for each of the following pieces of
#      information.
#
#       - Name
#       - Address Line 1
#       - Address Line 2
#       - City
#       - State
#       - Zip Code
#       - Phone Number
#       - Email Address
#
#   3) Add a "Submit" button at the bottom of your form.
#
#   4) Give your form a color theme by changing the colors of your widgets.
#      Also, feel free to change the sizes of the widgets as you see fit.
#
#   5) Make sure you call the window's mainloop() method so your window will
#      appear.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
import tkinter as tk

window = tk.Tk()
window.title("Form")
def submit_form():
    name = name_entry.get()
    address1 = address1_entry.get()
    address2 = address2_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    zip_code = zip_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    print("Form Submitted")
    print("Name:", name)
    print("Address Line 1:", address1)
    print("Address Line 2:", address2)
    print("City:", city)
    print("State:", state)
    print("Zip Code:", zip_code)
    print("Phone Number:", phone)
    print("Email Address:", email)
labels = ["Name", "Address Line 1", "Address Line 2", "City", "State", "Zip Code", "Phone Number", "Email Address"]
entries = []
for i, label_text in enumerate(labels):
    label = tk.Label(window, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=5)
    
    entry = tk.Entry(window)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)
submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.grid(row=len(labels), column=0, columnspan=2, padx=10, pady=10)
window.configure(bg='cyan')
for entry in entries:
    entry.configure(bg='yellow')
window.mainloop()