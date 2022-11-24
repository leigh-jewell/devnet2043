from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

ACCOUNT_ADMIN_ACTIVATION: EventType
ADD: ChangeType
APP_ACTIVATION: EventType
APP_DE_ACTIVATION: EventType
CAMERA_COUNT: EventType
CONN_WIRED: Connection
CONN_WIRELESS: Connection
DESCRIPTOR: _descriptor.FileDescriptor
DEVICE_ACTIVE_EVENT: DevicePresenceEventType
DEVICE_COUNT: EventType
DEVICE_ENTRY: EventType
DEVICE_ENTRY_EVENT: DevicePresenceEventType
DEVICE_EXIT: EventType
DEVICE_EXIT_EVENT: DevicePresenceEventType
DEVICE_IN_ACTIVE_EVENT: DevicePresenceEventType
DEVICE_LOCATION_UPDATE: EventType
DEVICE_PRESENCE: EventType
DEVICE_RAW_USER_ID_CHANGE_EVENT: DevicePresenceEventType
DEVICE_SSID_CHANGE_EVENT: DevicePresenceEventType
FACEBOOK: SocialNetwork
FEMALE: Gender
GENDER_NOT_AVAILABLE: Gender
IOT_ACTION_BUTTON_CLICK: IOTActionType
IOT_ACTION_DOUBLE_TAP: IOTActionType
IOT_ACTION_UNKNOWN: IOTActionType
IOT_BLE_DEVICE: IOTDeviceType
IOT_DEVICE_UNKNOWN: IOTDeviceType
IOT_RFID_TAG: IOTDeviceType
IOT_TELEMETRY: EventType
IOT_TELE_PRESENCE_DEVICE: IOTDeviceType
IOT_USER_ACTION: EventType
IOT_WIRED_DEVICE: IOTDeviceType
IOT_ZIGBEE_DEVICE: IOTDeviceType
KEEP_ALIVE: EventType
LAPTOP: DeviceType
LINKEDIN: SocialNetwork
LOCATION_ANCHOR_UPDATE: EventType
LOCATION_CHANGE: EventType
MALE: Gender
MOBILE: DeviceType
MOVE: ChangeType
NETWORK_STATUS_UPDATE: EventType
NETWORK_TELEMETRY: EventType
NOT_AVAILABLE: DeviceType
OTHER: Gender
OTHER_DEVICE: DeviceType
PROFILE_UPDATE: EventType
RAW_CAMERA_COUNT: EventType
REMOVE: ChangeType
TABLET: DeviceType
TP_PEOPLE_COUNT_UPDATE: EventType
TWITTER: SocialNetwork
UPDATE: ChangeType
USER_ACTIVE_EVENT: UserPresenceEventType
USER_ENTRY_EVENT: UserPresenceEventType
USER_EXIT_EVENT: UserPresenceEventType
USER_IN_ACTIVE_EVENT: UserPresenceEventType
USER_PRESENCE: EventType

class AccountAdminChange(_message.Message):
    __slots__ = ["change_type", "login_email"]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOGIN_EMAIL_FIELD_NUMBER: _ClassVar[int]
    change_type: ChangeType
    login_email: str
    def __init__(self, change_type: _Optional[_Union[ChangeType, str]] = ..., login_email: _Optional[str] = ...) -> None: ...

class AppActivation(_message.Message):
    __slots__ = ["instance_name", "iot_groups", "mac_filters", "name", "partner_tenant_id", "reference_id", "spaces_tenant_id", "spaces_tenant_name"]
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    IOT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    MAC_FILTERS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARTNER_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACES_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACES_TENANT_NAME_FIELD_NUMBER: _ClassVar[int]
    instance_name: str
    iot_groups: _containers.RepeatedScalarFieldContainer[str]
    mac_filters: _containers.RepeatedScalarFieldContainer[str]
    name: str
    partner_tenant_id: str
    reference_id: str
    spaces_tenant_id: str
    spaces_tenant_name: str
    def __init__(self, spaces_tenant_name: _Optional[str] = ..., spaces_tenant_id: _Optional[str] = ..., partner_tenant_id: _Optional[str] = ..., name: _Optional[str] = ..., reference_id: _Optional[str] = ..., instance_name: _Optional[str] = ..., mac_filters: _Optional[_Iterable[str]] = ..., iot_groups: _Optional[_Iterable[str]] = ...) -> None: ...

