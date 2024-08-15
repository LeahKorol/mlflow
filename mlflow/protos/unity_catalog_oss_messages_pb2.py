
import google.protobuf
from packaging.version import Version
if Version(google.protobuf.__version__).major >= 5:
  # -*- coding: utf-8 -*-
  # Generated by the protocol buffer compiler.  DO NOT EDIT!
  # source: unity_catalog_oss_messages.proto
  # Protobuf Python Version: 5.26.0
  """Generated protocol buffer code."""
  from google.protobuf import descriptor as _descriptor
  from google.protobuf import descriptor_pool as _descriptor_pool
  from google.protobuf import symbol_database as _symbol_database
  from google.protobuf.internal import builder as _builder
  # @@protoc_insertion_point(imports)

  _sym_db = _symbol_database.Default()


  from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2
  from . import databricks_pb2 as databricks__pb2


  DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n unity_catalog_oss_messages.proto\x12\x13mlflow.unitycatalog\x1a\x15scalapb/scalapb.proto\x1a\x10\x64\x61tabricks.proto\"\xb5\x01\n\x15\x43reateRegisteredModel\x12G\n\x15registered_model_info\x18\x01 \x01(\x0b\x32(.mlflow.unitycatalog.RegisteredModelInfo\x1aS\n\x08Response\x12G\n\x15registered_model_info\x18\x01 \x01(\x0b\x32(.mlflow.unitycatalog.RegisteredModelInfo\"\x8a\x04\n\x13RegisteredModelInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61talog_name\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t\x12\r\n\x05owner\x18\x04 \x01(\t\x12\x0f\n\x07\x63omment\x18\x05 \x01(\t\x12.\n\x04tags\x18\x14 \x03(\x0b\x32 .mlflow.unitycatalog.TagKeyValue\x12\x18\n\x10storage_location\x18\x06 \x01(\t\x12\x14\n\x0cmetastore_id\x18\x07 \x01(\t\x12\x11\n\tfull_name\x18\t \x01(\t\x12\x12\n\ncreated_at\x18\x0b \x01(\x03\x12\x12\n\ncreated_by\x18\x0c \x01(\t\x12\x12\n\nupdated_at\x18\r \x01(\x03\x12\x12\n\nupdated_by\x18\x0e \x01(\t\x12:\n\x0esecurable_type\x18\x0f \x01(\x0e\x32\".mlflow.unitycatalog.SecurableType\x12:\n\x0esecurable_kind\x18\x10 \x01(\x0e\x32\".mlflow.unitycatalog.SecurableKind\x12\n\n\x02id\x18\x12 \x01(\t\x12>\n\x07\x61liases\x18\x13 \x03(\x0b\x32-.mlflow.unitycatalog.RegisteredModelAliasInfo\x12\x13\n\x0b\x62rowse_only\x18\x15 \x01(\x08\")\n\x0bTagKeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"C\n\x18RegisteredModelAliasInfo\x12\x12\n\nalias_name\x18\x01 \x01(\t\x12\x13\n\x0bversion_num\x18\x02 \x01(\x03*9\n\rSecurableType\x12\x1a\n\x16UNKNOWN_SECURABLE_TYPE\x10\x00\x12\x0c\n\x08\x46UNCTION\x10\x06*J\n\rSecurableKind\x12\x1a\n\x16UNKNOWN_SECURABLE_KIND\x10\x00\x12\x1d\n\x19\x46UNCTION_REGISTERED_MODEL\x10GB1\n\'com.databricks.api.proto.managedcatalog\xa0\x01\x01\xe2?\x02\x10\x01')

  _globals = globals()
  _builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
  _builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'unity_catalog_oss_messages_pb2', _globals)
  if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\'com.databricks.api.proto.managedcatalog\240\001\001\342?\002\020\001'
    _globals['_SECURABLETYPE']._serialized_start=919
    _globals['_SECURABLETYPE']._serialized_end=976
    _globals['_SECURABLEKIND']._serialized_start=978
    _globals['_SECURABLEKIND']._serialized_end=1052
    _globals['_CREATEREGISTEREDMODEL']._serialized_start=99
    _globals['_CREATEREGISTEREDMODEL']._serialized_end=280
    _globals['_CREATEREGISTEREDMODEL_RESPONSE']._serialized_start=197
    _globals['_CREATEREGISTEREDMODEL_RESPONSE']._serialized_end=280
    _globals['_REGISTEREDMODELINFO']._serialized_start=283
    _globals['_REGISTEREDMODELINFO']._serialized_end=805
    _globals['_TAGKEYVALUE']._serialized_start=807
    _globals['_TAGKEYVALUE']._serialized_end=848
    _globals['_REGISTEREDMODELALIASINFO']._serialized_start=850
    _globals['_REGISTEREDMODELALIASINFO']._serialized_end=917
  # @@protoc_insertion_point(module_scope)

