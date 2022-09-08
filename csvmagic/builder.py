from typing import Any, Dict, Optional

from .exceptions import IncompleteBuilderConfigurationException
from .processor import CSVProcessor, CSVProcessorMode


class Builder:
    def __init__(self) -> None:
        self._fields: Dict[str, Optional[Any]] = {
            "escaping_delimiter": None,
            "field_delimiter": None,
            "line_terminator": None,
            "mode": None,
        }

    # RFC 4180
    _defaults = {
        "escaping_delimiter": '"',
        "field_delimiter": ",",
        "line_terminator": "\r\n",
    }

    def use_mode(self, mode: CSVProcessorMode) -> "Builder":
        self._fields["mode"] = mode
        return self

    def use_line_terminator(self, terminator: str) -> "Builder":
        self._fields["line_terminator"] = terminator
        return self

    def use_field_delimiter(self, delimiter: str) -> "Builder":
        self._fields["field_delimiter"] = delimiter
        return self

    def use_escaping_delimiter(self, delimiter: str) -> "Builder":
        self._fields["escaping_delimiter"] = delimiter
        return self

    def apply_defaults(self) -> "Builder":
        Self = type(self)
        self._fields = {
            **self._fields,
            **Self._defaults,
        }
        return self

    def get_instance(self) -> CSVProcessor:
        self._check_if_fields_are_complete()
        return CSVProcessor(**self._fields)

    def _check_if_fields_are_complete(self) -> None:
        incomplete_fields = [
            it[0] for it in self._fields.items() if it[1] is None
        ]

        if incomplete_fields:
            raise IncompleteBuilderConfigurationException(
                ", ".join(incomplete_fields)
            )
