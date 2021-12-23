class Node:
    def __init__(self, id: int, location: tuple = None):
        self.id = id
        self.location = location
        self.tag = 0
        self.weight = 0

    def getId(self):
        self.id
    def __lt__(self, obj):
        """self < obj."""
        return self.weight < obj.weight

    def __le__(self, obj):
        """self <= obj."""
        return self.weight <= obj.weight

    def __eq__(self, obj):
        """self == obj."""
        return self.weight == obj.weight

    def __ne__(self, obj):
        """self != obj."""
        return self.weight != obj.weight

    def __gt__(self, obj):
        """self > obj."""
        return self.weight > obj.weight

    def __ge__(self, obj):
        """self >= obj."""
        return self.weight >= obj.weight
