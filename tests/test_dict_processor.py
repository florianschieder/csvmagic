from textwrap import dedent
from unittest import TestCase

from csvmagic import Builder, CSVProcessorMode
from csvmagic.exceptions import MalformedCSVFileException


class DictProcessorTests(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dict_helper = (Builder()
                           .use_mode(CSVProcessorMode.DICT)
                           .use_line_terminator('\n')
                           .use_field_delimiter(',')
                           .use_escaping_delimiter('"')
                           .get_instance())

    def test_can_parse_simple_document(self):
        csv = dedent("""\
        id,name,password
        1,foo,b2ab92264b8418cdf43267e614d66843
        2,bar,6953768a9033511d3df356e03655c585
        """)

        parsed = self.dict_helper.parse_from_string(csv)
        expected_result = [
            {"id": "1", "name": "foo",
             "password": "b2ab92264b8418cdf43267e614d66843"},
            {"id": "2", "name": "bar",
             "password": "6953768a9033511d3df356e03655c585"},
        ]
        self.assertEqual(expected_result, parsed)

    def test_handles_escaping_delimiters(self):
        csv = dedent("""\
        id,name,description
        1,foo,"Foo, Foo, and much more"
        2,bar,"Barbara, Foobar and whatever"
        """)

        parsed = self.dict_helper.parse_from_string(csv)
        expected_result = [
            {"id": "1", "name": "foo",
             "description": "Foo, Foo, and much more"},
            {"id": "2", "name": "bar",
             "description": "Barbara, Foobar and whatever"},
        ]
        self.assertEqual(expected_result, parsed)

    def test_can_parse_empty_document(self):
        scenarios = (
            "id,name,description",
            "id,name,description\n",
        )

        for i, scenario in enumerate(scenarios):
            with self.subTest(i):
                self.assertEqual([],
                                 self.dict_helper.parse_from_string(scenario))

    def test_cannot_parse_broken_files(self):
        scenarios = (
            """
            id,name,description
            a,b
            """,
            """
            id,name,description
            a,b,c,d
            """,
            """
            id,name,description
            a,b,c
            a,b,c,d
            """,
        )

        checked_scenarios = 0
        for i, scenario in enumerate(scenarios):
            with self.subTest(i):
                checked_scenarios += 1
                with self.assertRaises(MalformedCSVFileException):
                    self.dict_helper.parse_from_string(scenario)

        # Broken constellations of `assertRaises`, `subTest` and `for` loops
        # may cause a unit test not to cover what he should have covered.
        # Therefore we increment `checked_scenarios` to prove each scenario
        # has been covered properly.
        self.assertEqual(len(scenarios), checked_scenarios)
