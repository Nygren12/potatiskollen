import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def potatis_pressed_enter('input')
# # Lista med potatisar
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
    'färskpotatis': 'färsk',
    'primörpotatis': 'färsk',
    'timo': 'fast',
    'jazzy': 'fast'
}

# Kollar om potatisen finns i listan och skriver ut typen
if str(potatis) in potatis_typer:
    anvil.print(f"{potatis.capitalize()} räknas som en {potatis_typer[potatis]} potatis.")
else:
    anvil.print("Antingen har du stavat fel, ditt miffo. Eller så finns inte potatisen i databasen just nu.")