class Attribute(_message.Message):
    __slots__ = ["name", "values"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    name: str
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...

class CCXData(_message.Message):
    __slots__ = ["battery", "last_beacon_sequence_number", "last_beacon_time", "telemetries", "vendor"]
    class Battery(_message.Message):
        __slots__ = ["age", "days_remaining", "last_received_seq_num", "last_received_time", "percent_remaining", "tolerance"]
        AGE_FIELD_NUMBER: _ClassVar[int]
        DAYS_REMAINING_FIELD_NUMBER: _ClassVar[int]
        LAST_RECEIVED_SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
        LAST_RECEIVED_TIME_FIELD_NUMBER: _ClassVar[int]
        PERCENT_REMAINING_FIELD_NUMBER: _ClassVar[int]
        TOLERANCE_FIELD_NUMBER: _ClassVar[int]
        age: int
        days_remaining: int
        last_received_seq_num: int
        last_received_time: int
        percent_remaining: int
        tolerance: int
        def __init__(self, tolerance: _Optional[int] = ..., percent_remaining: _Optional[int] = ..., days_remaining: _Optional[int] = ..., age: _Optional[int] = ..., last_received_time: _Optional[int] = ..., last_received_seq_num: _Optional[int] = ...) -> None: ...
    class Telemetry(_message.Message):
        __slots__ = ["last_received_seq_num", "last_received_time", "type", "unit", "value"]
        class CCXTelemetryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        CCX_TELEMETRY_DISTANCE: CCXData.Telemetry.CCXTelemetryType
        CCX_TELEMETRY_EPC: CCXData.Telemetry.CCXTelemetryType
        CCX_TELEMETRY_FUEL: CCXData.Telemetry.CCXTelemetryType
        CCX_TELEMETRY_GPS: CCXData.Telemetry.CCXTelemetryType
        CCX_TELEMETRY_HUMIDITY: CCXData.Telemetry.CCXTelemetryType
        CCX_TELEMETRY_MOTION: CCXData.Telemetry.CCXTelemetryType
        CCX_TELEMETRY_MOTIONPROB: CCXData.Telemetry.CCXTelemetryType
        CCX_TELEMETRY_PRESSURE: CCXData.Telemetry.CCXTelemetryType
        CCX_TELEMETRY_QUANTITY: CCXData.Telemetry.CCXTelemetryType
        CCX_TELEMETRY_STATUS: CCXData.Telemetry.CCXTelemetryType
        CCX_TELEMETRY_TEMPERATURE: CCXData.Telemetry.CCXTelemetryType
        CCX_TELEMETRY_UNKNOWN: CCXData.Telemetry.CCXTelemetryType
        LAST_RECEIVED_SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
        LAST_RECEIVED_TIME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        UNIT_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        last_received_seq_num: int
        last_received_time: int
        type: CCXData.Telemetry.CCXTelemetryType
        unit: str
        value: str
        def __init__(self, type: _Optional[_Union[CCXData.Telemetry.CCXTelemetryType, str]] = ..., unit: _Optional[str] = ..., value: _Optional[str] = ..., last_received_time: _Optional[int] = ..., last_received_seq_num: _Optional[int] = ...) -> None: ...
    class Vendor(_message.Message):
        __slots__ = ["data", "element_id", "id", "last_received_seq_num", "last_received_time"]
        DATA_FIELD_NUMBER: _ClassVar[int]
        ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        LAST_RECEIVED_SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
        LAST_RECEIVED_TIME_FIELD_NUMBER: _ClassVar[int]
        data: bytes
        element_id: int
        id: int
        last_received_seq_num: int
        last_received_time: int
        def __init__(self, id: _Optional[int] = ..., element_id: _Optional[int] = ..., data: _Optional[bytes] = ..., last_received_time: _Optional[int] = ..., last_received_seq_num: _Optional[int] = ...) -> None: ...
    BATTERY_FIELD_NUMBER: _ClassVar[int]
    LAST_BEACON_SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LAST_BEACON_TIME_FIELD_NUMBER: _ClassVar[int]
    TELEMETRIES_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    battery: CCXData.Battery
    last_beacon_sequence_number: int
    last_beacon_time: int
    telemetries: _containers.RepeatedCompositeFieldContainer[CCXData.Telemetry]
    vendor: CCXData.Vendor
    def __init__(self, telemetries: _Optional[_Iterable[_Union[CCXData.Telemetry, _Mapping]]] = ..., battery: _Optional[_Union[CCXData.Battery, _Mapping]] = ..., vendor: _Optional[_Union[CCXData.Vendor, _Mapping]] = ..., last_beacon_time: _Optional[int] = ..., last_beacon_sequence_number: _Optional[int] = ...) -> None: ...

class CameraCounts(_message.Message):
    __slots__ = ["count", "count_delta", "location"]
    COUNT_DELTA_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    count: int
    count_delta: int
    location: Location
    def __init__(self, location: _Optional[_Union[Location, _Mapping]] = ..., count: _Optional[int] = ..., count_delta: _Optional[int] = ...) -> None: ...

class Device(_message.Message):
    __slots__ = ["attributes", "device_id", "device_model", "dhcp_profile_info", "email", "first_name", "gender", "last_name", "mac_address", "manufacturer", "mobile", "opt_ins", "os", "os_version", "postal_code", "social_network_info", "tags", "type", "user_id"]
    class OptIn(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class DHCPProfileInfo(_message.Message):
        __slots__ = ["dc_certainty_metric", "dc_device_class_tag", "dc_profile_name", "dc_protocol_map"]
        DC_CERTAINTY_METRIC_FIELD_NUMBER: _ClassVar[int]
        DC_DEVICE_CLASS_TAG_FIELD_NUMBER: _ClassVar[int]
        DC_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
        DC_PROTOCOL_MAP_FIELD_NUMBER: _ClassVar[int]
        dc_certainty_metric: str
        dc_device_class_tag: str
        dc_profile_name: str
        dc_protocol_map: str
        def __init__(self, dc_profile_name: _Optional[str] = ..., dc_device_class_tag: _Optional[str] = ..., dc_certainty_metric: _Optional[str] = ..., dc_protocol_map: _Optional[str] = ...) -> None: ...
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MODEL_FIELD_NUMBER: _ClassVar[int]
    DHCP_PROFILE_INFO_FIELD_NUMBER: _ClassVar[int]
    EMAIL: Device.OptIn
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    MOBILE_NUMBER: Device.OptIn
    OPT_INS_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    SOCIAL_NETWORK_INFO_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TERMS_AND_CONDITIONS: Device.OptIn
    TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[Attribute]
    device_id: str
    device_model: str
    dhcp_profile_info: Device.DHCPProfileInfo
    email: str
    first_name: str
    gender: Gender
    last_name: str
    mac_address: str
    manufacturer: str
    mobile: str
    opt_ins: _containers.RepeatedScalarFieldContainer[Device.OptIn]
    os: str
    os_version: str
    postal_code: str
    social_network_info: _containers.RepeatedCompositeFieldContainer[SocialNetworkInfo]
    tags: _containers.RepeatedScalarFieldContainer[str]
    type: DeviceType
    user_id: str
    def __init__(self, device_id: _Optional[str] = ..., user_id: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., mobile: _Optional[str] = ..., email: _Optional[str] = ..., gender: _Optional[_Union[Gender, str]] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., postal_code: _Optional[str] = ..., opt_ins: _Optional[_Iterable[_Union[Device.OptIn, str]]] = ..., attributes: _Optional[_Iterable[_Union[Attribute, _Mapping]]] = ..., mac_address: _Optional[str] = ..., manufacturer: _Optional[str] = ..., os: _Optional[str] = ..., os_version: _Optional[str] = ..., type: _Optional[_Union[DeviceType, str]] = ..., social_network_info: _Optional[_Iterable[_Union[SocialNetworkInfo, _Mapping]]] = ..., device_model: _Optional[str] = ..., dhcp_profile_info: _Optional[_Union[Device.DHCPProfileInfo, _Mapping]] = ...) -> None: ...

class DeviceCounts(_message.Message):
    __slots__ = ["associated_count", "associated_delta", "ble_tag_count", "estimated_capacity_percentage", "estimated_density", "estimated_probing_count", "location", "probing_delta", "probing_randomized_percentage", "rfid_tag_count", "user_count", "wired_user_count", "wireless_user_count"]
    ASSOCIATED_COUNT_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_DELTA_FIELD_NUMBER: _ClassVar[int]
    BLE_TAG_COUNT_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_CAPACITY_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_DENSITY_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_PROBING_COUNT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PROBING_DELTA_FIELD_NUMBER: _ClassVar[int]
    PROBING_RANDOMIZED_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    RFID_TAG_COUNT_FIELD_NUMBER: _ClassVar[int]
    USER_COUNT_FIELD_NUMBER: _ClassVar[int]
    WIRED_USER_COUNT_FIELD_NUMBER: _ClassVar[int]
    WIRELESS_USER_COUNT_FIELD_NUMBER: _ClassVar[int]
    associated_count: int
    associated_delta: int
    ble_tag_count: int
    estimated_capacity_percentage: float
    estimated_density: float
    estimated_probing_count: int
    location: Location
    probing_delta: int
    probing_randomized_percentage: float
    rfid_tag_count: int
    user_count: int
    wired_user_count: int
    wireless_user_count: int
    def __init__(self, location: _Optional[_Union[Location, _Mapping]] = ..., associated_count: _Optional[int] = ..., estimated_probing_count: _Optional[int] = ..., probing_randomized_percentage: _Optional[float] = ..., associated_delta: _Optional[int] = ..., probing_delta: _Optional[int] = ..., estimated_density: _Optional[float] = ..., estimated_capacity_percentage: _Optional[float] = ..., user_count: _Optional[int] = ..., wireless_user_count: _Optional[int] = ..., wired_user_count: _Optional[int] = ..., rfid_tag_count: _Optional[int] = ..., ble_tag_count: _Optional[int] = ...) -> None: ...

class DeviceEntry(_message.Message):
    __slots__ = ["days_since_last_visit", "device", "device_classification", "entry_date_time", "entry_timestamp", "location", "time_zone", "visit_id"]
    DAYS_SINCE_LAST_VISIT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    ENTRY_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ENTRY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    VISIT_ID_FIELD_NUMBER: _ClassVar[int]
    days_since_last_visit: int
    device: Device
    device_classification: str
    entry_date_time: str
    entry_timestamp: int
    location: Location
    time_zone: str
    visit_id: str
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., visit_id: _Optional[str] = ..., entry_timestamp: _Optional[int] = ..., entry_date_time: _Optional[str] = ..., time_zone: _Optional[str] = ..., device_classification: _Optional[str] = ..., days_since_last_visit: _Optional[int] = ...) -> None: ...

class DeviceExit(_message.Message):
    __slots__ = ["device", "device_classification", "entry_date_time", "entry_timestamp", "exit_date_time", "exit_timestamp", "location", "time_zone", "visit_classification", "visit_duration_minutes", "visit_id"]
    DEVICE_CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    ENTRY_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ENTRY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EXIT_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXIT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    VISIT_CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    VISIT_DURATION_MINUTES_FIELD_NUMBER: _ClassVar[int]
    VISIT_ID_FIELD_NUMBER: _ClassVar[int]
    device: Device
    device_classification: str
    entry_date_time: str
    entry_timestamp: int
    exit_date_time: str
    exit_timestamp: int
    location: Location
    time_zone: str
    visit_classification: str
    visit_duration_minutes: int
    visit_id: str
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., visit_id: _Optional[str] = ..., visit_duration_minutes: _Optional[int] = ..., entry_timestamp: _Optional[int] = ..., entry_date_time: _Optional[str] = ..., exit_timestamp: _Optional[int] = ..., exit_date_time: _Optional[str] = ..., time_zone: _Optional[str] = ..., device_classification: _Optional[str] = ..., visit_classification: _Optional[str] = ...) -> None: ...

class DeviceInfo(_message.Message):
    __slots__ = ["company_id", "device_id", "device_mac_address", "device_name", "device_type", "firmware_version", "group", "label", "manufacturer", "raw_device_id", "service_uuid"]
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    RAW_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_UUID_FIELD_NUMBER: _ClassVar[int]
    company_id: str
    device_id: str
    device_mac_address: str
    device_name: str
    device_type: IOTDeviceType
    firmware_version: str
    group: _containers.RepeatedScalarFieldContainer[str]
    label: str
    manufacturer: str
    raw_device_id: str
    service_uuid: str
    def __init__(self, device_type: _Optional[_Union[IOTDeviceType, str]] = ..., device_id: _Optional[str] = ..., device_mac_address: _Optional[str] = ..., group: _Optional[_Iterable[str]] = ..., device_name: _Optional[str] = ..., firmware_version: _Optional[str] = ..., raw_device_id: _Optional[str] = ..., manufacturer: _Optional[str] = ..., company_id: _Optional[str] = ..., service_uuid: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...

class DeviceLocation(_message.Message):
    __slots__ = ["confidence_factor", "device", "device_classification", "ipv4", "ipv6", "last_seen", "latitude", "location", "longitude", "map_id", "max_detected_rssi", "raw_user_id", "ssid", "unc", "visit_id", "x_pos", "y_pos"]
    CONFIDENCE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    IPV4_FIELD_NUMBER: _ClassVar[int]
    IPV6_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    MAP_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_DETECTED_RSSI_FIELD_NUMBER: _ClassVar[int]
    RAW_USER_ID_FIELD_NUMBER: _ClassVar[int]
    SSID_FIELD_NUMBER: _ClassVar[int]
    UNC_FIELD_NUMBER: _ClassVar[int]
    VISIT_ID_FIELD_NUMBER: _ClassVar[int]
    X_POS_FIELD_NUMBER: _ClassVar[int]
    Y_POS_FIELD_NUMBER: _ClassVar[int]
    confidence_factor: float
    device: Device
    device_classification: str
    ipv4: str
    ipv6: _containers.RepeatedScalarFieldContainer[str]
    last_seen: int
    latitude: float
    location: Location
    longitude: float
    map_id: str
    max_detected_rssi: int
    raw_user_id: str
    ssid: str
    unc: float
    visit_id: str
    x_pos: float
    y_pos: float
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., ssid: _Optional[str] = ..., raw_user_id: _Optional[str] = ..., visit_id: _Optional[str] = ..., last_seen: _Optional[int] = ..., device_classification: _Optional[str] = ..., map_id: _Optional[str] = ..., x_pos: _Optional[float] = ..., y_pos: _Optional[float] = ..., confidence_factor: _Optional[float] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., unc: _Optional[float] = ..., max_detected_rssi: _Optional[int] = ..., ipv4: _Optional[str] = ..., ipv6: _Optional[_Iterable[str]] = ...) -> None: ...

