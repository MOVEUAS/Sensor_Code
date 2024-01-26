# Air Quality Sensor Repository

This repository contains code for different air quality sensors. Each directory represents a specific sensor model, and the code within each directory is tailored to that sensor.

## ALSPHASENSE

**Authors:** Kaleb Nails, Erik Liebergall, Marc Compere  
**Created:** 10/6/2023  
**Modified:** 13 Dec 2023

### Description

This directory contains code for the ALSPHASENSE air quality sensor. The main script, `pm25_SPS30_Senirion_Run.py`, interfaces with the sensor, reads data, and logs it to a CSV file.

### Instructions

1. Connect the ALSPHASENSE sensor to your system.
2. Run the `pm25_SPS30_Senirion_Run.py` script with the appropriate device name as a command-line argument (default is `/dev/ttyUSB0`).
   ```bash
   python3 pm25_SPS30_Senirion_Run.py /dev/ttyUSB0
   
The script will log air quality data to a CSV file with a timestamp.

# PMS plantower

**Authors:** Erik Liebergall, Leah Smith, Kaleb Nails, Marc Compere  
**Created:** 10 Feb 2023  
**Modified:** 11 Oct 2023

## Description

This directory contains code for the PMS plantower air quality sensor. The `pm25_simpletest.py` script interfaces with the sensor, reads data, and outputs air quality information to the console.

## Instructions

1. Connect the PMS plantower sensor to your system.
2. Run the `pm25_simpletest.py` script with the appropriate device name as a command-line argument (default is `/dev/ttyUSB0`).
   ```bash
   python3 pm25_simpletest.py /dev/ttyUSB0


  
