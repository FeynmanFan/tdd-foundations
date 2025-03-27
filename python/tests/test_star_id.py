import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.celestial import CelestialObject
from src.spectra import SpectraComparator

def test_sirius_is_star():
    sirius = CelestialObject(spectra=[300, 450, 700])
    assert True == sirius.is_star()

def test_spectra_is_sol():
    # arrange
    spectra = [100, 200, 300]
    spectraComparator = SpectraComparator()

    # act
    result = spectraComparator.isSolar(spectra)

    # assert
    assert True == result

def test_spectra_is_not_sol():
    # arrange 
    spectra = [300, 450, 700]
    spectraComparator = SpectraComparator()

    #act
    result = spectraComparator.isSolar(spectra)

    #assert
    assert False == result

def test_spectra_is_nebula():
    # arrange
    spectra = [100, 700, 200]
    cel = CelestialObject(spectra=spectra)

    # act
    result = cel.is_nebula()

    # assert
    assert True == result