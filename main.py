import qrcode
from os import system as sy
while True:
    sy("cls")
    print("- - - - - Crie seu QRCode gratuitamente - - - - - ")
    link = str(input(" Cole seu link aqui: "))
    qr = qrcode.QRCode(
        version=1,  # 1 a 40 (define o tamanho)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # L, M, Q, H (nível de correção de erro)
        box_size=10,  # Tamanho de cada "quadradinho"
        border=4,  # Quantidade de caixas de margem
    )

    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode_exemplo.png")
    break