class DevicePosition(_message.Message):
    __slots__ = ["confidence_factor", "last_located_time", "latitude", "location_id", "longitude", "map_id", "x_pos", "y_pos"]
    CONFIDENCE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    LAST_LOCATED_TIME_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    MAP_ID_FIELD_NUMBER: _ClassVar[int]
    X_POS_FIELD_NUMBER: _ClassVar[int]
    Y_POS_FIELD_NUMBER: _ClassVar[int]
    confidence_factor: float
    last_located_time: int
    latitude: float
    location_id: str
    longitude: float
    map_id: str
    x_pos: float
    y_pos: float
    def __init__(self, x_pos: _Optional[float] = ..., y_pos: _Optional[float] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., confidence_factor: _Optional[float] = ..., map_id: _Optional[str] = ..., location_id: _Optional[str] = ..., last_located_time: _Optional[int] = ...) -> None: ...

class DevicePresence(_message.Message):
    __slots__ = ["active_devices_count", "days_since_last_visit", "device", "device_classification", "entry_date_time", "entry_timestamp", "exit_date_time", "exit_timestamp", "in_active_devices_count", "location", "presence_event_type", "raw_user_id", "ssid", "time_zone", "visit_classification", "visit_duration_minutes", "visit_id", "was_in_active"]
    ACTIVE_DEVICES_COUNT_FIELD_NUMBER: _ClassVar[int]
    DAYS_SINCE_LAST_VISIT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    ENTRY_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ENTRY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EXIT_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXIT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IN_ACTIVE_DEVICES_COUNT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PRESENCE_EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RAW_USER_ID_FIELD_NUMBER: _ClassVar[int]
    SSID_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    VISIT_CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    VISIT_DURATION_MINUTES_FIELD_NUMBER: _ClassVar[int]
    VISIT_ID_FIELD_NUMBER: _ClassVar[int]
    WAS_IN_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    active_devices_count: int
    days_since_last_visit: int
    device: Device
    device_classification: str
    entry_date_time: str
    entry_timestamp: int
    exit_date_time: str
    exit_timestamp: int
    in_active_devices_count: int
    location: Location
    presence_event_type: DevicePresenceEventType
    raw_user_id: str
    ssid: str
    time_zone: str
    visit_classification: str
    visit_duration_minutes: int
    visit_id: str
    was_in_active: bool
    def __init__(self, presence_event_type: _Optional[_Union[DevicePresenceEventType, str]] = ..., was_in_active: bool = ..., device: _Optional[_Union[Device, _Mapping]] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., ssid: _Optional[str] = ..., raw_user_id: _Optional[str] = ..., visit_id: _Optional[str] = ..., days_since_last_visit: _Optional[int] = ..., entry_timestamp: _Optional[int] = ..., entry_date_time: _Optional[str] = ..., exit_timestamp: _Optional[int] = ..., exit_date_time: _Optional[str] = ..., visit_duration_minutes: _Optional[int] = ..., time_zone: _Optional[str] = ..., device_classification: _Optional[str] = ..., visit_classification: _Optional[str] = ..., active_devices_count: _Optional[int] = ..., in_active_devices_count: _Optional[int] = ...) -> None: ...

class DeviceProfileData(_message.Message):
    __slots__ = ["add_tags", "attributes", "email", "first_name", "gender", "last_name", "mobile", "remove_tags", "social_network_info", "type"]
    ADD_TAGS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_TAGS_FIELD_NUMBER: _ClassVar[int]
    SOCIAL_NETWORK_INFO_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    add_tags: _containers.RepeatedScalarFieldContainer[str]
    attributes: _containers.RepeatedCompositeFieldContainer[Attribute]
    email: EmailInfo
    first_name: str
    gender: Gender
    last_name: str
    mobile: MobileInfo
    remove_tags: _containers.RepeatedScalarFieldContainer[str]
    social_network_info: _containers.RepeatedCompositeFieldContainer[SocialNetworkInfo]
    type: DeviceType
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., gender: _Optional[_Union[Gender, str]] = ..., mobile: _Optional[_Union[MobileInfo, _Mapping]] = ..., email: _Optional[_Union[EmailInfo, _Mapping]] = ..., social_network_info: _Optional[_Iterable[_Union[SocialNetworkInfo, _Mapping]]] = ..., type: _Optional[_Union[DeviceType, str]] = ..., add_tags: _Optional[_Iterable[str]] = ..., remove_tags: _Optional[_Iterable[str]] = ..., attributes: _Optional[_Iterable[_Union[Attribute, _Mapping]]] = ...) -> None: ...

class Dimension(_message.Message):
    __slots__ = ["height", "length", "offset_x", "offset_y", "width"]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_X_FIELD_NUMBER: _ClassVar[int]
    OFFSET_Y_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    height: float
    length: float
    offset_x: float
    offset_y: float
    width: float
    def __init__(self, length: _Optional[float] = ..., width: _Optional[float] = ..., height: _Optional[float] = ..., offset_x: _Optional[float] = ..., offset_y: _Optional[float] = ...) -> None: ...

