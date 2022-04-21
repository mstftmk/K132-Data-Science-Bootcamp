# Final Project
Kodluyoruz - Carbon Veri Bilimi Bootcamp'i 7. final projesi için, CNN ile duygu tahmini gerçekleştirdim.

> Öncelikle Data klasörü içindeki zip dosyasında bulunan veriyi çıkartın. Ya da [Kaggle](https://www.kaggle.com/datasets/deadskull7/fer2013) üzerinden veriyi indirip, Data klasörü içine aktarın.

## Results

> Happy Face
![Example1](https://github.com/mstftmk/K132-Data-Science-Bootcamp/blob/main/Final%20Project/Data/images/Example1.png?raw=true)

> Sad Face
![Example1](https://github.com/mstftmk/K132-Data-Science-Bootcamp/blob/main/Final%20Project/Data/images/Example2.png?raw=true)

## Requirements

```python
import tensorflow
import keras
from keras.models import Sequential, Model, model_from_json
from keras.layers import Conv2D, MaxPool2D, AveragePooling2D
from keras.layers import Dense, Activation, Dropout, Flatten, BatchNormalization
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint
from keras.models import load_model
from PIL import Image

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```
