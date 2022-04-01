import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 600
#API: Application Programming Interface
# 8d1a935488e64726a9c860b3a6100252
#api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}

def test_func(entry):
    print("This is the Entry:", entry)

def format_reponse(weather):
    try:
        name = weather["name"]
        desc = weather["weather"][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature(*F): %s' % (name, desc, temp)
        # final_str = str(name) + " " + str(desc) + " " + str(temp)
    except:
        final_str = "There was a problem retriving that information"
    
    return final_str

def get_weather(city):
    weather_key = "8d1a935488e64726a9c860b3a6100252"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key, "q": city, "units": "imperial"}
    response = requests.get(url, params=params)
    weather = response.json()

    # print(weather["name"])
    # print(weather["weather"][0]['description'])
    # print(weather['main']['temp'])
    label["text"] = format_reponse(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bg_img = tk.PhotoImage(file="weather.gif")
bg_label = tk.Label(root)
bg_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=("Courier", 10))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font= ("Courier", 10), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lower_frame, font=("Courier", 15), bg='white')
label.place(relwidth=1, relheight=1)

# print(tk.font.families())

#Remember to get the script for weather app with icons
root.mainloop()