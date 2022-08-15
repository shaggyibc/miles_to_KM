from tkinter import *
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=600, height=300)
window.config(padx=20, pady=20)


def output_km(km):
    my_label3 = Label(text=f"{km} Km", font=("Ariel", 20, "bold"))
    # my_label.config(padx=30, pady=30)
    my_label3.grid(column=3, row=3)

# def miles_scale(value):
#     # miles_text = value + " Miles"
#     my_label2 = Label(text=f"{value} Miles", font=("Ariel", 20, "bold"))
#     my_label2.grid(column=1, row=0)
#     km = round(int(value) * 1.609)
#     output_km(km)

def button_clicked():
    # Gets text in entry
    miles = entry.get()
    km = round(int(miles) * 1.609)
    output_km(km)



# my_label = Label(text="", font=("Ariel", 10, "bold"))
# my_label.config(padx=0, pady=30)
# my_label.grid(column=0, row=0)

# miles = Scale(from_=0, to=100, command=miles_scale)
# miles.grid(column=2, row=0)

# my_label2 = Label(text="Miles", font=("Ariel", 20, "bold"))
# # my_label2.config(padx=30, pady=30)
# my_label2.grid(column=1, row=0)

my_label4= Label(text="is equal to", font=("Ariel", 20, "bold"))
my_label4.config(padx=0, pady=30)
my_label4.grid(column=2, row=1)

# my_label5= Label(text="km", font=("Ariel", 20, "bold"))
# my_label5.config(padx=0, pady=30)
# my_label5.grid(column=2, row=1)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=4, row=1)

entry = Entry(width=10)
#Add some text to begin with
entry.insert(END, string="")
entry.grid(column=4, row=0)









window.mainloop()


