This python script provides a helpful way to decide whether to get to my uni by bike or by moped/car.
Given a starting and an ending location, they get geocoded via google maps geocode api to coordinates and the angle (bearing) between the two is calculated. It then gets the weather through openweathermap apis, and if it rains and there's wind blowing in from a range of +/- 36 deg of the bearing, it suggests you to not go by bike. I made this because countless times i've worn waterproof clothing and still got wet because the wind blew the rain straight into my face.

Now, of course the straighter the path is from starting to ending location, the better it is, since i make my calculations based only on the starting and ending coordinates. if from A to B you take a very uneven route, you might face some parts of the path with wind, some parts without... it's not hard to imagine such a situation in which this program wouldn't be useful.
I also suggest using it only for paths of small length.

you MUST provide your own api keys for google cloud platform and openweathermap for the program to work

