from unittest import TestCase
from unittest.mock import patch

from csvmagic import Builder, CSVProcessor, CSVProcessorMode
from csvmagic.exceptions import IncompleteBuilderConfigurationException


class BuilderTests(TestCase):
    def test_can_apply_defaults(self):
        builder = (Builder()
                   .apply_defaults()
                   .use_mode(CSVProcessorMode.DICT))

        TestCase = self

        class MockCSVProcessor:
            def __init__(self, **kwargs):
                expected_args = {
                    "mode": CSVProcessorMode.DICT,
                    "escaping_delimiter": '"',
                    "field_delimiter": ',',
                    "line_terminator": '\r\n',
                }
                TestCase.assertEqual(expected_args, kwargs)

        with patch("csvmagic.builder.CSVProcessor", MockCSVProcessor):
            self.assertIsInstance(builder.get_instance(), MockCSVProcessor)

    def test_incomplete_configuration(self):
        builder = Builder().apply_defaults()

        with self.assertRaises(IncompleteBuilderConfigurationException) as cm:
            builder.get_instance()
        self.assertEqual("", str(cm.exception))

    def test_passes_values_properly(self):
        builder = (Builder()
                   .use_line_terminator("\n")
                   .use_field_delimiter(";")
                   .use_escaping_delimiter("'")
                   .use_mode(CSVProcessorMode.DICT))

        TestCase = self

        class MockCSVProcessor:
            def __init__(self, **kwargs):
                expected_args = {
                    "mode": CSVProcessorMode.DICT,
                    "escaping_delimiter": "'",
                    "field_delimiter": ";",
                    "line_terminator": "\n",
                }
                TestCase.assertEqual(expected_args, kwargs)

        with patch("csvmagic.builder.CSVProcessor", MockCSVProcessor):
            self.assertIsInstance(builder.get_instance(), MockCSVProcessor)

    def test_constructs_processor(self):
        builder = (Builder()
                   .use_line_terminator('\n')
                   .use_field_delimiter(',')
                   .use_escaping_delimiter('"')
                   .use_mode(CSVProcessorMode.DICT))
        self.assertIsInstance(builder.get_instance(), CSVProcessor)
