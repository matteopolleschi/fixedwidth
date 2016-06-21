"""
The ImppnLine class definition.
"""

from fixedwidth.fixedwidth import FixedWidth
from copy import deepcopy

IMPPN_CONFIG = {

    "first_name": {
        "required": True,
        "type": "string",
        "start_pos": 1,
        "end_pos": 10,
        "alignment": "left",
        "padding": " "
    },

    "last_name": {
        "required": True,
        "type": "string",
        "start_pos": 11,
        "end_pos": 30,
        "alignment": "left",
        "padding": " "
    },

    "nickname": {
        "required": False,
        "type": "string",
        "start_pos": 31,
        "length": 15,
        "alignment": "left",
        "padding": " "
    },

    "age": {
        "type": "integer",
        "alignment": "right",
        "start_pos": 46,
        "padding": "0",
        "length": 3,
        "required": True
    },

    "meal": {
        "type": "string",
        "start_pos": 49,
        "default": "no preference",
        "padding": " ",
        "end_pos": 68,
        "length": 20,
        "alignment": "left",
        "required": False
    }

}

def imppn_line():
    """
Imppn line
    """
    imppn_config = deepcopy(IMPPN_CONFIG)
    imppn_obj = FixedWidth(imppn_config)
    imppn_obj.update(last_name="Smith", first_name="Michael",
        age=32, meal="vegetarian"
    )
    return imppn_obj.line

if __name__ == "__main__":
    print imppn_line()