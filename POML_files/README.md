
Overview 

In this project I utilize Azure's Machine Learning Tools for the classification of a bank marketing dataset. In that dataset, there are several features (demographic, financial etc) about persons who acquired a specific service from the bank(s). Using the data, we would like to be able to predict situations in which persons would or would not acquire that service. 

A link to the screencast video on YouTube
https://youtu.be/5Wa9yKfQE2I

Architectural Diagram

![Architectural Diagram](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/POML_ML_Architecture.jpg)

Improving the Project in the Future

The project could certainly be improved with more indepth experimentation, including the use of additional parameters, different metrics and better datasets. For example, the accuracy metric was used, but is possibly affected by skewed datasets. The dataset's classes are severely skewed with close to 90% of the records being attributed to one class. There is the possibility the model 
could improve with better balance or a different metric. Also, while parameters were fed to the automl config, it may be useful to allow those to be fed to the pipeline later as arguments.

Screenshots required with a short description to demonstrate key steps. 

Times in some screenshots seem to differ by 6hrs in cases as I worked between my computer and the Lab VM. E.g. Img 37 which says 2:29am start, but it's really 8:29pm. Important to note. The uploaded Ipynb does not include the provided screenshots of the RunDetails widgets. I had to refresh as the notebook was not refreshing to reflect completion of the run in line with ML Studio. 

The registered dataset

![Registered Dataset](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_02.png)
![Exploring the Dataset](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_03.png)


The Experiment and Best Model

![The Completed Experiment](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_06.png)
![The Best Model](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_07.png)
![Model Explanation](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_09.png)

Deployed Model and Result from 2 Inputs

![Deployed Model](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_12.png)
![Consumed Model](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_13.png)

Enabling AppInsights

![Run Log and Enable AppInsights](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_14.png)
![Log Output](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_15.png)
![Log Output](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_16.png)
![App Insights Enabled](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_17.png)
![App Insights](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_18.png)

Swagger API Review

![Swagger Review of Model Endpoint's Swagger.Json](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_19.png)
![Swagger Input Payload](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_20.png)
![Swagger Input FieldTypes](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_21.png)
![Swagger Output](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_22.png)

Benchmark for 10 and 1000

![Benchmark start for 10](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_24.png)
![Benchmark end for 10](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_25.png)
![Benchmark start for 1000](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_23.png)

AppInsights Performance for Benchmarking

![AppInsights for Benchmarking](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_26.png)

Pipeline and Runs from SDK call and Rest

![Pipeline Run](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_31.png)
![Pipeline Done](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_34.png)
![Created Pipeline](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_38.png)

Publish and Run incl REST run

![Publish Pipeline](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_36.png)
![Run Published Pipeline](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_37.png)
![Pipeline Overview](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_40.png)
![Finished Pipeline Run](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_39.png)
Pipeline call via Rest API - screenshot subsequently done in Jupyter Labs

![Pipeline call via Rest API](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_42.png)

Dataset with AutoML
![Dataset with AutoML](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_41.png)

Pipeline Run via the SDK
![Pipeline Run from SDK](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_32.png)
![Pipeline Run from SDK](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_28.png)


