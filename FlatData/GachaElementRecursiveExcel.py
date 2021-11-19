# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class GachaElementRecursiveExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GachaElementRecursiveExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsGachaElementRecursiveExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # GachaElementRecursiveExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GachaElementRecursiveExcel
    def ID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # GachaElementRecursiveExcel
    def GachaGroupID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # GachaElementRecursiveExcel
    def ParcelType_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GachaElementRecursiveExcel
    def ParcelID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # GachaElementRecursiveExcel
    def ParcelAmountMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GachaElementRecursiveExcel
    def ParcelAmountMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GachaElementRecursiveExcel
    def Prob(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GachaElementRecursiveExcel
    def State(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(8)
def GachaElementRecursiveExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddID(builder, ID): builder.PrependInt64Slot(0, ID, 0)
def GachaElementRecursiveExcelAddID(builder, ID):
    """This method is deprecated. Please switch to AddID."""
    return AddID(builder, ID)
def AddGachaGroupID(builder, GachaGroupID): builder.PrependInt64Slot(1, GachaGroupID, 0)
def GachaElementRecursiveExcelAddGachaGroupID(builder, GachaGroupID):
    """This method is deprecated. Please switch to AddGachaGroupID."""
    return AddGachaGroupID(builder, GachaGroupID)
def AddParcelType_(builder, ParcelType_): builder.PrependInt32Slot(2, ParcelType_, 0)
def GachaElementRecursiveExcelAddParcelType_(builder, ParcelType_):
    """This method is deprecated. Please switch to AddParcelType_."""
    return AddParcelType_(builder, ParcelType_)
def AddParcelID(builder, ParcelID): builder.PrependInt64Slot(3, ParcelID, 0)
def GachaElementRecursiveExcelAddParcelID(builder, ParcelID):
    """This method is deprecated. Please switch to AddParcelID."""
    return AddParcelID(builder, ParcelID)
def AddParcelAmountMin(builder, ParcelAmountMin): builder.PrependInt32Slot(4, ParcelAmountMin, 0)
def GachaElementRecursiveExcelAddParcelAmountMin(builder, ParcelAmountMin):
    """This method is deprecated. Please switch to AddParcelAmountMin."""
    return AddParcelAmountMin(builder, ParcelAmountMin)
def AddParcelAmountMax(builder, ParcelAmountMax): builder.PrependInt32Slot(5, ParcelAmountMax, 0)
def GachaElementRecursiveExcelAddParcelAmountMax(builder, ParcelAmountMax):
    """This method is deprecated. Please switch to AddParcelAmountMax."""
    return AddParcelAmountMax(builder, ParcelAmountMax)
def AddProb(builder, Prob): builder.PrependInt32Slot(6, Prob, 0)
def GachaElementRecursiveExcelAddProb(builder, Prob):
    """This method is deprecated. Please switch to AddProb."""
    return AddProb(builder, Prob)
def AddState(builder, State): builder.PrependInt32Slot(7, State, 0)
def GachaElementRecursiveExcelAddState(builder, State):
    """This method is deprecated. Please switch to AddState."""
    return AddState(builder, State)
def End(builder): return builder.EndObject()
def GachaElementRecursiveExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)