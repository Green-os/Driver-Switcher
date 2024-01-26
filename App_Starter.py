import subprocess

def run_command_with_dri_prime(driver_index, command):
    try:
        # Sürücü numarası doğrulama
        if driver_index not in [0, 1]:
            raise ValueError("Bilinmeyen sürücü numarası.0 numara Intel HD Graphics 520 veya 1 numara AMD Radeon R5 M330.")

        # Girilen komutları "DRI_PRIME" sürücü numarası ile çalıştırılıyor
        subprocess.run(f'DRI_PRIME={driver_index} {command}', shell=True, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Komut bu hata ile iptal edildi: {e}")
    except ValueError as ve:
        print(f"Sürücü hatası: {ve}")
    except Exception as e:
        print(f"Beklenmeyen bir hata ile karşılaşıldı: {e}")

if __name__ == "__main__":
    try:
        # Kullanıcıdan kullanılmak istenen sürücü numarası alımı
        DRI = int(input("Sürücüleri seçin (0 = Intel HD Graphics 520, 1 = AMD Radeon R5 M330): "))
        
        # Yanlış giriş
        if DRI not in [0, 1]:
            raise ValueError("Bilinmeyen giriş. Lütfen 0 veya 1 giriniz")

        command = input("Komutunuzu giriniz: ")

        # Girilen komutu "DRI_PRIME" sürücü numarası ile çalıştırılıyor
        run_command_with_dri_prime(DRI, command)

    except ValueError as ve:
        print(f"Bilinmeyen giriş: {ve}")
    except KeyboardInterrupt:
        print("\nİşlem kullanıcı tarafından iptal edildi.")
    except Exception as e:
        print(f"Bilinmeyen bir hata ile karşılaşıldı {e}")
