# Weather Forecast Telegram Bot 🌤️

This repository contains a Python script that fetches weather data from the Meteoblue API and sends a formatted weather forecast message to a Telegram chat. The forecast includes hourly data from 8:00 AM to 10:00 PM, highlighting key metrics like felt temperature, precipitation probability, and wind speed.

---

## Features 🚀

- **Weather Data Retrieval**: Fetches weather data for a specific location using the Meteoblue API.
- **Customizable Time Range**: Displays forecast data for specific hours (8 AM to 10 PM).
- **Telegram Integration**: Sends weather forecasts to a Telegram chat using the Telegram Bot API.
- **Dynamic Message Formatting**: Includes weather icons and formatted data for easy readability.
- **Environment Variables**: Securely manages sensitive credentials using a `.env` file.

---

## Project Structure 📂

```
.
|-- script.py             # Main script to fetch weather data and send Telegram messages
|-- .env                  # Environment variables for sensitive credentials
|-- README.md             # Documentation
```

---

## Prerequisites 🛠️

Make sure you have the following tools installed:

- Python 3.8+
- Required Python libraries: `requests`
- Meteoblue API key
- Telegram Bot API key

Install necessary Python libraries:

```bash
pip install requests
```

---

## Setup ⚙️

1. **Clone the Repository**

```bash
git clone https://github.com/MarcRibera/weather-telegram-bot.git
cd weather-telegram-bot
```

2. **Add Environment Variables**
   Create a `.env` file in the root directory to store your API keys and other settings. There is and .env.example file that you can use as a template.

```env
MBLUE_KEY=your_meteoblue_api_key
LAT=your_latitude
LON=your_longitude
BOT_API_KEY=your_telegram_bot_api_key
CHAT_ID=your_telegram_chat_id
```

3. **Run the Script**
   Execute the script using Python:

```bash
python3 main.py
```

---

## How It Works 🛠️

1. **Weather Data Fetching**:

   - The script uses the Meteoblue API to retrieve weather data for the specified latitude and longitude.
   - Filters hourly data for the range of 8:00 AM to 10:00 PM.

2. **Message Formatting**:

   - Formats the data into a readable Telegram message.
   - Includes weather icons based on precipitation probability.

3. **Telegram Message Sending**:
   - Sends the formatted message to the specified Telegram chat using the Telegram Bot API.

---

## Example Output 📧

Example Telegram message:

```
☀️ Weather for Tue, 28 Dec 2024 ☀️
Felt Temp | Prob Precip | Wind Speed:
08h:   15°   |   10 %   |   5 km/h
09h:   16°   |   20 %   |   6 km/h
...
22h:   12°   |   -   |   3 km/h
```

## IMPORTANT Notes 📝

- In order to create a Bot and get the **BOT_API_KEY** and **CHAT_ID**, you need to create a bot on Telegram and get it's API Key and Chat ID. Check the following link for more information:
  [Medium Article](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e)
- Ensure the `.env` file is secure and never push it to a public repository.
- Ensure the `.env` file is filled with `your API keys`.
- Modify the time range in the `get_data_from_8_to_22` function if needed.

---

Happy Coding! 🌟
