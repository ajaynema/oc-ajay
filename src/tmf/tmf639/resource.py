class Resource:
    def __init__(self):
        self.id=None
        self.href=None
        self.publicIdentifier=None
        self.description=None
        self.category=None
        self.validFor = None
        self.name = None
        self.lifecycleState = None
        #Indicates the (class) type of resource. For physical resource this will be ‘Equipment’, For logical Resource this can be 'Resource Function', 'MSISDN', 'IP Address'.
        self.type = None
        self.baseType = None
        self.schemaLocation = None
        self.version = None
        self.resourceRelationship = None #Place[]
        self.place = None #[]
        self.note = None #Note[]
        self.resourceSpecification = None   
        self.relatedParty = None #RelatedPartyRef[]
        self.resorceCharacteristic = None #ResourceCharacteristic[]
        self.resourceAttachment = None #ResorceAttachment[]
