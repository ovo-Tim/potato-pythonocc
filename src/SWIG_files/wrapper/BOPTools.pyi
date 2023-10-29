from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.IntTools import *
from OCC.Core.gp import *
from OCC.Core.TopAbs import *
from OCC.Core.TopTools import *
from OCC.Core.Message import *
from OCC.Core.Geom import *
from OCC.Core.Geom2d import *
from OCC.Core.BRepAdaptor import *

# the following typedef cannot be wrapped as is
BOPTools_Box2dPairSelector = NewType("BOPTools_Box2dPairSelector", Any)
# the following typedef cannot be wrapped as is
BOPTools_Box2dTree = NewType("BOPTools_Box2dTree", Any)
# the following typedef cannot be wrapped as is
BOPTools_Box2dTreeSelector = NewType("BOPTools_Box2dTreeSelector", Any)
# the following typedef cannot be wrapped as is
BOPTools_BoxPairSelector = NewType("BOPTools_BoxPairSelector", Any)
# the following typedef cannot be wrapped as is
BOPTools_BoxTree = NewType("BOPTools_BoxTree", Any)
# the following typedef cannot be wrapped as is
BOPTools_BoxTreeSelector = NewType("BOPTools_BoxTreeSelector", Any)
# the following typedef cannot be wrapped as is
BOPTools_IndexedDataMapOfSetShape = NewType("BOPTools_IndexedDataMapOfSetShape", Any)
# the following typedef cannot be wrapped as is
BOPTools_ListIteratorOfListOfConnexityBlock = NewType("BOPTools_ListIteratorOfListOfConnexityBlock", Any)
# the following typedef cannot be wrapped as is
BOPTools_ListIteratorOfListOfCoupleOfShape = NewType("BOPTools_ListIteratorOfListOfCoupleOfShape", Any)
# the following typedef cannot be wrapped as is
BOPTools_MapIteratorOfMapOfSet = NewType("BOPTools_MapIteratorOfMapOfSet", Any)
# the following typedef cannot be wrapped as is
BOPTools_MapOfSet = NewType("BOPTools_MapOfSet", Any)

class BOPTools_ListOfConnexityBlock:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> BOPTools_ConnexityBlock: ...
    def Last(self) -> BOPTools_ConnexityBlock: ...
    def Append(self, theItem: BOPTools_ConnexityBlock) -> BOPTools_ConnexityBlock: ...
    def Prepend(self, theItem: BOPTools_ConnexityBlock) -> BOPTools_ConnexityBlock: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> BOPTools_ConnexityBlock: ...
    def SetValue(self, theIndex: int, theValue: BOPTools_ConnexityBlock) -> None: ...

class BOPTools_ListOfCoupleOfShape:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> BOPTools_CoupleOfShape: ...
    def Last(self) -> BOPTools_CoupleOfShape: ...
    def Append(self, theItem: BOPTools_CoupleOfShape) -> BOPTools_CoupleOfShape: ...
    def Prepend(self, theItem: BOPTools_CoupleOfShape) -> BOPTools_CoupleOfShape: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> BOPTools_CoupleOfShape: ...
    def SetValue(self, theIndex: int, theValue: BOPTools_CoupleOfShape) -> None: ...

