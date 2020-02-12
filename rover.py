import requests

from plotly.graph_objs import Scatter
from plotly import offline

from datetime import datetime as dt

class Rover:

    def __init__(self, name):

        """ Defines an instance of Rover, uses formatted string to obtain data about the
            specified rover.

            Note: Only acceptable value for the 'name' parameter are: Curiosity, Opportunity, and Spirit
        """
        self.name = name
        """ 
            Please note that there is a small request limit when using the default DEMO_KEY which will cause errors
            to arise once your request limit has been reached. To obtain your own API key for this program please 
            visit the link below and edit the self.api_key attribute accordingly.
            
            resource: https://api.nasa.gov/
        """
        self.api_key = "DEMO_KEY"
        rover_dict = self._load_json()

        # Assigns necessary values to attributes of the rover.
        self.landing_date = rover_dict['landing_date']
        self.launch_date = rover_dict['launch_date']
        self.status = rover_dict['status']
        self.max_date = rover_dict['max_date']
        self.max_sol = rover_dict['max_sol']
        self.total_photos = rover_dict['total_photos']

    def _load_json(self):

        """ Helper function to return the necessary JSON object """

        # A while-loop combined with a try-except block ensures a valid rover name is provided.
        while True:
            url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{self.name}/?' \
                  f'&api_key={self.api_key}'

            req = requests.get(url)

            # Assigns the JSON file starting at index 'rover'.
            try:
                return req.json()['rover']
            except KeyError:
                self.name = 'curiosity'
                print("error: Invalid rover name was provided, defaulting to 'curiosity'.")


    def describe_rover(self):

        """ Prints the information of the current instance to the console """

        print("\nROVER INFORMATION\n*********************************")
        print(f"Name: {self.name.title()}")
        print(f"Launch Date: {self.launch_date}")
        print(f"Landing Date: {self.landing_date}")
        print(f"Status: {self.status.title()}")
        print(f"Max Date: {self.max_date}")
        print(f"Max Sol: {self.max_sol}")
        print(f"Total Photos Captured: {self.total_photos}")
        print("*********************************")

    def search_photo(self, date):

        """ This method will search for and return hyperlinks for all the images taken by the rover,
        specified by the date argument that the user passes. """

        # Modifying current instance's max_date format to match user-input date format.
        temp = self.max_date.split('-')
        modified_max = f"{temp[1]}/{temp[2]}/{temp[0]}"
        rover_date = dt.strptime(modified_max, "%m/%d/%Y")

        try:
            input_date = dt.strptime(date, "%m/%d/%Y")
        except ValueError:
            print("error: Invalid date was entered!")
        else:
            if input_date > rover_date:
                print(f"error: Date can't surpass {modified_max} for this rover, please try a lower date.")
            else:
                temp = date.split("/")
                url_date_string = f"{temp[2]}-{temp[0]}-{temp[1]}"  # Modify user input for date to work in URL.
                url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{self.name}" \
                      f"/photos?earth_date={url_date_string}&api_key={self.api_key}"

                req = requests.get(url)

                try:
                    if len(req.json()['photos']) == 0:
                        print("error: No photo data available for that date.")
                    else:
                        print("\nData Retrieved:\n")
                        for photo in req.json()['photos']:
                            print(photo['img_src'])
                except KeyError:
                    print("error: No photo data available for that date.")


    def photo_analysis(self):

        """ This method will graph the number of photos captured for each Sol of the current
        rover instance that is called """

        url = f"https://api.nasa.gov/mars-photos/api/v1/manifests/{self.name}/" \
              f"?&api_key={self.api_key}"

        req = requests.get(url)
        # Creates a variable that points to the 'photos' dictionary of the JSON file.
        photo_dict = req.json()['photo_manifest']['photos']

        # Empty lists created to store data.
        labels, sols, photos = [], [], []

        for photo in photo_dict:
            sols.append(photo['sol'])
            photos.append(photo['total_photos'])

            label = f"Sol: {photo['sol']}<br />Photos Captured: {photo['total_photos']}"
            labels.append(label)

        # Holds data for the graph and assigns a color format to the plotted data.
        data = [{
            'type': 'scatter',
            'x': sols,
            'y': photos,
            'hovertext': labels,
            'marker': {
                'color': 'rgb(147, 72, 56)',
                'line': {'width': 1.5, 'color': 'rgb(20, 20, 20)'},
            },
            'opacity': 0.8,
        }]

        # Adjusts elements of each axis and displays document title.
        layout = {
            'title': f"Photos Per Sol (Day on Mars) taken by: {self.name.title()} Rover",
            'titlefont': {'size': 20},
            'xaxis': {
                'title': 'Sol',
                'titlefont': {'size': 25},
                'tickfont': {'size': 15},
            },
            'yaxis': {
                'title': 'Photos',
                'titlefont': {'size': 25},
                'tickfont': {'size': 15},
            },

        }

        figure = {'data': data, 'layout': layout}
        filename = f'{self.name}_photo_data.html'
        offline.plot(figure, filename=filename)
        print(f"\nData successfully saved as: {filename}")
