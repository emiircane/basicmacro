import keyboard
import time

def main():
    print("'e' tuşunu otomatik olarak basıyorum...")
    print("Durdurmak için ESC tuşuna basın")
    
    while True:
        if keyboard.is_pressed('esc'):
            print("Program sonlandırıldı.")
            break
            
        # 'e' tuşuna bas
        keyboard.press_and_release('e')
        
        # Kısa bir süre bekle
        time.sleep(0.1)  # Bu değeri değiştirerek basma sıklığını ayarlayabilirsiniz

if __name__ == "__main__":
    # Kullanıcıya programı başlatmadan önce hazırlanma süresi
    print("3 saniye içinde program başlayacak, klavyeyi kullanacağınız yere odaklanın...")
    time.sleep(3)
    main() 