class BOPTools_AlgoTools:
    @staticmethod
    def AreFacesSameDomain(theF1: TopoDS_Face, theF2: TopoDS_Face, theContext: IntTools_Context, theFuzz: Optional[float] = Precision.Confusion()) -> bool: ...
    @overload
    @staticmethod
    def ComputeState(thePoint: gp_Pnt, theSolid: TopoDS_Solid, theTol: float, theContext: IntTools_Context) -> TopAbs_State: ...
    @overload
    @staticmethod
    def ComputeState(theVertex: TopoDS_Vertex, theSolid: TopoDS_Solid, theTol: float, theContext: IntTools_Context) -> TopAbs_State: ...
    @overload
    @staticmethod
    def ComputeState(theEdge: TopoDS_Edge, theSolid: TopoDS_Solid, theTol: float, theContext: IntTools_Context) -> TopAbs_State: ...
    @overload
    @staticmethod
    def ComputeState(theFace: TopoDS_Face, theSolid: TopoDS_Solid, theTol: float, theBounds: TopTools_IndexedMapOfShape, theContext: IntTools_Context) -> TopAbs_State: ...
    @staticmethod
    def ComputeStateByOnePoint(theShape: TopoDS_Shape, theSolid: TopoDS_Solid, theTol: float, theContext: IntTools_Context) -> TopAbs_State: ...
    @staticmethod
    def ComputeTolerance(theFace: TopoDS_Face, theEdge: TopoDS_Edge) -> Tuple[bool, float, float]: ...
    @overload
    @staticmethod
    def ComputeVV(theV: TopoDS_Vertex, theP: gp_Pnt, theTolP: float) -> int: ...
    @overload
    @staticmethod
    def ComputeVV(theV1: TopoDS_Vertex, theV2: TopoDS_Vertex, theFuzz: Optional[float] = Precision.Confusion()) -> int: ...
    @staticmethod
    def CopyEdge(theEdge: TopoDS_Edge) -> TopoDS_Edge: ...
    @staticmethod
    def CorrectCurveOnSurface(theS: TopoDS_Shape, theMapToAvoid: TopTools_IndexedMapOfShape, theTolMax: Optional[float] = 0.0001, theRunParallel: Optional[bool] = False) -> None: ...
    @staticmethod
    def CorrectPointOnCurve(theS: TopoDS_Shape, theMapToAvoid: TopTools_IndexedMapOfShape, theTolMax: Optional[float] = 0.0001, theRunParallel: Optional[bool] = False) -> None: ...
    @overload
    @staticmethod
    def CorrectRange(aE1: TopoDS_Edge, aE2: TopoDS_Edge, aSR: IntTools_Range, aNewSR: IntTools_Range) -> None: ...
    @overload
    @staticmethod
    def CorrectRange(aE: TopoDS_Edge, aF: TopoDS_Face, aSR: IntTools_Range, aNewSR: IntTools_Range) -> None: ...
    @staticmethod
    def CorrectShapeTolerances(theS: TopoDS_Shape, theMapToAvoid: TopTools_IndexedMapOfShape, theRunParallel: Optional[bool] = False) -> None: ...
    @staticmethod
    def CorrectTolerances(theS: TopoDS_Shape, theMapToAvoid: TopTools_IndexedMapOfShape, theTolMax: Optional[float] = 0.0001, theRunParallel: Optional[bool] = False) -> None: ...
    @staticmethod
    def DTolerance() -> float: ...
    @staticmethod
    def Dimension(theS: TopoDS_Shape) -> int: ...
    @staticmethod
    def Dimensions(theS: TopoDS_Shape) -> Tuple[int, int]: ...
    @staticmethod
    def GetEdgeOff(theEdge: TopoDS_Edge, theFace: TopoDS_Face, theEdgeOff: TopoDS_Edge) -> bool: ...
    @staticmethod
    def GetEdgeOnFace(theEdge: TopoDS_Edge, theFace: TopoDS_Face, theEdgeOnF: TopoDS_Edge) -> bool: ...
    @staticmethod
    def GetFaceOff(theEdge: TopoDS_Edge, theFace: TopoDS_Face, theLCEF: BOPTools_ListOfCoupleOfShape, theFaceOff: TopoDS_Face, theContext: IntTools_Context) -> bool: ...
    @staticmethod
    def IsBlockInOnFace(aShR: IntTools_Range, aF: TopoDS_Face, aE: TopoDS_Edge, aContext: IntTools_Context) -> bool: ...
    @staticmethod
    def IsHole(theW: TopoDS_Shape, theF: TopoDS_Shape) -> bool: ...
    @overload
    @staticmethod
    def IsInternalFace(theFace: TopoDS_Face, theEdge: TopoDS_Edge, theFace1: TopoDS_Face, theFace2: TopoDS_Face, theContext: IntTools_Context) -> int: ...
    @overload
    @staticmethod
    def IsInternalFace(theFace: TopoDS_Face, theEdge: TopoDS_Edge, theLF: TopTools_ListOfShape, theContext: IntTools_Context) -> int: ...
    @overload
    @staticmethod
    def IsInternalFace(theFace: TopoDS_Face, theSolid: TopoDS_Solid, theMEF: TopTools_IndexedDataMapOfShapeListOfShape, theTol: float, theContext: IntTools_Context) -> bool: ...
    @staticmethod
    def IsInvertedSolid(theSolid: TopoDS_Solid) -> bool: ...
    @staticmethod
    def IsMicroEdge(theEdge: TopoDS_Edge, theContext: IntTools_Context, theCheckSplittable: Optional[bool] = True) -> bool: ...
    @staticmethod
    def IsOpenShell(theShell: TopoDS_Shell) -> bool: ...
    @overload
    @staticmethod
    def IsSplitToReverse(theSplit: TopoDS_Shape, theShape: TopoDS_Shape, theContext: IntTools_Context, theError: Optional[int] = None) -> bool: ...
    @overload
    @staticmethod
    def IsSplitToReverse(theSplit: TopoDS_Face, theShape: TopoDS_Face, theContext: IntTools_Context, theError: Optional[int] = None) -> bool: ...
    @overload
    @staticmethod
    def IsSplitToReverse(theSplit: TopoDS_Edge, theShape: TopoDS_Edge, theContext: IntTools_Context, theError: Optional[int] = None) -> bool: ...
    @staticmethod
    def IsSplitToReverseWithWarn(theSplit: TopoDS_Shape, theShape: TopoDS_Shape, theContext: IntTools_Context, theReport: Optional[Message_Report] = None) -> bool: ...
    @staticmethod
    def MakeConnexityBlock(theLS: TopTools_ListOfShape, theMapAvoid: TopTools_IndexedMapOfShape, theLSCB: TopTools_ListOfShape, theAllocator: NCollection_BaseAllocator) -> None: ...
    @overload
    @staticmethod
    def MakeConnexityBlocks(theS: TopoDS_Shape, theConnectionType: TopAbs_ShapeEnum, theElementType: TopAbs_ShapeEnum, theLCB: TopTools_ListOfShape) -> None: ...
    @overload
    @staticmethod
    def MakeConnexityBlocks(theS: TopoDS_Shape, theConnectionType: TopAbs_ShapeEnum, theElementType: TopAbs_ShapeEnum, theLCB: TopTools_ListOfListOfShape, theConnectionMap: TopTools_IndexedDataMapOfShapeListOfShape) -> None: ...
    @overload
    @staticmethod
    def MakeConnexityBlocks(theLS: TopTools_ListOfShape, theConnectionType: TopAbs_ShapeEnum, theElementType: TopAbs_ShapeEnum, theLCB: BOPTools_ListOfConnexityBlock) -> None: ...
    @staticmethod
    def MakeContainer(theType: TopAbs_ShapeEnum, theShape: TopoDS_Shape) -> None: ...
    @staticmethod
    def MakeEdge(theCurve: IntTools_Curve, theV1: TopoDS_Vertex, theT1: float, theV2: TopoDS_Vertex, theT2: float, theTolR3D: float, theE: TopoDS_Edge) -> None: ...
    @overload
    @staticmethod
    def MakeNewVertex(aP1: gp_Pnt, aTol: float, aNewVertex: TopoDS_Vertex) -> None: ...
    @overload
    @staticmethod
    def MakeNewVertex(aV1: TopoDS_Vertex, aV2: TopoDS_Vertex, aNewVertex: TopoDS_Vertex) -> None: ...
    @overload
    @staticmethod
    def MakeNewVertex(aE1: TopoDS_Edge, aP1: float, aE2: TopoDS_Edge, aP2: float, aNewVertex: TopoDS_Vertex) -> None: ...
    @overload
    @staticmethod
    def MakeNewVertex(aE1: TopoDS_Edge, aP1: float, aF2: TopoDS_Face, aNewVertex: TopoDS_Vertex) -> None: ...
    @staticmethod
    def MakePCurve(theE: TopoDS_Edge, theF1: TopoDS_Face, theF2: TopoDS_Face, theCurve: IntTools_Curve, thePC1: bool, thePC2: bool, theContext: Optional[IntTools_Context] = IntTools_Context()) -> None: ...
    @staticmethod
    def MakeSectEdge(aIC: IntTools_Curve, aV1: TopoDS_Vertex, aP1: float, aV2: TopoDS_Vertex, aP2: float, aNewEdge: TopoDS_Edge) -> None: ...
    @staticmethod
    def MakeSplitEdge(aE1: TopoDS_Edge, aV1: TopoDS_Vertex, aP1: float, aV2: TopoDS_Vertex, aP2: float, aNewEdge: TopoDS_Edge) -> None: ...
    @staticmethod
    def MakeVertex(theLV: TopTools_ListOfShape, theV: TopoDS_Vertex) -> None: ...
    @staticmethod
    def OrientEdgesOnWire(theWire: TopoDS_Shape) -> None: ...
    @staticmethod
    def OrientFacesOnShell(theShell: TopoDS_Shape) -> None: ...
    @staticmethod
    def PointOnEdge(aEdge: TopoDS_Edge, aPrm: float, aP: gp_Pnt) -> None: ...
    @staticmethod
    def Sense(theF1: TopoDS_Face, theF2: TopoDS_Face, theContext: IntTools_Context) -> int: ...
    @staticmethod
    def TreatCompound(theS: TopoDS_Shape, theList: TopTools_ListOfShape, theMap: Optional[TopTools_MapOfShape] = None) -> None: ...
    @overload
    @staticmethod
    def UpdateVertex(aIC: IntTools_Curve, aT: float, aV: TopoDS_Vertex) -> None: ...
    @overload
    @staticmethod
    def UpdateVertex(aE: TopoDS_Edge, aT: float, aV: TopoDS_Vertex) -> None: ...
    @overload
    @staticmethod
    def UpdateVertex(aVF: TopoDS_Vertex, aVN: TopoDS_Vertex) -> None: ...

