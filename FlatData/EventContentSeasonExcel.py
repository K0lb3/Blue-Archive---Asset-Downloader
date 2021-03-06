# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EventContentSeasonExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EventContentSeasonExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsEventContentSeasonExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # EventContentSeasonExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EventContentSeasonExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentSeasonExcel
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EventContentSeasonExcel
    def EventContentType_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EventContentSeasonExcel
    def OpenConditionContent_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EventContentSeasonExcel
    def ContentLockType_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EventContentSeasonExcel
    def EventDisplay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # EventContentSeasonExcel
    def EventItemId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentSeasonExcel
    def BeforehandExposedTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EventContentSeasonExcel
    def EventContentOpenTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EventContentSeasonExcel
    def EventContentCloseTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EventContentSeasonExcel
    def ExtensionTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EventContentSeasonExcel
    def MainIconParcelPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EventContentSeasonExcel
    def SubIconParcelPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EventContentSeasonExcel
    def BeforehandBgImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EventContentSeasonExcel
    def MinigamePrologScenarioGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentSeasonExcel
    def BeforehandScenarioGroupId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # EventContentSeasonExcel
    def BeforehandScenarioGroupIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # EventContentSeasonExcel
    def BeforehandScenarioGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventContentSeasonExcel
    def BeforehandScenarioGroupIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        return o == 0

    # EventContentSeasonExcel
    def MainBannerImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EventContentSeasonExcel
    def MainBgImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def Start(builder): builder.StartObject(18)
def EventContentSeasonExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(0, EventContentId, 0)
def EventContentSeasonExcelAddEventContentId(builder, EventContentId):
    """This method is deprecated. Please switch to AddEventContentId."""
    return AddEventContentId(builder, EventContentId)
def AddName(builder, Name): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(Name), 0)
def EventContentSeasonExcelAddName(builder, Name):
    """This method is deprecated. Please switch to AddName."""
    return AddName(builder, Name)
def AddEventContentType_(builder, EventContentType_): builder.PrependInt32Slot(2, EventContentType_, 0)
def EventContentSeasonExcelAddEventContentType_(builder, EventContentType_):
    """This method is deprecated. Please switch to AddEventContentType_."""
    return AddEventContentType_(builder, EventContentType_)
def AddOpenConditionContent_(builder, OpenConditionContent_): builder.PrependInt32Slot(3, OpenConditionContent_, 0)
def EventContentSeasonExcelAddOpenConditionContent_(builder, OpenConditionContent_):
    """This method is deprecated. Please switch to AddOpenConditionContent_."""
    return AddOpenConditionContent_(builder, OpenConditionContent_)
def AddContentLockType_(builder, ContentLockType_): builder.PrependInt32Slot(4, ContentLockType_, 0)
def EventContentSeasonExcelAddContentLockType_(builder, ContentLockType_):
    """This method is deprecated. Please switch to AddContentLockType_."""
    return AddContentLockType_(builder, ContentLockType_)
def AddEventDisplay(builder, EventDisplay): builder.PrependBoolSlot(5, EventDisplay, 0)
def EventContentSeasonExcelAddEventDisplay(builder, EventDisplay):
    """This method is deprecated. Please switch to AddEventDisplay."""
    return AddEventDisplay(builder, EventDisplay)
def AddEventItemId(builder, EventItemId): builder.PrependInt64Slot(6, EventItemId, 0)
def EventContentSeasonExcelAddEventItemId(builder, EventItemId):
    """This method is deprecated. Please switch to AddEventItemId."""
    return AddEventItemId(builder, EventItemId)
def AddBeforehandExposedTime(builder, BeforehandExposedTime): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(BeforehandExposedTime), 0)
def EventContentSeasonExcelAddBeforehandExposedTime(builder, BeforehandExposedTime):
    """This method is deprecated. Please switch to AddBeforehandExposedTime."""
    return AddBeforehandExposedTime(builder, BeforehandExposedTime)
