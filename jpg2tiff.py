import aspose.words as aw

doc = aw.Document()
builder = aw.DocumentBuilder(doc)

shape = builder.insert_image("mask_6_3.jpg")
shape.image_data.save("mask_6_3.tiff")