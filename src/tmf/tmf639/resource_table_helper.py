import sys, os.path

sys.path.append("./../../")
sys.path.append("./../")

from db.db_table_helper import DbTableHelper
from resource_inventory_db_constants import ResourceInventoryDbConstants

class ResourceTableHelper(DbTableHelper):
    def __init__(self):
        super.__init__(ResourceInventoryDbConstants.DB_RESOURCE_INVENTORY,ResourceInventoryDbConstants.TABLE_RESOURCE)