class EmailInfo(_message.Message):
    __slots__ = ["address", "opted_in", "verified"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    OPTED_IN_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    address: str
    opted_in: bool
    verified: bool
    def __init__(self, address: _Optional[str] = ..., verified: bool = ..., opted_in: bool = ...) -> None: ...

class EventRecord(_message.Message):
    __slots__ = ["account_admin_change", "app_activation", "camera_counts", "device_counts", "device_entry", "device_exit", "device_location_update", "device_presence", "device_profile_update", "event_type", "iot_telemetry", "iot_user_action", "location_anchor_update", "location_hierarchy_change", "network_status_update", "network_telemetry", "partner_tenant_id", "raw_camera_counts", "record_timestamp", "record_uid", "spaces_tenant_id", "spaces_tenant_name", "tp_people_count_update", "user_presence"]
    ACCOUNT_ADMIN_CHANGE_FIELD_NUMBER: _ClassVar[int]
    APP_ACTIVATION_FIELD_NUMBER: _ClassVar[int]
    CAMERA_COUNTS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COUNTS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ENTRY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_EXIT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LOCATION_UPDATE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PRESENCE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PROFILE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    IOT_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    IOT_USER_ACTION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ANCHOR_UPDATE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_HIERARCHY_CHANGE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_STATUS_UPDATE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    PARTNER_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    RAW_CAMERA_COUNTS_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RECORD_UID_FIELD_NUMBER: _ClassVar[int]
    SPACES_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACES_TENANT_NAME_FIELD_NUMBER: _ClassVar[int]
    TP_PEOPLE_COUNT_UPDATE_FIELD_NUMBER: _ClassVar[int]
    USER_PRESENCE_FIELD_NUMBER: _ClassVar[int]
    account_admin_change: AccountAdminChange
    app_activation: AppActivation
    camera_counts: CameraCounts
    device_counts: DeviceCounts
    device_entry: DeviceEntry
    device_exit: DeviceExit
    device_location_update: DeviceLocation
    device_presence: DevicePresence
    device_profile_update: Device
    event_type: EventType
    iot_telemetry: IOTTelemetry
    iot_user_action: IOTUserAction
    location_anchor_update: LocationAnchorUpdate
    location_hierarchy_change: LocationChange
    network_status_update: NetworkStatusUpdate
    network_telemetry: NetworkTelemetry
    partner_tenant_id: str
    raw_camera_counts: RawCameraCounts
    record_timestamp: int
    record_uid: str
    spaces_tenant_id: str
    spaces_tenant_name: str
    tp_people_count_update: TPPeopleCountUpdate
    user_presence: UserPresence
    def __init__(self, record_uid: _Optional[str] = ..., record_timestamp: _Optional[int] = ..., spaces_tenant_id: _Optional[str] = ..., spaces_tenant_name: _Optional[str] = ..., partner_tenant_id: _Optional[str] = ..., event_type: _Optional[_Union[EventType, str]] = ..., device_entry: _Optional[_Union[DeviceEntry, _Mapping]] = ..., device_exit: _Optional[_Union[DeviceExit, _Mapping]] = ..., device_profile_update: _Optional[_Union[Device, _Mapping]] = ..., location_hierarchy_change: _Optional[_Union[LocationChange, _Mapping]] = ..., device_location_update: _Optional[_Union[DeviceLocation, _Mapping]] = ..., app_activation: _Optional[_Union[AppActivation, _Mapping]] = ..., account_admin_change: _Optional[_Union[AccountAdminChange, _Mapping]] = ..., tp_people_count_update: _Optional[_Union[TPPeopleCountUpdate, _Mapping]] = ..., device_presence: _Optional[_Union[DevicePresence, _Mapping]] = ..., user_presence: _Optional[_Union[UserPresence, _Mapping]] = ..., iot_telemetry: _Optional[_Union[IOTTelemetry, _Mapping]] = ..., iot_user_action: _Optional[_Union[IOTUserAction, _Mapping]] = ..., device_counts: _Optional[_Union[DeviceCounts, _Mapping]] = ..., camera_counts: _Optional[_Union[CameraCounts, _Mapping]] = ..., raw_camera_counts: _Optional[_Union[RawCameraCounts, _Mapping]] = ..., network_telemetry: _Optional[_Union[NetworkTelemetry, _Mapping]] = ..., location_anchor_update: _Optional[_Union[LocationAnchorUpdate, _Mapping]] = ..., network_status_update: _Optional[_Union[NetworkStatusUpdate, _Mapping]] = ...) -> None: ...

class EventsStreamRequest(_message.Message):
    __slots__ = ["from_timestamp", "max_partition", "min_partition", "replica_id"]
    FROM_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MAX_PARTITION_FIELD_NUMBER: _ClassVar[int]
    MIN_PARTITION_FIELD_NUMBER: _ClassVar[int]
    REPLICA_ID_FIELD_NUMBER: _ClassVar[int]
    from_timestamp: int
    max_partition: int
    min_partition: int
    replica_id: int
    def __init__(self, min_partition: _Optional[int] = ..., max_partition: _Optional[int] = ..., from_timestamp: _Optional[int] = ..., replica_id: _Optional[int] = ...) -> None: ...

class Facebook(_message.Message):
    __slots__ = ["attributes", "email", "first_name", "id", "last_name", "middle_name", "name", "name_format", "picture", "short_name"]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    MIDDLE_NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FORMAT_FIELD_NUMBER: _ClassVar[int]
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[Attribute]
    email: str
    first_name: str
    id: str
    last_name: str
    middle_name: str
    name: str
    name_format: str
    picture: str
    short_name: str
    def __init__(self, id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., middle_name: _Optional[str] = ..., name: _Optional[str] = ..., short_name: _Optional[str] = ..., name_format: _Optional[str] = ..., picture: _Optional[str] = ..., email: _Optional[str] = ..., attributes: _Optional[_Iterable[_Union[Attribute, _Mapping]]] = ...) -> None: ...

class FloorMap(_message.Message):
    __slots__ = ["image_data", "map_details"]
    IMAGE_DATA_FIELD_NUMBER: _ClassVar[int]
    MAP_DETAILS_FIELD_NUMBER: _ClassVar[int]
    image_data: bytes
    map_details: MapDetails
    def __init__(self, map_details: _Optional[_Union[MapDetails, _Mapping]] = ..., image_data: _Optional[bytes] = ...) -> None: ...

class FloorMapRequest(_message.Message):
    __slots__ = ["map_id", "partner_tenant_id"]
    MAP_ID_FIELD_NUMBER: _ClassVar[int]
    PARTNER_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    map_id: str
    partner_tenant_id: str
    def __init__(self, map_id: _Optional[str] = ..., partner_tenant_id: _Optional[str] = ...) -> None: ...

class GetDeviceRequest(_message.Message):
    __slots__ = ["device_id", "mac_address", "partner_tenant_id"]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PARTNER_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    mac_address: str
    partner_tenant_id: str
    def __init__(self, partner_tenant_id: _Optional[str] = ..., mac_address: _Optional[str] = ..., device_id: _Optional[str] = ...) -> None: ...

class IOTTelemetry(_message.Message):
    __slots__ = ["accelerometer", "air_pressure", "air_quality", "ambient_light", "battery", "carbon_emissions", "ccx_data", "detected_position", "device_info", "device_rtc_time", "eddy_stone", "humidity", "i_beacon", "illum_sensor", "illum_solar_cell", "illuminance", "last_user_action", "location", "magnet_contact", "max_detected_rssi", "occupancy_status", "pir_trigger", "placed_position", "push_button", "raw_header", "raw_payload", "sequence_num", "temperature", "tp_data", "vendor_info", "voltage"]
    class PushButtonAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Accelerometer(_message.Message):
        __slots__ = ["counter", "last_movement_timestamp", "x", "y", "z"]
        COUNTER_FIELD_NUMBER: _ClassVar[int]
        LAST_MOVEMENT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        X_FIELD_NUMBER: _ClassVar[int]
        Y_FIELD_NUMBER: _ClassVar[int]
        Z_FIELD_NUMBER: _ClassVar[int]
        counter: int
        last_movement_timestamp: int
        x: float
        y: float
        z: float
        def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., last_movement_timestamp: _Optional[int] = ..., counter: _Optional[int] = ...) -> None: ...
    class AirPressure(_message.Message):
        __slots__ = ["pressure"]
        PRESSURE_FIELD_NUMBER: _ClassVar[int]
        pressure: float
        def __init__(self, pressure: _Optional[float] = ...) -> None: ...
    class AirQuality(_message.Message):
        __slots__ = ["air_quality_index", "air_quality_ppb", "air_quality_status"]
        AIR_QUALITY_INDEX_FIELD_NUMBER: _ClassVar[int]
        AIR_QUALITY_PPB_FIELD_NUMBER: _ClassVar[int]
        AIR_QUALITY_STATUS_FIELD_NUMBER: _ClassVar[int]
        air_quality_index: float
        air_quality_ppb: int
        air_quality_status: str
        def __init__(self, air_quality_index: _Optional[float] = ..., air_quality_ppb: _Optional[int] = ..., air_quality_status: _Optional[str] = ...) -> None: ...
    class AmbientLight(_message.Message):
        __slots__ = ["value_lx"]
        VALUE_LX_FIELD_NUMBER: _ClassVar[int]
        value_lx: int
        def __init__(self, value_lx: _Optional[int] = ...) -> None: ...
    class Battery(_message.Message):
        __slots__ = ["last_retrieved", "unit", "value"]
        class BatteryUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        LAST_RETRIEVED_FIELD_NUMBER: _ClassVar[int]
        MILLI_VOLTS: IOTTelemetry.Battery.BatteryUnit
        PERCENTAGE: IOTTelemetry.Battery.BatteryUnit
        UNIT_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        last_retrieved: int
        unit: IOTTelemetry.Battery.BatteryUnit
        value: float
        def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[IOTTelemetry.Battery.BatteryUnit, str]] = ..., last_retrieved: _Optional[int] = ...) -> None: ...
    class CarbonEmissions(_message.Message):
        __slots__ = ["co2_ppm"]
        CO2_PPM_FIELD_NUMBER: _ClassVar[int]
        co2_ppm: int
        def __init__(self, co2_ppm: _Optional[int] = ...) -> None: ...
    class Eddystone(_message.Message):
        __slots__ = ["beacon_mac_address", "namespace", "uid", "url"]
        BEACON_MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        NAMESPACE_FIELD_NUMBER: _ClassVar[int]
        UID_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        beacon_mac_address: str
        namespace: str
        uid: str
        url: str
        def __init__(self, beacon_mac_address: _Optional[str] = ..., uid: _Optional[str] = ..., namespace: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
    class Humidity(_message.Message):
        __slots__ = ["humidity_in_percentage", "raw_humidity"]
        HUMIDITY_IN_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        RAW_HUMIDITY_FIELD_NUMBER: _ClassVar[int]
        humidity_in_percentage: int
        raw_humidity: int
        def __init__(self, humidity_in_percentage: _Optional[int] = ..., raw_humidity: _Optional[int] = ...) -> None: ...
    class IllumSensor(_message.Message):
        __slots__ = ["value_lx"]
        VALUE_LX_FIELD_NUMBER: _ClassVar[int]
        value_lx: int
        def __init__(self, value_lx: _Optional[int] = ...) -> None: ...
    class IllumSolarCell(_message.Message):
        __slots__ = ["value_lx"]
        VALUE_LX_FIELD_NUMBER: _ClassVar[int]
        value_lx: int
        def __init__(self, value_lx: _Optional[int] = ...) -> None: ...
    class Illuminance(_message.Message):
        __slots__ = ["unit", "value"]
        class IlluminanceUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        LUX: IOTTelemetry.Illuminance.IlluminanceUnit
        PERCENTAGE: IOTTelemetry.Illuminance.IlluminanceUnit
        UNIT_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        unit: IOTTelemetry.Illuminance.IlluminanceUnit
        value: float
        def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[IOTTelemetry.Illuminance.IlluminanceUnit, str]] = ...) -> None: ...
    class LastUserAction(_message.Message):
        __slots__ = ["timestamp", "type"]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        timestamp: int
        type: IOTActionType
        def __init__(self, type: _Optional[_Union[IOTActionType, str]] = ..., timestamp: _Optional[int] = ...) -> None: ...
    class MagnetContact(_message.Message):
        __slots__ = ["contact_type"]
        class ContactType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        CLOSED: IOTTelemetry.MagnetContact.ContactType
        CONTACT_TYPE_FIELD_NUMBER: _ClassVar[int]
        OPEN: IOTTelemetry.MagnetContact.ContactType
        contact_type: IOTTelemetry.MagnetContact.ContactType
        def __init__(self, contact_type: _Optional[_Union[IOTTelemetry.MagnetContact.ContactType, str]] = ...) -> None: ...
    class OccupancyStatus(_message.Message):
        __slots__ = ["status"]
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        NOT_OCCUPIED: IOTTelemetry.OccupancyStatus.Status
        OCCUPIED: IOTTelemetry.OccupancyStatus.Status
        STATUS_FIELD_NUMBER: _ClassVar[int]
        status: IOTTelemetry.OccupancyStatus.Status
        def __init__(self, status: _Optional[_Union[IOTTelemetry.OccupancyStatus.Status, str]] = ...) -> None: ...
    class PIRTrigger(_message.Message):
        __slots__ = ["timestamp"]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        timestamp: int
        def __init__(self, timestamp: _Optional[int] = ...) -> None: ...
    class PushButton(_message.Message):
        __slots__ = ["action", "action_button_labels"]
        ACTION_BUTTON_LABELS_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        action: IOTTelemetry.PushButtonAction
        action_button_labels: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, action: _Optional[_Union[IOTTelemetry.PushButtonAction, str]] = ..., action_button_labels: _Optional[_Iterable[str]] = ...) -> None: ...
    class TPData(_message.Message):
        __slots__ = ["active_calls", "air_quality_index", "air_quality_status", "ambient_light", "ambient_noise", "close_proximity", "dryness_score", "humidity_in_percentage", "people_count", "presence", "presentation_state", "reverberation_time", "sound_level", "standby_state", "temperature_in_celsius", "time_stamp"]
        ACTIVE_CALLS_FIELD_NUMBER: _ClassVar[int]
        AIR_QUALITY_INDEX_FIELD_NUMBER: _ClassVar[int]
        AIR_QUALITY_STATUS_FIELD_NUMBER: _ClassVar[int]
        AMBIENT_LIGHT_FIELD_NUMBER: _ClassVar[int]
        AMBIENT_NOISE_FIELD_NUMBER: _ClassVar[int]
        CLOSE_PROXIMITY_FIELD_NUMBER: _ClassVar[int]
        DRYNESS_SCORE_FIELD_NUMBER: _ClassVar[int]
        HUMIDITY_IN_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        PEOPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
        PRESENCE_FIELD_NUMBER: _ClassVar[int]
        PRESENTATION_STATE_FIELD_NUMBER: _ClassVar[int]
        REVERBERATION_TIME_FIELD_NUMBER: _ClassVar[int]
        SOUND_LEVEL_FIELD_NUMBER: _ClassVar[int]
        STANDBY_STATE_FIELD_NUMBER: _ClassVar[int]
        TEMPERATURE_IN_CELSIUS_FIELD_NUMBER: _ClassVar[int]
        TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
        active_calls: int
        air_quality_index: float
        air_quality_status: str
        ambient_light: str
        ambient_noise: int
        close_proximity: bool
        dryness_score: int
        humidity_in_percentage: int
        people_count: int
        presence: bool
        presentation_state: int
        reverberation_time: int
        sound_level: int
        standby_state: int
        temperature_in_celsius: float
        time_stamp: int
        def __init__(self, presence: bool = ..., people_count: _Optional[int] = ..., standby_state: _Optional[int] = ..., ambient_noise: _Optional[int] = ..., dryness_score: _Optional[int] = ..., active_calls: _Optional[int] = ..., presentation_state: _Optional[int] = ..., time_stamp: _Optional[int] = ..., air_quality_index: _Optional[float] = ..., temperature_in_celsius: _Optional[float] = ..., humidity_in_percentage: _Optional[int] = ..., sound_level: _Optional[int] = ..., ambient_light: _Optional[str] = ..., reverberation_time: _Optional[int] = ..., close_proximity: bool = ..., air_quality_status: _Optional[str] = ...) -> None: ...
    class Temperature(_message.Message):
        __slots__ = ["raw_temperature", "temperature_in_celsius"]
        RAW_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
        TEMPERATURE_IN_CELSIUS_FIELD_NUMBER: _ClassVar[int]
        raw_temperature: float
        temperature_in_celsius: float
        def __init__(self, temperature_in_celsius: _Optional[float] = ..., raw_temperature: _Optional[float] = ...) -> None: ...
    class VendorInfo(_message.Message):
        __slots__ = ["manufacturer_id"]
        MANUFACTURER_ID_FIELD_NUMBER: _ClassVar[int]
        manufacturer_id: int
        def __init__(self, manufacturer_id: _Optional[int] = ...) -> None: ...
    class Voltage(_message.Message):
        __slots__ = ["value_mv"]
        VALUE_MV_FIELD_NUMBER: _ClassVar[int]
        value_mv: float
        def __init__(self, value_mv: _Optional[float] = ...) -> None: ...
    class iBeacon(_message.Message):
        __slots__ = ["advertized_tx_power", "beacon_mac_address", "major", "minor", "uuid"]
        ADVERTIZED_TX_POWER_FIELD_NUMBER: _ClassVar[int]
        BEACON_MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        MAJOR_FIELD_NUMBER: _ClassVar[int]
        MINOR_FIELD_NUMBER: _ClassVar[int]
        UUID_FIELD_NUMBER: _ClassVar[int]
        advertized_tx_power: int
        beacon_mac_address: str
        major: int
        minor: int
        uuid: str
        def __init__(self, beacon_mac_address: _Optional[str] = ..., uuid: _Optional[str] = ..., major: _Optional[int] = ..., minor: _Optional[int] = ..., advertized_tx_power: _Optional[int] = ...) -> None: ...
    ACCELEROMETER_FIELD_NUMBER: _ClassVar[int]
    AIR_PRESSURE_FIELD_NUMBER: _ClassVar[int]
    AIR_QUALITY_FIELD_NUMBER: _ClassVar[int]
    AMBIENT_LIGHT_FIELD_NUMBER: _ClassVar[int]
    BATTERY_FIELD_NUMBER: _ClassVar[int]
    CARBON_EMISSIONS_FIELD_NUMBER: _ClassVar[int]
    CCX_DATA_FIELD_NUMBER: _ClassVar[int]
    DETECTED_POSITION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    DEVICE_RTC_TIME_FIELD_NUMBER: _ClassVar[int]
    EDDY_STONE_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    ILLUMINANCE_FIELD_NUMBER: _ClassVar[int]
    ILLUM_SENSOR_FIELD_NUMBER: _ClassVar[int]
    ILLUM_SOLAR_CELL_FIELD_NUMBER: _ClassVar[int]
    I_BEACON_FIELD_NUMBER: _ClassVar[int]
    LAST_USER_ACTION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    MAGNET_CONTACT_FIELD_NUMBER: _ClassVar[int]
    MAX_DETECTED_RSSI_FIELD_NUMBER: _ClassVar[int]
    OCCUPANCY_STATUS_FIELD_NUMBER: _ClassVar[int]
    PBA_PRESS: IOTTelemetry.PushButtonAction
    PBA_RELEASE: IOTTelemetry.PushButtonAction
    PIR_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    PLACED_POSITION_FIELD_NUMBER: _ClassVar[int]
    PUSH_BUTTON_FIELD_NUMBER: _ClassVar[int]
    RAW_HEADER_FIELD_NUMBER: _ClassVar[int]
    RAW_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUM_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TP_DATA_FIELD_NUMBER: _ClassVar[int]
    VENDOR_INFO_FIELD_NUMBER: _ClassVar[int]
    VOLTAGE_FIELD_NUMBER: _ClassVar[int]
    accelerometer: IOTTelemetry.Accelerometer
    air_pressure: IOTTelemetry.AirPressure
    air_quality: IOTTelemetry.AirQuality
    ambient_light: IOTTelemetry.AmbientLight
    battery: IOTTelemetry.Battery
    carbon_emissions: IOTTelemetry.CarbonEmissions
    ccx_data: CCXData
    detected_position: DevicePosition
    device_info: DeviceInfo
    device_rtc_time: int
    eddy_stone: IOTTelemetry.Eddystone
    humidity: IOTTelemetry.Humidity
    i_beacon: IOTTelemetry.iBeacon
    illum_sensor: IOTTelemetry.IllumSensor
    illum_solar_cell: IOTTelemetry.IllumSolarCell
    illuminance: IOTTelemetry.Illuminance
    last_user_action: IOTTelemetry.LastUserAction
    location: Location
    magnet_contact: IOTTelemetry.MagnetContact
    max_detected_rssi: int
    occupancy_status: IOTTelemetry.OccupancyStatus
    pir_trigger: IOTTelemetry.PIRTrigger
    placed_position: DevicePosition
    push_button: IOTTelemetry.PushButton
    raw_header: int
    raw_payload: bytes
    sequence_num: int
    temperature: IOTTelemetry.Temperature
    tp_data: IOTTelemetry.TPData
    vendor_info: IOTTelemetry.VendorInfo
    voltage: IOTTelemetry.Voltage
    def __init__(self, device_info: _Optional[_Union[DeviceInfo, _Mapping]] = ..., detected_position: _Optional[_Union[DevicePosition, _Mapping]] = ..., placed_position: _Optional[_Union[DevicePosition, _Mapping]] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., temperature: _Optional[_Union[IOTTelemetry.Temperature, _Mapping]] = ..., accelerometer: _Optional[_Union[IOTTelemetry.Accelerometer, _Mapping]] = ..., illuminance: _Optional[_Union[IOTTelemetry.Illuminance, _Mapping]] = ..., device_rtc_time: _Optional[int] = ..., battery: _Optional[_Union[IOTTelemetry.Battery, _Mapping]] = ..., last_user_action: _Optional[_Union[IOTTelemetry.LastUserAction, _Mapping]] = ..., i_beacon: _Optional[_Union[IOTTelemetry.iBeacon, _Mapping]] = ..., eddy_stone: _Optional[_Union[IOTTelemetry.Eddystone, _Mapping]] = ..., raw_header: _Optional[int] = ..., raw_payload: _Optional[bytes] = ..., sequence_num: _Optional[int] = ..., pir_trigger: _Optional[_Union[IOTTelemetry.PIRTrigger, _Mapping]] = ..., air_pressure: _Optional[_Union[IOTTelemetry.AirPressure, _Mapping]] = ..., vendor_info: _Optional[_Union[IOTTelemetry.VendorInfo, _Mapping]] = ..., ccx_data: _Optional[_Union[CCXData, _Mapping]] = ..., tp_data: _Optional[_Union[IOTTelemetry.TPData, _Mapping]] = ..., humidity: _Optional[_Union[IOTTelemetry.Humidity, _Mapping]] = ..., air_quality: _Optional[_Union[IOTTelemetry.AirQuality, _Mapping]] = ..., carbon_emissions: _Optional[_Union[IOTTelemetry.CarbonEmissions, _Mapping]] = ..., ambient_light: _Optional[_Union[IOTTelemetry.AmbientLight, _Mapping]] = ..., voltage: _Optional[_Union[IOTTelemetry.Voltage, _Mapping]] = ..., illum_solar_cell: _Optional[_Union[IOTTelemetry.IllumSolarCell, _Mapping]] = ..., illum_sensor: _Optional[_Union[IOTTelemetry.IllumSensor, _Mapping]] = ..., occupancy_status: _Optional[_Union[IOTTelemetry.OccupancyStatus, _Mapping]] = ..., magnet_contact: _Optional[_Union[IOTTelemetry.MagnetContact, _Mapping]] = ..., max_detected_rssi: _Optional[int] = ..., push_button: _Optional[_Union[IOTTelemetry.PushButton, _Mapping]] = ...) -> None: ...

