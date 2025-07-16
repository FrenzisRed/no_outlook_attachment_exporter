# no_outlook_attachment_exporter.py
Small Script to extract attachments from outlook .msg files without having outlook.

Usage:

```
python3 no_outlook_attachment_exporter.py -file path\to\file.msg -save path\to\save\extracted\files
parser = argparse.ArgumentParser(description="Extract attachments from a .msg file.")
parser.add_argument("-file",required=True, help="path/to/file/and/filename.msg")
parser.add_argument("-save",required=True, help="path/to/save/attachments")
args = parser.parse_args()
```
