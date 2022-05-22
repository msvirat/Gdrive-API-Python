from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_desktop.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPE = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPE)

folder_names = ['Dummy1', 'Dummy2']
for folder_name in folder_names:
    file_metadata = {
        'name': folder_name,
        "mimeType": 'application/vnd.google-apps.folder',
        # 'parents': []
    }
    service.files().create(body=file_metadata).execute()


