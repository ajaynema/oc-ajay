from resource import Resource
class PhysicalResource(Resource) :
    def __init__(self):
        super.__init__()
        self.manufactureDate = None
        self.powerState = None
        self.serialNumber = None
        self.versionNumber = None
