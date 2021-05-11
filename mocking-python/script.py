import unittest
from unittest import mock
from mylib import RemovalService


class RmTestCase(unittest.TestCase):

    @mock.patch('mylib.os.path')
    @mock.patch('mylib.os')
    def test_rm(self, mock_os, mock_path):
        reference = RemovalService()

        # set up the mock
        mock_path.isfile.return_value = False

        reference.rm("/tmp/oki")

        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called)

        # make the file 'exist'
        mock_path.isfile.return_value = True

        reference.rm("/tmp/oki")

        mock_os.remove.assert_called_with("/tmp/oki")


if __name__ == '__main__':
    unittest.main()
