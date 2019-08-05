# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chat_service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12\x63hat_service.proto\"g\n\x0b\x43hatMessage\x12\x11\n\tsender_id\x18\x01 \x01(\t\x12\x13\n\x0bsender_name\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x01\x12\x0f\n\x07subject\x18\x04 \x01(\t\x12\x0c\n\x04\x62ody\x18\x05 \x01(\tb\x06proto3')
)




_CHATMESSAGE = _descriptor.Descriptor(
  name='ChatMessage',
  full_name='ChatMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender_id', full_name='ChatMessage.sender_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender_name', full_name='ChatMessage.sender_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ChatMessage.timestamp', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subject', full_name='ChatMessage.subject', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='ChatMessage.body', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=22,
  serialized_end=125,
)

DESCRIPTOR.message_types_by_name['ChatMessage'] = _CHATMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChatMessage = _reflection.GeneratedProtocolMessageType('ChatMessage', (_message.Message,), dict(
  DESCRIPTOR = _CHATMESSAGE,
  __module__ = 'chat_service_pb2'
  # @@protoc_insertion_point(class_scope:ChatMessage)
  ))
_sym_db.RegisterMessage(ChatMessage)


# @@protoc_insertion_point(module_scope)