def AddEventContentOpenTime(builder, EventContentOpenTime): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(EventContentOpenTime), 0)
def EventContentSeasonExcelAddEventContentOpenTime(builder, EventContentOpenTime):
    """This method is deprecated. Please switch to AddEventContentOpenTime."""
    return AddEventContentOpenTime(builder, EventContentOpenTime)
def AddEventContentCloseTime(builder, EventContentCloseTime): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(EventContentCloseTime), 0)
def EventContentSeasonExcelAddEventContentCloseTime(builder, EventContentCloseTime):
    """This method is deprecated. Please switch to AddEventContentCloseTime."""
    return AddEventContentCloseTime(builder, EventContentCloseTime)
def AddExtensionTime(builder, ExtensionTime): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(ExtensionTime), 0)
def EventContentSeasonExcelAddExtensionTime(builder, ExtensionTime):
    """This method is deprecated. Please switch to AddExtensionTime."""
    return AddExtensionTime(builder, ExtensionTime)
def AddMainIconParcelPath(builder, MainIconParcelPath): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(MainIconParcelPath), 0)
def EventContentSeasonExcelAddMainIconParcelPath(builder, MainIconParcelPath):
    """This method is deprecated. Please switch to AddMainIconParcelPath."""
    return AddMainIconParcelPath(builder, MainIconParcelPath)
def AddSubIconParcelPath(builder, SubIconParcelPath): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(SubIconParcelPath), 0)
def EventContentSeasonExcelAddSubIconParcelPath(builder, SubIconParcelPath):
    """This method is deprecated. Please switch to AddSubIconParcelPath."""
    return AddSubIconParcelPath(builder, SubIconParcelPath)
def AddBeforehandBgImagePath(builder, BeforehandBgImagePath): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(BeforehandBgImagePath), 0)
def EventContentSeasonExcelAddBeforehandBgImagePath(builder, BeforehandBgImagePath):
    """This method is deprecated. Please switch to AddBeforehandBgImagePath."""
    return AddBeforehandBgImagePath(builder, BeforehandBgImagePath)
def AddMinigamePrologScenarioGroupId(builder, MinigamePrologScenarioGroupId): builder.PrependInt64Slot(14, MinigamePrologScenarioGroupId, 0)
def EventContentSeasonExcelAddMinigamePrologScenarioGroupId(builder, MinigamePrologScenarioGroupId):
    """This method is deprecated. Please switch to AddMinigamePrologScenarioGroupId."""
    return AddMinigamePrologScenarioGroupId(builder, MinigamePrologScenarioGroupId)
def AddBeforehandScenarioGroupId(builder, BeforehandScenarioGroupId): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(BeforehandScenarioGroupId), 0)
def EventContentSeasonExcelAddBeforehandScenarioGroupId(builder, BeforehandScenarioGroupId):
    """This method is deprecated. Please switch to AddBeforehandScenarioGroupId."""
    return AddBeforehandScenarioGroupId(builder, BeforehandScenarioGroupId)
def StartBeforehandScenarioGroupIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def EventContentSeasonExcelStartBeforehandScenarioGroupIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartBeforehandScenarioGroupIdVector(builder, numElems)
def AddMainBannerImagePath(builder, MainBannerImagePath): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(MainBannerImagePath), 0)
def EventContentSeasonExcelAddMainBannerImagePath(builder, MainBannerImagePath):
    """This method is deprecated. Please switch to AddMainBannerImagePath."""
    return AddMainBannerImagePath(builder, MainBannerImagePath)
def AddMainBgImagePath(builder, MainBgImagePath): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(MainBgImagePath), 0)
def EventContentSeasonExcelAddMainBgImagePath(builder, MainBgImagePath):
    """This method is deprecated. Please switch to AddMainBgImagePath."""
    return AddMainBgImagePath(builder, MainBgImagePath)
def End(builder): return builder.EndObject()
def EventContentSeasonExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)