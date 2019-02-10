# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Mechatronics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import AHRS_pb2 as AHRS__pb2
import pressureTransducers_pb2 as pressureTransducers__pb2
import hydrophones_pb2 as hydrophones__pb2
import DVL_pb2 as DVL__pb2
import leakDetect_pb2 as leakDetect__pb2
import PMUD_pb2 as PMUD__pb2
import pneumatics_pb2 as pneumatics__pb2
import guiComm_pb2 as guiComm__pb2
import thrusters_pb2 as thrusters__pb2
import PID_pb2 as PID__pb2
import PID_Error_pb2 as PID__Error__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Mechatronics.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12Mechatronics.proto\x1a\nAHRS.proto\x1a\x19pressureTransducers.proto\x1a\x11hydrophones.proto\x1a\tDVL.proto\x1a\x10leakDetect.proto\x1a\nPMUD.proto\x1a\x10pneumatics.proto\x1a\rguiComm.proto\x1a\x0fthrusters.proto\x1a\tPID.proto\x1a\x0fPID_Error.proto\"\xd8\x02\n\x0cMechatronics\x12\x13\n\x04type\x18\x01 \x01(\x0e\x32\x05.Type\x12\x13\n\x04\x61hrs\x18\x02 \x01(\x0b\x32\x05.AHRS\x12+\n\rpressureTrans\x18\x03 \x01(\x0b\x32\x14.PressureTransducers\x12\x1c\n\x06hydros\x18\x04 \x01(\x0b\x32\x0c.Hydrophones\x12\x11\n\x03\x64vl\x18\x05 \x01(\x0b\x32\x04.DVL\x12\x1f\n\nleakDetect\x18\x06 \x01(\x0b\x32\x0b.LeakDetect\x12\x13\n\x04pmud\x18\x08 \x01(\x0b\x32\x05.PMUD\x12\x1f\n\npneumatics\x18\t \x01(\x0b\x32\x0b.Pneumatics\x12\x19\n\x07guiComm\x18\n \x01(\x0b\x32\x08.GUIComm\x12\x1c\n\x08thruster\x18\x0b \x01(\x0b\x32\n.Thrusters\x12\x11\n\x03pid\x18\x0c \x01(\x0b\x32\x04.PID\x12\x1d\n\tpid_error\x18\r \x01(\x0b\x32\n.PID_Error*\xcf\x01\n\x04Type\x12\r\n\tAHRS_DATA\x10\x00\x12\x18\n\x14PRESSURE_TRANSDUCERS\x10\x01\x12\x0f\n\x0bHYDROPHONES\x10\x02\x12\x0c\n\x08\x44VL_DATA\x10\x03\x12\x12\n\x0eLEAK_DETECTION\x10\x04\x12\x15\n\x11THRUSTER_FEEDBACK\x10\x05\x12\r\n\tPMUD_DATA\x10\x06\x12\x0e\n\nPNEUMATICS\x10\x07\x12\x0c\n\x08GUI_COMM\x10\x08\x12\r\n\tTHRUSTERS\x10\t\x12\x08\n\x04PIDS\x10\n\x12\x0e\n\nPID_ERRORS\x10\x0b\x62\x06proto3')
  ,
  dependencies=[AHRS__pb2.DESCRIPTOR,pressureTransducers__pb2.DESCRIPTOR,hydrophones__pb2.DESCRIPTOR,DVL__pb2.DESCRIPTOR,leakDetect__pb2.DESCRIPTOR,PMUD__pb2.DESCRIPTOR,pneumatics__pb2.DESCRIPTOR,guiComm__pb2.DESCRIPTOR,thrusters__pb2.DESCRIPTOR,PID__pb2.DESCRIPTOR,PID__Error__pb2.DESCRIPTOR,])

_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AHRS_DATA', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRESSURE_TRANSDUCERS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HYDROPHONES', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DVL_DATA', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEAK_DETECTION', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THRUSTER_FEEDBACK', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PMUD_DATA', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PNEUMATICS', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GUI_COMM', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THRUSTERS', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PIDS', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PID_ERRORS', index=11, number=11,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=547,
  serialized_end=754,
)
_sym_db.RegisterEnumDescriptor(_TYPE)

Type = enum_type_wrapper.EnumTypeWrapper(_TYPE)
AHRS_DATA = 0
PRESSURE_TRANSDUCERS = 1
HYDROPHONES = 2
DVL_DATA = 3
LEAK_DETECTION = 4
THRUSTER_FEEDBACK = 5
PMUD_DATA = 6
PNEUMATICS = 7
GUI_COMM = 8
THRUSTERS = 9
PIDS = 10
PID_ERRORS = 11



_MECHATRONICS = _descriptor.Descriptor(
  name='Mechatronics',
  full_name='Mechatronics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Mechatronics.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ahrs', full_name='Mechatronics.ahrs', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pressureTrans', full_name='Mechatronics.pressureTrans', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hydros', full_name='Mechatronics.hydros', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dvl', full_name='Mechatronics.dvl', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='leakDetect', full_name='Mechatronics.leakDetect', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pmud', full_name='Mechatronics.pmud', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pneumatics', full_name='Mechatronics.pneumatics', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guiComm', full_name='Mechatronics.guiComm', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='thruster', full_name='Mechatronics.thruster', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pid', full_name='Mechatronics.pid', index=10,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pid_error', full_name='Mechatronics.pid_error', index=11,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=544,
)

_MECHATRONICS.fields_by_name['type'].enum_type = _TYPE
_MECHATRONICS.fields_by_name['ahrs'].message_type = AHRS__pb2._AHRS
_MECHATRONICS.fields_by_name['pressureTrans'].message_type = pressureTransducers__pb2._PRESSURETRANSDUCERS
_MECHATRONICS.fields_by_name['hydros'].message_type = hydrophones__pb2._HYDROPHONES
_MECHATRONICS.fields_by_name['dvl'].message_type = DVL__pb2._DVL
_MECHATRONICS.fields_by_name['leakDetect'].message_type = leakDetect__pb2._LEAKDETECT
_MECHATRONICS.fields_by_name['pmud'].message_type = PMUD__pb2._PMUD
_MECHATRONICS.fields_by_name['pneumatics'].message_type = pneumatics__pb2._PNEUMATICS
_MECHATRONICS.fields_by_name['guiComm'].message_type = guiComm__pb2._GUICOMM
_MECHATRONICS.fields_by_name['thruster'].message_type = thrusters__pb2._THRUSTERS
_MECHATRONICS.fields_by_name['pid'].message_type = PID__pb2._PID
_MECHATRONICS.fields_by_name['pid_error'].message_type = PID__Error__pb2._PID_ERROR
DESCRIPTOR.message_types_by_name['Mechatronics'] = _MECHATRONICS
DESCRIPTOR.enum_types_by_name['Type'] = _TYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Mechatronics = _reflection.GeneratedProtocolMessageType('Mechatronics', (_message.Message,), dict(
  DESCRIPTOR = _MECHATRONICS,
  __module__ = 'Mechatronics_pb2'
  # @@protoc_insertion_point(class_scope:Mechatronics)
  ))
_sym_db.RegisterMessage(Mechatronics)


# @@protoc_insertion_point(module_scope)