else:
  # -*- coding: utf-8 -*-
  # Generated by the protocol buffer compiler.  DO NOT EDIT!
  # source: unity_catalog_oss_messages.proto
  """Generated protocol buffer code."""
  from google.protobuf.internal import enum_type_wrapper
  from google.protobuf import descriptor as _descriptor
  from google.protobuf import descriptor_pool as _descriptor_pool
  from google.protobuf import message as _message
  from google.protobuf import reflection as _reflection
  from google.protobuf import symbol_database as _symbol_database
  # @@protoc_insertion_point(imports)

  _sym_db = _symbol_database.Default()


  from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2
  from . import databricks_pb2 as databricks__pb2


  DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n unity_catalog_oss_messages.proto\x12\x13mlflow.unitycatalog\x1a\x15scalapb/scalapb.proto\x1a\x10\x64\x61tabricks.proto\"\xb5\x01\n\x15\x43reateRegisteredModel\x12G\n\x15registered_model_info\x18\x01 \x01(\x0b\x32(.mlflow.unitycatalog.RegisteredModelInfo\x1aS\n\x08Response\x12G\n\x15registered_model_info\x18\x01 \x01(\x0b\x32(.mlflow.unitycatalog.RegisteredModelInfo\"\x8a\x04\n\x13RegisteredModelInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61talog_name\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t\x12\r\n\x05owner\x18\x04 \x01(\t\x12\x0f\n\x07\x63omment\x18\x05 \x01(\t\x12.\n\x04tags\x18\x14 \x03(\x0b\x32 .mlflow.unitycatalog.TagKeyValue\x12\x18\n\x10storage_location\x18\x06 \x01(\t\x12\x14\n\x0cmetastore_id\x18\x07 \x01(\t\x12\x11\n\tfull_name\x18\t \x01(\t\x12\x12\n\ncreated_at\x18\x0b \x01(\x03\x12\x12\n\ncreated_by\x18\x0c \x01(\t\x12\x12\n\nupdated_at\x18\r \x01(\x03\x12\x12\n\nupdated_by\x18\x0e \x01(\t\x12:\n\x0esecurable_type\x18\x0f \x01(\x0e\x32\".mlflow.unitycatalog.SecurableType\x12:\n\x0esecurable_kind\x18\x10 \x01(\x0e\x32\".mlflow.unitycatalog.SecurableKind\x12\n\n\x02id\x18\x12 \x01(\t\x12>\n\x07\x61liases\x18\x13 \x03(\x0b\x32-.mlflow.unitycatalog.RegisteredModelAliasInfo\x12\x13\n\x0b\x62rowse_only\x18\x15 \x01(\x08\")\n\x0bTagKeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"C\n\x18RegisteredModelAliasInfo\x12\x12\n\nalias_name\x18\x01 \x01(\t\x12\x13\n\x0bversion_num\x18\x02 \x01(\x03*9\n\rSecurableType\x12\x1a\n\x16UNKNOWN_SECURABLE_TYPE\x10\x00\x12\x0c\n\x08\x46UNCTION\x10\x06*J\n\rSecurableKind\x12\x1a\n\x16UNKNOWN_SECURABLE_KIND\x10\x00\x12\x1d\n\x19\x46UNCTION_REGISTERED_MODEL\x10GB1\n\'com.databricks.api.proto.managedcatalog\xa0\x01\x01\xe2?\x02\x10\x01')

  _SECURABLETYPE = DESCRIPTOR.enum_types_by_name['SecurableType']
  SecurableType = enum_type_wrapper.EnumTypeWrapper(_SECURABLETYPE)
  _SECURABLEKIND = DESCRIPTOR.enum_types_by_name['SecurableKind']
  SecurableKind = enum_type_wrapper.EnumTypeWrapper(_SECURABLEKIND)
  UNKNOWN_SECURABLE_TYPE = 0
  FUNCTION = 6
  UNKNOWN_SECURABLE_KIND = 0
  FUNCTION_REGISTERED_MODEL = 71


  _CREATEREGISTEREDMODEL = DESCRIPTOR.message_types_by_name['CreateRegisteredModel']
  _CREATEREGISTEREDMODEL_RESPONSE = _CREATEREGISTEREDMODEL.nested_types_by_name['Response']
  _REGISTEREDMODELINFO = DESCRIPTOR.message_types_by_name['RegisteredModelInfo']
  _TAGKEYVALUE = DESCRIPTOR.message_types_by_name['TagKeyValue']
  _REGISTEREDMODELALIASINFO = DESCRIPTOR.message_types_by_name['RegisteredModelAliasInfo']
  CreateRegisteredModel = _reflection.GeneratedProtocolMessageType('CreateRegisteredModel', (_message.Message,), {

    'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
      'DESCRIPTOR' : _CREATEREGISTEREDMODEL_RESPONSE,
      '__module__' : 'unity_catalog_oss_messages_pb2'
      # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.CreateRegisteredModel.Response)
      })
    ,
    'DESCRIPTOR' : _CREATEREGISTEREDMODEL,
    '__module__' : 'unity_catalog_oss_messages_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.CreateRegisteredModel)
    })
  _sym_db.RegisterMessage(CreateRegisteredModel)
  _sym_db.RegisterMessage(CreateRegisteredModel.Response)

  RegisteredModelInfo = _reflection.GeneratedProtocolMessageType('RegisteredModelInfo', (_message.Message,), {
    'DESCRIPTOR' : _REGISTEREDMODELINFO,
    '__module__' : 'unity_catalog_oss_messages_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.RegisteredModelInfo)
    })
  _sym_db.RegisterMessage(RegisteredModelInfo)

  TagKeyValue = _reflection.GeneratedProtocolMessageType('TagKeyValue', (_message.Message,), {
    'DESCRIPTOR' : _TAGKEYVALUE,
    '__module__' : 'unity_catalog_oss_messages_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.TagKeyValue)
    })
  _sym_db.RegisterMessage(TagKeyValue)

  RegisteredModelAliasInfo = _reflection.GeneratedProtocolMessageType('RegisteredModelAliasInfo', (_message.Message,), {
    'DESCRIPTOR' : _REGISTEREDMODELALIASINFO,
    '__module__' : 'unity_catalog_oss_messages_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.unitycatalog.RegisteredModelAliasInfo)
    })
  _sym_db.RegisterMessage(RegisteredModelAliasInfo)

  if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\'com.databricks.api.proto.managedcatalog\240\001\001\342?\002\020\001'
    _SECURABLETYPE._serialized_start=919
    _SECURABLETYPE._serialized_end=976
    _SECURABLEKIND._serialized_start=978
    _SECURABLEKIND._serialized_end=1052
    _CREATEREGISTEREDMODEL._serialized_start=99
    _CREATEREGISTEREDMODEL._serialized_end=280
    _CREATEREGISTEREDMODEL_RESPONSE._serialized_start=197
    _CREATEREGISTEREDMODEL_RESPONSE._serialized_end=280
    _REGISTEREDMODELINFO._serialized_start=283
    _REGISTEREDMODELINFO._serialized_end=805
    _TAGKEYVALUE._serialized_start=807
    _TAGKEYVALUE._serialized_end=848
    _REGISTEREDMODELALIASINFO._serialized_start=850
    _REGISTEREDMODELALIASINFO._serialized_end=917
  # @@protoc_insertion_point(module_scope)
