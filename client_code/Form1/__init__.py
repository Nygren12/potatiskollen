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

  def potatis_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

def potatis_pressed_enter(self, **event_args):
  anvil.server.call('send_feedback', potatis).show()