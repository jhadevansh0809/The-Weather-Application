from tkinter import *
import requests
root=Tk()

root.geometry("500x600")
root.title("Weather Update")
root.maxsize(500,600)

strvar1=StringVar()
screen1 = Entry(root, textvar=strvar1, font=("lucida 25 italic"), bg='white', borderwidth=6, relief=SUNKEN)
screen1.pack(ipady=15, padx=15, pady=10)

def theweather():
    def clear_frame():
        for widgets in frame.winfo_children():
            widgets.destroy()
    clear_frame()
    API_KEY = "c7d61981715f88af00b2b47b7c40ab75"
    CITY = strvar1.get()
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        l1 = Label(frame, text=f"{CITY.upper()}", font="Helvetica 20 bold", fg="red", pady=22).pack(fill=X)
        l2 = Label(frame, text="{:.2f} degree celcius".format(temperature - 273), font="Helvetica 15 bold",
                   fg="red", pady=22).pack(fill=X)
        l3 = Label(frame, text=f"Humidity: {humidity}", font="Helvetica 15 bold", fg="red", pady=22).pack(fill=X)
        l4 = Label(frame, text=f"Weather Report: {report[0]['description']}", font="Helvetica 15 bold", fg="red",
                   pady=22).pack(fill=X)


b1 = Button(root, text="ENTER", bg="green", font=("lucida 15 italic"),command=theweather).pack(ipadx=30, ipady=5, pady=10)
frame = Frame(root, borderwidth=6, bg="light green")
frame.pack(fill=X,anchor="nw",ipadx=180,ipady=180,padx=5,pady=20)

root.configure(background="orange")
root.mainloop()