import PyPDF2 
import pyttsx3 


path = open('./Btech 3rd year syllabus.pdf', 'rb') 


pdfReader = PyPDF2.PdfFileReader(path) 


from_page = pdfReader.getPage(10) 

text = from_page.extractText() 

 
speak = pyttsx3.init() 
speak.say(text) 
speak.runAndWait() 
