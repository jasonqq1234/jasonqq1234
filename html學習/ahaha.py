import qrcode
import os

# 創建存放QR碼的資料夾
folder_name = "QRCODE"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# 生成並保存QR碼
start_number = 3131313131
end_number = 1655255
num_of_qr_codes = 15
step = (end_number - start_number) // (num_of_qr_codes - 1)

for i in range(start_number, end_number + 1, step):
    # 生成QR碼
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(i)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # 保存QR碼圖像
    file_path = os.path.join(folder_name, f"qr_{i}.png")
    img.save(file_path)

print(f"已生成{num_of_qr_codes}個QR碼，數字範圍從{start_number}到{end_number}。")
