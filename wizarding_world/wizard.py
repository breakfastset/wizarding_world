class Wizard:
    """Represent a Wizard object"""

    def __init__(self, name, age, level, magPt):
        """Initialize the Wizard object"""
        self.name = name
        self.age = age
        self.level = level
        self.magPt = magPt

    def cast(self, spellPoints):
        """Cast spells depending on the magical points"""
        if self.magPt <= spellPoints:  # False if not enough magical points to cast
            return False
        else:
            self.magPt -= spellPoints  # Update magical Points when spell is cast
            return True

    def __str__(self):
        """Return a String Representation of the Wizard object"""
        message = "The Wizard's Name is {}, whose age is {} years. " \
                  "Current level of the Wizard is {}. " \
                  "Woah {} magical Points!".format(self.name, self.age, self.level, self.magPt)
        return message
