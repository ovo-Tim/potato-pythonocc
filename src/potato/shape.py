from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.AIS import AIS_Shape
from OCC.Core.gp import gp_Pnt

import time

class potato_shape():
    def __init__(self, pos=(0,0,0), size) -> None:
        self._size = size
        self._pos = pos

        self._ais_shape = None

        self.build()
    
    def update_shape(self):
        self._shape = self.box.Shape()

        self._ais_shape.SetShape(self._shape)

    def Shape(self):
        self.update_shape()
        return self._shape

    def AIS_Shape(self):
        self.update_shape()
        return self._ais_shape
    
    def SetSize(self, size: tuple):
        self._size = size
        self.build()

    def SetPos(self, pos: tuple):
        self._pos = pos
        self.build()

class potato_box(potato_shape):
    def __init__(self, pos=(0, 0, 0), size=(15, 15, 15)) -> None:
        super().__init__(pos, size)

    def build(self):
        self.box = BRepPrimAPI_MakeBox(gp_Pnt(*self._pos), *self._size)
        if self._ais_shape is None:
            self._ais_shape = AIS_Shape(self.box.Shape())
        self.update_shape()

    
