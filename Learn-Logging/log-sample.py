import logging

"""
Có 5 cấp độ ghi nhật ký, theo thứ tự là: 
    DEBUG, 
    INFO, 
    WARNING, 
    ERROR, 
    CRITICAL,
nếu mức mặc định ghi nhật ký là WARNING thì nó sẽ ghi lại mọi thứ là cảnh báo(WARNING) trở lên như 
lỗi(ERROR), CRITICAL và bao gồm cả chính nó WARNING. Nó bỏ qua 2 cấp độ trên. Hoặc ta để cấp độ 
mặc định là DEBUG thì nó sẽ ghi lại mọi thứ của cả 5 cấp độ.
    
Nếu ta không chỉ định mức độ ghi nhật ký mặc định thì nó sẽ tự hiểu mức độ mặc định là WARNING
và nó sẽ chỉ ghi lại cấp độ WARNING và các cấp độ cao hơn ERROR, CRITICAL
"""

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="logging.log"
)

def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Divide Function"""
    return x / y

def layDu(x, y):
    return x % y

num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
logging.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logging.info("Sub: {} - {} = {}".format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logging.warning("Mul: {} * {} = {}".format(num_1, num_2, mul_result)) 

div_result = divide(num_1, num_2)
logging.error("Div: {} / {} = {}".format(num_1, num_2, div_result))

du_result = layDu(num_1, num_2)
logging.critical("Du: {} / {} = {}".format(num_1, num_2, du_result))










