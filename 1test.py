from fileinput import filename
import logging


logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

class math():
        
    def plus(a ,b):
        return a + b

    def minus(a,b):
        return a - b

    def divine(a,b):
        return a/b

    def multi(a,b):
        return a*b

a=5
b=10
cong = math.plus(a, b)
logging.info(cong)

tru = math.minus(a,b)
logging.debug (tru)

chia = math.divine(a,b)
logging.debug (chia)

nhan = math.multi(a,b)
logging.debug (nhan)
