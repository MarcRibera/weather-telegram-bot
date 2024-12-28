import requests
from datetime import datetime

def load_env_vars():
    env_vars = {}
    with open('.env','r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                key,value = line.split('=')
                env_vars[key] = value
    return env_vars

env_vars = load_env_vars()

MBLUE_URL = "https://my.meteoblue.com/packages/basic-1h_basic-day"
MBLUE_api_key = env_vars['MBLUE_KEY']
LAT = env_vars['LAT']
LON = env_vars['LON']
BOT_API_KEY = env_vars['BOT_API_KEY']
CHAT_ID = env_vars['CHAT_ID']

def get_forecast():
    payload = {
        "lat":LAT,
        "lon":LON,
        "apikey":MBLUE_api_key,
        "format":"json",
        "tz":"Europe%2Fmadrid",
        "forecast_days": "1",
        "windspeed":"kmh",
        "temperature":"C",
    }
    request = requests.get(url=MBLUE_URL, params=payload)
    request.raise_for_status()
    return request.json()

def get_data_from_8_to_22(jsonData):
    today_data = {
    "date": "",
    "felt_temp": [],#felttemparature
    "prec_prob": [], #precipitation_probability
    "wind_speed": [], #windspeed
}
    date_string = jsonData["data_day"]["time"][0]
    date_object = datetime.strptime(date_string, '%Y-%m-%d').date()
    today_data["date"] = date_object.strftime("%a, %d %b %Y")
    today_data['felt_temp'] = jsonData["data_1h"]["felttemperature"][8:23]
    today_data['prec_prob'] = jsonData["data_1h"]["precipitation_probability"][8:23]
    today_data['wind_speed'] = jsonData["data_1h"]["windspeed"][8:23]

    return today_data

def parse_message(data):
    weather_icon = "\u2600"
    for i in data['prec_prob']:
        if i > 65: 
            weather_icon = "\u2614"
        elif i > 30:
            weather_icon = "\u2601"

    message = "<blockquote> {} Weather for <b>{} {}</b></blockquote>".format(weather_icon, data["date"], weather_icon)
    message += "Felt Temp | Prob Precip | Wind Speed: \n"

    hour = 8
    for i in range(len(data['felt_temp'])):
        message += "{}h:   {}°   |   {} %   |   {} km/h {} \n".format(
            "<i>" + str(hour).zfill(2) + "</i>", # hour
            str(round(data['felt_temp'][i])).zfill(2), # temp
           "-" if data['prec_prob'][i] == 0 else str(round(data['prec_prob'][i])).zfill(2), # preci
            round(data['wind_speed'][i]), # wind
            "\n" if hour == 12 or hour == 17 else "",
        )
        hour += 1

    return message


forescast_data = get_forecast()
today_data = get_data_from_8_to_22(forescast_data)
message = parse_message(today_data)

send_message_url = f"https://api.telegram.org/bot{BOT_API_KEY}/sendMessage?parse_mode=HTML&chat_id={CHAT_ID}&text={message}"
requests.get(send_message_url)

