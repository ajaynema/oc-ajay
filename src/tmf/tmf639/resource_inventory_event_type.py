from enum import Enum

class ResourceInventoryEventType(Enum):
    ResourceCreationNotification = "ResourceCreationNotification"
    ResourceAttributeValueChangeNotification ="ResourceAttributeValueChangeNotification"
    ResourceStateChangeNotification ="ResourceStateChangeNotification"
    ResourceRemoveNotification ="ResourceRemoveNotification"
    
    @staticmethod
    def ResourceTypeCreationNotification(resource_type):
        return resource_type+"CreationNotification"
    
    @staticmethod
    def ResourceTypeAttributeValueChangeNotification(resource_type):
        return resource_type+"AttributeValueChangeNotification"

    @staticmethod
    def ResourceTypeStateChangeNotification(resource_type):
        return resource_type+"StateChangeNotification"
    
    @staticmethod
    def ResourceTypeRemoveNotification(resource_type):
        return resource_type+"RemoveNotification"
    
