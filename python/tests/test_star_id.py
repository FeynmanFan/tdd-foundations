import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.celestial import CelestialObject

def test_sirius_is_star():
    sirius = CelestialObject("Sirius", emits_light=True)
    assert sirius.is_star() == True