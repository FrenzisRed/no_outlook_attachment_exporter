import extract_msg
import os
import hashlib
import argparse

parser = argparse.ArgumentParser(description="Extract attachments from a .msg file.")
parser.add_argument("-file",required=True, help="path/to/file/and/filename.msg")
parser.add_argument("-save",required=True, help="path/to/save/attachments")
args = parser.parse_args()

msg_path = args.file
output_folder = args.save

os.makedirs(output_folder, exist_ok=True)

msg = extract_msg.Message(msg_path)

for attachment in msg.attachments:
	filename = attachment.longFilename or attachment.shortFilename or "unknown_attachment.bin"
	output_path = os.path.join(output_folder,filename)
	with open(output_path, 'wb') as f:
		f.write(attachment.data)
	sha256 = hashlib.sha256(attachment.data).hexdigest()
	print(f"Saved: {filename} (SHA256: {sha256})")