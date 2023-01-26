from tkinter import *

import phonenumbers
from PIL import Image, ImageTk
import tkintermapview
from phonenumbers import geocoder
import requests


class MapWindow:
    def __init__(self, window, master=None):
        self.root = window
        self.bg = "#ed1a77"
        self.dark_bg = "#0b1478"
        self.leel_font = "Leelawadee UI Semilight"
        self.root.config(bg=self.dark_bg)
        self.api_key = None
        # --------------------------------------------------------------------------------------------------------------
        self.map_view = tkintermapview.TkinterMapView(self.root, width=800, height=510, corner_radius=0)
        self.map_view.place(relx=0.25, rely=0.25)
        # --------------------------------------------------------------------------------------------------------------
        # Functions

        def phone_checker():
            ph_number = self.text_field.get()
            data = {}
            api_key = "qAoFuvgYZZ02ZXhbNVht3ixk0k2HnG7EUOigVyAE"
            google_api_key = "AIzaSyAxcsh8ZgHvNlXuKagxn4l8mx5u4ZeJEWQ"
            headers = {
                "apikey": "qAoFuvgYZZ02ZXhbNVht3ixk0k2HnG7EUOigVyAE"
            }
            url = f"https://api.numlookupapi.com/v1/validate/{ph_number}?apikey={api_key}"
            resp = requests.get(url, headers=headers, data=data)
            result = resp.text
            y = result.split(":")
            # line = result["line_type"]
            carrier = y[9].split(" ")
            flag = False
            for _ in carrier:
                if carrier[:2][0][:2] == '""':
                    flag = True
                else:
                    flag = False
            if flag is True:
                cc = "None"
            else:
                cc = carrier[0][1::] + " " + carrier[1]
            rr = y[8].split(",")
            local = rr[0][1:-1:]
            line = y[10][1:-2:]
            number_check = phonenumbers.parse(ph_number)
            location = geocoder.description_for_number(number_check, "en")
            country_code = str(number_check.country_code)
            # carrier = result['carrier']
            # time_zone = ll[2]['timezone']['name']
            # line_type = ll[-3]['Line Type'][15::]
            nat_no = number_check.national_number
            google_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={local}+{location}&key={google_api_key}"
            google_req = requests.get(google_url)
            a = google_req.json()
            lat = a['results'][0]['geometry']['location']['lat']
            lng = a['results'][0]['geometry']['location']['lng']
            self.a.config(text=nat_no, font=(self.leel_font, 15, "bold"))
            self.b.config(text=cc, font=(self.leel_font, 15, "bold"))
            self.c.config(text=local, font=(self.leel_font, 15, "bold"))
            self.d.config(text=location, font=(self.leel_font, 15, "bold"))
            self.e.config(text="+"+country_code, font=(self.leel_font, 15, "bold"))
            self.f.config(text=line, font=(self.leel_font, 15, "bold"))
            self.g.config(text=lat, font=(self.leel_font, 15, "bold"))
            self.h.config(text=lng, font=(self.leel_font, 15, "bold"))
            marker_one = self.map_view.set_marker(lat, lng, text=nat_no)
            self.map_view.set_position(lat, lng)
            self.map_view.set_zoom(15)

        # --------------------------------------------------------------------------------------------------------------
        self.logo_img = Image.open("Untitled.png")
        self.logo_img = self.logo_img.resize((80, 80), Image.Resampling.LANCZOS)
        self.logo_img = ImageTk.PhotoImage(self.logo_img)

        self.lolo_im = Image.open("logotext.png")
        self.lolo_im = ImageTk.PhotoImage(self.lolo_im)

        self.search_bar_image = Image.open("search.png")
        self.search_bar_image = ImageTk.PhotoImage(self.search_bar_image)

        self.search_button_img = Image.open("search_icon.png")
        self.search_button_img = ImageTk.PhotoImage(self.search_button_img)
        # --------------------------------------------------------------------------------------------------------------
        # Labels
        self.logo_label = Label(self.root, image=self.logo_img, bd=0, bg=self.dark_bg, fg=self.dark_bg)
        self.logo_label.place(x=10, y=10)

        self.logo_text = Label(self.root, image=self.lolo_im, bd=0, bg=self.dark_bg)
        self.logo_text.place(x=90, y=20)

        self.search_bar = Label(self.root, image=self.search_bar_image, bd=0, bg=self.dark_bg, fg="#151819")
        self.search_bar.place(x=540, y=20)

        Label(self.root, text="Search", fg="white", bd=0, bg="#151819", width=7,
              font=(self.leel_font, 17)).place(x=570, y=40)

        self.phone_number_label = Label(self.root, text="Phone Number", bd=0, bg=self.dark_bg,
                                        font=(self.leel_font, 15), fg="white")
        self.phone_number_label.place(x=40, y=150-20)

        self.a = Label(self.root, text="---", bd=0, bg=self.dark_bg, fg="white", font=(self.leel_font, 15))
        self.a.place(x=40, y=185-20)

        self.carrier_label = Label(self.root, text="Carrier", bd=0, bg=self.dark_bg, fg="white",
                                   font=(self.leel_font, 15))
        self.carrier_label.place(x=40, y=250-20)

        self.b = Label(self.root, text="---", bd=0, bg=self.dark_bg, fg="white", font=(self.leel_font, 15))
        self.b.place(x=40, y=285-20)

        self.location_label = Label(self.root, text="Location", bd=0, bg=self.dark_bg, fg="white",
                                    font=(self.leel_font, 15))
        self.location_label.place(x=40, y=350-20)

        self.c = Label(self.root, text="---", bd=0, bg=self.dark_bg, fg="white", font=(self.leel_font, 15))
        self.c.place(x=40, y=385-20)

        self.region_label = Label(self.root, text="Region", bd=0, bg=self.dark_bg, fg="white",
                                  font=(self.leel_font, 15))
        self.region_label.place(x=40, y=450-20)

        self.d = Label(self.root, text="---", bd=0, bg=self.dark_bg, fg="white", font=(self.leel_font, 15))
        self.d.place(x=40, y=485-20)

        self.country_code_label = Label(self.root, text="Country Code", bg=self.dark_bg, fg="white", bd=0,
                                        font=(self.leel_font, 15))
        self.country_code_label.place(x=40, y=550-20)

        self.e = Label(self.root, text="---", bd=0, bg=self.dark_bg, fg="white", font=(self.leel_font, 15))
        self.e.place(x=40, y=585-20)

        self.line_type_label = Label(self.root, text="Line Type", bd=0, bg=self.dark_bg, fg="white",
                                     font=(self.leel_font, 15))
        self.line_type_label.place(x=40, y=650-20)

        self.f = Label(self.root, text="---", bd=0, bg=self.dark_bg, fg="white", font=(self.leel_font, 15))
        self.f.place(x=40, y=685-20)

        self.latitude_label = Label(self.root, text="Lat:", bd=0, bg=self.dark_bg, fg="white",
                                    font=(self.leel_font, 15))
        self.latitude_label.place(x=270, y=150)

        self.g = Label(self.root, text="---", bd=0, bg=self.dark_bg, fg="white", font=(self.leel_font, 15))
        self.g.place(x=310, y=150)

        self.longitude_label = Label(self.root, text="Long:", bd=0, bg=self.dark_bg, fg="white",
                                     font=(self.leel_font, 15))
        self.longitude_label.place(x=420, y=150)

        self.h = Label(self.root, text="---", bd=0, bg=self.dark_bg, fg="white", font=(self.leel_font, 15))
        self.h.place(x=480, y=150)
        # --------------------------------------------------------------------------------------------------------------
        # Buttons
        self.search_button = Button(self.root, image=self.search_button_img, bd=0, bg="#151819", fg=self.dark_bg,
                                    command=phone_checker)
        self.search_button.place(x=920, y=30)
        # --------------------------------------------------------------------------------------------------------------
        self.text_field = Entry(self.root, bd=0, bg="#151819", fg="white", width=18, font=(self.leel_font, 20))
        self.text_field.place(x=660, y=37)


if __name__ == "__main__":
    window = Tk()
    window.geometry("1080x720")
    window.iconbitmap('icon.ico')
    window.title("Phone-Locator-IO")
    window.resizable(False, False)
    x = MapWindow(window)
    window.mainloop()
