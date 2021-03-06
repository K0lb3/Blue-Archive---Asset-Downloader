# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class SchoolDungeonStageExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SchoolDungeonStageExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsSchoolDungeonStageExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # SchoolDungeonStageExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SchoolDungeonStageExcel
    def StageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # SchoolDungeonStageExcel
    def DungeonType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # SchoolDungeonStageExcel
    def Difficulty(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # SchoolDungeonStageExcel
    def BattleDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # SchoolDungeonStageExcel
    def PrevStageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # SchoolDungeonStageExcel
    def StageActionPointCostAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # SchoolDungeonStageExcel
    def EnterCostType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # SchoolDungeonStageExcel
    def EnterCostAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # SchoolDungeonStageExcel
    def GroundId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # SchoolDungeonStageExcel
    def StarGoal(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # SchoolDungeonStageExcel
    def StarGoalAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # SchoolDungeonStageExcel
    def StarGoalLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SchoolDungeonStageExcel
    def StarGoalIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0

    # SchoolDungeonStageExcel
    def StarGoalAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # SchoolDungeonStageExcel
    def StarGoalAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # SchoolDungeonStageExcel
    def StarGoalAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SchoolDungeonStageExcel
    def StarGoalAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        return o == 0

    # SchoolDungeonStageExcel
    def StageTopography_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # SchoolDungeonStageExcel
    def RecommandLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # SchoolDungeonStageExcel
    def StageRewardId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # SchoolDungeonStageExcel
    def PlayTimeLimitInSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(15)
def SchoolDungeonStageExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddStageId(builder, StageId): builder.PrependInt64Slot(0, StageId, 0)
def SchoolDungeonStageExcelAddStageId(builder, StageId):
    """This method is deprecated. Please switch to AddStageId."""
    return AddStageId(builder, StageId)
def AddDungeonType(builder, DungeonType): builder.PrependInt32Slot(1, DungeonType, 0)
def SchoolDungeonStageExcelAddDungeonType(builder, DungeonType):
    """This method is deprecated. Please switch to AddDungeonType."""
    return AddDungeonType(builder, DungeonType)
def AddDifficulty(builder, Difficulty): builder.PrependInt32Slot(2, Difficulty, 0)
def SchoolDungeonStageExcelAddDifficulty(builder, Difficulty):
    """This method is deprecated. Please switch to AddDifficulty."""
    return AddDifficulty(builder, Difficulty)
def AddBattleDuration(builder, BattleDuration): builder.PrependInt64Slot(3, BattleDuration, 0)
def SchoolDungeonStageExcelAddBattleDuration(builder, BattleDuration):
    """This method is deprecated. Please switch to AddBattleDuration."""
    return AddBattleDuration(builder, BattleDuration)
def AddPrevStageId(builder, PrevStageId): builder.PrependInt64Slot(4, PrevStageId, 0)
def SchoolDungeonStageExcelAddPrevStageId(builder, PrevStageId):
    """This method is deprecated. Please switch to AddPrevStageId."""
    return AddPrevStageId(builder, PrevStageId)
def AddStageActionPointCostAmount(builder, StageActionPointCostAmount): builder.PrependInt64Slot(5, StageActionPointCostAmount, 0)
def SchoolDungeonStageExcelAddStageActionPointCostAmount(builder, StageActionPointCostAmount):
    """This method is deprecated. Please switch to AddStageActionPointCostAmount."""
    return AddStageActionPointCostAmount(builder, StageActionPointCostAmount)
def AddEnterCostType(builder, EnterCostType): builder.PrependInt32Slot(6, EnterCostType, 0)
def SchoolDungeonStageExcelAddEnterCostType(builder, EnterCostType):
    """This method is deprecated. Please switch to AddEnterCostType."""
    return AddEnterCostType(builder, EnterCostType)
def AddEnterCostAmount(builder, EnterCostAmount): builder.PrependInt64Slot(7, EnterCostAmount, 0)
def SchoolDungeonStageExcelAddEnterCostAmount(builder, EnterCostAmount):
    """This method is deprecated. Please switch to AddEnterCostAmount."""
    return AddEnterCostAmount(builder, EnterCostAmount)
def AddGroundId(builder, GroundId): builder.PrependInt32Slot(8, GroundId, 0)
def SchoolDungeonStageExcelAddGroundId(builder, GroundId):
    """This method is deprecated. Please switch to AddGroundId."""
    return AddGroundId(builder, GroundId)
def AddStarGoal(builder, StarGoal): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(StarGoal), 0)
def SchoolDungeonStageExcelAddStarGoal(builder, StarGoal):
    """This method is deprecated. Please switch to AddStarGoal."""
    return AddStarGoal(builder, StarGoal)
def StartStarGoalVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def SchoolDungeonStageExcelStartStarGoalVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartStarGoalVector(builder, numElems)
def AddStarGoalAmount(builder, StarGoalAmount): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(StarGoalAmount), 0)
def SchoolDungeonStageExcelAddStarGoalAmount(builder, StarGoalAmount):
    """This method is deprecated. Please switch to AddStarGoalAmount."""
    return AddStarGoalAmount(builder, StarGoalAmount)
def StartStarGoalAmountVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def SchoolDungeonStageExcelStartStarGoalAmountVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartStarGoalAmountVector(builder, numElems)
def AddStageTopography_(builder, StageTopography_): builder.PrependInt32Slot(11, StageTopography_, 0)
def SchoolDungeonStageExcelAddStageTopography_(builder, StageTopography_):
    """This method is deprecated. Please switch to AddStageTopography_."""
    return AddStageTopography_(builder, StageTopography_)
def AddRecommandLevel(builder, RecommandLevel): builder.PrependInt64Slot(12, RecommandLevel, 0)
def SchoolDungeonStageExcelAddRecommandLevel(builder, RecommandLevel):
    """This method is deprecated. Please switch to AddRecommandLevel."""
    return AddRecommandLevel(builder, RecommandLevel)
def AddStageRewardId(builder, StageRewardId): builder.PrependInt64Slot(13, StageRewardId, 0)
def SchoolDungeonStageExcelAddStageRewardId(builder, StageRewardId):
    """This method is deprecated. Please switch to AddStageRewardId."""
    return AddStageRewardId(builder, StageRewardId)
def AddPlayTimeLimitInSeconds(builder, PlayTimeLimitInSeconds): builder.PrependInt64Slot(14, PlayTimeLimitInSeconds, 0)
def SchoolDungeonStageExcelAddPlayTimeLimitInSeconds(builder, PlayTimeLimitInSeconds):
    """This method is deprecated. Please switch to AddPlayTimeLimitInSeconds."""
    return AddPlayTimeLimitInSeconds(builder, PlayTimeLimitInSeconds)
def End(builder): return builder.EndObject()
def SchoolDungeonStageExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)