# OkCupid_Dating_with_ML

We cleanned the data using Python, Pandas
presentation using:
Flask, Java script, Html, ccs
tableau, plotly, Machine learning

Sally Ahmed
cleanned 4 columns from the data and Graph it
using sunburst graph using plotly 
creating Tableau presentation.

Manochitra Kumar: **Clustering and creating a recommendation algorithm:**

The scope for this part of the project was to cluster the user’s profiles into groups and to try to find a match more easily with the help of machine learning algorithms. We tried using different modelling/training methods for the data we had.
The first step was to clean and preprocess the available data in a way it can be understood by the algorithms. 

The preprocess consisted of splitting the data into numerical (age, income, height) and categorical variables (diet, education, job). Then the numerical variables were scaled using standardscaler and the categorical variables were transformed from string to float using ohehotencoder.

**Kmeans clustering** algorithm was chosen to cluster the profile data into different groups. The results from kmeans were plotted and from the elbow graph we were able to pick 7 clusters.  And when we investigate the cluster plot , we immediately see that there are no distinct clusters.

We then did feature reduction using PCA, and the elbow plot showed 7 clusters, and the cluster plot also didn’t show much distinct clusters.

We added the clusters to the original dataset. we proceeded with training the model with supervised ML.
We used **K nearest neighbour and random forest** method for this purpose. The accuracy score for the KNN method was 63% and 55% for training and testing data respectively. However, on the other hand randomforest model gave as a very good score of above 90% for both training and testing data.

Now that the model is trained, we created a pipeline to be used as the basis for processing data and predicting for the recommendation system to work. We saved the model in a pickle file and this will load the pipeline when there is new test data available.

When user inputs data in the form created in html, the pipeline predicts the cluster that the user falls into and pulls 5 random profiles from the OkCupid dataset and shows it as a table, which is similar to the way dating app works.




Ruby
For my portion of the projection, I wanted to do Supervised Machine Learning and predict Body Type from a select part of the data provided. Cleaning up the data into a way that I can use
it for Machine Learning, I proceeded to  break down my data to be able to input it to the models. Running that and seeing how the outcomes were like,
I ended up also running a separate test with gender prediction to see how the two differ. Running Random Forest & Neural Network for Body Type resulted in high training & low testing scores. Running Random Forest, Logistic Regression, & Neural Network for Gender results in higher training & testing. 


Sam
I cleaned the columns of "Education", "Job", and "Income". For the income part, I should make some data in the dataset because there are many blanks in the income data. For making it reasonable, I referenced a lot of data from the pole website or Job recruiting website, and I divided the income into 5 portion which are '0 - 10%', '10 - 25%', '25 - 50%', '50 - 75%', '75 - 100%'. 

Also I coordinated the website for 'Text Analysis' and 'Essay Sentimental Analysis', 'Sentimental testing'. In order to make an interactive experience, I used flask. 

I made essay analysis test using VaderSentimentalAnalyzer which is a trained data. 
