import json
import os
import tempfile
import unittest

from scanner.reporter import save_json


class TestReporter(unittest.TestCase):

    def test_save_json(self):
        test_data = [
            {
                "port": 22,
                "service": "SSH"
            }
        ]

        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".json",
            delete=False
        ) as temp_file:

            filename = temp_file.name

        try:
            save_json(
                filename,
                "127.0.0.1",
                test_data
            )

            with open(filename, "r") as file:
                data = json.load(file)

            self.assertEqual(
                data["target"],
                "127.0.0.1"
            )

            self.assertEqual(
                data["total_open"],
                1
            )

            self.assertEqual(
                data["open_ports"][0]["port"],
                22
            )

        finally:
            os.remove(filename)


if __name__ == "__main__":
    unittest.main()