class BOPTools_AlgoTools2D:
    @overload
    @staticmethod
    def AdjustPCurveOnFace(theF: TopoDS_Face, theC3D: Geom_Curve, theC2D: Geom2d_Curve, theC2DA: Geom2d_Curve, theContext: Optional[IntTools_Context] = IntTools_Context()) -> None: ...
    @overload
    @staticmethod
    def AdjustPCurveOnFace(theF: TopoDS_Face, theFirst: float, theLast: float, theC2D: Geom2d_Curve, theC2DA: Geom2d_Curve, theContext: Optional[IntTools_Context] = IntTools_Context()) -> None: ...
    @staticmethod
    def AdjustPCurveOnSurf(aF: BRepAdaptor_Surface, aT1: float, aT2: float, aC2D: Geom2d_Curve, aC2DA: Geom2d_Curve) -> None: ...
    @staticmethod
    def AttachExistingPCurve(aEold: TopoDS_Edge, aEnew: TopoDS_Edge, aF: TopoDS_Face, aCtx: IntTools_Context) -> int: ...
    @staticmethod
    def BuildPCurveForEdgeOnFace(aE: TopoDS_Edge, aF: TopoDS_Face, theContext: Optional[IntTools_Context] = IntTools_Context()) -> None: ...
    @overload
    @staticmethod
    def CurveOnSurface(aE: TopoDS_Edge, aF: TopoDS_Face, aC: Geom2d_Curve, theContext: Optional[IntTools_Context] = IntTools_Context()) -> float: ...
    @overload
    @staticmethod
    def CurveOnSurface(aE: TopoDS_Edge, aF: TopoDS_Face, aC: Geom2d_Curve, theContext: Optional[IntTools_Context] = IntTools_Context()) -> Tuple[float, float, float]: ...
    @staticmethod
    def EdgeTangent(anE: TopoDS_Edge, aT: float, Tau: gp_Vec) -> bool: ...
    @overload
    @staticmethod
    def HasCurveOnSurface(aE: TopoDS_Edge, aF: TopoDS_Face, aC: Geom2d_Curve) -> Tuple[bool, float, float, float]: ...
    @overload
    @staticmethod
    def HasCurveOnSurface(aE: TopoDS_Edge, aF: TopoDS_Face) -> bool: ...
    @overload
    @staticmethod
    def IntermediatePoint(aFirst: float, aLast: float) -> float: ...
    @overload
    @staticmethod
    def IntermediatePoint(anE: TopoDS_Edge) -> float: ...
    @staticmethod
    def IsEdgeIsoline(theE: TopoDS_Edge, theF: TopoDS_Face) -> Tuple[bool, bool]: ...
    @staticmethod
    def Make2D(aE: TopoDS_Edge, aF: TopoDS_Face, aC: Geom2d_Curve, theContext: Optional[IntTools_Context] = IntTools_Context()) -> Tuple[float, float, float]: ...
    @overload
    @staticmethod
    def MakePCurveOnFace(aF: TopoDS_Face, C3D: Geom_Curve, aC: Geom2d_Curve, theContext: Optional[IntTools_Context] = IntTools_Context()) -> float: ...
    @overload
    @staticmethod
    def MakePCurveOnFace(aF: TopoDS_Face, C3D: Geom_Curve, aT1: float, aT2: float, aC: Geom2d_Curve, theContext: Optional[IntTools_Context] = IntTools_Context()) -> float: ...
    @staticmethod
    def PointOnSurface(aE: TopoDS_Edge, aF: TopoDS_Face, aT: float, theContext: Optional[IntTools_Context] = IntTools_Context()) -> Tuple[float, float]: ...

