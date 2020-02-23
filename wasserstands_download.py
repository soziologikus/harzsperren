import schedule
import time
import os
import datetime
import PyPDF2
from datetime import date


def download_pdf():
    #Herunterladen der pdf-Datei von den Harzer Wasserwerken
    os.system("wget http://talis.harzwasserwerke.de/talsperren/talis/hochwasserdaten.pdf")
    print(str(datetime.datetime.now()) + " -- pdf-Datei heruntergeladen.")

def delete_pdf():
    #Nachdem die Daten aus der pdf-Datei ausgelesen werden muss ich die pdf-Datei löschen.
    os.system("rm hochwasserdaten.pdf")
    print(str(datetime.datetime.now()) + " -- pdf-Datei gelöscht.")

def move_pdf():
    # Statt die pdf zu löschen kann man sie auch in einen Ordner schieben und umbenenen.
    # Dann kann ich die Dtaen im Nachhinein kontrollieren
    today = date.today()
    os.system("mv hochwasserdaten.pdf archiv/hochwasserdaten_" + str(today) + ".pdf")

def read_pdf_write_csv():
    #Öffnen der Datei - der Modus "rb" öffnet die Datei als binary file
    pdf_file = open("hochwasserdaten.pdf", "rb")

    #Was folgt ist eine Reihe von Befehlen um am ende eine Stringvariable "page_content" mit dem Textinhalt der pdf zu bekommen
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    str(page_content)
    
    #Jetzt erstelle ich eine Listenvariable "split_page_content", in der jede Zeile ein String-Listeneintrag ist
    split_page_content = page_content.splitlines()

    #Auslesen der Daten aus der Listenvariable
    datum = split_page_content[8]

    oder = datum + ";" + split_page_content[24] + ";" + split_page_content[27] + ";" + split_page_content[28] + ";" + split_page_content[29] + ";" + split_page_content[30]
    soese = datum + ";" + split_page_content[31] + ";" + split_page_content[34] + ";" + split_page_content[35] + ";" + split_page_content[36] + ";" + split_page_content[37]
    ecker = datum + ";" + split_page_content[38] + ";" + split_page_content[41] + ";" + split_page_content[42] + ";" + split_page_content[43] + ";" + split_page_content[44]
    oker = datum + ";" + split_page_content[45] + ";" + split_page_content[48] + ";" + split_page_content[49] + ";" + split_page_content[50] + ";" + split_page_content[51]
    grane = datum + ";" + split_page_content[52] + ";" + split_page_content[55] + ";" + split_page_content[56] + ";" + split_page_content[57] + ";" + split_page_content[58]
    innerste = datum + ";" + split_page_content[59] + ";" + split_page_content[62] + ";" + split_page_content[63] + ";" + split_page_content[64] + ";" + split_page_content[65]

    #Jetzt füge ich alle ausgelesenen strings in eine Stringvariable namens "zeile"
    zeile = oder + "\n" + soese + "\n" + ecker + "\n" + oker + "\n" + grane + "\n" + innerste + "\n"
    print(str(datetime.datetime.now()) + " -- Daten aus der pdf-Datei ausgelesen.")
    
    #Jetzt schreibe ich die Daten in eine csv-Datei
    csv_datei = open("harzer_wasserstaende.csv", "a")
    csv_datei.write(zeile)
    csv_datei.close()
    print(str(datetime.datetime.now()) + " -- csv-Datei geschrieben.")

def build_and_write_jpeg():
    os.system("Rscript auswertung.R")
    os.system("mv oder_plot.jpg soese_plot.jpg ecker_plot.jpg oker_plot.jpg grane_plot.jpg innerste_plot.jpg /var/www/html/img/")
       


schedule.every().day.at("11:02").do(download_pdf)
schedule.every().day.at("11:04").do(read_pdf_write_csv)
schedule.every().day.at("11:06").do(move_pdf)
schedule.every().day.at("11:08").do(build_and_write_jpeg)

while True:
    schedule.run_pending()
    time.sleep(1)
