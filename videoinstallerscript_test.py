import unittest
from unittest.mock import patch
from io import StringIO
import yt_dlp_example 

 # Replace with the actual name of your script

class TestDownloadVideo(unittest.TestCase):

    @patch('builtins.input', side_effect=["https://www.youtube.com/watch?v=VIDEO_ID"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_download_video(self, mock_stdout, mock_input):
        with patch('yt_dlp.YoutubeDL') as mock_ydl:
            yt_instance = mock_ydl.return_value
            yt_instance.download.return_value = None

            yt_dlp_example.download_video()  # Replace with the actual function name in your script

        expected_output = "Video downloaded successfully Tyrrick\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()