class IOTUserAction(_message.Message):
    __slots__ = ["action_count", "action_timestamp", "action_type", "detected_position", "device_info", "location", "placed_position"]
    ACTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACTION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    DETECTED_POSITION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PLACED_POSITION_FIELD_NUMBER: _ClassVar[int]
    action_count: int
    action_timestamp: int
    action_type: IOTActionType
    detected_position: DevicePosition
    device_info: DeviceInfo
    location: Location
    placed_position: DevicePosition
    def __init__(self, device_info: _Optional[_Union[DeviceInfo, _Mapping]] = ..., detected_position: _Optional[_Union[DevicePosition, _Mapping]] = ..., placed_position: _Optional[_Union[DevicePosition, _Mapping]] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., action_type: _Optional[_Union[IOTActionType, str]] = ..., action_count: _Optional[int] = ..., action_timestamp: _Optional[int] = ...) -> None: ...

class LinkedIn(_message.Message):
    __slots__ = ["attributes", "email", "first_name", "id", "last_name", "profile_picture"]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_PICTURE_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[Attribute]
    email: str
    first_name: str
    id: str
    last_name: str
    profile_picture: str
    def __init__(self, id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., profile_picture: _Optional[str] = ..., email: _Optional[str] = ..., attributes: _Optional[_Iterable[_Union[Attribute, _Mapping]]] = ...) -> None: ...

