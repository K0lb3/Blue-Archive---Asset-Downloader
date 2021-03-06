# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FavorLevelExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FavorLevelExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsFavorLevelExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # FavorLevelExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FavorLevelExcel
    def Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FavorLevelExcel
    def ExpType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # FavorLevelExcel
    def ExpTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # FavorLevelExcel
    def ExpTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # FavorLevelExcel
    def ExpTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def Start(builder): builder.StartObject(2)
def FavorLevelExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddLevel(builder, Level): builder.PrependInt64Slot(0, Level, 0)
def FavorLevelExcelAddLevel(builder, Level):
    """This method is deprecated. Please switch to AddLevel."""
    return AddLevel(builder, Level)
def AddExpType(builder, ExpType): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(ExpType), 0)
def FavorLevelExcelAddExpType(builder, ExpType):
    """This method is deprecated. Please switch to AddExpType."""
    return AddExpType(builder, ExpType)
def StartExpTypeVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def FavorLevelExcelStartExpTypeVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartExpTypeVector(builder, numElems)
def End(builder): return builder.EndObject()
def FavorLevelExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)