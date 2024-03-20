# Sensor Data Post-Processing

## Overview

This Python script is designed for post-processing sensor data files. It reads CSV files containing sensor data, organizes the data by sensor type, combines the data, and saves the combined data into new CSV files. The script is configured to work with Sensirion, Plantower, and Alphasense sensor data.
This is robust, but if sensor heading are changed from the sensors it will not work.
## Features

- **Sensor Data Organization:** The script organizes sensor data by sensor type and combines it into a single DataFrame.
- **Column Interleaving:** Columns from each sensor are interleaved in the output DataFrame.
- **CSV Output:** The combined and cleaned sensor data is saved as a CSV file with a timestamp in the filename.
- **Variable Column Omision:** If you are missing a column or you have one you dont need, there is a
  ```bash
  .drop(columns=['...'])
  ```

 for each sensor. If you add something inside these brackets they will be removed from the final product.

## Usage

1. **Prepare Data Files:** Place the sensor data CSV files in the same directory as the script.
2. **Run the Script:** Execute the script, and it will process the data files and save the combined data in CSV format.

## Dependencies

- pandas
- os
- datetime

## Usage Example

```bash
python post_processing.py 
```
## Dependencies

- pandas
- os
- datetime

---
