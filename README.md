# E Tuşu Makrosu

Bu uygulama, klavyenizdeki 'e' tuşuna otomatik olarak basan basit bir makrodur.

## Kullanım Seçenekleri

### 1. Exe Dosyası (Önerilen) - Hiçbir Şey İndirmeniz Gerekmez!

- `dist` klasöründeki `e_takibi.exe` dosyasını çalıştırmanız yeterlidir
- Herhangi bir kurulum veya Python yüklemenize gerek yoktur
- Çalıştırdıktan sonra 3 saniyelik süre içinde makronun çalışmasını istediğiniz pencereye tıklayın
- Durdurmak için ESC tuşuna basın

### 2. Python Kullanarak

Python ile çalıştırmak için gereksinimler:

```
pip install keyboard
```

Kullanım:

1. Programı çalıştırın: `python e_takibi.py`
2. 3 saniyelik süre içinde e tuşunun basılmasını istediğiniz alana odaklanın (metin düzenleyici, not defteri vb.)
3. Program 'e' tuşuna otomatik olarak basmaya başlayacak
4. Durdurmak için ESC tuşuna basın

## Özellikler

- Otomatik olarak 'e' tuşuna basar
- ESC tuşu ile kolayca durdurulabilir
- Başlamadan önce 3 saniyelik hazırlık süresi
- Basma hızı ayarlanabilir

## Ayarlamalar

Kodda şu değişiklikleri yaparak makroyu özelleştirebilirsiniz:

- Basma hızını değiştirmek: `time.sleep(0.1)` değerini düzenleyin (daha küçük değer = daha hızlı)
- Farklı bir tuşa basmak: `keyboard.press_and_release('e')` kodundaki 'e' harfini değiştirin

## Not

- Windows Güvenlik Uyarısı alabilirsiniz, bu normal bir durumdur çünkü uygulama klavye kontrolü kullanıyor
- Güvenilir bir kaynaktan aldığınıza emin olduğunuz uygulamalara izin vermeniz önerilir 