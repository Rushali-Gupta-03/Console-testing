# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmodel.proto\x12\x05model\"\"\n\x0ePredictRequest\x12\x10\n\x08\x66\x65\x61tures\x18\x01 \x03(\x02\"%\n\x0fPredictResponse\x12\x12\n\nprediction\x18\x01 \x01(\x02\"#\n\x0b\x44\x61taRequest\x12\x14\n\x0c\x64\x61taset_name\x18\x01 \x01(\t\"\'\n\x0c\x44\x61taResponse\x12\x17\n\x0fserialized_data\x18\x01 \x01(\x0c\x32\x80\x01\n\x0cModelService\x12:\n\x07Predict\x12\x15.model.PredictRequest\x1a\x16.model.PredictResponse\"\x00\x12\x34\n\x07GetData\x12\x12.model.DataRequest\x1a\x13.model.DataResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PREDICTREQUEST']._serialized_start=22
  _globals['_PREDICTREQUEST']._serialized_end=56
  _globals['_PREDICTRESPONSE']._serialized_start=58
  _globals['_PREDICTRESPONSE']._serialized_end=95
  _globals['_DATAREQUEST']._serialized_start=97
  _globals['_DATAREQUEST']._serialized_end=132
  _globals['_DATARESPONSE']._serialized_start=134
  _globals['_DATARESPONSE']._serialized_end=173
  _globals['_MODELSERVICE']._serialized_start=176
  _globals['_MODELSERVICE']._serialized_end=304
# @@protoc_insertion_point(module_scope)