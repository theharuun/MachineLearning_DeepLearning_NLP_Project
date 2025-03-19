# [TR]
# Makine Öğrenimi & Derin Öğrenme & Doğal Dil İşleme (NLP) Projeleri

## 📌 Proje Genel Bakış
Bu depo, farklı yapay zeka tekniklerini keşfeden çeşitli Makine Öğrenimi , Derin Öğrenme ve Doğal Dil İşleme projelerini içerir. Amaç, ML ve DL kavramlarını yapılandırılmış ve pratik bir şekilde uygulamaktır.

## 🛠️ Kurulum
Projeye başlamak için depoyu klonlayın ve gerekli bağımlılıkları yükleyin:

```bash
# Depoyu klonlayın
git clone https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project.git
cd MachineLearning_DeepLearning_Project

# Bağımlılıkları yükleyin
pip install -r requirements.txt
```

## 📂 Proje Yapısı

---

## 🤖 Makine Öğrenimi Projeleri

### [Spark-ML/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Machine%20Learning/Spark-ML/spark_regresyon.ipynb)
- **Açıklama:**  
  Spark kullanarak california evleri üzerinde fiyat tahmini yapan regresyon modeli kuruldu.

### [ClustringKmeans/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Machine%20Learning/ClusteringKmeans/kMeans.ipynb)
- **Açıklama:**  
  K-Means algoritması kullanılarak veri kümesi üzerinde sınıflandırma modelleri geliştirilir. Verilerin benzerliklerine göre gruplandırılması sağlanarak, denetimli öğrenme yöntemleriyle model performansının artırılması hedeflenir.

### [Clustring_with_using_Tsfresh_featuring/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Machine%20Learning/Clustring_with_using_Tsfresh_featuring/YZUP-VYU-Proje-Harun-Korkmaz.ipynb)
- **Açıklama:**  
  TSFRESH kütüphanesi ile zaman serisi verilerinden otomatik olarak öznitelikler çıkarılır. Elde edilen öznitelikler, kümeleme algoritmalarıyla verinin yapısal özelliklerini ortaya koymak amacıyla kullanılır.

### [Diyabet/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Machine%20Learning/Diyabet/app.ipynb)
- **Açıklama:**  
  Diyabet verileri üzerinde, veri temizleme, eksik verilerin tamamlanması ve gürültünün giderilmesi gibi ön işleme adımları uygulanır. Sonrasında, özellik seçimi teknikleriyle en anlamlı öznitelikler belirlenip makine öğrenimi modelleriyle diyabet risk tahmini gerçekleştirilir.

### [Exploratory_Data_Analysis_EDA/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Machine%20Learning/Exploratory_Data_Analysis_EDA/eda.ipynb)
- **Açıklama:**  
  Veri kümesinin genel yapısını ve dağılımını anlamaya yönelik kapsamlı keşifsel veri analizi (EDA) yapılır. Grafikler, özet istatistikler ve korelasyon analizleri ile verideki gizli ilişkiler ve önemli noktalar belirlenir.

### [PredictCarPrice/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Machine%20Learning/PredictCarPrice/hcg.ipynb)
- **Açıklama:**  
  Araç fiyatlarının, model, kilometre, yaş gibi özelliklere göre tahmin edildiği bir projedir. Veri analizi ve model optimizasyonu aşamaları ile doğru fiyatlandırma stratejileri geliştirilir.

### [PredictRentHouse/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/tree/main/Machine%20Learning/PredictRentHouse)
- **Açıklama:**  
  Kiralık ev fiyatlarının doğru şekilde öngörülmesi amacıyla, emlak verileri üzerinde özellik mühendisliği ve çeşitli regresyon modelleri uygulanır.

### [PredictTypeFlower/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Machine%20Learning/PredictTypeFlower/app.ipynb)
- **Açıklama:**  
  Çiçek verilerinden elde edilen öznitelikler kullanılarak, çiçek türlerinin doğru şekilde sınıflandırılması hedeflenir. Bu projede verinin doğru etiketlenmesi ve model hassasiyeti ön plandadır.

### [svm_knn_data_mining/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/tree/main/Machine%20Learning/svm_knn_data_mining)
- **Açıklama:**  
  Destek Vektör Makinesi (SVM) ve En Yakın Komşu (KNN) algoritmalarının kullanıldığı veri madenciliği projeleridir. Farklı algoritmaların karşılaştırılmasıyla, hangi yöntemin veriye daha uygun olduğu ve en iyi performansı sunduğu belirlenmeye çalışılır.

