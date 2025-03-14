# Milli teknoloji Yapay zeka uzmanlık Veri Yoğun Uygulamaları Ödevi
# Eğitmen : Dr.İsmail Güzel 

# Hisse Senetlerinin Sektörel Benzerlik Analizi ve Sınıflandırma Modeli

## Proje Tanımı
Bu proje, farklı sektörlerdeki hisse senetlerinin zaman serisi davranışlarını analiz ederek, bir hisse senedinin hangi sektöre daha çok benzediğini belirlemeyi amaçlamaktadır. Elde edilen bilgiler, yatırım stratejileri için kullanılabilecektir.

## Proje Adımları

### 1. Veri Toplama
- **Kullanılacak Araçlar:** `yfinance`, `investpy`, `quandl`
- 2005-01-01 tarihinden itibaren aylık getirilere sahip hisse senetleri ve sektör verileri toplanacak.
- Web scraping teknikleri ile hisse senedi ve sektör listeleri elde edilecek.

### 2. Veri Ön İşleme
- Eksik veriler ortalama, medyan veya forward/backward fill yöntemleriyle doldurulacak.
- Zaman serisi verileri üzerinde log dönüşümü, fark alma (differencing) gibi dönüşümler uygulanacak.
- Kategorik değişkenler (`one-hot encoding`, `label encoding`) ile sayısal hale getirilecek.
- Veriler, `StandardScaler` veya `MinMaxScaler` ile ölçeklendirilecek.

### 3. Öznitelik Çıkarımı ve Seçme
- **Kullanılacak Araç:** `tsfresh`
- Zaman serisi verilerinden ortalama, standart sapma, otokorelasyon gibi istatistiksel özellikler çıkarılacak.
- L1 regularization (Lasso), Recursive Feature Elimination (RFE) veya Principal Component Analysis (PCA) ile en önemli özellikler seçilecek.

### 4. Model Geliştirme
- **Kullanılacak Modeller:** `Random Forest`, `Gradient Boosting`, `XGBoost`
- **Hiperparametre Optimizasyonu:** `Grid Search`, `Bayesian Optimization`
- **Doğrulama:** Cross-validation yöntemleri uygulanacak.

### 5. Model Değerlendirme
- **Performans Metrikleri:** `Accuracy`, `F1-score`, `ROC-AUC`
- Modelin performansı backtesting ile de test edilebilir (opsiyonel).

### 6. Sektörel Benzerlik Analizi
- Bir hisse senedinin hangi sektöre daha çok benzediği tespit edilecek.
- Örneğin, Real-Estate sektöründeki hisse senetlerinin benzerlikleri analiz edilecek.

### 7. Faktör Hesaplama ve İleri Analiz (Opsiyonel)
- **Finansal Faktörler:** Momentum, volatilite, RSI, MACD hesaplanacak.
- Modelin performansı bu faktörler üzerinden test edilecek.

### 8. Sonuçların Görselleştirilmesi ve Raporlama
- **Görselleştirme Araçları:** `Matplotlib`, `Seaborn`, `Plotly`
- Zaman serisi grafikleri, sektörel benzerlik matrisleri ve model performans metrikleri sunulacak.
- Proje raporu detaylı olarak hazırlanacak.

## Beklenen Çıktılar
- Hisse senetlerinin sektörel benzerliklerini gösteren bir sınıflandırma modeli.
- Farklı sektörlerdeki hisse senetlerinin davranışlarını analiz eden bir rapor.
- Yatırım stratejileri için sektörel benzerlik bilgisi.

## Kullanılacak Araçlar ve Teknolojiler
- **Programlama Dili:** Python
- **Kütüphaneler:** `yfinance`, `investpy`, `quandl`, `tsfresh`, `scikit-learn`, `XGBoost`, `CatBoost`, `Matplotlib`, `Seaborn`, `Plotly`
- **Veri Kaynakları:** Borsa verileri, sektörel endeksler, finansal API'ler
