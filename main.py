# Project: SproutKeeper Application
# File: main.py

# Standard-library imports
import sys, os

# Third-party or local library imports
from PyQt5.QtWidgets import Application
from PyQt5.QtCore import QFile, QtextStream
from ui.window import MainWindow

# Runs the main program
def main():
  # Ensure the app can find resources relative to the main.py file
  base_dir = os.path.dirname(os.path.abspath(__file__))
  os.chdir(base_dir)
  
  app = QApplication(sys.argv)

  window = ManWindow()
  window.show()

  sys.exit(app.exec__())

if __name__ == "__main__":
  print(f"Running {__name__}\n")
  main()
  print("Program finished.")
