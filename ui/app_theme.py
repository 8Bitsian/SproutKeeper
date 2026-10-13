# Standard-library imports
from pathlib import Path

# Third-party imports
from PyQt6.QtCore import QFile, QIODevice, QTextStream
from PyQt6.QtGui import QFontDatabase

# Global variables
BASE_DIR = Path(__file__).resolve().parent.parent

# Geneated colors from https://coolors.co/cbdd7e-261c15-f7f7f2-e4e6c3-44744a
COLORS = {
  "COFFEE_BEAN": "261C15",
  "CREEPER": "533F4A",
  "FERN": "44744A",
  "CREAM": "CBDD7E",
  "BEIGE": "E4E6C3",
  "PORCELIAN": "F7F7F2",
}

def load_fonts():
  """Loads the application fonts"""
  font_dir = BASE_DIR / "resources" / "fonts"

  for font_path in font_dir.glob("*.ttf"):
    font_id = QFontDatabase.addApplicationFont(str(font_path))
    if font_id == -1:
      print(f"Could not load font: {font_path}")
      
def load_stylesheet(app,filepath):
  """Loads the QSS stylesheet"""
  if file_path is None:
    file_path = BASE_DIR / "resources" / "qss" / "styles.qss"
    
  file = QFile(str(filepath))
  mode = QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text
  
  if not file.open(mode):
    print(f"Could not load stylesheet: {filepath}")
    return

  try:
    style_sheet = QTextStream(file).readAll()
  finally:
    file.close()

  for color_name, hex_color in COLORS.items():
    style_sheet = style_sheet.replace(f"{{{{{color_name}}}}}", hex_color)

  app.setStyleSheet(style_sheet)
