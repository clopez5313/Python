class Point():
    def __init__(self, name, latitude, longitude):
        self._name = name
        self._latitude = latitude
        self._longitude = longitude

    def getLatLong(self):
        return(self._latitude, self._longitude)