### [Bank_Customer_Churn_LR/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/tree/main/Machine%20Learning/Bank_Customer_Churn_LR/main.ipynb)
- **Description:**
   Bu proje, makine öğrenimi teknikleri, özellikle Lojistik Regresyon ve Rastgele Orman kullanarak müşteri kaybını tahmin etmeye odaklanıyor. Özellik mühendisliği uygulayarak, sınıf dengesizliğini ele alarak ve hiperparametreleri optimize ederek, hangi modelin kaybı tahmin etmede en iyi performansı gösterdiğini belirlemeyi amaçlıyoruz. Sonuçlar, dengeli ve etkili bir tahmin modeli sağlamak için doğruluk, geri çağırma ve kesinlik kullanılarak değerlendirilir.

### [Credict_Score_Classification/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/tree/main/Machine%20Learning/Credict_Score_Classification/main.ipynb)
- **Description:**
    This project focuses on classifying credit scores based on customers’ information using machine learning techniques, specifically Random Forest. By applying feature engineering, addressing class imbalance, and optimizing hyperparameters, we aim to determine which model performs best in predicting loss. The results are evaluated using accuracy, recall, and precision to provide a balanced and effective prediction model.

    **Not: Veri setine kodun içerisinden erişebilirsiniz.**

---

## 🧠 Derin Öğrenme Projeleri

### [Cnn_Mnist_Dataset_Deep_Learning/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Deep%20Learning/Cnn_Mnist_Dataset_Deep_Learning/app.ipynb)
- **Açıklama:**  
  MNIST el yazısı rakamlar veri seti kullanılarak, Evrişimli Sinir Ağı (CNN) modeli eğitilir. Görüntü sınıflandırması amacıyla farklı katmanlar ve filtreleme yöntemleri uygulanır.

### [TensorMedImageClassifier/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Deep%20Learning/TensorMedImageClassifier/main.ipynb)
- **Açıklama:**  
  TensorFlow tabanlı bir ortamda geliştirilen bu projede, evrişimli sinir ağı (CNN) mimarisi kullanılarak zaman serisi verilerinin tahmini gerçekleştirilir.  


### [X-Ray-Akciger/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Deep%20Learning/X-Ray-Akciger/akciger_kanser_tespit.ipynb)
- **Açıklama:**  
  Transfer öğrenme yöntemiyle, önceden eğitilmiş derin öğrenme modelleri X-ray görüntüleri üzerinden akciğer hastalıklarının veya anormalliklerinin tespiti için kullanılır. Model, hızlı adaptasyon ve yüksek doğrulukla sonuç üretmeye odaklanmıştır.


### [ResNetTransformingMedicalImageClassifier/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Deep%20Learning/ResNetTransformingMedicalImageClassifier/main.ipynb)
- **Açıklama:**  
  Transfer öğrenme yöntemiyle, önceden eğitilmiş derin öğrenme modelleri üzerinden sınıflandırma katmanını kendimizin oluşturmasıyla vitamin ve ilaçların sınıflandırması yapılmıştır.
  Transforming Model olarak ResNet50 modeli kullanılmıştır.


### [ANN-Personalized-Tratment-Classing/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Deep%20Learning/ANN-Personalized-Tratment-Classing/kisisellestirilmistedavi.ipynb)
- **Açıklama:**
    Rastgele sağlık değerleri oluşturulup yeni sütunlar eklenerek bir dataframe hazırlandı, bu veri üzerinde yapay sinir ağı ile model eğitimi gerçekleştirildi, elde edilen model görselleştirilip değerlendirildi ve overfitting durumunda ekstra çalışmayı önlemek amacıyla EarlyStopping yöntemi ile erken durdurma işlemi uygulandı.


### [EfficientNet-Eye-Disease-Detection/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Deep%20Learning/EfficientNet-Eye-Disease-Detection/main.ipynb)
- **Açıklama:**
    Kaagleda bulunan göz veri seti üzerinde EfficentNetB2 transfer modelini kullanarak parametre iyileştirilmeleri yapılarak elimizdeki veri seti üzerinde göz hastalıkları sınıflandırması tamamlandı yüzde 80 başarı elde edildi.


### [CNN-CIFAR10/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Deep%20Learning/CNN-CIFAR10/main.ipynb)
- **Açıklama:**
    Tensorflow ile kerastan CIFAR veri seti üzerinde evrişimli sinir ağı modeli ile sınıflandırma projesi yapıldı
---

## 🤖 Doğal Dil İşleme Projeleri

### [IMDB-Classification-nlp/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Natural%20Language%20Processing%20(NLP)/IMDB-Classification-nlp/main.ipynb)
- **Açıklama:**
    Kaagleda bulunan IMDM yorumları veri seti üzerinde doğal dil işleme ile sınıflandırma işlemi yapıldı .