class BOPTools_AlgoTools3D:
    @overload
    @staticmethod
    def DoSplitSEAMOnFace(theESplit: TopoDS_Edge, theFace: TopoDS_Face) -> bool: ...
    @overload
    @staticmethod
    def DoSplitSEAMOnFace(theEOrigin: TopoDS_Edge, theESplit: TopoDS_Edge, theFace: TopoDS_Face) -> bool: ...
    @overload
    @staticmethod
    def GetApproxNormalToFaceOnEdge(aE: TopoDS_Edge, aF: TopoDS_Face, aT: float, aPx: gp_Pnt, aD: gp_Dir, theContext: IntTools_Context) -> bool: ...
    @overload
    @staticmethod
    def GetApproxNormalToFaceOnEdge(theE: TopoDS_Edge, theF: TopoDS_Face, aT: float, aP: gp_Pnt, aDNF: gp_Dir, aDt2D: float) -> bool: ...
    @overload
    @staticmethod
    def GetApproxNormalToFaceOnEdge(theE: TopoDS_Edge, theF: TopoDS_Face, aT: float, aDt2D: float, aP: gp_Pnt, aDNF: gp_Dir, theContext: IntTools_Context) -> bool: ...
    @overload
    @staticmethod
    def GetNormalToFaceOnEdge(aE: TopoDS_Edge, aF: TopoDS_Face, aT: float, aD: gp_Dir, theContext: Optional[IntTools_Context] = IntTools_Context()) -> None: ...
    @overload
    @staticmethod
    def GetNormalToFaceOnEdge(aE: TopoDS_Edge, aF: TopoDS_Face, aD: gp_Dir, theContext: Optional[IntTools_Context] = IntTools_Context()) -> None: ...
    @staticmethod
    def GetNormalToSurface(aS: Geom_Surface, U: float, V: float, aD: gp_Dir) -> bool: ...
    @staticmethod
    def IsEmptyShape(aS: TopoDS_Shape) -> bool: ...
    @staticmethod
    def MinStepIn2d() -> float: ...
    @staticmethod
    def OrientEdgeOnFace(aE: TopoDS_Edge, aF: TopoDS_Face, aER: TopoDS_Edge) -> None: ...
    @overload
    @staticmethod
    def PointInFace(theF: TopoDS_Face, theP: gp_Pnt, theP2D: gp_Pnt2d, theContext: IntTools_Context) -> int: ...
    @overload
    @staticmethod
    def PointInFace(theF: TopoDS_Face, theE: TopoDS_Edge, theT: float, theDt2D: float, theP: gp_Pnt, theP2D: gp_Pnt2d, theContext: IntTools_Context) -> int: ...
    @overload
    @staticmethod
    def PointInFace(theF: TopoDS_Face, theL: Geom2d_Curve, theP: gp_Pnt, theP2D: gp_Pnt2d, theContext: IntTools_Context, theDt2D: Optional[float] = 0.0) -> int: ...
    @overload
    @staticmethod
    def PointNearEdge(aE: TopoDS_Edge, aF: TopoDS_Face, aT: float, aDt2D: float, aP2D: gp_Pnt2d, aPx: gp_Pnt, theContext: IntTools_Context) -> int: ...
    @overload
    @staticmethod
    def PointNearEdge(aE: TopoDS_Edge, aF: TopoDS_Face, aT: float, aDt2D: float, aP2D: gp_Pnt2d, aPx: gp_Pnt) -> int: ...
    @overload
    @staticmethod
    def PointNearEdge(aE: TopoDS_Edge, aF: TopoDS_Face, aT: float, aP2D: gp_Pnt2d, aPx: gp_Pnt, theContext: IntTools_Context) -> int: ...
    @overload
    @staticmethod
    def PointNearEdge(aE: TopoDS_Edge, aF: TopoDS_Face, aP2D: gp_Pnt2d, aPx: gp_Pnt, theContext: IntTools_Context) -> int: ...
    @staticmethod
    def SenseFlag(aNF1: gp_Dir, aNF2: gp_Dir) -> int: ...

