class SpectraComparator:
    # ATTENTION! All this code is physics nonsense

    SOLAR_SPECTRA = [100, 200, 300]

    def isSolar(self, spectra):
        if len(spectra) != len(self.SOLAR_SPECTRA):
            return False
        
        return spectra == self.SOLAR_SPECTRA

    def hasAbsorptionLines(self, spectra):
        # Absorption lines might be indicated by a significant dip (decrease) in intensity
        return spectra[1] < spectra[0] or spectra[2] < spectra[1]
    
    def isEmissionDominant(self, spectra): 
        # Emission dominant means intensity increases across the spectrum
        return spectra[0] < spectra[1] and spectra[2] > spectra[0]

    def hasGasSignature(self, spectra):
        # Gas signature requires a specific peak in the middle (e.g., H-alpha line)
        return spectra[1] > spectra[0] and spectra[1] > spectra[2]