### [Turkish-Text-Project-NLP/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Natural%20Language%20Processing%20(NLP)/Turkish-Text-Project-NLP/main.ipynb)
- **Açıklama:**
    Githubda bulunan beyaz perde film sitesindeki TÜRKÇE yorumların doğal dil işleme ile sınıflandırılması yapılmıştır  .

### [Sentiment-Anaylisis-In-Nlp-Model-With-Rnn/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Natural%20Language%20Processing%20(NLP)/Sentiment-Anaylisis-In-Nlp-Model-With-Rnn/main.ipynb)
- **Açıklama:**
    ChatGtp ile üretilen veri seti üzerinde duygu analizi yapıldı bu kısımda rnn modeli kullanıldı  .

### [Clinical-Test-Classification-NLP/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Natural%20Language%20Processing%20(NLP)/Clinical-Test-Classification-NLP/main.ipynb)
- **Açıklama:**
    Hastaların şikâyetlerine ilişkin veri setinde sınıflandırmalar yapılarak NLP kullanılarak tamamlandı.

---

Her proje grubu, ilgili alanlarda temel kavramların pekiştirilmesi ve pratik uygulamaların geliştirilmesi için zengin örnekler sunmaktadır. İlgili kodlar, veri setleri ve ek dokümantasyonlar projelerin iç dizinlerinde yer almaktadır.

