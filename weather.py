from flask import Flask, render_template, request

# import json to load JSON data to a python dictionary
import json

# urllib.request to make a request to api
import urllib.request

# for converting sunrise and sunset times
from datetime import datetime


def currentWeather(city):
	# API key
	api = '2c90ea371cc5b1fa55fbfdb455130fcb'

	# source contain json data from api
	source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID='+api+'&units=metric').read()

	f = open("currentweatherdata.json", "wb")
	f.write(source)
	f.close()

	# converting JSON data to a dictionary
	list_of_data = json.loads(source)

	# data for variable list_of_data
	data = {
		"country_code": str(list_of_data['sys']['country']),
		"temp_c": str(round((list_of_data['main']['temp']), 1)),
		"temp_k": str(list_of_data['main']['temp']),
		"weather": str(list_of_data['weather'][0]['description']),
		"windspeed": str(round(((list_of_data['wind']['speed'])*2.237), 1)),
		"sunrise": str(list_of_data['sys']['sunrise']),
		"sunset": str(list_of_data['sys']['sunset']),
		"pressure": str(list_of_data['main']['pressure']),
		"humidity": str(list_of_data['main']['humidity']),
		"city": str(list_of_data['name']),
		"coordinates": str(list_of_data['coord']),
		"icon_filename": "static/icons/notfound.svg",
		"weather_icon":"static/weather_icons/01.png"
	}

	data['weather'] = data['weather'].title()

	# if we have an icon for chosen city, add the filename
	cityIcons = ['london', 'moscow', 'new york', 'paris', 'rome', 'tokyo']
	if data["city"].lower() in cityIcons:
		data["icon_filename"] = "static/icons/" + data["city"].lower() + ".svg"

	# get the weather icon code
	icon_code = str(list_of_data['weather'][0]['icon'])
	icon_code = icon_code[0:2]
	icon_code = "static/weather_icons/" + icon_code + ".png"
	data["weather_icon"] = icon_code

	# convert the sunrise and sunset data into a useful time format
	rise = int(data['sunrise'])
	rise = datetime.fromtimestamp(rise, tz=None).strftime("%Y-%m-%d%H:%M:%S")
	rise = rise[-8:-3]
	data['sunrise'] = rise

	set = int(data['sunset'])
	set = datetime.fromtimestamp(set, tz=None).strftime("%Y-%m-%d%H:%M:%S")
	set = set[-8:-3]
	data['sunset'] = set

	return data

def today(city):
	# API key
	api = '2c90ea371cc5b1fa55fbfdb455130fcb'

	# source contain json data from api
	source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+city+'&cnt=9&units=metric&appid='+api).read()

	f = open("forecastdata.json", "wb")
	f.write(source)
	f.close()

	# converting JSON data to a dictionary
	list_of_data = json.loads(source)

	todayData = {
		'time0_time': (list_of_data['list'][0]['dt']),
		'time0_temp': str(round(list_of_data['list'][0]['main']['temp'], 1)),
		'time0_wind': str(round(list_of_data['list'][0]['wind']['speed'], 1)),

		'time1_time': (list_of_data['list'][1]['dt']),
		'time1_temp': str(round(list_of_data['list'][1]['main']['temp'], 1)),
		'time1_wind': str(round(list_of_data['list'][1]['wind']['speed'], 1)),

		'time2_time': (list_of_data['list'][2]['dt']),
		'time2_temp': str(round(list_of_data['list'][2]['main']['temp'], 1)),
		'time2_wind': str(round(list_of_data['list'][2]['wind']['speed'], 1)),

		'time3_time': (list_of_data['list'][3]['dt']),
		'time3_temp': str(round(list_of_data['list'][3]['main']['temp'], 1)),
		'time3_wind': str(round(list_of_data['list'][3]['wind']['speed'], 1)),

		'time4_time': (list_of_data['list'][4]['dt']),
		'time4_temp': str(round(list_of_data['list'][4]['main']['temp'], 1)),
		'time4_wind': str(round(list_of_data['list'][4]['wind']['speed'], 1)),

		'time5_time': (list_of_data['list'][5]['dt']),
		'time5_temp': str(round(list_of_data['list'][5]['main']['temp'], 1)),
		'time5_wind': str(round(list_of_data['list'][5]['wind']['speed'], 1)),

		'time6_time': (list_of_data['list'][6]['dt']),
		'time6_temp': str(round(list_of_data['list'][6]['main']['temp'], 1)),
		'time6_wind': str(round(list_of_data['list'][6]['wind']['speed'], 1)),

		'time7_time': (list_of_data['list'][7]['dt']),
		'time7_temp': str(round(list_of_data['list'][7]['main']['temp'], 1)),
		'time7_wind': str(round(list_of_data['list'][7]['wind']['speed'], 1)),

		'time8_time': (list_of_data['list'][8]['dt']),
		'time8_temp': str(round(list_of_data['list'][8]['main']['temp'], 1)),
		'time8_wind': str(round(list_of_data['list'][8]['wind']['speed'], 1)),
	}

	for i in range(9):
		i = str(i)
		todayData['time'+i+'_time'] = datetime.fromtimestamp(todayData['time'+i+'_time'], tz=None).strftime("%H:%M")

	labels = [
		todayData["time0_time"],
		todayData["time1_time"],
		todayData["time2_time"],
		todayData["time3_time"],
		todayData["time4_time"],
		todayData["time5_time"],
		todayData["time6_time"],
		todayData["time7_time"],
		todayData["time8_time"]
	]

	tempdata = [
		todayData["time0_temp"],
		todayData["time1_temp"],
		todayData["time2_temp"],
		todayData["time3_temp"],
		todayData["time4_temp"],
		todayData["time5_temp"],
		todayData["time6_temp"],
		todayData["time7_temp"],
		todayData["time8_temp"]
	]

	winddata = [
		todayData["time0_wind"],
		todayData["time1_wind"],
		todayData["time2_wind"],
		todayData["time3_wind"],
		todayData["time4_wind"],
		todayData["time5_wind"],
		todayData["time6_wind"],
		todayData["time7_wind"],
		todayData["time8_wind"]
	]

	return(todayData, labels, tempdata, winddata)

def photo(city):
	api_key = 'i49SEJCaR_aWTUzLW0hSNvnF9mH7S-KUx1xi8n3daro'

	source = urllib.request.urlopen('https://api.unsplash.com/search/photos?query=' + city +'&per_page=1&client_id=' + api_key).read()

	# converting JSON response data to a dictionary
	response = json.loads(source)
	url = str(response['results'][0]['urls']['regular'])
	return url


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods =['POST', 'GET'])
def weather():
	if request.method == 'POST':
		city = request.form['city']
		country = request.form['country']
	else:
		# default city
		city = 'london'
		country = 'GB'
	
	# replace spaces in the city with +
	city = city.replace(' ', '+')

	# Get a photo of city before adding on country
	photodata = {
		'url': photo(city),
	}

	# remove blank spaces from country, then check whether it's empty or not
	country = country.strip()
	if not country:
		pass
	else:
		# if not empty, add country onto city
		city = city + ',' + country


	# get the current weather data from the api
	data = currentWeather(city)

	# save the multiple returned values into different variables
	todayData, labels, tempdata, winddata = today(city)

	
	# return website and data files
	return render_template('index2.html', data=data, todayData=todayData, labels=labels, tempdata=tempdata, winddata=winddata, photodata=photodata)



if __name__ == '__main__':
	app.run(debug = True)
