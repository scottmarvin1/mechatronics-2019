# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PMUD.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='PMUD.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\nPMUD.proto\"F\n\x04PMUD\x12\x0f\n\x07voltage\x18\x01 \x01(\x02\x12\x0f\n\x07\x63urrent\x18\x02 \x01(\x02\x12\x0e\n\x06isSafe\x18\x03 \x01(\x08\x12\x0c\n\x04kill\x18\x04 \x01(\x08\x62\x06proto3')
)




_PMUD = _descriptor.Descriptor(
  name='PMUD',
  full_name='PMUD',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='voltage', full_name='PMUD.voltage', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current', full_name='PMUD.current', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isSafe', full_name='PMUD.isSafe', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kill', full_name='PMUD.kill', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=84,
)

DESCRIPTOR.message_types_by_name['PMUD'] = _PMUD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PMUD = _reflection.GeneratedProtocolMessageType('PMUD', (_message.Message,), dict(
  DESCRIPTOR = _PMUD,
  __module__ = 'PMUD_pb2'
  # @@protoc_insertion_point(class_scope:PMUD)
  ))
_sym_db.RegisterMessage(PMUD)


# @@protoc_insertion_point(module_scope)
