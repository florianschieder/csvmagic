from enum import Enum, unique


# TODO move this into the C world and import here somehow
@unique
class CSVProcessorMode(Enum):
    DICT = 0x0


class CSVProcessorStub:
    def __init__(self,
                 escaping_delimiter: str,
                 field_delimiter: str,
                 line_terminator: str,
                 mode: CSVProcessorMode):
        pass

    def parse_from_string(self, string):
        raise NotImplementedError()


CSVProcessor = CSVProcessorStub