class Location(_message.Message):
    __slots__ = ["ap_count", "floor_number", "inferred_location_types", "location_id", "name", "parent", "source_location_id"]
    AP_COUNT_FIELD_NUMBER: _ClassVar[int]
    FLOOR_NUMBER_FIELD_NUMBER: _ClassVar[int]
    INFERRED_LOCATION_TYPES_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    ap_count: int
    floor_number: int
    inferred_location_types: _containers.RepeatedScalarFieldContainer[str]
    location_id: str
    name: str
    parent: Location
    source_location_id: str
    def __init__(self, location_id: _Optional[str] = ..., name: _Optional[str] = ..., inferred_location_types: _Optional[_Iterable[str]] = ..., parent: _Optional[_Union[Location, _Mapping]] = ..., source_location_id: _Optional[str] = ..., floor_number: _Optional[int] = ..., ap_count: _Optional[int] = ...) -> None: ...

class LocationAnchorInfo(_message.Message):
    __slots__ = ["adv_tx_power", "frequency", "identifier", "latitude", "longitude", "major", "map_id", "minor", "tx_power", "uuid", "x_pos", "y_pos", "z_pos"]
    ADV_TX_POWER_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    MAP_ID_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    TX_POWER_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    X_POS_FIELD_NUMBER: _ClassVar[int]
    Y_POS_FIELD_NUMBER: _ClassVar[int]
    Z_POS_FIELD_NUMBER: _ClassVar[int]
    adv_tx_power: int
    frequency: int
    identifier: str
    latitude: float
    longitude: float
    major: int
    map_id: str
    minor: int
    tx_power: int
    uuid: str
    x_pos: str
    y_pos: str
    z_pos: str
    def __init__(self, identifier: _Optional[str] = ..., uuid: _Optional[str] = ..., major: _Optional[int] = ..., minor: _Optional[int] = ..., tx_power: _Optional[int] = ..., adv_tx_power: _Optional[int] = ..., frequency: _Optional[int] = ..., x_pos: _Optional[str] = ..., y_pos: _Optional[str] = ..., z_pos: _Optional[str] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., map_id: _Optional[str] = ...) -> None: ...

class LocationAnchorUpdate(_message.Message):
    __slots__ = ["change_type", "location", "location_anchor_info"]
    class UpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ADD_UPDATE: LocationAnchorUpdate.UpdateType
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DELETE: LocationAnchorUpdate.UpdateType
    LOCATION_ANCHOR_INFO_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    change_type: LocationAnchorUpdate.UpdateType
    location: Location
    location_anchor_info: LocationAnchorInfo
    def __init__(self, change_type: _Optional[_Union[LocationAnchorUpdate.UpdateType, str]] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., location_anchor_info: _Optional[_Union[LocationAnchorInfo, _Mapping]] = ...) -> None: ...

class LocationChange(_message.Message):
    __slots__ = ["change_type", "location", "location_details"]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    change_type: ChangeType
    location: Location
    location_details: LocationDetails
    def __init__(self, change_type: _Optional[_Union[ChangeType, str]] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., location_details: _Optional[_Union[LocationDetails, _Mapping]] = ...) -> None: ...

