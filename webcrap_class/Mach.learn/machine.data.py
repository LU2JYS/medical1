classifiers = [ 
KNeighborsClassifier(3), 
SVC(kernel="linear", C=0.025), 
SVC(gamma=2, C=1), 
GaussianProcessClassifier(1.0 * RBF(1.0)), 
DecisionTreeClassifier(max_depth=5), 
RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1), 
MLPClassifier(alpha=1, max_iter=1000), 
AdaBoostClassifier(), 
GaussianNB(), 
QuadraticDiscriminantAnalysis(), 
]

#---------------------------------------------------------------------------------
