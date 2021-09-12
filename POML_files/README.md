
Overview 

In this project I utilize Azure's Machine Learning Tools for the classification of a bank marketing dataset. In that dataset, there are several features (demographic, financial etc) about persons who acquired a specific service from the bank(s). Using the data, we would like to be able to predict situations in which persons would or would not acquire that service. 

Architectural Diagram

Improving the Project in the Future
The project could certainly be improved with more indepth experimentation, including the use of additional parameters, different metrics and better datasets. For example, the accuracy metric was used, but is possibly affected by skewed datasets. The dataset's classes are severely skewed with close to 90% of the records being attributed to one class. There is the possibility the model (by way of a more appropriate metric scoring mechanism) could improve with better balance or a different metric. Also, while parameters were fed to the automl config, it may be useful to allow those to be fed to the pipeline later as arguments.

Screenshots required with a short description to demonstrate key steps

A link to the screencast video on YouTube
https://youtu.be/5Wa9yKfQE2I