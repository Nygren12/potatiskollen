from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def Searchbar_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    pass

  def Search_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    
# Användaren skriver in en potatissort
potatis = input("Vilken potatis har du? ").strip().lower()

    # Lista med potatisar
potatis_typer = {
    'king edward': 'mjölig',
    'bintje': 'mjölig',
    'melody': 'fast',
    'asterix': 'fast',
    'charlotte': 'fast',
    'amandine': 'fast',
    'ratte': 'fast',
    'connect': 'mjölig',
    'fontane': 'mjölig',
    'king edward': 'mjölig',
    'mandel': 'mjölig',
    'matilda': 'mjölig',
    'amadine': 'fast',
    'anya': 'fast',
    'apache': 'fast',
    'asterix': 'fast',
    'ballerina': 'fast',
    'belana': 'fast',
    'cherie': 'fast',
    'folva': 'fast',
    'gala': 'fast',
    'hertha': 'fast',
    'labella': 'fast',
    'linzer delikatesse': 'fast',
    'melody': 'fast',
    'ratte': 'fast',
    'sava': 'fast',
    'sparris': 'fast',
    'blå Kongo': 'färgad',
    'cecile': 'färgad',
    'duble fun': 'färgad',
    'violet queen': 'färgad',
    'early puritan': 'färsk',
    'estelle': 'färsk',
    'magda': 'färsk',
    'maria': 'färsk',
    'marilyn': 'färsk',
    'rocket': 'färsk',
    'rosara': 'färsk',
    'solist': 'färsk',
    'swift': 'färsk',
    'färskpotatis': 'färsk, duuh',
    'primörpotatis': 'färsk',
    'timo': 'fast',
    'jazzy': 'fast'
}

# Kollar om potatisen finns i listan och skriver ut typen
if potatis in potatis_typer:
    print(f"{potatis.capitalize()} räknas som en {potatis_typer[potatis]} potatis.")
else:
    print("Antingen har du stavat fel, ditt miffo. Eller så finns inte potatisen i databasen just nu.")