from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io
import re

def pdf2txt_file(inPDFfile,outTXTfile):
    inFile=open(inPDFfile,'rb')
    resMgr=PDFResourceManager()
    retData=io.StringIO()
    TxtConverter=TextConverter(resMgr,retData,laparams=LAParams())
    Interpreter=PDFPageInterpreter(resMgr,TxtConverter)

    for page in PDFPage.get_pages(inFile):
        Interpreter.process_page(page)

    txt=retData.getvalue()
    text=re.sub(r"^\s+", "", txt)
    with open(outTXTfile,'w',encoding='utf-8') as f:
        f.write(text)
    return text
    
def pdf2txt(inPDFfile):
    inFile=open(inPDFfile,'rb')
    resMgr=PDFResourceManager()
    retData=io.StringIO()
    TxtConverter=TextConverter(resMgr,retData,laparams=LAParams())
    Interpreter=PDFPageInterpreter(resMgr,TxtConverter)

    for page in PDFPage.get_pages(inFile):
        Interpreter.process_page(page)

    txt=retData.getvalue()
    text=re.sub(r"^\s+", "", txt)
    return text

# pdf2txt_file('anantapoudel.pdf','sample_input.txt')
