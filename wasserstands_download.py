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

    #Herstellen einzelner Strings mit den entsprechenden Daten aus der pdf-Datei
    oder = datum + ";" + split_page_content[split_page_content.index("Oder")] + ";" + split_page_content[split_page_content.index("Oder")+3] + ";" + split_page_content[split_page_content.index("Oder")+4] + ";" + split_page_content[split_page_content.index("Oder")+5] + ";" + split_page_content[split_page_content.index("Oder")+6]
    soese = datum + ";" + split_page_content[split_page_content.index("Söse")] + ";" + split_page_content[split_page_content.index("Söse")+3] + ";" + split_page_content[split_page_content.index("Söse")+4] + ";" + split_page_content[split_page_content.index("Söse")+5] + ";" + split_page_content[split_page_content.index("Söse")+6]
    ecker = datum + ";" + split_page_content[split_page_content.index("Ecker")] + ";" + split_page_content[split_page_content.index("Ecker")+3] + ";" + split_page_content[split_page_content.index("Ecker")+4] + ";" + split_page_content[split_page_content.index("Ecker")+5] + ";" + split_page_content[split_page_content.index("Ecker")+6]
    oker = datum + ";" + split_page_content[split_page_content.index("Oker")] + ";" + split_page_content[split_page_content.index("Oker")+3] + ";" + split_page_content[split_page_content.index("Oker")+4] + ";" + split_page_content[split_page_content.index("Oker")+5] + ";" + split_page_content[split_page_content.index("Oker")+6]
    grane = datum + ";" + split_page_content[split_page_content.index("Grane")] + ";" + split_page_content[split_page_content.index("Grane")+3] + ";" + split_page_content[split_page_content.index("Grane")+4] + ";" + split_page_content[split_page_content.index("Grane")+5] + ";" + split_page_content[split_page_content.index("Grane")+6]
    innerste = datum + ";" + split_page_content[split_page_content.index("Innerste")] + ";" + split_page_content[split_page_content.index("Innerste")+3] + ";" + split_page_content[split_page_content.index("Innerste")+4] + ";" + split_page_content[split_page_content.index("Innerste")+5] + ";" + split_page_content[split_page_content.index("Innerste")+6]

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
