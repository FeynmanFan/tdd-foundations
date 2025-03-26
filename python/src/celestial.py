import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.spectra import SpectraComparator

class CelestialObject:
    def __init__(self, spectra):
        self.spectra = spectra
    
    def is_star(self):
        spectraComparator = SpectraComparator()

        return not spectraComparator.isSolar(self.spectra)