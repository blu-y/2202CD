
"use strict";

let WaypointClear = require('./WaypointClear.js')
let FileWrite = require('./FileWrite.js')
let LogRequestList = require('./LogRequestList.js')
let WaypointPull = require('./WaypointPull.js')
let CommandInt = require('./CommandInt.js')
let CommandAck = require('./CommandAck.js')
let CommandTriggerInterval = require('./CommandTriggerInterval.js')
let CommandHome = require('./CommandHome.js')
let FileClose = require('./FileClose.js')
let SetMode = require('./SetMode.js')
let MountConfigure = require('./MountConfigure.js')
let ParamSet = require('./ParamSet.js')
let LogRequestData = require('./LogRequestData.js')
let FileRename = require('./FileRename.js')
let FileChecksum = require('./FileChecksum.js')
let CommandLong = require('./CommandLong.js')
let StreamRate = require('./StreamRate.js')
let WaypointPush = require('./WaypointPush.js')
let FileRead = require('./FileRead.js')
let FileRemove = require('./FileRemove.js')
let VehicleInfoGet = require('./VehicleInfoGet.js')
let WaypointSetCurrent = require('./WaypointSetCurrent.js')
let LogRequestEnd = require('./LogRequestEnd.js')
let FileMakeDir = require('./FileMakeDir.js')
let CommandVtolTransition = require('./CommandVtolTransition.js')
let FileOpen = require('./FileOpen.js')
let CommandBool = require('./CommandBool.js')
let FileRemoveDir = require('./FileRemoveDir.js')
let SetMavFrame = require('./SetMavFrame.js')
let ParamPull = require('./ParamPull.js')
let CommandTOL = require('./CommandTOL.js')
let ParamGet = require('./ParamGet.js')
let CommandTriggerControl = require('./CommandTriggerControl.js')
let MessageInterval = require('./MessageInterval.js')
let FileTruncate = require('./FileTruncate.js')
let FileList = require('./FileList.js')
let ParamPush = require('./ParamPush.js')

module.exports = {
  WaypointClear: WaypointClear,
  FileWrite: FileWrite,
  LogRequestList: LogRequestList,
  WaypointPull: WaypointPull,
  CommandInt: CommandInt,
  CommandAck: CommandAck,
  CommandTriggerInterval: CommandTriggerInterval,
  CommandHome: CommandHome,
  FileClose: FileClose,
  SetMode: SetMode,
  MountConfigure: MountConfigure,
  ParamSet: ParamSet,
  LogRequestData: LogRequestData,
  FileRename: FileRename,
  FileChecksum: FileChecksum,
  CommandLong: CommandLong,
  StreamRate: StreamRate,
  WaypointPush: WaypointPush,
  FileRead: FileRead,
  FileRemove: FileRemove,
  VehicleInfoGet: VehicleInfoGet,
  WaypointSetCurrent: WaypointSetCurrent,
  LogRequestEnd: LogRequestEnd,
  FileMakeDir: FileMakeDir,
  CommandVtolTransition: CommandVtolTransition,
  FileOpen: FileOpen,
  CommandBool: CommandBool,
  FileRemoveDir: FileRemoveDir,
  SetMavFrame: SetMavFrame,
  ParamPull: ParamPull,
  CommandTOL: CommandTOL,
  ParamGet: ParamGet,
  CommandTriggerControl: CommandTriggerControl,
  MessageInterval: MessageInterval,
  FileTruncate: FileTruncate,
  FileList: FileList,
  ParamPush: ParamPush,
};
