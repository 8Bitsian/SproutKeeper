# Project: SproutKeeper
# Description: This is the file for layout managers

# Third-party or local library imports
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QFormLayout, QWidget, QLabel, QLineEdit, QSpinBox

def create_layout():
    """Creates a standardized form layout for adding/editing plants."""
    form_layout = QFormLayout()
    form_layout.setSpacing(15)
    
    name_input = QLineEdit()
    name_input.setPlaceholderText("e.g., Monstera Deliciosa")
    
    species_input = QLineEdit()
    species_input.setPlaceholderText("e.g., Swiss Cheese Plant")
    
    interval_input = QSpinBox()
    interval_input.setRange(1, 365)
    interval_input.setValue(7)
    interval_input.setSuffix(" days")
    
    location_input = QLineEdit()
    location_input.setPlaceholderText("e.g., Living Room Window")
    
    form_layout.addRow(QLabel("Plant Name:"), name_input)
    form_layout.addRow(QLabel("Species:"), species_input)
    form_layout.addRow(QLabel("Water Every:"), interval_input)
    form_layout.addRow(QLabel("Location:"), location_input)
    
    return form_layout, {
        'name': name_input,
        'species': species_input,
        'interval': interval_input,
        'location': location_input
    }
