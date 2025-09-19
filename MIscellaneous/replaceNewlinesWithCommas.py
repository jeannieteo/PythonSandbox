with open("C:\\Users\\User\\Downloads\\test.txt", "r") as fileR:
    s = fileR.read()
    cleaned_text = s.replace("\n", ",")
with open("C:\\Users\\User\Downloads\\testComma.txt", "w") as fileW:
    fileW.write(cleaned_text)