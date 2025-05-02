from typing import Any

from singer_sdk import typing as th

AirtableThumbnail = th.ObjectType(
    th.Property("height", th.NumberType),
    th.Property("url", th.StringType),
    th.Property("width", th.NumberType),
)

AirtableThumbnailSet = th.ObjectType(
    th.Property("full", AirtableThumbnail),
    th.Property("large", AirtableThumbnail),
    th.Property("small", AirtableThumbnail),
)

AirtableAttachment = th.ObjectType(
    th.Property("filename", th.StringType),
    th.Property("height", th.NumberType),
    th.Property("id", th.StringType),
    th.Property("size", th.NumberType),
    th.Property("thumbnails", AirtableThumbnailSet),
    th.Property("type", th.StringType),
    th.Property("url", th.StringType),
    th.Property("width", th.NumberType),
)

AirtableCollaborator = th.ObjectType(
    th.Property("email", th.StringType),
    th.Property("id", th.StringType),
    th.Property("name", th.StringType),
    th.Property("permissionLevel", th.StringType),
    th.Property("profilePicUrl", th.StringType),
)

Button = th.ObjectType(
    th.Property("label", th.StringType),
    th.Property("url", th.URIType),
)

Formula = th.OneOf(
    th.StringType,
    th.NumberType,
)

Lookup = th.OneOf(
    th.ArrayType(th.StringType),
    th.ArrayType(th.NumberType),
)

AIRTABLE_TO_SINGER_MAPPING: dict[str, Any] = {
    "aiText": th.StringType,
    "autoNumber": th.StringType,
    "barcode": th.StringType,
    "button": Button,
    "checkbox": th.BooleanType,
    "count": th.StringType,
    "createdBy": th.StringType,
    "createdTime": th.DateTimeType,
    "currency": th.StringType,
    "date": th.DateType,
    "dateTime": th.DateTimeType,
    "duration": th.StringType,
    "email": th.StringType,
    "externalSyncSource": th.StringType,
    "formula": Formula,
    "lastModifiedBy": th.StringType,
    "lastModifiedTime": th.DateTimeType,
    "lookup": Lookup,
    "multilineText": th.StringType,
    "multipleAttachments": th.ArrayType(AirtableAttachment),
    "multipleCollaborators": th.ArrayType(AirtableCollaborator),
    "multipleLookupValues": th.ArrayType(th.StringType),
    "multipleRecordLinks": th.ArrayType(th.StringType),
    "multipleSelects": th.ArrayType(th.StringType),
    "number": th.NumberType,
    "percent": th.StringType,
    "phoneNumber": th.StringType,
    "rating": th.StringType,
    "richText": th.StringType,
    "rollup": th.StringType,
    "singleCollaborator": th.StringType,
    "singleLineText": th.StringType,
    "singleSelect": th.StringType,
    "url": th.StringType,
}
