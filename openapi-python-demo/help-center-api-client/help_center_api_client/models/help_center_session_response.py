from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.help_center_session_object import HelpCenterSessionObject


T = TypeVar("T", bound="HelpCenterSessionResponse")


@_attrs_define
class HelpCenterSessionResponse:
    """
    Attributes:
        current_session (Union[Unset, HelpCenterSessionObject]):
    """

    current_session: Union[Unset, "HelpCenterSessionObject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_session: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.current_session, Unset):
            current_session = self.current_session.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_session is not UNSET:
            field_dict["current_session"] = current_session

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.help_center_session_object import HelpCenterSessionObject

        d = dict(src_dict)
        _current_session = d.pop("current_session", UNSET)
        current_session: Union[Unset, HelpCenterSessionObject]
        if isinstance(_current_session, Unset):
            current_session = UNSET
        else:
            current_session = HelpCenterSessionObject.from_dict(_current_session)

        help_center_session_response = cls(
            current_session=current_session,
        )

        help_center_session_response.additional_properties = d
        return help_center_session_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
