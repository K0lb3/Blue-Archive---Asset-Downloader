# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class BGM_GlobalExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BGM_GlobalExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsBGM_GlobalExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # BGM_GlobalExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # BGM_GlobalExcel
    def GroupBGMId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # BGM_GlobalExcel
    def BGMIdKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # BGM_GlobalExcel
    def BGMIdJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # BGM_GlobalExcel
    def BGMIdTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # BGM_GlobalExcel
    def BGMIdTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # BGM_GlobalExcel
    def BGMIdEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # BGM_GlobalExcel
    def BGMIdDe(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # BGM_GlobalExcel
    def BGMIdFr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(8)
def BGM_GlobalExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddGroupBGMId(builder, GroupBGMId): builder.PrependInt64Slot(0, GroupBGMId, 0)
def BGM_GlobalExcelAddGroupBGMId(builder, GroupBGMId):
    """This method is deprecated. Please switch to AddGroupBGMId."""
    return AddGroupBGMId(builder, GroupBGMId)
def AddBGMIdKr(builder, BGMIdKr): builder.PrependInt64Slot(1, BGMIdKr, 0)
def BGM_GlobalExcelAddBGMIdKr(builder, BGMIdKr):
    """This method is deprecated. Please switch to AddBGMIdKr."""
    return AddBGMIdKr(builder, BGMIdKr)
def AddBGMIdJp(builder, BGMIdJp): builder.PrependInt64Slot(2, BGMIdJp, 0)
def BGM_GlobalExcelAddBGMIdJp(builder, BGMIdJp):
    """This method is deprecated. Please switch to AddBGMIdJp."""
    return AddBGMIdJp(builder, BGMIdJp)
def AddBGMIdTh(builder, BGMIdTh): builder.PrependInt64Slot(3, BGMIdTh, 0)
def BGM_GlobalExcelAddBGMIdTh(builder, BGMIdTh):
    """This method is deprecated. Please switch to AddBGMIdTh."""
    return AddBGMIdTh(builder, BGMIdTh)
def AddBGMIdTw(builder, BGMIdTw): builder.PrependInt64Slot(4, BGMIdTw, 0)
def BGM_GlobalExcelAddBGMIdTw(builder, BGMIdTw):
    """This method is deprecated. Please switch to AddBGMIdTw."""
    return AddBGMIdTw(builder, BGMIdTw)
def AddBGMIdEn(builder, BGMIdEn): builder.PrependInt64Slot(5, BGMIdEn, 0)
def BGM_GlobalExcelAddBGMIdEn(builder, BGMIdEn):
    """This method is deprecated. Please switch to AddBGMIdEn."""
    return AddBGMIdEn(builder, BGMIdEn)
def AddBGMIdDe(builder, BGMIdDe): builder.PrependInt64Slot(6, BGMIdDe, 0)
def BGM_GlobalExcelAddBGMIdDe(builder, BGMIdDe):
    """This method is deprecated. Please switch to AddBGMIdDe."""
    return AddBGMIdDe(builder, BGMIdDe)
def AddBGMIdFr(builder, BGMIdFr): builder.PrependInt64Slot(7, BGMIdFr, 0)
def BGM_GlobalExcelAddBGMIdFr(builder, BGMIdFr):
    """This method is deprecated. Please switch to AddBGMIdFr."""
    return AddBGMIdFr(builder, BGMIdFr)
def End(builder): return builder.EndObject()
def BGM_GlobalExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)