---
🔹 **Oluşturan & Bakımı Üstlenen:** [**Harun Korkmaz**](https://github.com/theharuun)

---

# [EN]
# Machine Learning & Deep Learning  & Natural Language Processing (NLP) Projects

## 📌 Project Overview
This repository contains various Machine Learning , Deep Learning and Natural Language Processing (NLP) projects that explore different AI techniques. The goal is to provide structured and practical implementations of ML and DL concepts.

## 🛠️ Installation
To get started, clone the repository and install the required dependencies:

```bash
# Clone the repository
git clone https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project.git
cd MachineLearning_DeepLearning_Project

# Install dependencies
pip install -r requirements.txt
```

## 📂 Project Structure

## 🤖 Machine Learning Projects

### [Spark-ML/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Machine%20Learning/Spark-ML/spark_regresyon.ipynb)
- **Description:**
  A regression model that estimates prices on California houses was established using Spark.

### [ClustringKmeans/](](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Machine%20Learning/ClusteringKmeans/kMeans.ipynb))
- **Description:**
    Classification models are developed on the dataset using the K-Means algorithm. It is aimed to increase model performance with supervised learning methods by grouping the data according to their similarities.

### [Clustring_with_using_Tsfresh_featuring/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Machine%20Learning/Clustring_with_using_Tsfresh_featuring/YZUP-VYU-Proje-Harun-Korkmaz.ipynb)
- **Description:**
    Features are automatically extracted from time series data with the TSFRESH library. The obtained features are used to reveal the structural features of the data with clustering algorithms.

### [Diabetes/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Machine%20Learning/Diyabet/app.ipynb)
- **Description:**
    Pre-processing steps such as data cleaning, completion of missing data, and noise removal are applied to the diabetes data. Then, the most meaningful features are determined with feature selection techniques and diabetes risk prediction is performed with machine learning models.

### [Exploratory_Data_Analysis_EDA/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Machine%20Learning/Exploratory_Data_Analysis_EDA/eda.ipynb)
- **Description:**
    A comprehensive exploratory data analysis (EDA) is performed to understand the general structure and distribution of the dataset. Hidden relationships and important points in the data are determined with graphs, summary statistics and correlation analyses.

### [PredictCarPrice/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Machine%20Learning/PredictCarPrice/hcg.ipynb)
- **Description:**
    This is a project where vehicle prices are predicted according to features such as model, mileage, and age. Correct pricing strategies are developed with data analysis and model optimization stages.

### [PredictRentHouse/]](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/tree/main/Machine%20Learning/PredictRentHouse)
- **Description:**
    In order to correctly predict rental house prices, feature engineering and various regression models are applied to real estate data.

### [PredictTypeFlower/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Machine%20Learning/PredictTypeFlower/app.ipynb)
- **Description:**
    The aim is to correctly classify flower types using attributes obtained from flower data. Correct labeling of data and model sensitivity are at the forefront in this project.

### [svm_knn_data_mining/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/tree/main/Machine%20Learning/svm_knn_data_mining)
- **Description:**
    These are data mining projects using Support Vector Machine (SVM) and Nearest Neighbor (KNN) algorithms. By comparing different algorithms, it is tried to determine which method is more suitable for the data and provides the best performance.

### [Bank_Customer_Churn_LR/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/tree/main/Machine%20Learning/Bank_Customer_Churn_LR/main.ipynb)
- **Description:**
    This project focuses on predicting customer churn using machine learning techniques, specifically Logistic Regression and Random Forest. By applying feature engineering, addressing class imbalance, and optimizing hyperparameters, we aim to determine which model performs best in predicting churn. The results are evaluated using accuracy, recall, and precision to provide a balanced and effective prediction model.


### [Credict_Score_Classification/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/tree/main/Machine%20Learning/Credict_Score_Classification/main.ipynb)
- **Description:**
    This project focuses on classifying credit scores based on customers’ information using machine learning techniques, specifically Random Forest. By applying feature engineering, addressing class imbalance, and optimizing hyperparameters, we aim to determine which model performs best in predicting loss. The results are evaluated using accuracy, recall, and precision to provide a balanced and effective prediction model.

    **Note: You can access the dataset code from within.**

---

## 🧠 Deep Learning Projects

### [Cnn_Mnist_Dataset_Deep_Learning/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Deep%20Learning/Cnn_Mnist_Dataset_Deep_Learning/app.ipynb)
- **Description:**
    Using the MNIST handwritten digits dataset, a Convolutional Neural Network (CNN) model is trained. Different layers and filtering methods are applied for image classification.

### [TensorMedImageClassifier/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Deep%20Learning/TensorMedImageClassifier/main.ipynb)
- **Description:**
    In this project developed in a TensorFlow-based environment, time series data is predicted using the convolutional neural network (CNN) architecture.

### [X-Ray-Lung/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Deep%20Learning/X-Ray-Akciger/akciger_kanser_tespit.ipynb)
- **Description:**
    With the transfer learning method, pre-trained deep learning models are used to detect lung diseases or abnormalities on X-ray images. The model focuses on fast adaptation and high accuracy.


### [ResNetTransformingMedicalImageClassifier/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Deep%20Learning/ResNetTransformingMedicalImageClassifier/main.ipynb)
- **Description:**
    Classification of vitamins and drugs was made by creating the classification layer ourselves from pre-trained deep learning models with the transfer learning method.
    ResNet50 model was used as the Transforming Model.
    

### [ANN-Personalized-Tratment-Classing/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Deep%20Learning/ANN-Personalized-Tratment-Classing/kisisellestirilmistedavi.ipynb)
- **Description:**
    A data frame is prepared by creating random health values ​​and adding new columns, model training is done on this data with an artificial neural network, the obtained model is visualized and evaluated, and the early stopping process is stopped with the EarlyStopping method for extra protection in case of overfitting.


### [EfficientNet-Eye-Disease-Detection/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Deep%20Learning/EfficientNet-Eye-Disease-Detection/main.ipynb)
- **Description:**
    By using the EfficentNetB2 transfer model on the eye data set in Kaagle, parameter improvements were made and the eye disease classification was completed on the data set we have, 80 percent success was achieved.
    

### [CNN-CIFAR10/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Deep%20Learning/CNN-CIFAR10/main.ipynb)
- **Description:**
A classification project was done with a convolutional neural network model on the Kerastan CIFAR dataset using Tensorflow

---

## 🤖 Natural Language Processing Projects

### [IMDB-Classification-nlp/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Natural%20Language%20Processing%20(NLP)/IMDB-Classification-nlp/main.ipynb)
- **Description:**
    A classification process was performed using natural language processing on the IMDM comments dataset found on Kaagle. 


### [Turkish-Text-Project-NLP/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Natural%20Language%20Processing%20(NLP)/Turkish-Text-Project-NLP/main.ipynb)
- **Description:**
    TURKISH comments on the white screen movie site on Github were classified using natural language processing.

### [Sentiment-Anaylisis-In-Nlp-Model-With-Rnn/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Natural%20Language%20Processing%20(NLP)/Sentiment-Anaylisis-In-Nlp-Model-With-Rnn/main.ipynb)
- **Description:**
Sentiment analysis was performed on the dataset generated with ChatGtp and this adjustment was made and the rnn model was saved.

### [Clinical-Test-Classification-NLP/](https://github.com/theharuun/MachineLearning_DeepLearning_NLP_Project/blob/main/Natural%20Language%20Processing%20(NLP)/Clinical-Test-Classification-NLP/main.ipynb)
- **Description:**
Classifications were worked on in the dataset of patients' complaints and completed using NLP.



---

Project groups provide rich examples for reinforcing basic concepts and developing practical applications in the relevant fields. Related codes, datasets and additional documentation are located in the internal directories of the projects.

---
🔹 **Created & Maintained by** [**Harun Korkmaz**](https://github.com/theharuun)

