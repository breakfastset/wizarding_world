class Wizard:
    """Represent a Wizard object"""

    def __init__(self, name, age, level, magical_points):
        """Initialize the Wizard object"""
        self.name = name
        self.age = age
        self.level = level
        self.magical_points = magical_points

    def cast(self, spell_points):
        """Cast spells depending on the magical points"""
        if self.magical_points <= spell_points:  # False if not enough magical points to cast
            return False
        else:
            self.magical_points -= spell_points  # Update magical Points when spell is cast
            return True

    def __str__(self):
        """Return a String Representation of the Wizard object"""
        message = "The Wizard's Name is {}, whose age is {} years. " \
                  "Current level of the Wizard is {}. " \
                  "Woah {} magical Points!".format(self.name, self.age, self.level, self.magical_points)
        return message
