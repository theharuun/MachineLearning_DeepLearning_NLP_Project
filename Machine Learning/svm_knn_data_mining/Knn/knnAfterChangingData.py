import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

data = pd.read_csv('DataMiningDataSetContainsMeanInsteadOfNan.csv')

X = data[['Cinsiyet', 'Yas', 'TahminiMaas']]
y = data['IngilizceBilme']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)



# birdenn fazla n ye göre hesaplama yapıldı 
for n in [3, 5, 7, 9, 11]:
 model = KNeighborsClassifier(n_neighbors=n)
 model.fit(X_train, y_train)
 y_pred = model.predict(X_test)
 conf_matrix = confusion_matrix(y_test, y_pred)
 accuracy = accuracy_score(y_test, y_pred)
 print(f"Confusion Matrix for {n}:\n", conf_matrix) 
 print(f"Accuracy for {n}:", accuracy)
