# Sensor Data Post-Processing

## Overview

This Python script is designed for post-processing sensor data files. It reads CSV files containing sensor data, organizes the data by sensor type, combines the data, and saves the combined data into new CSV files. The script is configured to work with Sensirion, Plantower, and Alphasense sensor data.
This is robust, but if sensor heading are changed from the sensors it will not work.

Note the sensors automatically make their csv in the directories directly above /sensor_Code, to run post processing move them into Sensor_Code


### 📝 File Structure Before post processing after collecting data, after moving the relevant CSV's into Sensor_Code.

```text
📦Sensor_Code
 ┣ 📂Alphasense                        
 ┃ ┣ 📄OPC_Simple_v2.py
 ┃ ┣ 📄README.md
 ┃ ┗ 📄start_Alphasense_loggers.sh
 ┣ 📂PMS plantower
 ┃ ┣ 📄.gitkeep
 ┃ ┣ 📄README.md
 ┃ ┣ 📄 pm25_simpletest.py
 ┃ ┗ 📄start_Plantower_loggers.sh
 ┣ 📂Post_Processing
 ┃ ┣ 📄Post_Processing.py
 ┃ ┗ 📄README.md
 ┣ 📂Sensirion
 ┃ ┣ 📄.gitkeep
 ┃ ┣ 📄 README.md
 ┃ ┣ 📄SPS30_Senirion_run.py
 ┃ ┣ 📄exampleReadSPS30.py
 ┃ ┣ 📄sps30.py
 ┃ ┣ 📄start_Sensirion_loggers.sh
 ┃ ┗ 📄stop_Sensirion_loggers.sh
 ┣ 📂Viasala
 ┃ ┗ 📄.gitkeep
 ┣ 📄Alphasense_Start_Script.sh
 ┣ 📄Sensor_Start_Script.sh
 ┣ 📄gui_popup.py
 ┣ 📄requirements.txt
 ┣ 📄YYYY_MM_DD_##_##_##_Sensirion_sps30_{serial code}.csv
 ┣ 📄YYYY_MM_DD_##_##_##_pm25_simplest_plantower_pt#_CSV.csv
 ┣ 📄YYYY_MM_DD_##_##_##_Alphasense_OPC-N3-{serial code}.csv
 ┗ 📄README.md
```

### File structure after post processing, it should look like this, and new files should appear in Post_Processing. Once you are done delete the CSV's in Sensor_Code after you backed them up.

```text
📦Sensor_Code
 ┣ 📂Alphasense                         
 ┃ ┣ 📄OPC_Simple_v2.py
 ┃ ┣ 📄README.md
 ┃ ┗ 📄start_Alphasense_loggers.sh
 ┣ 📂PMS plantower
 ┃ ┣ 📄.gitkeep
 ┃ ┣ 📄README.md
 ┃ ┣ 📄 pm25_simpletest.py
 ┃ ┗ 📄start_Plantower_loggers.sh
 ┣ 📂Post_Processing
 ┃ ┣ 📄Post_Processing.py
 ┃ ┣ 📄YYYY_MM_DD_Sensirion.csv
 ┃ ┣ 📄YYYY_MM_DD_plantower.csv
 ┃ ┣ 📄YYYY_MM_DD_Alphasense.csv
 ┃ ┣ 📄Post_Processing.py
 ┃ ┗ 📄README.md
 ┣ 📂Sensirion
 ┃ ┣ 📄.gitkeep
 ┃ ┣ 📄 README.md
 ┃ ┣ 📄SPS30_Senirion_run.py
 ┃ ┣ 📄exampleReadSPS30.py
 ┃ ┣ 📄sps30.py
 ┃ ┣ 📄start_Sensirion_loggers.sh
 ┃ ┗ 📄stop_Sensirion_loggers.sh
 ┣ 📂Viasala
 ┃ ┗ 📄.gitkeep
 ┣ 📄Alphasense_Start_Script.sh
 ┣ 📄Sensor_Start_Script.sh
 ┣ 📄gui_popup.py
 ┣ 📄requirements.txt
 ┣ 📄sensor_UART_configs.json
 ┣ 📄YYYY_MM_DD_##_##_##_Sensirion_sps30_{serial code}.csv
 ┣ 📄YYYY_MM_DD_##_##_##_pm25_simplest_plantower_pt#_CSV.csv
 ┣ 📄YYYY_MM_DD_##_##_##_Alphasense_OPC-N3-{serial code}.csv
 ┗ 📄README.md
```





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
cd ~/Sensor_Code/Post_Processing
python post_processing.py 
```
## Dependencies

- pandas
- os
- datetime

---
# plot_generator.py
This is an independent program from what is mentioned above. This uses current file formating as of 2024 to create graphs for a specific amount of sensors listed in the hardcoded program. This should help quick data generation. It is important to note it downsamples down to 20 minutes, so don't use it on very short data sets. Below is a sample image of the type of graph it will generate given the correct inputs.
![image](https://github.com/MOVEUAS/Sensor_Code/assets/117048000/8cd80975-528e-47b7-bceb-4e5dbd0442fd)

