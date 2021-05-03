PyBer Analysis
Overview of SurfsUp Analysis
We intend on opening up a Surf 'n Scoop shop to provide locals and tourists with surf boards and icecream on a beach in Oahu. We've gained the attention of an investor, W. Avy, however we will need to provide statistics supporting the viability of our store year-round to W. Avy's board of directors in order to obtain funding.
Our initial round of analysis was carried ou on a set of weather data provided to use on a SQLite database. To access it, SQL Alchemy was used to perform queries. Our findings were then presented to the board of directors on a web application using Flask and Visual Studio Code.

The current analysis builds of our previous work to provide a side-by-side comparison of temperatures and precipitation levels for the months of June and December in Oahu.

Results
Analysis revealed three key differences between the weather in June and December:

The temperature is, on average, higher in June than in December
There is a greater variance in temperature in December than in June
June and December share similar maximium temperatures, but December reaches much lower minimum temperatures the June.
SurfsUp Analysis Summary
Temperature Comparison
Upon analysis, it is evident that temperature are typically higher in th month of June (M = 74.94) than that of December (M = 71.04). That being said, there is a greater variance in December (SD = 3.75) temperatures than those in June (SD = 3.25) and, while both June and December share similar maximium temperatures, December (min = 56, max = 83) reaches much lower minimum temperatures the June (min = 64, max = 85).
"/Output/June_temp_describe" is not created yet. Click to create.

"/Output/Dec_temp_describe" is not created yet. Click to create.
Visualizations of the spread of temperature data collected for each month shows that Decembers mimimum is one of a cluster of outliers slightly skewing (skew = 0.41) the mean temperature to the left (as shown below). This , alongside the similar mean temperatures, suggests that while December temperatures do dip lower than those of June, most days between months are not very dissimilar.
"/Output/June_temp_box" is not created yet. Click to create.

"/Output/Dec_temp_box" is not created yet. Click to create.
These results indicate that the level of temperature flucuation throughout the calender year is low and the odds of seasonal changes in temperature impacting the viability of keeping a weather-reliant shop open year-long is slim. However, other facets of the weather that may impact traffic to the business. One such factor is preciptiation.

Descriptive analytics alongside analysis of spread were performed to assess fluctuations in preciptitation between the month of June and December. Results showed a very small increase in precipitation in December with slightly greater variance however precipiation levels remain consistently low (June M = 0.14, SD = 0.34; December: M = 0.22, SD = 0.54).
Furthermore, analysis of spread revealed that both June (skew = 5.67) and December (skew = 4.96) precipitation data were skewed highly to the right (as shown below). This indicates that levels are typically low with a few days of high precipitation occuring across both months. Such findings are highly favourable for a shop aiming to serve surfers and tourists.

"/Output/June_prcp_box" is not created yet. Click to create.

"/Output/Dec_prcp_box" is not created yet. Click to create.
