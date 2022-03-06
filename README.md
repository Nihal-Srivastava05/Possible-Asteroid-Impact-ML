# Problem Statement
Asteroids are small, rocky objects that orbit the Sun. Although asteroids orbit the Sun like planets, they are much smaller than planets. There are lots of asteroids in our solar system. Asteroids with a 1 km (0.62 mi) diameter strike Earth every 500,000 years on average. Large collisions – with 5 km (3 mi) objects – happen approximately once every twenty million years. The National Aeronautics and Space Administration (NASA) is an independent agency of the U.S. federal government responsible for the civilian space program, as well as aeronautics and space research. NASA was established in 1958, succeeding the National Advisory Committee for Aeronautics. Sentry is a highly automated collision monitoring system that continually scans the most current asteroid for possibilities of future impact with Earth over the next 100 years built by NASA.

## Dataset
The dataset which we have used is called Possible Asteroid Impacts with Earth which is collected by NASA and is available at Kaggle (https://www.kaggle.com/nasa/asteroid-impacts). his dataset includes the Sentry system's list of possible asteroid impacts with Earth and their probability, in addition to a list of all known near Earth asteroids and their characteristics. The asteroid orbit and impact risk data was collected by NASA's Near-Earth Object Program at the Jet Propulsion Laboratory (California Institute of Technology). This link contains two datasets orbit.csv and impacts.csv.  
Impact dataset all about the impact a certain asteroid can cause based on certain features and has a continuous data column possible impact which we can predict using ML. Features present:  
- Object Name
- Period Start
- Period End
- Possible Impacts
- Cumulative Impact Probability
- Asteroid Velocity
- Asteroid Magnitude
- Asteroid Diameter (km)
- Cumulative Palermo Scale
- Maximum Palermo Scale
- Maximum Torino Scale  

Orbit dataset is asteroid classification dataset classifies the asteroids into few categories based on certain features and has a categorical column called Object classification we can use to predict in ML. Features present:  
- Object Name
- Object Classification
- Epoch (TDB)
- Orbit Axis (AU)
- Orbit Eccentricity
- Orbit Inclination (deg)
- Perihelion Argument (deg)
- Node Longitude (deg)
- Mean Anomoly (deg)
- Perihelion Distance (AU)
- Aphelion Distance (AU)
- Orbital Period (yr)
- Minimum Orbit Intersection Distance (AU)
- Orbital Reference

## Models Used:
We are performing various insight generation and prediction on this dataset using ML algorithms and methods so this can be better understood and can be used to predict for later asteriods which will be discovered.  
In start we performed some ML **Regression** using some common models like Linear regression, RandomForestRegressor, SVR and hyperparameter tuning of regression using elastic net. **Elastic net** is a Linear regression model with both L1 and L2 regulization built in with alpha being their ratios which we can tune to get a better result. We performed **GridSearchCV** to get the most optimal values for those along with **polynomial feature** extraction to see if combination of features results in better performance.    
Next we ran **classification** algorithms on it to predict the asteroid classification (In orbit dataset) using RandomForestClassifier and DecisionTreeClassifier. A **decision tree** is a type of supervised machine learning used to categorize or make predictions based on how a previous set of questions were answered. The model is a form of supervised learning, meaning that the model is trained and tested on a set of data that contains the desired categorization. It uses the concept of entropy or gini index to see which features are more important and better for the given data and accordinly predict using those values.  
Finally, we also performed some **clustering** on top of the impact's dataset using the **K-means** algorithm to cluster the dataset into different groups and see which group has more impact and which less so we can see that which are the general range of values for other features which have high impact and vice versa. K-means clustering is a very famous and powerful unsupervised machine learning algorithm. K-means clustering uses “centroids”, K different randomly-initiated points in the data, and assigns every data point to the nearest centroid. After every point has been assigned, the centroid is moved to the average of all of the points assigned to it and then based on these centroids it classifies the given data into clusters.  

## Contributors:
Nihal Srivastava (https://github.com/Nihal-Srivastava05)  
Varun Kamath (https://github.com/VarunK1505)  
Ronit Naik (https://github.com/RonitNaik9)  
