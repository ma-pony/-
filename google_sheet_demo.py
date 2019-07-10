import logging
import os
import pickle

from googleapiclient.discovery import build

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class GoogleSheet:
    def __init__(self, spreadsheet_id: str, range_name: str):
        self.service = None
        self.spreadsheet_id = spreadsheet_id
        self.range_name = range_name

    def start_client(self):
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server()
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
                
        service = build('sheets', 'v4', credentials=creds)
        self.service = service

    def update_google_sheet(self, values: list):
        """
        更新
        :param values:
        :return:
        """
        body = {
            'values': values
        }
        result = self.service.spreadsheets().values().update(
            spreadsheetId=self.spreadsheet_id, range=self.range_name,
            valueInputOption="USER_ENTERED", body=body).execute()
        logger.info(f"sheet update result: {result}")

    def clear_google_sheet(self):
        """
        清空 sheet
        :return:
        """
        result = self.service.spreadsheets().values().clear(
            spreadsheetId=self.spreadsheet_id, range=self.range_name).execute()
        logger.info(f"sheet clear result: {result}")

    def append_google_sheet(self, values: list):
        """
        追加
        :param values:
        :return:
        """
        body = {
            'values': values
        }
        result = self.service.spreadsheets().values().append(
            spreadsheetId=self.spreadsheet_id, range=self.range_name,
            valueInputOption="USER_ENTERED", body=body).execute()
        logger.info(f"sheet append result: {result}")

    def copy_to_sheet(self):
        """
        复制一个sheet
        :return:
        """
        body = {
            "destinationSpreadsheetId": self.spreadsheet_id
        }
        result = self.service.spreadsheets().sheets().copyTo(
            body=body,
            spreadsheetId=self.spreadsheet_id,
            sheetId=0).execute()
        logger.info(f"copy to sheet result: {result}")
        
    def delete_google_sheet(self, sheet_id: int):
        """
        删除一个sheet
        :param sheet_id:
        :return:
        """
        request = {"requests": [{"deleteSheet": {"sheetId": sheet_id}}]}
        result = (
            self.service.spreadsheets()
                .batchUpdate(spreadsheetId=self.spreadsheet_id, body=request)
                .execute()
        )
        logger.info(f"delete sheet result: {result}")
        return result.get("sheetId")

    def create_google_sheet(self, title: str, sheet_id: int):
        """
         创建一个sheet
        :param title:
        :param sheet_id:
        :return:
        """
        request = {
            "requests": [
                {
                    "addSheet": {
                        "properties": {
                            "sheetId": sheet_id,
                            "title": title
                        }
                    }
                }
            ]
        }
        result = (
            self.service.spreadsheets()
                .batchUpdate(spreadsheetId=self.spreadsheet_id, body=request)
                .execute()
        )

        logger.info(f"create sheet result: {result}")
