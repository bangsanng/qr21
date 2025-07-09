import qrcode

# 이 주소는 Render에서 배포한 주소로 바꿔주세요!
url = "https://qr-attendance-1-2wje.onrender.com"

# QR 생성
img = qrcode.make(url)
img.save("attendance_qr.png")

print("QR 코드 생성 완료!")
