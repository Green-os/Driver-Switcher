# Driver-Switcher (TR)

Bu basit Python betiği, belirli bir grafik sürücüsü ile bir komutu çalıştırmak için DRI_PRIME çevresel değişkenini kullanır.
Bu, laptoplarda Optimus veya benzeri grafik geçiş teknolojileri bulunan kullanıcılar için kullanışlıdır.

## Kullanım

### 1. Gereksinimler
- Python yüklü olmalıdır.
- Harici sürücülerin doğru bir şekilde yüklü olduğundan emin olun.

### 2. Kodu İndirme
```bash
git clone 
cd Driver-Switcher/
```
### 3. Kodu çalıştırma
```bash
python3 App_starterpy
```

### 4. Sürücü Seçimi
- Program, kullanılacak sürücü numarasını soracaktır (örneğin, "0" Intel, "1" AMD).
- Yanlış bir sürücü numarası girdiğinizde hata alırsınız.
- Kendi sürücü numaralarınızı girebilirsiniz.

### 5. Komut Girişi
- Ardından, çalıştırmak istediğiniz komutu girin.

### 6. Sonuçlar
- Her şey doğruysa, komut belirtilen sürücüyle çalıştırılır.
- Bir hata oluşursa, hata mesajı görüntülenir.

## Örnek
```bash
Sürücüleri seçin:
0 - Intel HD Graphics
1 - AMD Radeon
Seçiminiz (0 veya 1): 0

Komutunuzu giriniz: glxinfo | grep "OpenGL version"
```
Bu örnekte, Intel HD Graphics sürücüsüyle "glxinfo | grep "OpenGL version"" komutu çalıştırılır.

### Hata Durumları
- Yanlış sürücü numarası veya uyumsuz komut girişi durumunda hata mesajları alırsınız.

### Katkılar
- Her türlü katkıya açığız. Hataları bildirin, önerilerde bulunun veya pull talepleri gönderin.


# Driver-Switcher (EN)

This simple Python script utilizes the DRI_PRIME environmental variable to run a command with a specific graphics driver. It is useful for users with laptops featuring technologies like Optimus, allowing them to switch between graphics drivers.

## Usage

### 1. Requirements
- Python must be installed.
- Ensure that the necessary external drivers are correctly installed.


### 2. Download the Code
```bash
git clone 
cd Driver-Switcher/
```


### 3. Run the Code
```bash
python3 App_starter.py
```


### 4. Driver Selection
- The program will prompt you to choose the driver number (e.g., "0" for Intel, "1" for AMD).
- If you enter an incorrect driver number, you will receive an error.
- You can input your own driver numbers.
### 5. Command Input
- Enter the command you want to run.


### 6. Results
-If everything is correct, the command will be executed with the specified driver.
-If an error occurs, an error message will be displayed.


## Example
```bash
Choose the driver:
0 - Intel HD Graphics
1 - AMD Radeon
Your choice (0 or 1): 0

Enter your command: glxinfo | grep "OpenGL version"
```
- In this example, the "glxinfo | grep "OpenGL version"" command will be executed with the Intel HD Graphics driver.


### Error Cases
- If you input an incorrect driver number or an incompatible command, you will receive error messages.


### Contributions
- We welcome any contributions. Report errors, provide suggestions, or submit pull requests.
