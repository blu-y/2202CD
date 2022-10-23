
"use strict";

let WheelOdomStamped = require('./WheelOdomStamped.js');
let Vibration = require('./Vibration.js');
let CommandCode = require('./CommandCode.js');
let ExtendedState = require('./ExtendedState.js');
let HilSensor = require('./HilSensor.js');
let ESCTelemetryItem = require('./ESCTelemetryItem.js');
let PlayTuneV2 = require('./PlayTuneV2.js');
let Param = require('./Param.js');
let AttitudeTarget = require('./AttitudeTarget.js');
let State = require('./State.js');
let CameraImageCaptured = require('./CameraImageCaptured.js');
let CamIMUStamp = require('./CamIMUStamp.js');
let MagnetometerReporter = require('./MagnetometerReporter.js');
let HilStateQuaternion = require('./HilStateQuaternion.js');
let TimesyncStatus = require('./TimesyncStatus.js');
let ESCStatusItem = require('./ESCStatusItem.js');
let OnboardComputerStatus = require('./OnboardComputerStatus.js');
let OpticalFlowRad = require('./OpticalFlowRad.js');
let CellularStatus = require('./CellularStatus.js');
let RCIn = require('./RCIn.js');
let RTKBaseline = require('./RTKBaseline.js');
let ManualControl = require('./ManualControl.js');
let Tunnel = require('./Tunnel.js');
let RTCM = require('./RTCM.js');
let LandingTarget = require('./LandingTarget.js');
let Altitude = require('./Altitude.js');
let MountControl = require('./MountControl.js');
let CompanionProcessStatus = require('./CompanionProcessStatus.js');
let StatusText = require('./StatusText.js');
let HomePosition = require('./HomePosition.js');
let LogEntry = require('./LogEntry.js');
let HilActuatorControls = require('./HilActuatorControls.js');
let ADSBVehicle = require('./ADSBVehicle.js');
let VFR_HUD = require('./VFR_HUD.js');
let DebugValue = require('./DebugValue.js');
let FileEntry = require('./FileEntry.js');
let ESCTelemetry = require('./ESCTelemetry.js');
let ESCInfoItem = require('./ESCInfoItem.js');
let Thrust = require('./Thrust.js');
let BatteryStatus = require('./BatteryStatus.js');
let NavControllerOutput = require('./NavControllerOutput.js');
let ParamValue = require('./ParamValue.js');
let Mavlink = require('./Mavlink.js');
let RadioStatus = require('./RadioStatus.js');
let HilGPS = require('./HilGPS.js');
let ESCStatus = require('./ESCStatus.js');
let Waypoint = require('./Waypoint.js');
let WaypointList = require('./WaypointList.js');
let GlobalPositionTarget = require('./GlobalPositionTarget.js');
let OverrideRCIn = require('./OverrideRCIn.js');
let LogData = require('./LogData.js');
let GPSRAW = require('./GPSRAW.js');
let EstimatorStatus = require('./EstimatorStatus.js');
let PositionTarget = require('./PositionTarget.js');
let ActuatorControl = require('./ActuatorControl.js');
let RCOut = require('./RCOut.js');
let VehicleInfo = require('./VehicleInfo.js');
let GPSINPUT = require('./GPSINPUT.js');
let TerrainReport = require('./TerrainReport.js');
let GPSRTK = require('./GPSRTK.js');
let Trajectory = require('./Trajectory.js');
let xyz = require('./xyz.js');
let WaypointReached = require('./WaypointReached.js');
let HilControls = require('./HilControls.js');
let ESCInfo = require('./ESCInfo.js');

module.exports = {
  WheelOdomStamped: WheelOdomStamped,
  Vibration: Vibration,
  CommandCode: CommandCode,
  ExtendedState: ExtendedState,
  HilSensor: HilSensor,
  ESCTelemetryItem: ESCTelemetryItem,
  PlayTuneV2: PlayTuneV2,
  Param: Param,
  AttitudeTarget: AttitudeTarget,
  State: State,
  CameraImageCaptured: CameraImageCaptured,
  CamIMUStamp: CamIMUStamp,
  MagnetometerReporter: MagnetometerReporter,
  HilStateQuaternion: HilStateQuaternion,
  TimesyncStatus: TimesyncStatus,
  ESCStatusItem: ESCStatusItem,
  OnboardComputerStatus: OnboardComputerStatus,
  OpticalFlowRad: OpticalFlowRad,
  CellularStatus: CellularStatus,
  RCIn: RCIn,
  RTKBaseline: RTKBaseline,
  ManualControl: ManualControl,
  Tunnel: Tunnel,
  RTCM: RTCM,
  LandingTarget: LandingTarget,
  Altitude: Altitude,
  MountControl: MountControl,
  CompanionProcessStatus: CompanionProcessStatus,
  StatusText: StatusText,
  HomePosition: HomePosition,
  LogEntry: LogEntry,
  HilActuatorControls: HilActuatorControls,
  ADSBVehicle: ADSBVehicle,
  VFR_HUD: VFR_HUD,
  DebugValue: DebugValue,
  FileEntry: FileEntry,
  ESCTelemetry: ESCTelemetry,
  ESCInfoItem: ESCInfoItem,
  Thrust: Thrust,
  BatteryStatus: BatteryStatus,
  NavControllerOutput: NavControllerOutput,
  ParamValue: ParamValue,
  Mavlink: Mavlink,
  RadioStatus: RadioStatus,
  HilGPS: HilGPS,
  ESCStatus: ESCStatus,
  Waypoint: Waypoint,
  WaypointList: WaypointList,
  GlobalPositionTarget: GlobalPositionTarget,
  OverrideRCIn: OverrideRCIn,
  LogData: LogData,
  GPSRAW: GPSRAW,
  EstimatorStatus: EstimatorStatus,
  PositionTarget: PositionTarget,
  ActuatorControl: ActuatorControl,
  RCOut: RCOut,
  VehicleInfo: VehicleInfo,
  GPSINPUT: GPSINPUT,
  TerrainReport: TerrainReport,
  GPSRTK: GPSRTK,
  Trajectory: Trajectory,
  xyz: xyz,
  WaypointReached: WaypointReached,
  HilControls: HilControls,
  ESCInfo: ESCInfo,
};
