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

# random_state=1 자동으로 훈련세트,테스트세트가 섞이지 않도록 도와준다..
# stratify= : 설정데이터를 가지고 랜덤으로 데이터를 섞어줌.

# 자동으로 섞어준다>>>>>>>>>>>>>>>>>>>>>>굿굿
train_input,test_input,train_target,test_target=train_test_split(
    datas,results,stratify=results,random_state=1
)
train_input

freq = list(map(lambda n : n/total,cnt)) #map,zip 많이 사용한다

#---------------------------------------------------------------------------------
#선형회귀 모델
# lr.coef_  : 기울기 , lr.intercept_ : y절편