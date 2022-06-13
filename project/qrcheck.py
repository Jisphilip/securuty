# import cv2
# # Name of the QR Code Image file
# filename = "static/test.jpg"
# # read the QRCODE image
# image = cv2.imread(filename)
# # initialize the cv2 QRCode detector
# detector = cv2.QRCodeDetector()
# # detect and decode
# data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
# # if there is a QR code
# # print the data
# if vertices_array is not None:
#   print(data)
# else:
#   print("There was some error") 


import cv2
img=cv2.imread("static/qrcode/34c2653c-ea80-40c2-911c-33aaadaac18d.png")
det=cv2.QRCodeDetector()
val, pts, st_code=det.detectAndDecode(img)
print(val)