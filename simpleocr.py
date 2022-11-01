import easyocr as ocr  #OCR

reader = ocr.Reader(['en'],model_storage_directory='/models')

result = reader.readtext("outliers.jpeg")

for text in result:
    print(text[1])