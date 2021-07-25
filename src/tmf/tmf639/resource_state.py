from enum import Enum

class ResourceState(Enum):
    Planning = "Planning"
    Installing = "Installing"
    Operating ="Operating"
    Retiring = "Retiring"