# TTN BME280 Weather Station - Pycom LoPy4

This repository contains all the code and steps required to setup a BME280 with the Pycom LoPy4 on TTN Australia.

# Getting Started

This code is for a BME280 sensor attached to the LoPy4 via i2c. The code is set to send the temperature, humidity, and pressure values to The Things Network every 120 seconds. The TTN Application EUI, Application Key, Region, and time period can all be configured in main.py.

Download this repository and open the code file in your IDE, enter your TTN EUI, Key, and region and upload the project to your LoPy4. Your LoPy4 should flash red when starting, green when connected to TTN, and blue when sensing and uploading weather data to TTN.

# DIYODE Magazine Article

[Off-Grid LoRaWAN Weather Station](https://diyodemag.com/projects/long_range_report_off-grid_lorawan_weather_station)

# License

This project is licensed under the MIT License. This project contains code from [robert-hh/BME280](https://github.com/robert-hh/BME280) and [Core Electronics](https://core-electronics.com.au/tutorials/temperature-sensing-pycom-tmp36-tutorial.html).
