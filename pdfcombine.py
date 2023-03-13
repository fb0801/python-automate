import PyPDF2
import sys
import os


for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        print(file)
        merger = PyPDF2.PdfFileMerger()
        merger.append(file)
        merger.write("combined.pdf")
    else:
        print("Sorry file not accepted")