class LocationDetails(_message.Message):
    __slots__ = ["category", "city", "country", "latitude", "longitude", "map_details", "metadata", "state", "time_zone"]
    class Metadata(_message.Message):
        __slots__ = ["key", "values"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        key: str
        values: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, key: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    MAP_DETAILS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    category: str
    city: str
    country: str
    latitude: float
    longitude: float
    map_details: MapDetails
    metadata: _containers.RepeatedCompositeFieldContainer[LocationDetails.Metadata]
    state: str
    time_zone: str
    def __init__(self, time_zone: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., country: _Optional[str] = ..., category: _Optional[str] = ..., metadata: _Optional[_Iterable[_Union[LocationDetails.Metadata, _Mapping]]] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., map_details: _Optional[_Union[MapDetails, _Mapping]] = ...) -> None: ...

class LocationInfo(_message.Message):
    __slots__ = ["location", "location_details"]
    LOCATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: Location
    location_details: LocationDetails
    def __init__(self, location: _Optional[_Union[Location, _Mapping]] = ..., location_details: _Optional[_Union[LocationDetails, _Mapping]] = ...) -> None: ...

class LocationInfoRequest(_message.Message):
    __slots__ = ["location_id", "partner_tenant_id"]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    PARTNER_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    partner_tenant_id: str
    def __init__(self, location_id: _Optional[str] = ..., partner_tenant_id: _Optional[str] = ...) -> None: ...

class MapDetails(_message.Message):
    __slots__ = ["dimension", "image_height", "image_width", "map_id", "mime_type"]
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_WIDTH_FIELD_NUMBER: _ClassVar[int]
    MAP_ID_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    dimension: Dimension
    image_height: int
    image_width: int
    map_id: str
    mime_type: str
    def __init__(self, map_id: _Optional[str] = ..., image_width: _Optional[int] = ..., image_height: _Optional[int] = ..., mime_type: _Optional[str] = ..., dimension: _Optional[_Union[Dimension, _Mapping]] = ...) -> None: ...

class MobileInfo(_message.Message):
    __slots__ = ["number", "opted_in", "verified"]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    OPTED_IN_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    number: str
    opted_in: bool
    verified: bool
    def __init__(self, number: _Optional[str] = ..., verified: bool = ..., opted_in: bool = ...) -> None: ...

class NetworkStatusUpdate(_message.Message):
    __slots__ = ["connector_info", "controller_info", "device_type", "last_heard", "status"]
    class NetworkDeviceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class NetworkDeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class ConnectorInfo(_message.Message):
        __slots__ = ["docker_version", "id", "ip_address", "name", "ova_version"]
        DOCKER_VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        OVA_VERSION_FIELD_NUMBER: _ClassVar[int]
        docker_version: str
        id: str
        ip_address: str
        name: str
        ova_version: str
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., ip_address: _Optional[str] = ..., ova_version: _Optional[str] = ..., docker_version: _Optional[str] = ...) -> None: ...
    class ControllerInfo(_message.Message):
        __slots__ = ["connector_id", "connector_name", "id", "ip_address", "name", "type", "version"]
        CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
        CONNECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        connector_id: str
        connector_name: str
        id: str
        ip_address: str
        name: str
        type: str
        version: str
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., ip_address: _Optional[str] = ..., version: _Optional[str] = ..., connector_id: _Optional[str] = ..., connector_name: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
    CONNECTOR_INFO_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_INFO_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LAST_HEARD_FIELD_NUMBER: _ClassVar[int]
    NDS_ACTIVE: NetworkStatusUpdate.NetworkDeviceStatus
    NDS_CONNECTED: NetworkStatusUpdate.NetworkDeviceStatus
    NDS_DISCONNECTED: NetworkStatusUpdate.NetworkDeviceStatus
    NDS_INACTIVE: NetworkStatusUpdate.NetworkDeviceStatus
    NDS_UNKNOWN: NetworkStatusUpdate.NetworkDeviceStatus
    NDT_CONNECTOR: NetworkStatusUpdate.NetworkDeviceType
    NDT_CONTROLLER: NetworkStatusUpdate.NetworkDeviceType
    NDT_UNKNOWN: NetworkStatusUpdate.NetworkDeviceType
    STATUS_FIELD_NUMBER: _ClassVar[int]
    connector_info: NetworkStatusUpdate.ConnectorInfo
    controller_info: NetworkStatusUpdate.ControllerInfo
    device_type: NetworkStatusUpdate.NetworkDeviceType
    last_heard: int
    status: NetworkStatusUpdate.NetworkDeviceStatus
    def __init__(self, device_type: _Optional[_Union[NetworkStatusUpdate.NetworkDeviceType, str]] = ..., status: _Optional[_Union[NetworkStatusUpdate.NetworkDeviceStatus, str]] = ..., last_heard: _Optional[int] = ..., connector_info: _Optional[_Union[NetworkStatusUpdate.ConnectorInfo, _Mapping]] = ..., controller_info: _Optional[_Union[NetworkStatusUpdate.ControllerInfo, _Mapping]] = ...) -> None: ...

class NetworkTelemetry(_message.Message):
    __slots__ = ["location", "network_health", "network_performance"]
    class NetworkHealth(_message.Message):
        __slots__ = ["ap_telemetries", "network_availability"]
        class APTelemetryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        class APTelemetry(_message.Message):
            __slots__ = ["ap_telemetry_type", "average", "max", "min"]
            AP_TELEMETRY_TYPE_FIELD_NUMBER: _ClassVar[int]
            AVERAGE_FIELD_NUMBER: _ClassVar[int]
            MAX_FIELD_NUMBER: _ClassVar[int]
            MIN_FIELD_NUMBER: _ClassVar[int]
            ap_telemetry_type: NetworkTelemetry.NetworkHealth.APTelemetryType
            average: float
            max: int
            min: int
            def __init__(self, ap_telemetry_type: _Optional[_Union[NetworkTelemetry.NetworkHealth.APTelemetryType, str]] = ..., average: _Optional[float] = ..., min: _Optional[int] = ..., max: _Optional[int] = ...) -> None: ...
        class NetworkAvailability(_message.Message):
            __slots__ = ["band", "dns_lookup_success_percentage", "num_of_dns_lookup", "num_of_dns_lookup_success", "num_of_success", "num_of_tests", "success_percentage"]
            BAND_FIELD_NUMBER: _ClassVar[int]
            DNS_LOOKUP_SUCCESS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
            NUM_OF_DNS_LOOKUP_FIELD_NUMBER: _ClassVar[int]
            NUM_OF_DNS_LOOKUP_SUCCESS_FIELD_NUMBER: _ClassVar[int]
            NUM_OF_SUCCESS_FIELD_NUMBER: _ClassVar[int]
            NUM_OF_TESTS_FIELD_NUMBER: _ClassVar[int]
            SUCCESS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
            band: str
            dns_lookup_success_percentage: float
            num_of_dns_lookup: int
            num_of_dns_lookup_success: int
            num_of_success: int
            num_of_tests: int
            success_percentage: float
            def __init__(self, num_of_tests: _Optional[int] = ..., num_of_success: _Optional[int] = ..., success_percentage: _Optional[float] = ..., num_of_dns_lookup: _Optional[int] = ..., num_of_dns_lookup_success: _Optional[int] = ..., dns_lookup_success_percentage: _Optional[float] = ..., band: _Optional[str] = ...) -> None: ...
        AP_TELEMETRIES_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_UTILIZATION: NetworkTelemetry.NetworkHealth.APTelemetryType
        CLIENTS_PER_AP: NetworkTelemetry.NetworkHealth.APTelemetryType
        NETWORK_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
        NONE: NetworkTelemetry.NetworkHealth.APTelemetryType
        RSSI: NetworkTelemetry.NetworkHealth.APTelemetryType
        SNR: NetworkTelemetry.NetworkHealth.APTelemetryType
        ap_telemetries: _containers.RepeatedCompositeFieldContainer[NetworkTelemetry.NetworkHealth.APTelemetry]
        network_availability: _containers.RepeatedCompositeFieldContainer[NetworkTelemetry.NetworkHealth.NetworkAvailability]
        def __init__(self, network_availability: _Optional[_Iterable[_Union[NetworkTelemetry.NetworkHealth.NetworkAvailability, _Mapping]]] = ..., ap_telemetries: _Optional[_Iterable[_Union[NetworkTelemetry.NetworkHealth.APTelemetry, _Mapping]]] = ...) -> None: ...
    class NetworkPerformance(_message.Message):
        __slots__ = ["avg_dns_lookup_time_ms", "avg_download_bandwidth_mbps", "avg_packet_loss_percentage", "avg_rtt_ms", "avg_upload_bandwidth_mbps", "band", "jitter", "mos"]
        AVG_DNS_LOOKUP_TIME_MS_FIELD_NUMBER: _ClassVar[int]
        AVG_DOWNLOAD_BANDWIDTH_MBPS_FIELD_NUMBER: _ClassVar[int]
        AVG_PACKET_LOSS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        AVG_RTT_MS_FIELD_NUMBER: _ClassVar[int]
        AVG_UPLOAD_BANDWIDTH_MBPS_FIELD_NUMBER: _ClassVar[int]
        BAND_FIELD_NUMBER: _ClassVar[int]
        JITTER_FIELD_NUMBER: _ClassVar[int]
        MOS_FIELD_NUMBER: _ClassVar[int]
        avg_dns_lookup_time_ms: int
        avg_download_bandwidth_mbps: float
        avg_packet_loss_percentage: float
        avg_rtt_ms: int
        avg_upload_bandwidth_mbps: float
        band: str
        jitter: float
        mos: float
        def __init__(self, avg_upload_bandwidth_mbps: _Optional[float] = ..., avg_download_bandwidth_mbps: _Optional[float] = ..., avg_packet_loss_percentage: _Optional[float] = ..., avg_rtt_ms: _Optional[int] = ..., avg_dns_lookup_time_ms: _Optional[int] = ..., band: _Optional[str] = ..., jitter: _Optional[float] = ..., mos: _Optional[float] = ...) -> None: ...
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_HEALTH_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    location: Location
    network_health: NetworkTelemetry.NetworkHealth
    network_performance: _containers.RepeatedCompositeFieldContainer[NetworkTelemetry.NetworkPerformance]
    def __init__(self, network_health: _Optional[_Union[NetworkTelemetry.NetworkHealth, _Mapping]] = ..., network_performance: _Optional[_Iterable[_Union[NetworkTelemetry.NetworkPerformance, _Mapping]]] = ..., location: _Optional[_Union[Location, _Mapping]] = ...) -> None: ...

