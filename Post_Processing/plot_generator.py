# Author: Kaleb Nails
#This is a simple plotter to plot you data, note that is does down sample down to 20 minute intervals.

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data into DataFrames
df1 = pd.read_csv('2024_03_21__14_25_57_Alphasense_OPC-N3-177380512.csv')
df1 = df1[[' Dates (YMD)', 'PM2.5 ug/m3']]
df1[' Dates (YMD)'] = pd.to_datetime(df1[' Dates (YMD)'])
df1['PM2.5 ug/m3'] = pd.to_numeric(df1['PM2.5 ug/m3'], errors='coerce')
df1.set_index(' Dates (YMD)', inplace=True)
df1_resampled = df1.resample('20min').mean().reset_index()


df3 = pd.read_csv('2024_03_21__14_25_57_Alphasense_OPC-N3-177380511.csv')
df3 = df3[[' Dates (YMD)', 'PM2.5 ug/m3']]
df3[' Dates (YMD)'] = pd.to_datetime(df3[' Dates (YMD)'])
df3['PM2.5 ug/m3'] = pd.to_numeric(df3['PM2.5 ug/m3'], errors='coerce')
df3.set_index(' Dates (YMD)', inplace=True)
df3_resampled = df3.resample('20min').mean().reset_index()


df2 = pd.read_csv('2024_03_21__10_34_46_vaisala_aqt420.csv', header=None, skipinitialspace=True)
df2 = df2[[0, 12]]  # Date is in the first column, PM10 is in the 11th column
print(df2)
df2.columns = [' Dates (YMD)', 'PM2.5 ug/m3']
df2[' Dates (YMD)'] = pd.to_datetime(df2[' Dates (YMD)'])

###########################################################################
df4 = pd.read_csv('2024_03_21__14_48_19_pm25_simplest_plantower_pt1_CSV.csv')
print(df4.keys())
df4 = df4[[' Dates (YMD)', ' pm2.5 standard ug/m3']]
print(df4)
df4[' Dates (YMD)'] = pd.to_datetime(df4[' Dates (YMD)'])
df4[' pm2.5 standard ug/m3'] = pd.to_numeric(df4[' pm2.5 standard ug/m3'], errors='coerce')
df4.set_index(' Dates (YMD)', inplace=True)
df4_resampled = df4.resample('20min').mean().reset_index()

df5 = pd.read_csv('2024_03_21__14_48_19_pm25_simplest_plantower_pt2_CSV.csv')
df5 = df5[[' Dates (YMD)', ' pm2.5 standard ug/m3']]
df5[' Dates (YMD)'] = pd.to_datetime(df5[' Dates (YMD)'])
df5[' pm2.5 standard ug/m3'] = pd.to_numeric(df5[' pm2.5 standard ug/m3'], errors='coerce')
df5.set_index(' Dates (YMD)', inplace=True)
df5_resampled = df5.resample('20min').mean().reset_index()

df6 = pd.read_csv('2024_03_21__14_48_19_pm25_simplest_plantower_pt3_CSV.csv')
df6 = df6[[' Dates (YMD)', ' pm2.5 standard ug/m3']]
df6[' Dates (YMD)'] = pd.to_datetime(df6[' Dates (YMD)'])
df6[' pm2.5 standard ug/m3'] = pd.to_numeric(df6[' pm2.5 standard ug/m3'], errors='coerce')
df6.set_index(' Dates (YMD)', inplace=True)
df6_resampled = df6.resample('20min').mean().reset_index()

df7 = pd.read_csv('2024_03_21__14_48_19_pm25_simplest_plantower_pt4_CSV.csv')
df7 = df7[[' Dates (YMD)', ' pm2.5 standard ug/m3']]
df7[' Dates (YMD)'] = pd.to_datetime(df7[' Dates (YMD)'])
df7[' pm2.5 standard ug/m3'] = pd.to_numeric(df7[' pm2.5 standard ug/m3'], errors='coerce')
df7.set_index(' Dates (YMD)', inplace=True)
df7_resampled = df7.resample('20min').mean().reset_index()

###############################################
df8 = pd.read_csv('2024_03_21__14_17_18_Sensirion_sps30_533D09A32681430C.csv')
df8 = df8[[' Dates (YMD)', 'Mass Concentration PM2.5 (µg/m³)']]
df8[' Dates (YMD)'] = pd.to_datetime(df8[' Dates (YMD)'])
df8['Mass Concentration PM2.5 (µg/m³)'] = pd.to_numeric(df8['Mass Concentration PM2.5 (µg/m³)'], errors='coerce')
df8.set_index(' Dates (YMD)', inplace=True)
df8_resampled = df8.resample('20min').mean().reset_index()

df9 = pd.read_csv('2024_03_21__14_04_09_Sensirion_sps30_674C8CAB9A3123F6.csv')
df9 = df9[[' Dates (YMD)', 'Mass Concentration PM2.5 (µg/m³)']]
df9[' Dates (YMD)'] = pd.to_datetime(df9[' Dates (YMD)'])
df9['Mass Concentration PM2.5 (µg/m³)'] = pd.to_numeric(df9['Mass Concentration PM2.5 (µg/m³)'], errors='coerce')
df9.set_index(' Dates (YMD)', inplace=True)
df9_resampled = df9.resample('20min').mean().reset_index()



# Plot the data
plt.figure(figsize=(10, 6))

plt.plot(df2[' Dates (YMD)'], df2['PM2.5 ug/m3'],
         marker='x', linestyle='-.', label='Vaisala', markersize=.5, linewidth=4)

plt.plot(df3_resampled[' Dates (YMD)'], df3_resampled['PM2.5 ug/m3'],
         marker='o', linestyle='-', label='Alphasense 2', markersize=.5, linewidth=4)

plt.plot(df1_resampled[' Dates (YMD)'], df1_resampled['PM2.5 ug/m3'],
         marker='o', linestyle='-', label='Alphasense 1', markersize=.5, linewidth=4)

plt.plot(df4_resampled[' Dates (YMD)'], df4_resampled[' pm2.5 standard ug/m3'],
         marker='*', linestyle='--', label='Plantower 1', markersize=.5, linewidth=4)

plt.plot(df5_resampled[' Dates (YMD)'], df5_resampled[' pm2.5 standard ug/m3'],
         marker='*', linestyle='--', label='Plantower 2', markersize=.5, linewidth=4)

plt.plot(df6_resampled[' Dates (YMD)'], df6_resampled[' pm2.5 standard ug/m3'],
         marker='*', linestyle='--', label='Plantower 3', markersize=.5, linewidth=4)

plt.plot(df7_resampled[' Dates (YMD)'], df7_resampled[' pm2.5 standard ug/m3'],
         marker='*', linestyle='--', label='Plantower 4', markersize=.5, linewidth=4)

plt.plot(df8_resampled[' Dates (YMD)'], df8_resampled['Mass Concentration PM2.5 (µg/m³)'],
         marker='*', linestyle=':', label='Sensirion 1', markersize=.5, linewidth=4)

plt.plot(df9_resampled[' Dates (YMD)'], df9_resampled['Mass Concentration PM2.5 (µg/m³)'],
         marker='*', linestyle=':', label='Sensirion 2', markersize=.5, linewidth=4)

plt.xlabel('Time (MM-DD HH)',fontsize=20)
plt.ylabel('PM2.5 ug/m3',fontsize=20)
plt.grid(True)
plt.xticks(rotation=45,fontsize=18)
plt.yticks(fontsize=18)
plt.legend(fontsize=18)
plt.tight_layout()
plt.show()
