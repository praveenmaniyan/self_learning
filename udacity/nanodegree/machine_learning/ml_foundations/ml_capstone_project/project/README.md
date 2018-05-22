Machine Learning Engineer Nanodegree
Capstone Proposal

Praveen Maniyan

Datasets:
The dataset for building this Machine Learning problem can be taken from Folio Data Set found at https://archive.ics.uci.edu/ml/datasets/Folio



References:
"Data Augmentation for Plant Classification", Authors, Pornntiwa Pawara, Emmanuel Okafor, Lambert Schomaker, and Marco Wiering - https://www.researchgate.net/publication/319990090_Data_Augmentation_for_Plant_Classification

"Deep Learning for Plant Identification in Natural Environment", Authors, Yu Sun, Yuan Liu, Guan Wang, and Haiyan Zhang - https://www.hindawi.com/journals/cin/2017/7361042/

https://arxiv.org/pdf/1409.1556.pdf
http://deeplearning.net/software/theano/library/tensor/nnet/nnet.html#theano.tensor.nnet.nnet.binary_crossentropy
http://deeplearning.net/software/pylearn/formulas.html#pylearn.formulas.costs.binary_crossentropy
https://github.com/keras-team/keras/issues/6444
https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html
https://github.com/keras-team/keras/issues/3296
https://www.codesofinterest.com/2017/08/bottleneck-features-multi-class-classification-keras.html
https://stackoverflow.com/questions/47535596/how-do-i-get-the-true-labels-when-i-use-a-imagedatagenerator-flow-from-directory?rq=1
https://stackoverflow.com/questions/45806669/keras-how-to-use-predict-generator-with-imagedatagenerator
https://keras.io/preprocessing/image/
https://www.kaggle.com/keras/vgg16
https://archive.ics.uci.edu/ml/datasets/Folio
https://www.kaggle.com/c/leaf-classification#description
https://www.quora.com/in/What-is-the-VGG-neural-network

Libraries:
numpy
keras
matplotlib
cv2

Setup:
1. Unzip the project_submission.zip file to a folder say "project"
2. Under the project folder, create a "data" folder. Under the "data" folder create folders, "train" and "validation"
3. Download the data from "https://archive.ics.uci.edu/ml/machine-learning-databases/00338/Folio%20Leaf%20Dataset.rar"
4. Inside the rar file, find the "Folio" folder. Extract all the directories under it, to the above "train" folder
5. Recreate the same directory names of "train" in "validation" folder
6. From each folder under "train", like "ashanti blood", "betel", etc., move 4 files each to the corresponding directory in "validation" folder
7. Run the leaf_identification_v2.0.ipynb Jupyter Notebook