class CelestialObject:
    def __init__(self, name, emits_light=False):
        self.name = name
        self.emits_light = emits_light
    
    def is_star(self):
        return self.emits_light