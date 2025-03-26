class SpectraComparator:
    SOLAR_SPECTRA = [100, 200, 300]

    def isSolar(self, spectra):
        if len(spectra) != len(self.SOLAR_SPECTRA):
            return False
        
        return spectra == self.SOLAR_SPECTRA