class BOPTools_ConnexityBlock:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...
    def ChangeLoops(self) -> TopTools_ListOfShape: ...
    def ChangeShapes(self) -> TopTools_ListOfShape: ...
    def IsRegular(self) -> bool: ...
    def Loops(self) -> TopTools_ListOfShape: ...
    def SetRegular(self, theFlag: bool) -> None: ...
    def Shapes(self) -> TopTools_ListOfShape: ...

class BOPTools_CoupleOfShape:
    def __init__(self) -> None: ...
    def SetShape1(self, theShape: TopoDS_Shape) -> None: ...
    def SetShape2(self, theShape: TopoDS_Shape) -> None: ...
    def Shape1(self) -> TopoDS_Shape: ...
    def Shape2(self) -> TopoDS_Shape: ...

class BOPTools_Set:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self, theOther: BOPTools_Set) -> None: ...
    def Add(self, theS: TopoDS_Shape, theType: TopAbs_ShapeEnum) -> None: ...
    def Assign(self, Other: BOPTools_Set) -> BOPTools_Set: ...
    def HashCode(self, theUpperBound: int) -> int: ...
    def IsEqual(self, aOther: BOPTools_Set) -> bool: ...
    def NbShapes(self) -> int: ...
    def Shape(self) -> TopoDS_Shape: ...

class BOPTools_SetMapHasher:
    @staticmethod
    def HashCode(theSet: BOPTools_Set, theUpperBound: int) -> int: ...
    @staticmethod
    def IsEqual(aSet1: BOPTools_Set, aSet2: BOPTools_Set) -> bool: ...

#classnotwrapped
class BOPTools_Parallel: ...

#classnotwrapped
class BOPTools_BoxSelector: ...

#classnotwrapped
class BOPTools_BoxSet: ...

#classnotwrapped
class BOPTools_PairSelector: ...

# harray1 classes
# harray2 classes
# hsequence classes

