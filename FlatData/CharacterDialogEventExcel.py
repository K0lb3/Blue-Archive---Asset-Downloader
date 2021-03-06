# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterDialogEventExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterDialogEventExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCharacterDialogEventExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # CharacterDialogEventExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CharacterDialogEventExcel
    def CharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def EventID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def ProductionStep_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def DialogCategory_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def DialogCondition_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def DialogConditionDetail_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def DialogConditionDetailValue(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def DialogType_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def ActionName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogEventExcel
    def Duration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def AnimationName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogEventExcel
    def LocalizeKR(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogEventExcel
    def LocalizeJP(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogEventExcel
    def LocalizeTH(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogEventExcel
    def LocalizeTW(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogEventExcel
    def LocalizeEN(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogEventExcel
    def LocalizeDE(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogEventExcel
    def LocalizeFR(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogEventExcel
    def VoiceClipsKr(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # CharacterDialogEventExcel
    def VoiceClipsKrLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterDialogEventExcel
    def VoiceClipsKrIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        return o == 0

    # CharacterDialogEventExcel
    def VoiceClipsJp(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # CharacterDialogEventExcel
    def VoiceClipsJpLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterDialogEventExcel
    def VoiceClipsJpIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        return o == 0

    # CharacterDialogEventExcel
    def VoiceClipsTh(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # CharacterDialogEventExcel
    def VoiceClipsThLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterDialogEventExcel
    def VoiceClipsThIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        return o == 0

    # CharacterDialogEventExcel
    def VoiceClipsTw(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # CharacterDialogEventExcel
    def VoiceClipsTwLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterDialogEventExcel
    def VoiceClipsTwIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        return o == 0

    # CharacterDialogEventExcel
    def VoiceClipsEn(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # CharacterDialogEventExcel
    def VoiceClipsEnLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterDialogEventExcel
    def VoiceClipsEnIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        return o == 0

    # CharacterDialogEventExcel
    def VoiceClipsDe(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # CharacterDialogEventExcel
    def VoiceClipsDeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterDialogEventExcel
    def VoiceClipsDeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        return o == 0

    # CharacterDialogEventExcel
    def VoiceClipsFr(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # CharacterDialogEventExcel
    def VoiceClipsFrLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterDialogEventExcel
    def VoiceClipsFrIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        return o == 0

def Start(builder): builder.StartObject(26)
def CharacterDialogEventExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddCharacterId(builder, CharacterId): builder.PrependInt64Slot(0, CharacterId, 0)
def CharacterDialogEventExcelAddCharacterId(builder, CharacterId):
    """This method is deprecated. Please switch to AddCharacterId."""
    return AddCharacterId(builder, CharacterId)
def AddEventID(builder, EventID): builder.PrependInt64Slot(1, EventID, 0)
def CharacterDialogEventExcelAddEventID(builder, EventID):
    """This method is deprecated. Please switch to AddEventID."""
    return AddEventID(builder, EventID)
def AddProductionStep_(builder, ProductionStep_): builder.PrependInt32Slot(2, ProductionStep_, 0)
def CharacterDialogEventExcelAddProductionStep_(builder, ProductionStep_):
    """This method is deprecated. Please switch to AddProductionStep_."""
    return AddProductionStep_(builder, ProductionStep_)
def AddDialogCategory_(builder, DialogCategory_): builder.PrependInt32Slot(3, DialogCategory_, 0)
def CharacterDialogEventExcelAddDialogCategory_(builder, DialogCategory_):
    """This method is deprecated. Please switch to AddDialogCategory_."""
    return AddDialogCategory_(builder, DialogCategory_)
def AddDialogCondition_(builder, DialogCondition_): builder.PrependInt32Slot(4, DialogCondition_, 0)
def CharacterDialogEventExcelAddDialogCondition_(builder, DialogCondition_):
    """This method is deprecated. Please switch to AddDialogCondition_."""
    return AddDialogCondition_(builder, DialogCondition_)
def AddDialogConditionDetail_(builder, DialogConditionDetail_): builder.PrependInt32Slot(5, DialogConditionDetail_, 0)
def CharacterDialogEventExcelAddDialogConditionDetail_(builder, DialogConditionDetail_):
    """This method is deprecated. Please switch to AddDialogConditionDetail_."""
    return AddDialogConditionDetail_(builder, DialogConditionDetail_)
def AddDialogConditionDetailValue(builder, DialogConditionDetailValue): builder.PrependInt64Slot(6, DialogConditionDetailValue, 0)
def CharacterDialogEventExcelAddDialogConditionDetailValue(builder, DialogConditionDetailValue):
    """This method is deprecated. Please switch to AddDialogConditionDetailValue."""
    return AddDialogConditionDetailValue(builder, DialogConditionDetailValue)
def AddGroupId(builder, GroupId): builder.PrependInt64Slot(7, GroupId, 0)
def CharacterDialogEventExcelAddGroupId(builder, GroupId):
    """This method is deprecated. Please switch to AddGroupId."""
    return AddGroupId(builder, GroupId)
def AddDialogType_(builder, DialogType_): builder.PrependInt32Slot(8, DialogType_, 0)
def CharacterDialogEventExcelAddDialogType_(builder, DialogType_):
    """This method is deprecated. Please switch to AddDialogType_."""
    return AddDialogType_(builder, DialogType_)
def AddActionName(builder, ActionName): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(ActionName), 0)
def CharacterDialogEventExcelAddActionName(builder, ActionName):
    """This method is deprecated. Please switch to AddActionName."""
    return AddActionName(builder, ActionName)
def AddDuration(builder, Duration): builder.PrependInt64Slot(10, Duration, 0)
def CharacterDialogEventExcelAddDuration(builder, Duration):
    """This method is deprecated. Please switch to AddDuration."""
    return AddDuration(builder, Duration)
def AddAnimationName(builder, AnimationName): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(AnimationName), 0)
def CharacterDialogEventExcelAddAnimationName(builder, AnimationName):
    """This method is deprecated. Please switch to AddAnimationName."""
    return AddAnimationName(builder, AnimationName)
def AddLocalizeKR(builder, LocalizeKR): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeKR), 0)
def CharacterDialogEventExcelAddLocalizeKR(builder, LocalizeKR):
    """This method is deprecated. Please switch to AddLocalizeKR."""
    return AddLocalizeKR(builder, LocalizeKR)
def AddLocalizeJP(builder, LocalizeJP): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeJP), 0)
def CharacterDialogEventExcelAddLocalizeJP(builder, LocalizeJP):
    """This method is deprecated. Please switch to AddLocalizeJP."""
    return AddLocalizeJP(builder, LocalizeJP)
def AddLocalizeTH(builder, LocalizeTH): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeTH), 0)
def CharacterDialogEventExcelAddLocalizeTH(builder, LocalizeTH):
    """This method is deprecated. Please switch to AddLocalizeTH."""
    return AddLocalizeTH(builder, LocalizeTH)
def AddLocalizeTW(builder, LocalizeTW): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeTW), 0)
def CharacterDialogEventExcelAddLocalizeTW(builder, LocalizeTW):
    """This method is deprecated. Please switch to AddLocalizeTW."""
    return AddLocalizeTW(builder, LocalizeTW)
def AddLocalizeEN(builder, LocalizeEN): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeEN), 0)
def CharacterDialogEventExcelAddLocalizeEN(builder, LocalizeEN):
    """This method is deprecated. Please switch to AddLocalizeEN."""
    return AddLocalizeEN(builder, LocalizeEN)
def AddLocalizeDE(builder, LocalizeDE): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeDE), 0)
def CharacterDialogEventExcelAddLocalizeDE(builder, LocalizeDE):
    """This method is deprecated. Please switch to AddLocalizeDE."""
    return AddLocalizeDE(builder, LocalizeDE)
def AddLocalizeFR(builder, LocalizeFR): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeFR), 0)
def CharacterDialogEventExcelAddLocalizeFR(builder, LocalizeFR):
    """This method is deprecated. Please switch to AddLocalizeFR."""
    return AddLocalizeFR(builder, LocalizeFR)
