import json
import datetime
from enum import Enum, unique, Flag

class Raci(Flag):
    """
    A list of people showing who is
    * Responsible
    * Accountable
    * Consulted
    * Informed
    """
    RESPONSIBLE = 1
    ACCOUNTABLE = 2
    CONSULTED = 4
    INFORMED = 8


class ReadyList:
    """
    A node in a ReadyList graph.
    """
    def __init__(self, name, state, valid_to, raci=None, items=None):
        self.name = name
        self.state = state
        self.valid_to = valid_to
        self.raci = raci if raci is not None else {}
        self.items = items if items is not None else []

    def greet(self, name: str) -> str:
        """Return a greeting message for the given name."""
        return f"I'm {name}!"

    def __str__(self):
        return f"ReadyList(name='{self.name}', state='{self.state}', valid_to={self.valid_to}, raci={self.raci}, items={self.items})"

    @classmethod
    def from_string(cls, string):
        root = json.loads(string)
        return cls(name, state, valid_to, items)
