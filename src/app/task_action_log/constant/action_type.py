from enum import Enum, unique


@unique
class ActionType(Enum):
    UPDATE = "UPDATE"
    DELETE = "DELETE"
