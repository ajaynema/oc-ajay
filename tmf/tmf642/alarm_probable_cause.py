from enum import Enum

class AlarmProbableCause(Enum):
    abisBtsInterfaceFailure="abisBtsInterfaceFailure"
    abisTrxInterfaceFailure="abisTrxInterfaceFailure"
    adapterError="adapterError"
    airCompressorFailure="airCompressorFailure"
    airConditioningFailure="airConditioningFailure"
    airDryerFailure="airDryerFailure"
    ais="ais"
    antennaFailure="antennaFailure"
    applicationSubsystemFailure="applicationSubsystemFailure"
    authenticationFailure="authenticationFailure"
    backplaneFailure="backplaneFailure"
    bandwidthReduced="bandwidthReduced"
    batteryBreakdown="batteryBreakdown"
    batteryChargingFailure="batteryChargingFailure"
    batteryDischarging="batteryDischarging"
    batteryFailure="batteryFailure"
    breachOfConfidentiality="breachOfConfidentiality"
    broadcastChannelFailure="broadcastChannelFailure"
    cableTamper="cableTamper"
    callEstablishmentError="callEstablishmentError"
    callSetUpFailure="callSetUpFailure"
    clockSynchronizationProblem="clockSynchronizationProblem"
    combinerProblem="combinerProblem"
    commercialPowerFailure="commercialPowerFailure"
    communicationsProtocolError="communicationsProtocolError"
    communicationsSubsystemFailure="communicationsSubsystemFailure"
    configurationOrCustomizationError="configurationOrCustomizationError"
    congestion="congestion"
    connectionEstablishmentError="connectionEstablishmentError"
    coolingFanFailure="coolingFanFailure"
    coolingSystemFailure="coolingSystemFailure"
    corruptData="corruptData"
    cpuCyclesLimitExceeded="cpuCyclesLimitExceeded"
    dataSetOrModemError="dataSetOrModemError"
    databaseInconsistency="databaseInconsistency"
    degradedSignal="degradedSignal"
    delayedInformation="delayedInformation"
    demodulationFailure="demodulationFailure"
    denialOfService="denialOfService"
    diskFailure="diskFailure"
    duplicateInformation="duplicateInformation"
    enclosureDoorOpen="enclosureDoorOpen"
    engineFailure="engineFailure"
    equipmentFailure="equipmentFailure"
    equipmentIdentifierDuplication="equipmentIdentifierDuplication"
    excessiveBitErrorRate="excessiveBitErrorRate"
    excessiveReceiverTemperature="excessiveReceiverTemperature"
    excessiveResponseTime="excessiveResponseTime"
    excessiveRetransmissionRate="excessiveRetransmissionRate"
    excessiveTransmitterOutputPower="excessiveTransmitterOutputPower"
    excessiveTransmitterTemperature="excessiveTransmitterTemperature"
    excessiveVibration="excessiveVibration"
    explosiveGas="explosiveGas"
    externalEquipmentFailure="externalEquipmentFailure"
    externalIfDeviceProblem="externalIfDeviceProblem"
    externalPointFailure="externalPointFailure"
    externalPowerSupplyFailure="externalPowerSupplyFailure"
    externalTransmissionDeviceFailure="externalTransmissionDeviceFailure"
    farEndReceiverFailure="farEndReceiverFailure"
    fileError="fileError"
    fileSystemCallUnsuccessful="fileSystemCallUnsuccessful"
    fire="fire"
    fireDetectorFailure="fireDetectorFailure"
    flood="flood"
    framingError="framingError"
    frequencyHoppingDegraded="frequencyHoppingDegraded"
    frequencyHoppingFailure="frequencyHoppingFailure"
    frequencyRedefinitionFailed="frequencyRedefinitionFailed"
    fuseFailure="fuseFailure"
    generatorFailure="generatorFailure"
    heatingVentCoolingSystemProblem="heatingVentCoolingSystemProblem"
    highHumidity="highHumidity"
    highTemperature="highTemperature"
    highWind="highWind"
    humidityUnacceptable="humidityUnacceptable"
    iceBuildUp="iceBuildUp"
    informationMissing="informationMissing"
    informationModificationDetected="informationModificationDetected"
    informationOutOfSequence="informationOutOfSequence"
    inputDeviceError="inputDeviceError"
    inputOutputDeviceError="inputOutputDeviceError"
    inputParameterOutOfRange="inputParameterOutOfRange"
    intrusionDetection="intrusionDetection"
    invalidMessageReceived="invalidMessageReceived"
    invalidParameter="invalidParameter"
    invalidPointer="invalidPointer"
    ioDeviceError="ioDeviceError"
    keyExpired="keyExpired"
    lanError="lanError"
    lapdLinkProtocolFailure="lapdLinkProtocolFailure"
    leakDetected="leakDetected"
    lineCardProblem="lineCardProblem"
    lineInterfaceFailure="lineInterfaceFailure"
    linkFailure="linkFailure"
    localAlarmIndication="localAlarmIndication"
    localNodeTransmissionError="localNodeTransmissionError"
    lossOfFrame="lossOfFrame"
    lossOfMultiFrame="lossOfMultiFrame"
    lossOfPointer="lossOfPointer"
    lossOfRealTime="lossOfRealTime"
    lossOfRedundancy="lossOfRedundancy"
    lossOfSignal="lossOfSignal"
    lossOfSynchronisation="lossOfSynchronisation"
    lowBatteryThreshold="lowBatteryThreshold"
    lowCablePressure="lowCablePressure"
    lowFuel="lowFuel"
    lowHumidity="lowHumidity"
    lowTemperatue="lowTemperatue"
    lowWater="lowWater"
    mainsBreakdownWithBatteryBackUp="mainsBreakdownWithBatteryBackUp"
    mainsBreakdownWithoutBatteryBackUp="mainsBreakdownWithoutBatteryBackUp"
    materialSupplyExhausted="materialSupplyExhausted"
    memoryMismatch="memoryMismatch"
    messageNotExpected="messageNotExpected"
    messageNotInitialized="messageNotInitialized"
    messageOutOfSequence="messageOutOfSequence"
    modulationFailure="modulationFailure"
    multiplexerProblem="multiplexerProblem"
    neIdentifierDuplication="neIdentifierDuplication"
    nonRepudiationFailure="nonRepudiationFailure"
    other="other"
    ouputDeviceError="ouputDeviceError"
    outOfCpuCycles="outOfCpuCycles"
    outOfHoursActivity="outOfHoursActivity"
    outOfMemory="outOfMemory"
    outOfService="outOfService"
    pathTraceMismatch="pathTraceMismatch"
    payloadTypeMismatch="payloadTypeMismatch"
    performanceDegraded="performanceDegraded"
    powerProblems="powerProblems"
    powerSupplyFailure="powerSupplyFailure"
    pressureUnacceptable="pressureUnacceptable"
    proceduralError="proceduralError"
    processorProblem="processorProblem"
    protectingResourceFailure="protectingResourceFailure"
    protectionMechanismFailure="protectionMechanismFailure"
    protectionPathFailure="protectionPathFailure"
    pumpFailure="pumpFailure"
    queueSizeExceeded="queueSizeExceeded"
    realTimeClockFailure="realTimeClockFailure"
    receiveFailure="receiveFailure"
    receiverAntennaFault="receiverAntennaFault"
    receiverFailure="receiverFailure"
    receiverMulticouplerFailure="receiverMulticouplerFailure"
    rectifierFailure="rectifierFailure"
    rectifierHighVoltage="rectifierHighVoltage"
    rectifierLowVoltage="rectifierLowVoltage"
    reducedAlarmReporting="reducedAlarmReporting"
    reducedEventReporting="reducedEventReporting"
    reducedLoggingCapability="reducedLoggingCapability"
    reducedTransmitterOutputPower="reducedTransmitterOutputPower"
    reinitialized="reinitialized"
    remoteAlarmIndication="remoteAlarmIndication"
    remoteAlarmInterface="remoteAlarmInterface"
    remoteNodeTransmissionError="remoteNodeTransmissionError"
    replaceableUnitMissing="replaceableUnitMissing"
    replaceableUnitProblem="replaceableUnitProblem"
    replaceableUnitTypeMismatch="replaceableUnitTypeMismatch"
    resourceAtOrNearingCapacity="resourceAtOrNearingCapacity"
    responseTimeExecessive="responseTimeExecessive"
    retransmissionRateExcessive="retransmissionRateExcessive"
    routingFailure="routingFailure"
    signalLabelMismatch="signalLabelMismatch"
    signalQualityEvaluationFailure="signalQualityEvaluationFailure"
    smoke="smoke"
    softwareDownloadFailure="softwareDownloadFailure"
    softwareEnvironmentProblem="softwareEnvironmentProblem"
    softwareError="softwareError"
    softwareProgramAbnormallyTerminated="softwareProgramAbnormallyTerminated"
    softwareProgramError="softwareProgramError"
    ss7ProtocolFailure="ss7ProtocolFailure"
    storageCapacityProblem="storageCapacityProblem"
    synchronizationSourceMismatch="synchronizationSourceMismatch"
    systemCallUnsuccessful="systemCallUnsuccessful"
    systemResourcesOverload="systemResourcesOverload"
    temperatureUnacceptable="temperatureUnacceptable"
    terminalProblem="terminalProblem"
    thresholdCrossed="thresholdCrossed"
    timeoutExpired="timeoutExpired"
    timeslotHardwareFailure="timeslotHardwareFailure"
    timingProblem="timingProblem"
    toxicGas="toxicGas"
    toxicLeakDetected="toxicLeakDetected"
    transceiverFailure="transceiverFailure"
    transcoderOrRateAdapterProblem="transcoderOrRateAdapterProblem"
    transcoderProblem="transcoderProblem"
    transmissionError="transmissionError"
    transmitFailure="transmitFailure"
    transmiterFailure="transmiterFailure"
    transmitterAntennaFailure="transmitterAntennaFailure"
    transmitterAntennaNotAdjusted="transmitterAntennaNotAdjusted"
    transmitterFailure="transmitterFailure"
    transmitterOffFrequency="transmitterOffFrequency"
    trunkCardProblem="trunkCardProblem"
    unauthorizedAccessAttempt="unauthorizedAccessAttempt"
    unavailable="unavailable"
    underlyingResourceUnavailable="underlyingResourceUnavailable"
    unexpectedInformation="unexpectedInformation"
    variableOutOfRange="variableOutOfRange"
    ventilationsSystemFailure="ventilationsSystemFailure"
    versionMismatch="versionMismatch"
    watchdogTimerExpired="watchdogTimerExpired"












































































