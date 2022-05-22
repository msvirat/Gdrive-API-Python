import os
import io
from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload

CLIENT_SECRET_FILE = 'client_secret_desktop.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPE = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPE)


file_ids = ['12WuWBzQxZtiNpNLtAA3KDKn4iz_xzTWU', '1ko_jF8TSKN-fdtC1-hNKQp7xC4uty_rg']
file_names = ['new.jpg', 'new.pdf']

for file_id, file_name in zip(file_ids, file_names):
    request = service.files().get_media(fileId=file_id)

    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)
    done=False

    while not done:
        status, done= downloader.next_chunk()
        print('Download prograss {}.'.format(status.progress()*100))

    fh.seek(0)

    with open(os.path.join('./', file_name), 'wb') as f:
        f.write(fh.read())
        f.close()
