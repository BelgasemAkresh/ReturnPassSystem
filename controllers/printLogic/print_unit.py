from controllers.printLogic.pdf_printer import PDF_Printer
from model.kontakt import Kontakt
import yaml
import os


class Print_Unit:
    def __init__(self, kontakt, printer):
        self.kontakt: Kontakt = kontakt
        self.printer: PDF_Printer = printer

    def print(self):

        if self.kontakt is not None:

            with open('config.yaml', 'r', encoding='utf-8') as file:
                config = yaml.safe_load(file)

            pic = config.get('pic', {})
            self.printer.print_pic(
                self.kontakt.image_data,
                pic.get('x', 0),
                pic.get('y', 0),
                pic.get('x_scale', 1),
                pic.get('y_scale', 1)
            )


            #self.printer.print_pic(self.kontakt.image_data, 62, 24, 19, 22)
            # Liste der Felder mit Positionen aus der YAML-Datei
            keys = ['visaNumber', 'visaArt', 'vorname', 'nachname', 'passport', 'profession',
                    'visaIss', 'visaValid', 'duration', 'entriesNumber', 'work', "note", "entryFee", "port"]

            l = []
            for key in keys:
                pos = config.get(key)
                if pos and 'x' in pos and 'y' in pos:
                    l.append([key, (pos['x'], pos['y'])])

            print(l)
            for i in l:
                print(i,str(self.kontakt[i[0]]), i[1][0], i[1][1])
                self.printer.print_text(str(self.kontakt[i[0]]), i[1][0], i[1][1])

            #self.printer.print_text(  str(self.kontakt["port"]), 155, 26 )

            #self.printer.print_text(str(self.kontakt["note"]), 155, 14)

            #beispiel für einfache funktion
            #self.printer.print_text("التوقيع و الختم", 100, 15)

            #self.printer.print_text(str(self.kontakt["entryFee"]), 155, 20)


