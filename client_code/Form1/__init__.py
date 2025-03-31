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


  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    self.item['my_text'] = self.text_box_1.text.strip().lower()
    typer = {
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
    'blå Kongo': 'mjölig',
    'cecile': 'fast',
    'violet queen': 'ganska fast',
    'early puritan': 'lite mjölig',
    'estelle': 'fast',
    'magda': 'fast',
    'maria': 'fast',
    'marilyn': 'fast',
    'rocket': 'fast',
    'rosara': 'fast',
    'solist': 'fast',
    'swift': 'fast',
    'timo': 'fast',
    'kuk': 'sak som kanske intresserar dig. Men det är då fan inte en',
    'jazzy': 'fast'
}
# Kollar om potatisen finns i listan och skriver ut typen
    if self.item['my_text'] in typer:
      alert (f"{self.item['my_text'].capitalize()} är en {typer[self.item['my_text']]} potatis.")
    else:
      alert("Antingen har du stavat fel, eller så finns inte potatisen i databasen just nu. Kan också vara så att det är något fel i programmets kod som inte fungerar som det ska.")