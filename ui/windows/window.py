# Project: SproutKeeper
# Description:

# Standard-library imports
from pathlib import Path

# Third-party or local library imports
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget
from services.plant_care import PlantService
from ui.buttons import create_buttons
from ui.layouts import create_main_layout

# Runs the main window
class MainWindow(QMainWindow):
  # Initialization Method
  def __init__(self):
    super().__init__()
    
    # Stylize title of application
    self.setWindowTitle("SproutKeeper")
    self.resize(900, 600)

    pass
