Çanakkale Onsekiz Mart Üniversitesi Bilgisayar Mühendisliği 4. Sınıf Bilgi Erişim Sistemleri Örnek Projesi
Geliştirme Yönlendirmeleri
#### Client uygulaması'nın development süreci için (Client Application - Vue);

cd .\src\client\

#Peketlerin yüklenmesi
npm install

#Uygulamanın development modda çalıştırılması
npm run dev


#### Backend uygulaması'nın development süreci için(Backend Application - Python);
cd .\src\
#python virtual environment oluşturulacak
python -m venv comu
.\comu\Scripts\activate

#proje içine girilerek gerekli python paketleri install edilmeli
cd .\backend\
pip install -r requirements.txt


#uygulamanın local ortamda ayağa kaldırılması
uvicorn main:app --host 0.0.0.0 --port 8080


#api test
curl http://localhost:8080/samples/testtt




Uygulamanın ayağa kaldırılması(Docker Desktop)
Bu aşamada tüm uygulamalar uçtan uca birileri ile çalışır halede hazır olacaklardır.
cd .\src\
#Derleme
docker compose -f dockercompose.yaml build

#Çalıştırılması
docker compose -f dockercompose.yaml up


Uygulama ayağa kalktığında docker desktop üstünden ayağa kalkan pod'lar running statüye geçecektir.


Notlar
#### 25.12.2023
Derste yapılan client uygulamasının yeri client klasörünün altına taşındı
Client uygulaması stil hataları düzeltildi


Ödev
MongoDB üstünde full text search için gerekli index oluşturulmalı. Oluşturulacak index Apache Lucene analyzer'larından olmalı. Token ve Weight düzenlemeleri yüklenen örneğe göre redesign edilmeli.