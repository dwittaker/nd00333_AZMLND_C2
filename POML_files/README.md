# Overview

In this project I utilize Azure's Machine Learning Tools for the classification of a bank marketing dataset. In that dataset, there are several features (demographic, financial etc) about persons who acquired a specific service from the bank(s). Using the data, we would like to be able to predict situations in which persons would or would not acquire that service.

# Screencast
The screencast video can be viewed on YouTube by clicking the image below.

[![here](https://img.youtube.com/vi/5Wa9yKfQE2I/mqdefault.jpg)](https://youtu.be/5Wa9yKfQE2I)

# Architectural Diagram
This diagram outlines the major components in the MLOPS pipeline, inclusive of Azure ML Studio based tools and (Python) Notebook based tools.

![Architectural Diagram](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/POML_ML_Architecture.jpg)

# Improving the Project in the Future
The project could certainly be improved with more indepth experimentation, including the use of different metrics, additional parameters and better datasets. The following were noted:

- While hard-coded parameters were fed to the automl config, it may be useful to allow those to be fed to the pipeline later as arguments.
- The dataset's classes are severely skewed with close to 90% of the records being attributed to one class. 
- The accuracy metric was used which can be affected by skewed datasets, as per the accuracy paradox. [Read more here](https://machinelearningmastery.com/failure-of-accuracy-for-imbalanced-class-distributions/). 

There is the possibility the model could improve with better balance or a different metric. 


---

# Screenshots

Note: Times in some screenshots seem to differ by 6hrs in cases as I worked between my computer and the Lab VM. E.g. Img 37 says 2:29am start, but it's really 8:29pm. 

Note: The uploaded Ipynb does not include the provided screenshots of the RunDetails widgets. I had to refresh as the notebook was not refreshing to reflect completion of the run in line with ML Studio. 

### The registered dataset
The bankmarketing training dataset was retrieved from the provided repository. It was then uploaded using the ML Studio interface.

![Registered Dataset](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_02.png)

The data was also explored using the ML Studio interface to attain a better understanding of the features in the data. 

![Exploring the Dataset](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_03.png)

### The Experiment and Best Model
A new classification experiment was created using the bankmarketing training data, where the intention was to classify those types of persons (_or situations_) that would be likely to take out a certain type of service (specified in column Y). Deep Learning Models was not enabled. The experiment was set to complete training in 1hr.

![The new experiment](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_05.png)

For the experiment, a new compute cluster was created. It was set to 6 nodes maximum and 1 node minimum. It was set to approximately 120 seconds idle time to prevent unnecessary spend.

![The newly configured cluster being resized](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_04.png)

Once submitted, the experiment was monitored by way of its various child runs (and their child runs), their logs, the cluster node activities and the experiment statistics. 

It completed successfully with a VotingEnsemble as the best model with accuracy of 91.8%.

![The Completed Experiment](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_06.png)

For the purpose of understanding the model, the ensemble details were reviewed. The ensemble was made up of multiple XGBoost Classifiers with different weightings.
![The Best Model](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_07.png)

It was however noted that the second best model was indeed a single XGBoost classifier.
![The 2 best models](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_08.png)

To try to get a better appreciation for the featureset, the model's explanation was also briefly reviewed. The image below shows the 4 features that were deemed most important by the model in performing the classifications at 91% accuracy.
For future work, this could also be used for the purpose of dimensionality reduction, saving on compute time and possibly improving accuracy.
![Model Explanation](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_09.png)


### Deployed Model and Result from 2 Inputs

To put the model into production, it was deployed from the ML Studio interface. A form was filled out, denoting a name, compute type and the use of authentication.

![Deployment Form](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_11.png)

Once submitted, the deployment was monitored from the model's endpoing section, watching the deployment state for a 'healthy' indication.

![Deployed Model](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_12.png)

The json payload in the endpoint file was modified with sample values to enable 2 tests.

Once healthy, the model was tested using the endpoint.py file. It could also have been tested using the code provided on the model's 'consume' page. 

The script provided a json response with the result for the 2 tests.

![Consumed Model](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_13.png)


### Enabling AppInsights

Once a model is deployed to an endpoint, we need to ensure that endpoint is working appropriately. 

The most basic method is to view the associated log files. Having installed the workspace config file (that contains the environment information) and specified the endpoint's name, the provided script allows us to print those logs line by line.

A line is also added to enable appinsights, a more advanced method of monitoring the endpoint's activities.

![Run Log and Enable AppInsights](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_14.png)

This shows the output of the logs, once we have logged in separately via browser.

![Log Output](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_15.png)

This screenshot shows the logs for a few calls that were made to the endpoint, which is a web service.

![Log Output 2](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_16.png)

Having enabled appinsights in the logs.py file, the appinsights 'space' is setup and now reflected on the endpoint's page.

![App Insights Enabled](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_17.png)

By clicking the url on the page, we are redirected to the application insights section for the endpoint. It provides a whole host of useful information and tools, including alerts, failures and performance statistics in close to realtime.

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


