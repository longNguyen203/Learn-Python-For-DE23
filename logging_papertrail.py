"""import logging
from logging.handlers import SysLogHandler

PAPERTRAIL_HOST = "logs.papertrailapp.com"
PAPERTRAIL_PORT = 37554

def main() -> None:
    logger = logging.getLogger("LongDE2003")
    logger.setLevel(logging.DEBUG)
    handler = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))
    logger.addHandler(handler)
    
    logger.debug("This is a debug message.")
    
    
if __name__ == "__main__":
    main()"""
    
import logging

# Cấu hình logging
logging.basicConfig(filename='app.log', level=logging.INFO)

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        # Ghi log khi có lỗi chia cho 0
        logging.error("Tried to divide by zero")
        return None
    # Ghi log kết quả
    logging.info(f"{x} divided by {y} is {result}")
    return result

if __name__ == "__main__":
    num1 = 10
    num2 = 5
    result = divide(num1, num2)
    if result is not None:
        print(f"Result: {result}")
        
        
        
        
        
        