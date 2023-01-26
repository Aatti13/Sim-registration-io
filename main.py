"""
Phone-Locator-IO
--------------------------------------------------------------------------
I have only taken logo, speak button and search bar from the former.
--------------------------------------------------------------------------
Extra hexcodes got from Images...
Link for hexcode finder: https://html-color-codes.info/colors-from-image/#
--------------------------------------------------------------------------
APIs:
1. numberlookup API
2. Google Geocoder API
--------------------------------------------------------------------------
The Following Code does not contain any intentional errors...
--------------------------------------------------------------------------
No Lines of code have been deleted or omitted and the code is complete...
--------------------------------------------------------------------------
API keys have been removed for security reasons
Please use your own API key
--------------------------------------------------------------------------
Done by (IG): @aattreys.ks2022 
"""


# Imports
from tkinter import *

import phonenumbers
from PIL import Image, ImageTk
import tkintermapview
from phonenumbers import geocoder
import requests

# class initiation
class MapWindow:
    def __init__(self, window, master=None):
        
        '''
        Initialising Variables
        1. self.root --> Window initialisation
        2. self.dark_bg --> Background Initialisation
        3. self.leel_font = --> Font Initialisation
        '''
        # --------------------------------------------------------------------------------------------------------------
        self.root = window
        self.dark_bg = "#0b1478"
        self.leel_font = "Leelawadee UI Semilight"
        self.root.config(bg=self.dark_bg)
        # --------------------------------------------------------------------------------------------------------------
        self.map_view = tkintermapview.TkinterMapView(self.root, width=800, height=510, corner_radius=0)
        self.map_view.place(relx=0.25, rely=0.25)
        # --------------------------------------------------------------------------------------------------------------
        # Functions
        """
        Function: phone_checker() --> 0 parameters
        APIs used:
        1. nolookup API
        2. Google Geocoder API
        --> formats
        1. Numlookup: <str>
        2. Geocoder API: json
        """
        def phone_checker():
            """
            Phone number data extraction
            """
            ph_number = self.text_field.get()
            data = {}
            
            # API keys
            api_key = <YOUR-API-KEY> # Enter key as a string
            google_api_key = <API-KEY> # Enter key as a string
            headers = {
                "apikey": api_key
            }
            # --------------------------------------------------------------------------------------------------------------
            """
            nolookup API Request
            """
            
            url = f"https://api.numlookupapi.com/v1/validate/{ph_number}?apikey={api_key}"
            resp = requests.get(url, headers=headers, data=data)
            result = resp.text
            y = result.split(":")
            carrier = y[9].split(" ")
            flag = False
            # --------------------------------------------------------------------------------------------------------------
            """
            Init. carrier variable cc
            """
            
            for _ in carrier:
                if carrier[:2][0][:2] == '""':
                    flag = True
                else:
                    flag = False
            # --------------------------------------------------------------------------------------------------------------
            # flag checker...
            
            if flag is True:
                cc = "None"
            else:
                cc = carrier[0][1::] + " " + carrier[1]
                
            # --------------------------------------------------------------------------------------------------------------
            """
            Indiexing & slicing and retrieving data
            """
            
            rr = y[8].split(",")
            local = rr[0][1:-1:] # local data
            line = y[10][1:-2:]  # Line type data
            
            # --------------------------------------------------------------------------------------------------------------
            # using parser check phone number
            """
            1. location --> Country
            2. country_code --> the intera=national code
            3. nat_no --> number as shown in the country
            """
            
            number_check = phonenumbers.parse(ph_number)
            location = geocoder.description_for_number(number_check, "en")
            country_code = str(number_check.country_code)
            nat_no = number_check.national_number
            
            # --------------------------------------------------------------------------------------------------------------
            """
            Google Geocoder API
            """
            
            google_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={local}+{location}&key={google_api_key}"
            google_req = requests.get(google_url)
            a = google_req.json()
            
            # Getting latitude & longitude by indexing and key-valu pairs
            
            lat = a['results'][0]['geometry']['location']['lat']
            lng = a['results'][0]['geometry']['location']['lng']
            
            # --------------------------------------------------------------------------------------------------------------
            # Configuration Changes 
            """
            To Enter the Details obtained from API Request
            """
            
            self.a.config(text=nat_no, font=(self.leel_font, 15, "bold"))
            self.b.config(text=cc, font=(self.leel_font, 15, "bold"))
            self.c.config(text=local, font=(self.leel_font, 15, "bold"))
            self.d.config(text=location, font=(self.leel_font, 15, "bold"))
            self.e.config(text="+"+country_code, font=(self.leel_font, 15, "bold"))
            self.f.config(text=line, font=(self.leel_font, 15, "bold"))
            self.g.config(text=lat, font=(self.leel_font, 15, "bold"))
            self.h.config(text=lng, font=(self.leel_font, 15, "bold"))
            
            # --------------------------------------------------------------------------------------------------------------
            marker_one = self.map_view.set_marker(lat, lng, text=nat_no)
            self.map_view.set_position(lat, lng)
            self.map_view.set_zoom(15)

        # =============================================================================================================
        # Images
        """
        Loading images and converting into tkinter supportive files
        
        1. Logo Image
        2. Logo Text Image
        3. Search Bar Image
        4. Search button
        """
        
        self.logo_img = Image.open("Untitled.png")
        self.logo_img = self.logo_img.resize((80, 80), Image.Resampling.LANCZOS)
        self.logo_img = ImageTk.PhotoImage(self.logo_img)
        # --------------------------------------------------------------------------------------------------------------
        self.lolo_im = Image.open("logotext.png")
        self.lolo_im = ImageTk.PhotoImage(self.lolo_im)
        # --------------------------------------------------------------------------------------------------------------
        self.search_bar_image = Image.open("search.png")
        self.search_bar_image = ImageTk.PhotoImage(self.search_bar_image)

        self.search_button_img = Image.open("search_icon.png")
        self.search_button_img = ImageTk.PhotoImage(self.search_button_img)
        # ==============================================================================================================
        # Labels
        """
        Creating Labels for Window
        
        1. self.logo_label --> Logo Label
        2. self.logo_text --> Logo Text Label
        3. self.Search Bar Label
        4. Search Text Label
        5. self.phone_number_label --> Phone number Text Label
        6. self.a --> Phone number Data Label
        7. self.carrier_label --> Service Provider Label
        8. self.b --> Service Provider Data Label
        9. self.location_label --> Location Label
        10. self.c --> Location Data Label
        11. self.region_label --> Region Label
        12. self.d --> Region Data Label
        13. self.country_code_label --> Country Code Label
        14. self.e --> Country Code Data Label
        15. self.line_type_label --> Line Type Label
        16. self.f --> Line Type Data Label
        17. self.latitude_label --> Latitude Label
        18. self.g --> Latitude Data Label
        19. self.longitude_label --> Longitude Label
        20. self.h --> Longitude Data Label
        """
        # --------------------------------------------------------------------------------------------------------------
        # Logo Label
        self.logo_label = Label(self.root, image=self.logo_img, bd=0, bg=self.dark_bg, fg=self.dark_bg)
        self.logo_label.place(x=10, y=10)
        
        # --------------------------------------------------------------------------------------------------------------
        # Logo Text
        self.logo_text = Label(self.root, image=self.lolo_im, bd=0, bg=self.dark_bg)
        self.logo_text.place(x=90, y=20)
        
        # --------------------------------------------------------------------------------------------------------------
        # Logo Search Bar
        self.search_bar = Label(self.root, image=self.search_bar_image, bd=0, bg=self.dark_bg, fg="#151819")
        self.search_bar.place(x=540, y=20)
        
        # --------------------------------------------------------------------------------------------------------------
        # Search Text
        Label(self.root, text="Search", fg="white", bd=0, bg="#151819", width=7,
              font=(self.leel_font, 17)).place(x=570, y=40)
        
        # --------------------------------------------------------------------------------------------------------------
        # Phone Number Label
        self.phone_number_label = Label(self.root, text="Phone Number", bd=0, bg=self.dark_bg,
                                        font=(self.leel_font, 15), fg="white")
        self.phone_number_label.place(x=40, y=150-20)

        self.a = Label(self.root, text="---", bd=0, bg=self.dark_bg, fg="white", font=(self.leel_font, 15))
        self.a.place(x=40, y=185-20)
        
        # --------------------------------------------------------------------------------------------------------------
        # Carrier Label
        self.carrier_label = Label(self.root, text="Carrier", bd=0, bg=self.dark_bg, fg="white",
                                   font=(self.leel_font, 15))
        self.carrier_label.place(x=40, y=250-20)

        self.b = Label(self.root, text="---", bd=0, bg=self.dark_bg, fg="white", font=(self.leel_font, 15))
        self.b.place(x=40, y=285-20)
        
        # --------------------------------------------------------------------------------------------------------------
        # Location Label
        self.location_label = Label(self.root, text="Location", bd=0, bg=self.dark_bg, fg="white",
                                    font=(self.leel_font, 15))
        self.location_label.place(x=40, y=350-20)

        self.c = Label(self.root, text="---", bd=0, bg=self.dark_bg, fg="white", font=(self.leel_font, 15))
        self.c.place(x=40, y=385-20)
        
        # --------------------------------------------------------------------------------------------------------------
        # Region Label
        self.region_label = Label(self.root, text="Region", bd=0, bg=self.dark_bg, fg="white",
                                  font=(self.leel_font, 15))
        self.region_label.place(x=40, y=450-20)

        self.d = Label(self.root, text="---", bd=0, bg=self.dark_bg, fg="white", font=(self.leel_font, 15))
        self.d.place(x=40, y=485-20)
        
        # --------------------------------------------------------------------------------------------------------------
        # Country Code Label
        self.country_code_label = Label(self.root, text="Country Code", bg=self.dark_bg, fg="white", bd=0,
                                        font=(self.leel_font, 15))
        self.country_code_label.place(x=40, y=550-20)

        self.e = Label(self.root, text="---", bd=0, bg=self.dark_bg, fg="white", font=(self.leel_font, 15))
        self.e.place(x=40, y=585-20)
        
        # --------------------------------------------------------------------------------------------------------------
        # Line Type Label
        self.line_type_label = Label(self.root, text="Line Type", bd=0, bg=self.dark_bg, fg="white",
                                     font=(self.leel_font, 15))
        self.line_type_label.place(x=40, y=650-20)

        self.f = Label(self.root, text="---", bd=0, bg=self.dark_bg, fg="white", font=(self.leel_font, 15))
        self.f.place(x=40, y=685-20)
        
        # --------------------------------------------------------------------------------------------------------------
        # Latitude Label
        self.latitude_label = Label(self.root, text="Lat:", bd=0, bg=self.dark_bg, fg="white",
                                    font=(self.leel_font, 15))
        self.latitude_label.place(x=270, y=150)

        self.g = Label(self.root, text="---", bd=0, bg=self.dark_bg, fg="white", font=(self.leel_font, 15))
        self.g.place(x=310, y=150)
        
        # --------------------------------------------------------------------------------------------------------------
        # Longitude Label
        self.longitude_label = Label(self.root, text="Long:", bd=0, bg=self.dark_bg, fg="white",
                                     font=(self.leel_font, 15))
        self.longitude_label.place(x=420, y=150)

        self.h = Label(self.root, text="---", bd=0, bg=self.dark_bg, fg="white", font=(self.leel_font, 15))
        self.h.place(x=480, y=150)
        
        # ==============================================================================================================
        # Buttons
        """
        Search button initialisation
        """
        
        self.search_button = Button(self.root, image=self.search_button_img, bd=0, bg="#151819", fg=self.dark_bg,
                                    command=phone_checker)
        self.search_button.place(x=920, y=30)
        
        # ==============================================================================================================
        # Text Field Entry
        """
        To Enter the phone number for searching
        """
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
