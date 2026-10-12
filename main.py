# Standard-library imports
import sys

# Third-party imports
from PyQt6.QtWidgets import QApplication

# Local libary imports
from ui.app_theme import load_fonts, load_stylesheet
from ui.windows.main_window import MainWindow

def main():
  """Runs the main program"""
  app = QApplication(sys.argv)

  load_fonts()
  load_stylesheet(app)
  
  window = MainWindow()
  window.show()

  sys.exit(app.exec__())

if __name__ == "__main__":
  print(f"Running {__name__}\n")
  main()
  print("Program finished.")
