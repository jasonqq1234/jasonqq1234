import cv2
import pygame

def play_sound(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

def scan_qr_code():
    # 初始化攝像頭
    cap = cv2.VideoCapture(1)  # 根據你的設備，可能需要更改編號
    
    # 創建一個QRCodeDetector物件
    detector = cv2.QRCodeDetector()

    while True:
        # 讀取當前幀
        ret, img = cap.read()
        if not ret:
            print("無法獲取影像幀，請檢查攝像頭。")
            break

        # 檢測QR碼
        data, bbox, _ = detector.detectAndDecode(img)

        if bbox is not None and data:
            print(f"'{data}',")  # 打印掃描結果
            
            # 檢查掃描結果
            if data in ['1119390203',
'1342937195',
'1566484187',
'1790031179',
'2013578171',
'2237125163',
'225202235',
'2460672155',
'2684219147',
'2907766139',
'3131313131',
'672296219',
'895843211',
]:
                result_text = "Pass"
                play_sound("77.mp3")  # 播放音效
            else:
                result_text = "Didn't pass"
                play_sound("88.mp3")  # 播放音效
            
            # 顯示結果
            cv2.putText(img, f"Scan result: {data} - {result_text}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("QR Code Scanner", img)
            cv2.waitKey(2000)  # 暫停2秒

        else:
            # 如果沒有掃描到QR碼，則正常顯示攝像頭畫面
            cv2.imshow("QR Code Scanner", img)

        # 等待用戶按下任意按鍵或關閉視窗
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    # 釋放攝像頭資源並關閉所有窗口
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    pygame.init()  # 初始化pygame
    scan_qr_code()