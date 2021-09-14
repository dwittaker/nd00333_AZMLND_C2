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

---

### The Experiment and Best Model
A new classification experiment was created using the bankmarketing training data, where the intention was to classify those types of persons (_or situations_) that would be likely to take out a certain type of service (specified in *column Y*). Deep Learning Models was *not* enabled. The experiment was set to complete training in *1hr*.

![The new experiment](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_05.png)

For the experiment, a new compute cluster was created. It was set to *6 nodes maximum and 1 node minimum*. It was set to approximately *120* seconds idle time to prevent unnecessary spend.

![The newly configured cluster being resized](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_04.png)

Once submitted, the experiment was monitored by way of its various child runs (and their child runs), their logs, the cluster node activities and the experiment statistics. 

It completed successfully with a **VotingEnsemble** as the best model with accuracy of **91.8%**.

![The Completed Experiment](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_06.png)

For the purpose of understanding the model, the ensemble details were reviewed. The ensemble was made up of **multiple** **XGBoost** Classifiers with different weightings.

![The Best Model](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_07.png)

It was however noted that the second best model was indeed a single XGBoost classifier.

![The 2 best models](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_08.png)

To try to get a better appreciation for the featureset, the model's explanation was also briefly reviewed. The image below shows the 4 features that were deemed most important by the model in performing the classifications at 91% accuracy.
For future work, this could also be used for the purpose of dimensionality reduction, saving on compute time and possibly improving accuracy.

![Model Explanation](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_09.png)

---

### Deployed Model and Result from 2 Inputs

To put the model into production, it was deployed from the ML Studio interface. A form was filled out, denoting a name, compute type and the use of authentication.

![Deployment Form](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_11.png)

Once submitted, the deployment was monitored from the model's endpoing section, watching the deployment state for a 'healthy' indication.

![Deployed Model](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_12.png)

The json payload in the endpoint file was modified with sample values to enable 2 tests.

Once healthy, the model was tested using the endpoint.py file. It could also have been tested using the code provided on the model's 'consume' page. 

The script provided a json response with the result for the 2 tests.

![Consumed Model](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_13.png)

--- 

### Reviewing Logs and Enabling AppInsights

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

---

## Swagger API Review

Azure provides a Swagger JSon file for the purpose of documenting the endpoint's API use. This is critical for developers seeking to use the service as they will need to understand its functionality and its requirements.

For the purpose of this exercise, the swagger json was placed in the same folder with the provided swagger.sh (used for downloading the swagger image from docker) and the serve.py.

![Swagger files](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_46.png)

The serve.py allows us to host the swagger.json file locally as a local web url while allowing us to bypass any cross-origin restrictions.

![serve.py](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_45.png)

The docker image is downloaded and run, with the port being changed to 9000. 

![Swagger.sh](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_43.png)
![Docker images](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_44.png)

Once the Swagger image and the serve.py are running, we browse to the Swagger UI on the provided port 9000. 

Inside Swagger's UI, we then open the downloaded swagger.json via the localhost url exposed by serve.py on port 8000.

![Swagger Review of Model Endpoint's Swagger.Json](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_19.png)

To get a better understanding of the web service, we review its methods including GET (health check) and POST (submission for inference). 

The next 2 screenshots show a sample input followed by its data dictionary

![Swagger Input Payload](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_20.png)
![Swagger Input FieldTypes](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_21.png)

The following screenshot shows a sample response and field type from the endpoint followed by the details for error responses.

![Swagger Output](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_22.png)


---

## Benchmarking the Endpoint's performance

To ensure appropriate expectations, we must create a benchmark for the endpoint. This can be performed using the Apache Bench tool.

The tool allows us to simply specify the number of runs, the level of verbosity, the input data and its format, along with the Web Service URL and the authentication key.

![Benchmark call](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_47.png)

Upon running, the tool makes repeated calls (in this case, 10) to the endpoint.

![Benchmark start for 10](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_24.png)

Once completed, it calculates various statistics relevant to its impression of the performance of the endpoint.

![Benchmark end for 10](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_25.png)

This next screenshot shows the measured performance for a 1000 request test. It is not very different from that of the earlier, smaller test.

![Benchmark start for 1000](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_23.png)

The tool's measurements were comparable with Azure's App Insights, seen below.

![AppInsights for Benchmarking](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_26.png)


---

## Pipeline Run via the SDK

The provided code was modified to perform the required functions on the bank marketing training dataset. 

This involved using the environment's config json in the notebook's folder along with modifying the experiment name, the cluster name, pipeline name and other variables. It also included setting up a compute object for the purpose of running the notebook. A single 'Standard DS12_v2' was used for consistency.

![Code mods](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_27.png)

The following screenshots show where the pipeline experiment was subsequently submitted, along with the RunDetails widget showing the experiment's progress, its logs and links to open the ML Studio portal. 

![Pipeline Run from SDK](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_32.png)
![Pipeline Run from SDK](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_28.png)

---

## Pipeline Runs

After submission of the pipeline run, we can either monitor from the notebook or inside the portal. This next screenshot shows the portal while the model is still training.

![Pipeline Run](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_31.png)

This shows the graph page with the dataset and the automl training module along with the completed status. 

![Pipeline Done](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_34.png)

The above pipeline (lucid...) is shown here.

![Created Pipelines](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_38.png)

--- 

## Publish and Run incl REST API run

Once the pipeline is complete, we can download and review any metrics along with the best model. 

We can also choose to publish the pipeline (using ML Studio or the SDK) to an endpoint so it can be run via a REST API.

![Publish Pipeline](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_36.png)

The Pipeline is being run here via its Endpoint's Rest API. The following screenshot shows the RunDetails Widget showing the progress.

![Monitoring the Pipeline called via Rest API](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_37.png)

Pipeline endpoints can also be explored in ML Studio via an overview page which shows its status, steps and endpoint. We can also find its run history and status.

![Pipeline Overview](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_40.png)
![Finished Pipeline Run](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_39.png)

---  

## Pipeline call via REST API

This screenshot was subsequently done in Jupyter Labs. It shows where the Pipeline is being invoked by its Rest API. This essentially instructs it to process any new data and perform training.

![Pipeline call via Rest API](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_42_v2.png)

The following images show the run via the REST Api as well as the object in ML Studio.

![Monitoring the Pipeline called via Rest API](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_37.png)
![Created Pipelines](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_38.png)

---

## Dataset with AutoML

The image below shows the dataset that was used with the automl module.

![Dataset with AutoML](https://github.com/dwittaker/nd00333_AZMLND_C2/blob/main/POML_files/Images/Img_POML_41.png)

