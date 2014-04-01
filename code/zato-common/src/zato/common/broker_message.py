# -*- coding: utf-8 -*-

"""
Copyright (C) 2011 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# Bunch
from bunch import Bunch

MESSAGE = Bunch()
MESSAGE.MESSAGE_TYPE_LENGTH = 4
MESSAGE.TOKEN_LENGTH = 32
MESSAGE.TOKEN_START = MESSAGE.MESSAGE_TYPE_LENGTH
MESSAGE.TOKEN_END = MESSAGE.MESSAGE_TYPE_LENGTH + MESSAGE.TOKEN_LENGTH
MESSAGE.PAYLOAD_START = MESSAGE.MESSAGE_TYPE_LENGTH + MESSAGE.TOKEN_LENGTH
MESSAGE.NULL_TOKEN = '0' * MESSAGE.TOKEN_LENGTH

MESSAGE_TYPE = Bunch()
MESSAGE_TYPE.TO_SINGLETON = b'0000'
MESSAGE_TYPE.TO_PARALLEL_ANY = b'0001'
MESSAGE_TYPE.TO_PARALLEL_ALL = b'0002'

MESSAGE_TYPE.TO_AMQP_PUBLISHING_CONNECTOR_ALL = b'0003'
MESSAGE_TYPE.TO_AMQP_CONSUMING_CONNECTOR_ALL = b'0004'
MESSAGE_TYPE.TO_AMQP_CONNECTOR_ALL = b'0005'

MESSAGE_TYPE.TO_JMS_WMQ_PUBLISHING_CONNECTOR_ALL = b'0006'
MESSAGE_TYPE.TO_JMS_WMQ_CONSUMING_CONNECTOR_ALL = b'0007'
MESSAGE_TYPE.TO_JMS_WMQ_CONNECTOR_ALL = b'0008'

MESSAGE_TYPE.TO_ZMQ_PUBLISHING_CONNECTOR_ALL = b'0009'
MESSAGE_TYPE.TO_ZMQ_CONSUMING_CONNECTOR_ALL = b'0010'
MESSAGE_TYPE.TO_ZMQ_CONNECTOR_ALL = b'0011'

MESSAGE_TYPE.USER_DEFINED_START = b'5000'

TOPICS = {
    MESSAGE_TYPE.TO_SINGLETON: b'/zato/to-singleton',

    MESSAGE_TYPE.TO_PARALLEL_ANY: b'/zato/to-parallel/any',
    MESSAGE_TYPE.TO_PARALLEL_ALL: b'/zato/to-parallel/all',

    MESSAGE_TYPE.TO_AMQP_PUBLISHING_CONNECTOR_ALL: b'/zato/connector/amqp/publishing/all',
    MESSAGE_TYPE.TO_AMQP_CONSUMING_CONNECTOR_ALL: b'/zato/connector/amqp/consuming/all',
    MESSAGE_TYPE.TO_AMQP_CONNECTOR_ALL: b'/zato/connector/amqp/all',

    MESSAGE_TYPE.TO_JMS_WMQ_PUBLISHING_CONNECTOR_ALL: b'/zato/connector/jms-wmq/publishing/all',
    MESSAGE_TYPE.TO_JMS_WMQ_CONSUMING_CONNECTOR_ALL: b'/zato/connector/jms-wmq/consuming/all',
    MESSAGE_TYPE.TO_JMS_WMQ_CONNECTOR_ALL: b'/zato/connector/jms-wmq/all',

    MESSAGE_TYPE.TO_ZMQ_PUBLISHING_CONNECTOR_ALL: b'/zato/connector/zmq/publishing/all',
    MESSAGE_TYPE.TO_ZMQ_CONSUMING_CONNECTOR_ALL: b'/zato/connector/zmq/consuming/all',
    MESSAGE_TYPE.TO_ZMQ_CONNECTOR_ALL: b'/zato/connector/zmq/all',
}

KEYS = {k:v.replace('/zato','').replace('/',':') for k,v in TOPICS.items()}

SCHEDULER = Bunch()
SCHEDULER.CREATE = b'10000'
SCHEDULER.EDIT = b'10001'
SCHEDULER.DELETE = b'10002'
SCHEDULER.EXECUTE = b'10003'
SCHEDULER.JOB_EXECUTED = b'10004'

ZMQ_SOCKET = Bunch()
ZMQ_SOCKET.CLOSE = b'10100'

SECURITY = Bunch()
DEFINITION = Bunch()
OUTGOING = Bunch()
CHANNEL = Bunch()

SECURITY.BASIC_AUTH_CREATE = b'10200'
SECURITY.BASIC_AUTH_EDIT = b'10201'
SECURITY.BASIC_AUTH_DELETE = b'10202'
SECURITY.BASIC_AUTH_CHANGE_PASSWORD = b'10203'

SECURITY.TECH_ACC_CREATE = b'10300'
SECURITY.TECH_ACC_EDIT = b'10301'
SECURITY.TECH_ACC_DELETE = b'10302'
SECURITY.TECH_ACC_CHANGE_PASSWORD = b'10303'

SECURITY.WSS_CREATE = b'10400'
SECURITY.WSS_EDIT = b'10401'
SECURITY.WSS_DELETE = b'10402'
SECURITY.WSS_CHANGE_PASSWORD = b'10403'

DEFINITION.AMQP_CREATE = b'10500'
DEFINITION.AMQP_EDIT = b'10501'
DEFINITION.AMQP_DELETE = b'10502'
DEFINITION.AMQP_CHANGE_PASSWORD = b'10503'

DEFINITION.JMS_WMQ_CREATE = b'10504'
DEFINITION.JMS_WMQ_EDIT = b'10505'
DEFINITION.JMS_WMQ_DELETE = b'10506'

DEFINITION.ZMQ_CREATE = b'10507'
DEFINITION.ZMQ_EDIT = b'10508'
DEFINITION.ZMQ_DELETE = b'10509'

OUTGOING.AMQP_CREATE = b'10600'
OUTGOING.AMQP_EDIT = b'10601'
OUTGOING.AMQP_DELETE = b'10602'
OUTGOING.AMQP_PUBLISH = b'10603'

OUTGOING.JMS_WMQ_CREATE = b'10604'
OUTGOING.JMS_WMQ_EDIT = b'10605'
OUTGOING.JMS_WMQ_DELETE = b'10606'
OUTGOING.JMS_WMQ_SEND = b'10607'

OUTGOING.ZMQ_CREATE = b'10608'
OUTGOING.ZMQ_EDIT = b'10609'
OUTGOING.ZMQ_DELETE = b'10610'
OUTGOING.ZMQ_SEND = b'10611'

OUTGOING.SQL_CREATE_EDIT = b'10612' # Same for creating and updating the pools
OUTGOING.SQL_CHANGE_PASSWORD = b'10613'
OUTGOING.SQL_DELETE = b'10614'

OUTGOING.HTTP_SOAP_CREATE_EDIT = b'10615' # Same for creating and updating
OUTGOING.HTTP_SOAP_DELETE = b'10616'

OUTGOING.FTP_CREATE_EDIT = b'10617' # Same for creating and updating
OUTGOING.FTP_DELETE = b'10618'
OUTGOING.FTP_CHANGE_PASSWORD = b'10619'

CHANNEL.AMQP_CREATE = b'10700'
CHANNEL.AMQP_EDIT = b'10701'
CHANNEL.AMQP_DELETE = b'10702'
CHANNEL.AMQP_MESSAGE_RECEIVED = b'10703'

CHANNEL.JMS_WMQ_CREATE = b'10704'
CHANNEL.JMS_WMQ_EDIT = b'10705'
CHANNEL.JMS_WMQ_DELETE = b'10706'
CHANNEL.JMS_WMQ_MESSAGE_RECEIVED = b'10707'

CHANNEL.ZMQ_CREATE = b'10708'
CHANNEL.ZMQ_EDIT = b'10709'
CHANNEL.ZMQ_DELETE = b'10710'
CHANNEL.ZMQ_MESSAGE_RECEIVED = b'10711'

CHANNEL.HTTP_SOAP_CREATE_EDIT = b'10712' # Same for creating and updating
CHANNEL.HTTP_SOAP_DELETE = b'10713'
CHANNEL.HTTP_SOAP_AUDIT_RESPONSE = b'10714' # New in 1.2
CHANNEL.HTTP_SOAP_AUDIT_PATTERNS = b'10715' # New in 1.2
CHANNEL.HTTP_SOAP_AUDIT_STATE = b'10716' # New in 1.2
CHANNEL.HTTP_SOAP_AUDIT_CONFIG = b'10717' # New in 1.2

AMQP_CONNECTOR = Bunch()
AMQP_CONNECTOR.CLOSE = b'10801'

JMS_WMQ_CONNECTOR = Bunch()
JMS_WMQ_CONNECTOR.CLOSE = b'10802'

ZMQ_CONNECTOR = Bunch()
ZMQ_CONNECTOR.CLOSE = b'10803'

SERVICE = Bunch()
SERVICE.EDIT = b'10900'
SERVICE.DELETE = b'10901'
SERVICE.PUBLISH = b'10902'

HOT_DEPLOY = Bunch()
HOT_DEPLOY.CREATE = '11000'

STATS = Bunch()
STATS.DELETE = '11100'
STATS.DELETE_DAY = '11101'

SINGLETON = Bunch()
SINGLETON.CLOSE = b'11200'

# New in 1.2
SECURITY.OAUTH_CREATE = b'11300'
SECURITY.OAUTH_EDIT = b'11301'
SECURITY.OAUTH_DELETE = b'11302'
SECURITY.OAUTH_CHANGE_PASSWORD = b'11303'

# New in 1.2
MSG_NS = Bunch()
MSG_NS.CREATE = b'11400'
MSG_NS.EDIT = b'11401'
MSG_NS.DELETE = b'11402'

# New in 1.2
MSG_XPATH = Bunch()
MSG_XPATH.CREATE = b'11450'
MSG_XPATH.EDIT = b'11451'
MSG_XPATH.DELETE = b'11452'

# New in 1.2
MSG_ELEM_PATH = Bunch()
MSG_ELEM_PATH.CREATE = b'11500'
MSG_ELEM_PATH.EDIT = b'11501'
MSG_ELEM_PATH.DELETE = b'11502'

# New in 1.2
PUB_SUB_TOPIC = Bunch()
PUB_SUB_TOPIC.CREATE = b'11550'
PUB_SUB_TOPIC.EDIT = b'11551'
PUB_SUB_TOPIC.DELETE = b'11552'
PUB_SUB_TOPIC.ADD_DEFAULT_PRODUCER = b'11553'
PUB_SUB_TOPIC.DELETE_DEFAULT_PRODUCER = b'11554'

# New in 1.2
PUB_SUB_PRODUCER = Bunch()
PUB_SUB_PRODUCER.CREATE = b'11600'
PUB_SUB_PRODUCER.EDIT = b'11601'
PUB_SUB_PRODUCER.DELETE = b'11602'

# New in 1.2
PUB_SUB_CONSUMER = Bunch()
PUB_SUB_CONSUMER.CREATE = b'11650'
PUB_SUB_CONSUMER.EDIT = b'11651'
PUB_SUB_CONSUMER.DELETE = b'11652'

# New in 1.2
CLOUD = Bunch()
CLOUD.OPENSTACK_SWIFT_CREATE_EDIT = b'11700'
CLOUD.OPENSTACK_SWIFT_DELETE = b'11701'

# New in 1.2
SECURITY.NTLM_CREATE = b'11750'
SECURITY.NTLM_EDIT = b'11751'
SECURITY.NTLM_DELETE = b'11752'
SECURITY.NTLM_CHANGE_PASSWORD = b'11753'

# New in 1.2
SECURITY.AWS_CREATE = b'11760'
SECURITY.AWS_EDIT = b'11761'
SECURITY.AWS_DELETE = b'11762'
SECURITY.AWS_CHANGE_PASSWORD = b'11763'

# New in 1.2
CLOUD.AWS_S3_CREATE_EDIT = b'11800'
CLOUD.AWS_S3_DELETE = b'11801'

# New in 1.2
SECURITY.OPENSTACK_CREATE = b'11850'
SECURITY.OPENSTACK_EDIT = b'11851'
SECURITY.OPENSTACK_DELETE = b'11852'
SECURITY.OPENSTACK_CHANGE_PASSWORD = b'11853'

# New in 1.2
NOTIF = Bunch()
NOTIF.RUN_NOTIFIER = b'11900'
NOTIF.CLOUD_OPENSTACK_SWIFT_CREATE_EDIT = b'11901'
NOTIF.CLOUD_OPENSTACK_SWIFT_DELETE = b'11902'

code_to_name = {}

# To prevent 'RuntimeError: dictionary changed size during iteration'
bunch_name, bunch = None, None

for bunch_name, bunch in globals().items():
    if isinstance(bunch, Bunch) and not bunch is Bunch:
        if bunch not in(MESSAGE, MESSAGE_TYPE):
            for code_name, code_value in bunch.items():
                code_name = bunch_name + '_' + code_name
                code_to_name[code_value] = code_name

del bunch_name, bunch, code_name, code_value
