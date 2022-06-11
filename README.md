# Machine-Learning-Algorithms

Hi there, 

These are various machine learning algorithms that are related to various supervised and unsupervised types of learning.
These notebooks got the implementation of few algorithms that are widely used in the field of Machine Learning.

K NEAREST NEIGHBORS:

Initial one is about K nearest neighbors which is one of very simple and famous supervised learning algorithm

KNN is all about checking out the nearest neighbors depending on the distance and then assigning the label of the neighbor to the input variable. There's nothing related to learning in the KNN algorithm. Every test set's label is found out by checking out the nearest neighbors from the training set and depending on the type of problem( majority voting in case of classification and average in terms of regression), the label is assigned to the testing set.

The K value decides with how many neighbors, the label is to be calculated.

If the K value is small that means the bias will be low and variance is high because with smaller neighborhood, the model varies with the new data and this model tends to be overfitted.

If the K value is high, then the model will be generic and the bias will be high and less variance since the generic model will be fitted to any new data easily.

