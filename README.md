# mars_rovers
A menu-driven console application that will allow the user to obtain rover information through NASA's [Mars Rover Photos](https://api.nasa.gov/) API.

----
## Dependencies
To get started, you're going to have to make sure you have python 3.x with pip installed on your system along with the following:

    $ python -m pip install --user plotly
    $ python -m pip install --user requests

I recommend obtaining your own API key [here](https://api.nasa.gov/) and inserting the value into the api_key attribute of the Rover class if you plan on making a large amount of requests through the application.

example:

    #  ...&api_key=your_api_key
    self.api_key = your_api_key



## Log
v1.0

* (Photo Analysis) menu item is added, allowing the user to retrieve a data visualization through the plotly module. The visualization shows the number of photos taken for each sol (Mars day).

* (Search Captured Photos) menu item is added, allowing the user to obtain hyperlinks of images captured by the rover on an earth day provided by the user

* (View Stats) menu item is added, allowing user to obtain a brief overview of data regarding the selected rover

* Menu is stable, ability to handle invalid user input and prevent program from crashing