class RawCameraCounts(_message.Message):
    __slots__ = ["camera_id", "camera_zone_id", "count", "location"]
    CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
    CAMERA_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    camera_id: str
    camera_zone_id: str
    count: int
    location: Location
    def __init__(self, location: _Optional[_Union[Location, _Mapping]] = ..., camera_id: _Optional[str] = ..., camera_zone_id: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class SaveDeviceRequest(_message.Message):
    __slots__ = ["device_id", "device_profile_data", "mac_address", "partner_tenant_id"]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PROFILE_DATA_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PARTNER_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    device_profile_data: DeviceProfileData
    mac_address: str
    partner_tenant_id: str
    def __init__(self, partner_tenant_id: _Optional[str] = ..., mac_address: _Optional[str] = ..., device_id: _Optional[str] = ..., device_profile_data: _Optional[_Union[DeviceProfileData, _Mapping]] = ...) -> None: ...

class SocialNetworkInfo(_message.Message):
    __slots__ = ["facebook", "linked_in", "social_handle", "social_network", "twitter"]
    FACEBOOK_FIELD_NUMBER: _ClassVar[int]
    LINKED_IN_FIELD_NUMBER: _ClassVar[int]
    SOCIAL_HANDLE_FIELD_NUMBER: _ClassVar[int]
    SOCIAL_NETWORK_FIELD_NUMBER: _ClassVar[int]
    TWITTER_FIELD_NUMBER: _ClassVar[int]
    facebook: Facebook
    linked_in: LinkedIn
    social_handle: str
    social_network: SocialNetwork
    twitter: Twitter
    def __init__(self, social_network: _Optional[_Union[SocialNetwork, str]] = ..., social_handle: _Optional[str] = ..., facebook: _Optional[_Union[Facebook, _Mapping]] = ..., twitter: _Optional[_Union[Twitter, _Mapping]] = ..., linked_in: _Optional[_Union[LinkedIn, _Mapping]] = ...) -> None: ...

class TPPeopleCountUpdate(_message.Message):
    __slots__ = ["active_calls", "air_quality_index", "air_quality_status", "ambient_light", "ambient_noise", "close_proximity", "dryness_score", "humidity_in_percentage", "location", "mac_address", "people_count", "presence", "presentation_state", "reverberation_time", "sound_level", "standby_state", "temperature_in_celsius", "time_stamp", "tp_device_id"]
    ACTIVE_CALLS_FIELD_NUMBER: _ClassVar[int]
    AIR_QUALITY_INDEX_FIELD_NUMBER: _ClassVar[int]
    AIR_QUALITY_STATUS_FIELD_NUMBER: _ClassVar[int]
    AMBIENT_LIGHT_FIELD_NUMBER: _ClassVar[int]
    AMBIENT_NOISE_FIELD_NUMBER: _ClassVar[int]
    CLOSE_PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    DRYNESS_SCORE_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_IN_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PEOPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PRESENCE_FIELD_NUMBER: _ClassVar[int]
    PRESENTATION_STATE_FIELD_NUMBER: _ClassVar[int]
    REVERBERATION_TIME_FIELD_NUMBER: _ClassVar[int]
    SOUND_LEVEL_FIELD_NUMBER: _ClassVar[int]
    STANDBY_STATE_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_IN_CELSIUS_FIELD_NUMBER: _ClassVar[int]
    TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    TP_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    active_calls: int
    air_quality_index: float
    air_quality_status: str
    ambient_light: str
    ambient_noise: int
    close_proximity: bool
    dryness_score: int
    humidity_in_percentage: int
    location: Location
    mac_address: str
    people_count: int
    presence: bool
    presentation_state: int
    reverberation_time: int
    sound_level: int
    standby_state: int
    temperature_in_celsius: float
    time_stamp: int
    tp_device_id: str
    def __init__(self, tp_device_id: _Optional[str] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., presence: bool = ..., people_count: _Optional[int] = ..., standby_state: _Optional[int] = ..., ambient_noise: _Optional[int] = ..., dryness_score: _Optional[int] = ..., active_calls: _Optional[int] = ..., presentation_state: _Optional[int] = ..., time_stamp: _Optional[int] = ..., mac_address: _Optional[str] = ..., air_quality_index: _Optional[float] = ..., temperature_in_celsius: _Optional[float] = ..., humidity_in_percentage: _Optional[int] = ..., sound_level: _Optional[int] = ..., ambient_light: _Optional[str] = ..., reverberation_time: _Optional[int] = ..., close_proximity: bool = ..., air_quality_status: _Optional[str] = ...) -> None: ...

class Twitter(_message.Message):
    __slots__ = ["attributes", "email", "followers_count", "friends_count", "geo_enabled", "id", "lang", "location", "name", "profile_banner_url", "profile_image_url", "profile_verified", "screen_name", "statuses_count", "time_zone", "utc_offset"]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FOLLOWERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FRIENDS_COUNT_FIELD_NUMBER: _ClassVar[int]
    GEO_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_BANNER_URL_FIELD_NUMBER: _ClassVar[int]
    PROFILE_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PROFILE_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    SCREEN_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUSES_COUNT_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    UTC_OFFSET_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[Attribute]
    email: str
    followers_count: int
    friends_count: int
    geo_enabled: bool
    id: str
    lang: str
    location: str
    name: str
    profile_banner_url: str
    profile_image_url: str
    profile_verified: bool
    screen_name: str
    statuses_count: int
    time_zone: str
    utc_offset: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., screen_name: _Optional[str] = ..., friends_count: _Optional[int] = ..., followers_count: _Optional[int] = ..., profile_image_url: _Optional[str] = ..., profile_banner_url: _Optional[str] = ..., location: _Optional[str] = ..., statuses_count: _Optional[int] = ..., email: _Optional[str] = ..., profile_verified: bool = ..., utc_offset: _Optional[str] = ..., time_zone: _Optional[str] = ..., geo_enabled: bool = ..., lang: _Optional[str] = ..., attributes: _Optional[_Iterable[_Union[Attribute, _Mapping]]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ["attributes", "device_ids", "email", "first_name", "gender", "last_name", "mobile", "postal_code", "social_network_info", "tags", "user_id"]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    SOCIAL_NETWORK_INFO_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[Attribute]
    device_ids: _containers.RepeatedScalarFieldContainer[str]
    email: str
    first_name: str
    gender: Gender
    last_name: str
    mobile: str
    postal_code: str
    social_network_info: _containers.RepeatedCompositeFieldContainer[SocialNetworkInfo]
    tags: _containers.RepeatedScalarFieldContainer[str]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., device_ids: _Optional[_Iterable[str]] = ..., tags: _Optional[_Iterable[str]] = ..., mobile: _Optional[str] = ..., email: _Optional[str] = ..., gender: _Optional[_Union[Gender, str]] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., postal_code: _Optional[str] = ..., attributes: _Optional[_Iterable[_Union[Attribute, _Mapping]]] = ..., social_network_info: _Optional[_Iterable[_Union[SocialNetworkInfo, _Mapping]]] = ...) -> None: ...

class UserPresence(_message.Message):
    __slots__ = ["active_users_count", "connection", "entry_date_time", "entry_timestamp", "exit_date_time", "exit_timestamp", "in_active_users_count", "location", "presence_event_type", "raw_user_id", "time_zone", "user", "visit_duration_minutes", "visit_id", "was_in_active"]
    class UserCount(_message.Message):
        __slots__ = ["total_users", "users_with_user_id", "users_without_user_id"]
        TOTAL_USERS_FIELD_NUMBER: _ClassVar[int]
        USERS_WITHOUT_USER_ID_FIELD_NUMBER: _ClassVar[int]
        USERS_WITH_USER_ID_FIELD_NUMBER: _ClassVar[int]
        total_users: int
        users_with_user_id: int
        users_without_user_id: int
        def __init__(self, users_with_user_id: _Optional[int] = ..., users_without_user_id: _Optional[int] = ..., total_users: _Optional[int] = ...) -> None: ...
    ACTIVE_USERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    ENTRY_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ENTRY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EXIT_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXIT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IN_ACTIVE_USERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PRESENCE_EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RAW_USER_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    VISIT_DURATION_MINUTES_FIELD_NUMBER: _ClassVar[int]
    VISIT_ID_FIELD_NUMBER: _ClassVar[int]
    WAS_IN_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    active_users_count: UserPresence.UserCount
    connection: Connection
    entry_date_time: str
    entry_timestamp: int
    exit_date_time: str
    exit_timestamp: int
    in_active_users_count: UserPresence.UserCount
    location: Location
    presence_event_type: UserPresenceEventType
    raw_user_id: str
    time_zone: str
    user: User
    visit_duration_minutes: int
    visit_id: str
    was_in_active: bool
    def __init__(self, presence_event_type: _Optional[_Union[UserPresenceEventType, str]] = ..., was_in_active: bool = ..., user: _Optional[_Union[User, _Mapping]] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., raw_user_id: _Optional[str] = ..., visit_id: _Optional[str] = ..., entry_timestamp: _Optional[int] = ..., entry_date_time: _Optional[str] = ..., exit_timestamp: _Optional[int] = ..., exit_date_time: _Optional[str] = ..., visit_duration_minutes: _Optional[int] = ..., time_zone: _Optional[str] = ..., active_users_count: _Optional[_Union[UserPresence.UserCount, _Mapping]] = ..., in_active_users_count: _Optional[_Union[UserPresence.UserCount, _Mapping]] = ..., connection: _Optional[_Union[Connection, str]] = ...) -> None: ...

class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class IOTDeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class IOTActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class DevicePresenceEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class UserPresenceEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Connection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Gender(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SocialNetwork(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class DeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
