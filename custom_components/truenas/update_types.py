"""Definitions for TrueNAS update entities."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from homeassistant.components.update import UpdateEntityDescription


@dataclass
class TrueNASUpdateEntityDescription(UpdateEntityDescription):
    """Class describing entities."""

    ha_group: str | None = None
    ha_connection: str | None = None
    ha_connection_value: str | None = None
    title: str | None = None
    data_path: str | None = None
    data_attribute: str = "available"
    data_name: str | None = None
    data_uid: str | None = None
    data_reference: str | None = None
    data_attributes_list: List = field(default_factory=lambda: [])
    func: str | None = None


SENSOR_TYPES: tuple[TrueNASUpdateEntityDescription, ...] = (
    TrueNASUpdateEntityDescription(
        key="system_update",
        name="",
        ha_group="System",
        title="TrueNAS",
        data_path="system_info",
        data_attribute="update_available",
        data_name="",
        data_uid="",
        data_reference="",
        func="TrueNASUpdate",
    ),
    TrueNASUpdateEntityDescription(
        key="app_update",
        name="",
        ha_group="Apps",
        data_path="app",
        data_attribute="update_available",
        data_name="name",
        data_uid="id",
        data_reference="id",
        func="TrueNASAppUpdate",
    ),
)

SENSOR_SERVICES = []
