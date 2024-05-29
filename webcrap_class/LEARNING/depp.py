#딥러닝

import numpy as np
import pandas as pd
from tensorflow import keras


# 옵티마이저 방식
# 모델결정 model = keras.Sequential()
# Flatten 추가  model.add(keras.layers.Flatten(input_shape=(28,28)))
# Dense층 추가  model.add(keras.layers.Dense(100,activation='relu'))
# Dense층 추가  model.add(keras.layers.Dense(10,activation='softmax'))
# 모델 설정 옵티마이저 -adam
# model.compile(loss='sparse_categorical_crossentropy',metrics=['accuracy'])
# 모델훈련 model.fit(train_scaled,train_target,batch_size=32,epochs=5)
# 모델평가 model.evaluate(val_scaled,val_target)

# drop out 규제 : 과대적합을 낮추어주는 역할을 한다
# model.add(keras.layers.Dropout(0.3))
#### drop out 규제 : 과대적합을 낮추어주는 역할을 한다
#### epochs 를 증가할때 훈련세트에는 정확도가 높은데,  검증세트에는 정확도가 높지 않음

### 콜백 함수 >>>
### 손실율이 가장 낮은 위치의 모델을 저장시켜줌.
# 손실율이 가장 낮은 위치의 모델을 저장시켜줌.
# 확장자 h5, keras확장자명 변경
# checkpoint_cd = keras.callbacks.ModelCheckpoint('best_model.keras')
# history = model.fit(train_scaled,train_target,epochs=20,
#                     validation_data=(val_scaled,val_target),callbacks=[checkpoint_cd])