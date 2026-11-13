from .celestial_object import CelestialObject

class Sun(CelestialObject):
    """ Implements the Sun class.

    """

    def __init__(self, mass, name, luminosity):
        """
        Constructor method.
        """
        super().__init__(mass, name)
        self.luminosity = luminosity

    def __str__(self):
        text = "This sun is called " + self.name
        text += "\nMass: %.2f A.U." % self.mass
        # TODO: add units for luminosity
        text += "\nLuminosity: %.2f" % self.luminosity

        return text

