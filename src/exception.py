import sys
from src.logger import logging

def error_message_details(error,error_details:sys):
        _,_,exc_tb = error_details.exc_info()
        file_name=exc_tb.tb_frame.f_code.co_filename

        error_message = "Error occured in python script name [{0}] line number [{1}] error message",(file_name,exc_tb.tb_lineon,str(error))

        return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_details=error_details)
    