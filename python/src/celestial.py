import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.spectra import SpectraComparator

class CelestialObject:
    def __init__(self, spectra):
        self.spectra = spectra

    def is_Sol(self):
        return self.spectra == SpectraComparator.SOLAR_SPECTRA
    
    def is_star(self):
        spectraComparator = SpectraComparator()

        return (spectraComparator.isEmissionDominant(self.spectra) and
                not spectraComparator.hasAbsorptionLines(self.spectra) and
                not spectraComparator.hasGasSignature(self.spectra)
                )
    
    def is_planet(self):
        spectraComparator = SpectraComparator()
        # Planets typically show reflected stellar spectra with atmospheric absorption
        return (spectraComparator.hasAbsorptionLines(self.spectra) and 
                not spectraComparator.isEmissionDominant(self.spectra))
    
    def is_nebula(self):
        spectraComparator = SpectraComparator()
        # Nebulae typically show strong emission lines
        return (spectraComparator.isEmissionDominant(self.spectra) and 
                spectraComparator.hasGasSignature(self.spectra))