def AddVoiceClipsKr(builder, VoiceClipsKr): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(VoiceClipsKr), 0)
def CharacterDialogEventExcelAddVoiceClipsKr(builder, VoiceClipsKr):
    """This method is deprecated. Please switch to AddVoiceClipsKr."""
    return AddVoiceClipsKr(builder, VoiceClipsKr)
def StartVoiceClipsKrVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CharacterDialogEventExcelStartVoiceClipsKrVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartVoiceClipsKrVector(builder, numElems)
def AddVoiceClipsJp(builder, VoiceClipsJp): builder.PrependUOffsetTRelativeSlot(20, flatbuffers.number_types.UOffsetTFlags.py_type(VoiceClipsJp), 0)
def CharacterDialogEventExcelAddVoiceClipsJp(builder, VoiceClipsJp):
    """This method is deprecated. Please switch to AddVoiceClipsJp."""
    return AddVoiceClipsJp(builder, VoiceClipsJp)
def StartVoiceClipsJpVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CharacterDialogEventExcelStartVoiceClipsJpVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartVoiceClipsJpVector(builder, numElems)
def AddVoiceClipsTh(builder, VoiceClipsTh): builder.PrependUOffsetTRelativeSlot(21, flatbuffers.number_types.UOffsetTFlags.py_type(VoiceClipsTh), 0)
def CharacterDialogEventExcelAddVoiceClipsTh(builder, VoiceClipsTh):
    """This method is deprecated. Please switch to AddVoiceClipsTh."""
    return AddVoiceClipsTh(builder, VoiceClipsTh)
def StartVoiceClipsThVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CharacterDialogEventExcelStartVoiceClipsThVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartVoiceClipsThVector(builder, numElems)
def AddVoiceClipsTw(builder, VoiceClipsTw): builder.PrependUOffsetTRelativeSlot(22, flatbuffers.number_types.UOffsetTFlags.py_type(VoiceClipsTw), 0)
def CharacterDialogEventExcelAddVoiceClipsTw(builder, VoiceClipsTw):
    """This method is deprecated. Please switch to AddVoiceClipsTw."""
    return AddVoiceClipsTw(builder, VoiceClipsTw)
def StartVoiceClipsTwVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CharacterDialogEventExcelStartVoiceClipsTwVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartVoiceClipsTwVector(builder, numElems)
def AddVoiceClipsEn(builder, VoiceClipsEn): builder.PrependUOffsetTRelativeSlot(23, flatbuffers.number_types.UOffsetTFlags.py_type(VoiceClipsEn), 0)
def CharacterDialogEventExcelAddVoiceClipsEn(builder, VoiceClipsEn):
    """This method is deprecated. Please switch to AddVoiceClipsEn."""
    return AddVoiceClipsEn(builder, VoiceClipsEn)
def StartVoiceClipsEnVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CharacterDialogEventExcelStartVoiceClipsEnVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartVoiceClipsEnVector(builder, numElems)
def AddVoiceClipsDe(builder, VoiceClipsDe): builder.PrependUOffsetTRelativeSlot(24, flatbuffers.number_types.UOffsetTFlags.py_type(VoiceClipsDe), 0)
def CharacterDialogEventExcelAddVoiceClipsDe(builder, VoiceClipsDe):
    """This method is deprecated. Please switch to AddVoiceClipsDe."""
    return AddVoiceClipsDe(builder, VoiceClipsDe)
def StartVoiceClipsDeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CharacterDialogEventExcelStartVoiceClipsDeVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartVoiceClipsDeVector(builder, numElems)
def AddVoiceClipsFr(builder, VoiceClipsFr): builder.PrependUOffsetTRelativeSlot(25, flatbuffers.number_types.UOffsetTFlags.py_type(VoiceClipsFr), 0)
def CharacterDialogEventExcelAddVoiceClipsFr(builder, VoiceClipsFr):
    """This method is deprecated. Please switch to AddVoiceClipsFr."""
    return AddVoiceClipsFr(builder, VoiceClipsFr)
def StartVoiceClipsFrVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CharacterDialogEventExcelStartVoiceClipsFrVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartVoiceClipsFrVector(builder, numElems)
def End(builder): return builder.EndObject()
def CharacterDialogEventExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)