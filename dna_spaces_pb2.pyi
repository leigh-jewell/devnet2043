from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

ACCOUNT_ADMIN_ACTIVATION: EventType
ADD: ChangeType
APP_ACTIVATION: EventType
APP_DE_ACTIVATION: EventType
DESCRIPTOR: _descriptor.FileDescriptor
DEVICE_ACTIVE_EVENT: DevicePresenceEventType
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
KEEP_ALIVE: EventType
LINKEDIN: SocialNetwork
LOCATION_CHANGE: EventType
MALE: Gender
MOVE: ChangeType
OTHER: Gender
PROFILE_UPDATE: EventType
REMOVE: ChangeType
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
    __slots__ = ["instance_name", "name", "partner_tenant_id", "reference_id", "spaces_tenant_id", "spaces_tenant_name"]
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARTNER_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACES_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACES_TENANT_NAME_FIELD_NUMBER: _ClassVar[int]
    instance_name: str
    name: str
    partner_tenant_id: str
    reference_id: str
    spaces_tenant_id: str
    spaces_tenant_name: str
    def __init__(self, spaces_tenant_name: _Optional[str] = ..., spaces_tenant_id: _Optional[str] = ..., partner_tenant_id: _Optional[str] = ..., name: _Optional[str] = ..., reference_id: _Optional[str] = ..., instance_name: _Optional[str] = ...) -> None: ...

