# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TutorialExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TutorialExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTutorialExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # TutorialExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TutorialExcel
    def ID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TutorialExcel
    def CompletionReportEventName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TutorialExcel
    def CompulsoryTutorial(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # TutorialExcel
    def DescriptionTutorial(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # TutorialExcel
    def TutorialStageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TutorialExcel
    def UIName(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # TutorialExcel
    def UINameLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TutorialExcel
    def UINameIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # TutorialExcel
    def TutorialParentName(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # TutorialExcel
    def TutorialParentNameLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TutorialExcel
    def TutorialParentNameIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

def Start(builder): builder.StartObject(7)
def TutorialExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddID(builder, ID): builder.PrependInt64Slot(0, ID, 0)
def TutorialExcelAddID(builder, ID):
    """This method is deprecated. Please switch to AddID."""
    return AddID(builder, ID)
def AddCompletionReportEventName(builder, CompletionReportEventName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(CompletionReportEventName), 0)
def TutorialExcelAddCompletionReportEventName(builder, CompletionReportEventName):
    """This method is deprecated. Please switch to AddCompletionReportEventName."""
    return AddCompletionReportEventName(builder, CompletionReportEventName)
def AddCompulsoryTutorial(builder, CompulsoryTutorial): builder.PrependBoolSlot(2, CompulsoryTutorial, 0)
def TutorialExcelAddCompulsoryTutorial(builder, CompulsoryTutorial):
    """This method is deprecated. Please switch to AddCompulsoryTutorial."""
    return AddCompulsoryTutorial(builder, CompulsoryTutorial)
def AddDescriptionTutorial(builder, DescriptionTutorial): builder.PrependBoolSlot(3, DescriptionTutorial, 0)
def TutorialExcelAddDescriptionTutorial(builder, DescriptionTutorial):
    """This method is deprecated. Please switch to AddDescriptionTutorial."""
    return AddDescriptionTutorial(builder, DescriptionTutorial)
def AddTutorialStageId(builder, TutorialStageId): builder.PrependInt64Slot(4, TutorialStageId, 0)
def TutorialExcelAddTutorialStageId(builder, TutorialStageId):
    """This method is deprecated. Please switch to AddTutorialStageId."""
    return AddTutorialStageId(builder, TutorialStageId)
def AddUIName(builder, UIName): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(UIName), 0)
def TutorialExcelAddUIName(builder, UIName):
    """This method is deprecated. Please switch to AddUIName."""
    return AddUIName(builder, UIName)
def StartUINameVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def TutorialExcelStartUINameVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartUINameVector(builder, numElems)
def AddTutorialParentName(builder, TutorialParentName): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(TutorialParentName), 0)
def TutorialExcelAddTutorialParentName(builder, TutorialParentName):
    """This method is deprecated. Please switch to AddTutorialParentName."""
    return AddTutorialParentName(builder, TutorialParentName)
def StartTutorialParentNameVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def TutorialExcelStartTutorialParentNameVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartTutorialParentNameVector(builder, numElems)
def End(builder): return builder.EndObject()
def TutorialExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)