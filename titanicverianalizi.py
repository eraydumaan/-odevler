import pandas as pd
import os


file_path = "C:/Users/erayd/OneDrive/Masaüstü/python egitimi/train.csv"


if not os.path.exists(file_path):
    print("HATA: Dosya bulunamadi! Lutfen dosya yolunu ve adini kontrol edin.")
else:
    
    data = pd.read_csv(file_path)

    
    print("Veri setinin ilk 5 satiri:")
    print(data.head())

    
    print("\nVeri seti bilgileri:")
    print(data.info())

   
    print("\nEksik degerlerin sayisi:")
    print(data.isnull().sum())

    
    print("\nİstatistiksel ozet:")
    print(data.describe())

    
    print("\nVeri setinin boyutu:")
    print(data.shape)

    
    print("\nVeri setinin sutun isimleri:")
    print(data.columns)

    
    print("\nEksik degerlerin oranlari (%):")
    print(data.isnull().mean() * 100)

    
    print("\nVeri setinin son 5 satiri:")
    print(data.tail())

    
    print("\nVeri setinin ortalama yas degeri:")
    print(data["Age"].mean())

    
    print("\nVeri setinin en yuksek yas degeri:")
    print(data["Age"].max())

    
    print("\nVeri setinin en kucuk yas degeri:")
    print(data["Age"].min())

    
    print("\nToplam yolcu sayisi:")
    print(data["PassengerId"].count())

    
    print("\nBirinci sinif yolcu sayisi:")
    print(data[data["Pclass"] == 1]["PassengerId"].count())

    
    print("\nFarkli sinif yolcu sayilari:")
    print(data["Pclass"].value_counts())

    
    print("\nLokasyon bilgileri:")
    print(data["Embarked"].value_counts())

    
    print("\nTicket fiyatlarinin ortalamasi:")
    print(data["Fare"].mean())

  
    print("\nTicket fiyatlarinin en yuksek degeri:")
    print(data["Fare"].max())

    
    print("\nTicket fiyatlarinin en kucuk degeri:")
    print(data["Fare"].min())

    
    print("\nPassengerId sutunundaki benzersiz degerler:")
    print(data["PassengerId"].unique())

  
    print("\nPassengerId sütunundaki benzersiz değerlerin sayisi:")
    print(data["PassengerId"].nunique())

  
    print("\nParch bilgisi:")
    print(data["Parch"].value_counts())

    print("\ncabin farkli olan yolcu sayisi:")
    print(data["Cabin"].nunique())