class Device(_message.Message):
    __slots__ = ["device_id", "email", "first_name", "gender", "last_name", "mac_address", "manufacturer", "mobile", "opt_ins", "os", "os_version", "other_fields", "postal_code", "social_network_info", "tags", "type", "user_id"]
    class DeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class OptIn(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL: Device.OptIn
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    LAPTOP: Device.DeviceType
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    MOBILE: Device.DeviceType
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    MOBILE_NUMBER: Device.OptIn
    NOT_AVAILABLE: Device.DeviceType
    OPT_INS_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    OTHER_DEVICE: Device.DeviceType
    OTHER_FIELDS_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    SOCIAL_NETWORK_INFO_FIELD_NUMBER: _ClassVar[int]
    TABLET: Device.DeviceType
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TERMS_AND_CONDITIONS: Device.OptIn
    TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
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
    other_fields: _containers.RepeatedCompositeFieldContainer[OtherField]
    postal_code: str
    social_network_info: _containers.RepeatedCompositeFieldContainer[SocialNetworkInfo]
    tags: _containers.RepeatedScalarFieldContainer[str]
    type: Device.DeviceType
    user_id: str
    def __init__(self, device_id: _Optional[str] = ..., user_id: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., mobile: _Optional[str] = ..., email: _Optional[str] = ..., gender: _Optional[_Union[Gender, str]] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., postal_code: _Optional[str] = ..., opt_ins: _Optional[_Iterable[_Union[Device.OptIn, str]]] = ..., other_fields: _Optional[_Iterable[_Union[OtherField, _Mapping]]] = ..., mac_address: _Optional[str] = ..., manufacturer: _Optional[str] = ..., os: _Optional[str] = ..., os_version: _Optional[str] = ..., type: _Optional[_Union[Device.DeviceType, str]] = ..., social_network_info: _Optional[_Iterable[_Union[SocialNetworkInfo, _Mapping]]] = ...) -> None: ...

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

class DeviceLocation(_message.Message):
    __slots__ = ["confidence_factor", "device", "device_classification", "last_seen", "latitude", "location", "longitude", "map_id", "raw_user_id", "ssid", "visit_id", "x_pos", "y_pos"]
    CONFIDENCE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    MAP_ID_FIELD_NUMBER: _ClassVar[int]
    RAW_USER_ID_FIELD_NUMBER: _ClassVar[int]
    SSID_FIELD_NUMBER: _ClassVar[int]
    VISIT_ID_FIELD_NUMBER: _ClassVar[int]
    X_POS_FIELD_NUMBER: _ClassVar[int]
    Y_POS_FIELD_NUMBER: _ClassVar[int]
    confidence_factor: float
    device: Device
    device_classification: str
    last_seen: int
    latitude: float
    location: Location
    longitude: float
    map_id: str
    raw_user_id: str
    ssid: str
    visit_id: str
    x_pos: float
    y_pos: float
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., ssid: _Optional[str] = ..., raw_user_id: _Optional[str] = ..., visit_id: _Optional[str] = ..., last_seen: _Optional[int] = ..., device_classification: _Optional[str] = ..., map_id: _Optional[str] = ..., x_pos: _Optional[float] = ..., y_pos: _Optional[float] = ..., confidence_factor: _Optional[float] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

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

class EventRecord(_message.Message):
    __slots__ = ["account_admin_change", "app_activation", "device_entry", "device_exit", "device_location_update", "device_presence", "device_profile_update", "event_type", "location_hierarchy_change", "partner_tenant_id", "record_timestamp", "record_uid", "spaces_tenant_id", "spaces_tenant_name", "tp_people_count_update", "user_presence"]
    ACCOUNT_ADMIN_CHANGE_FIELD_NUMBER: _ClassVar[int]
    APP_ACTIVATION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ENTRY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_EXIT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LOCATION_UPDATE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PRESENCE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PROFILE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_HIERARCHY_CHANGE_FIELD_NUMBER: _ClassVar[int]
    PARTNER_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RECORD_UID_FIELD_NUMBER: _ClassVar[int]
    SPACES_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACES_TENANT_NAME_FIELD_NUMBER: _ClassVar[int]
    TP_PEOPLE_COUNT_UPDATE_FIELD_NUMBER: _ClassVar[int]
    USER_PRESENCE_FIELD_NUMBER: _ClassVar[int]
    account_admin_change: AccountAdminChange
    app_activation: AppActivation
    device_entry: DeviceEntry
    device_exit: DeviceExit
    device_location_update: DeviceLocation
    device_presence: DevicePresence
    device_profile_update: Device
    event_type: EventType
    location_hierarchy_change: LocationChange
    partner_tenant_id: str
    record_timestamp: int
    record_uid: str
    spaces_tenant_id: str
    spaces_tenant_name: str
    tp_people_count_update: TPPeopleCountUpdate
    user_presence: UserPresence
    def __init__(self, record_uid: _Optional[str] = ..., record_timestamp: _Optional[int] = ..., spaces_tenant_id: _Optional[str] = ..., spaces_tenant_name: _Optional[str] = ..., partner_tenant_id: _Optional[str] = ..., event_type: _Optional[_Union[EventType, str]] = ..., device_entry: _Optional[_Union[DeviceEntry, _Mapping]] = ..., device_exit: _Optional[_Union[DeviceExit, _Mapping]] = ..., device_profile_update: _Optional[_Union[Device, _Mapping]] = ..., location_hierarchy_change: _Optional[_Union[LocationChange, _Mapping]] = ..., device_location_update: _Optional[_Union[DeviceLocation, _Mapping]] = ..., app_activation: _Optional[_Union[AppActivation, _Mapping]] = ..., account_admin_change: _Optional[_Union[AccountAdminChange, _Mapping]] = ..., tp_people_count_update: _Optional[_Union[TPPeopleCountUpdate, _Mapping]] = ..., device_presence: _Optional[_Union[DevicePresence, _Mapping]] = ..., user_presence: _Optional[_Union[UserPresence, _Mapping]] = ...) -> None: ...

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
    __slots__ = ["email", "first_name", "id", "last_name", "middle_name", "name", "name_format", "other_fields", "picture", "short_name"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    MIDDLE_NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FORMAT_FIELD_NUMBER: _ClassVar[int]
    OTHER_FIELDS_FIELD_NUMBER: _ClassVar[int]
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    email: str
    first_name: str
    id: str
    last_name: str
    middle_name: str
    name: str
    name_format: str
    other_fields: _containers.RepeatedCompositeFieldContainer[OtherField]
    picture: str
    short_name: str
    def __init__(self, id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., middle_name: _Optional[str] = ..., name: _Optional[str] = ..., short_name: _Optional[str] = ..., name_format: _Optional[str] = ..., picture: _Optional[str] = ..., email: _Optional[str] = ..., other_fields: _Optional[_Iterable[_Union[OtherField, _Mapping]]] = ...) -> None: ...

class FloorImage(_message.Message):
    __slots__ = ["data", "mime_type", "name"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    mime_type: str
    name: str
    def __init__(self, name: _Optional[str] = ..., data: _Optional[bytes] = ..., mime_type: _Optional[str] = ...) -> None: ...

class FloorImageRequest(_message.Message):
    __slots__ = ["image_name"]
    IMAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    image_name: str
    def __init__(self, image_name: _Optional[str] = ...) -> None: ...

class LinkedIn(_message.Message):
    __slots__ = ["email", "first_name", "id", "last_name", "other_fields", "profile_picture"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    OTHER_FIELDS_FIELD_NUMBER: _ClassVar[int]
    PROFILE_PICTURE_FIELD_NUMBER: _ClassVar[int]
    email: str
    first_name: str
    id: str
    last_name: str
    other_fields: _containers.RepeatedCompositeFieldContainer[OtherField]
    profile_picture: str
    def __init__(self, id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., profile_picture: _Optional[str] = ..., email: _Optional[str] = ..., other_fields: _Optional[_Iterable[_Union[OtherField, _Mapping]]] = ...) -> None: ...

class Location(_message.Message):
    __slots__ = ["inferred_location_types", "location_id", "name", "parent"]
    INFERRED_LOCATION_TYPES_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    inferred_location_types: _containers.RepeatedScalarFieldContainer[str]
    location_id: str
    name: str
    parent: Location
    def __init__(self, location_id: _Optional[str] = ..., name: _Optional[str] = ..., inferred_location_types: _Optional[_Iterable[str]] = ..., parent: _Optional[_Union[Location, _Mapping]] = ...) -> None: ...

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
    __slots__ = ["image_height", "image_width", "map_id", "mime_type"]
    IMAGE_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_WIDTH_FIELD_NUMBER: _ClassVar[int]
    MAP_ID_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    image_height: int
    image_width: int
    map_id: str
    mime_type: str
    def __init__(self, map_id: _Optional[str] = ..., image_width: _Optional[int] = ..., image_height: _Optional[int] = ..., mime_type: _Optional[str] = ...) -> None: ...

class OtherField(_message.Message):
    __slots__ = ["name", "values"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    name: str
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...

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
    __slots__ = ["active_calls", "ambient_noise", "dryness_score", "location", "people_count", "presence", "presentation_state", "standby_state", "time_stamp", "tp_device_id"]
    ACTIVE_CALLS_FIELD_NUMBER: _ClassVar[int]
    AMBIENT_NOISE_FIELD_NUMBER: _ClassVar[int]
    DRYNESS_SCORE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PEOPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PRESENCE_FIELD_NUMBER: _ClassVar[int]
    PRESENTATION_STATE_FIELD_NUMBER: _ClassVar[int]
    STANDBY_STATE_FIELD_NUMBER: _ClassVar[int]
    TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    TP_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    active_calls: int
    ambient_noise: int
    dryness_score: int
    location: Location
    people_count: int
    presence: bool
    presentation_state: int
    standby_state: int
    time_stamp: int
    tp_device_id: str
    def __init__(self, tp_device_id: _Optional[str] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., presence: bool = ..., people_count: _Optional[int] = ..., standby_state: _Optional[int] = ..., ambient_noise: _Optional[int] = ..., dryness_score: _Optional[int] = ..., active_calls: _Optional[int] = ..., presentation_state: _Optional[int] = ..., time_stamp: _Optional[int] = ...) -> None: ...

class Twitter(_message.Message):
    __slots__ = ["email", "followers_count", "friends_count", "geo_enabled", "id", "lang", "location", "name", "other_fields", "profile_banner_url", "profile_image_url", "profile_verified", "screen_name", "statuses_count", "time_zone", "utc_offset"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FOLLOWERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FRIENDS_COUNT_FIELD_NUMBER: _ClassVar[int]
    GEO_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OTHER_FIELDS_FIELD_NUMBER: _ClassVar[int]
    PROFILE_BANNER_URL_FIELD_NUMBER: _ClassVar[int]
    PROFILE_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PROFILE_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    SCREEN_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUSES_COUNT_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    UTC_OFFSET_FIELD_NUMBER: _ClassVar[int]
    email: str
    followers_count: int
    friends_count: int
    geo_enabled: bool
    id: str
    lang: str
    location: str
    name: str
    other_fields: _containers.RepeatedCompositeFieldContainer[OtherField]
    profile_banner_url: str
    profile_image_url: str
    profile_verified: bool
    screen_name: str
    statuses_count: int
    time_zone: str
    utc_offset: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., screen_name: _Optional[str] = ..., friends_count: _Optional[int] = ..., followers_count: _Optional[int] = ..., profile_image_url: _Optional[str] = ..., profile_banner_url: _Optional[str] = ..., location: _Optional[str] = ..., statuses_count: _Optional[int] = ..., email: _Optional[str] = ..., profile_verified: bool = ..., utc_offset: _Optional[str] = ..., time_zone: _Optional[str] = ..., geo_enabled: bool = ..., lang: _Optional[str] = ..., other_fields: _Optional[_Iterable[_Union[OtherField, _Mapping]]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ["device_ids", "email", "first_name", "gender", "last_name", "mobile", "other_fields", "postal_code", "social_network_info", "tags", "user_id"]
    DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    OTHER_FIELDS_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    SOCIAL_NETWORK_INFO_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    device_ids: _containers.RepeatedScalarFieldContainer[str]
    email: str
    first_name: str
    gender: Gender
    last_name: str
    mobile: str
    other_fields: _containers.RepeatedCompositeFieldContainer[OtherField]
    postal_code: str
    social_network_info: _containers.RepeatedCompositeFieldContainer[SocialNetworkInfo]
    tags: _containers.RepeatedScalarFieldContainer[str]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., device_ids: _Optional[_Iterable[str]] = ..., tags: _Optional[_Iterable[str]] = ..., mobile: _Optional[str] = ..., email: _Optional[str] = ..., gender: _Optional[_Union[Gender, str]] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., postal_code: _Optional[str] = ..., other_fields: _Optional[_Iterable[_Union[OtherField, _Mapping]]] = ..., social_network_info: _Optional[_Iterable[_Union[SocialNetworkInfo, _Mapping]]] = ...) -> None: ...

class UserPresence(_message.Message):
    __slots__ = ["active_users_count", "entry_date_time", "entry_timestamp", "exit_date_time", "exit_timestamp", "in_active_users_count", "location", "presence_event_type", "raw_user_id", "time_zone", "user", "visit_duration_minutes", "visit_id", "was_in_active"]
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
    def __init__(self, presence_event_type: _Optional[_Union[UserPresenceEventType, str]] = ..., was_in_active: bool = ..., user: _Optional[_Union[User, _Mapping]] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., raw_user_id: _Optional[str] = ..., visit_id: _Optional[str] = ..., entry_timestamp: _Optional[int] = ..., entry_date_time: _Optional[str] = ..., exit_timestamp: _Optional[int] = ..., exit_date_time: _Optional[str] = ..., visit_duration_minutes: _Optional[int] = ..., time_zone: _Optional[str] = ..., active_users_count: _Optional[_Union[UserPresence.UserCount, _Mapping]] = ..., in_active_users_count: _Optional[_Union[UserPresence.UserCount, _Mapping]] = ...) -> None: ...

class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class DevicePresenceEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class UserPresenceEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Gender(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SocialNetwork(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
