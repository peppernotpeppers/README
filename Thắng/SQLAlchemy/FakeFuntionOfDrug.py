from faker import Faker
from faker.generator import random
from faker.providers import BaseProvider

fake = Faker()

class EffectOfDrug(BaseProvider):
    
    def effectName ():
        useAbleNameOfDrug = [
            'Đau bụng','Đau đầu','Đau tay','Đau trĩ','Đau chân','Đau răng','Đau tim','Đau gan','Đau thận','Ốm, sốt cao',
            'Đau đầu, sốt nhẹ','Tiêu chảy','Đau bụng','Nhỏ mắt','Viêm tai','Rocket 1h','Thuốc mỡ bôi vết bỏng',
            'Thuốc nhiễm trùng','Nước muối sinh lý','Vitamin A','Vitamin B','Vitamin C','Vitamin E','Chống suy tim',
            'Tránh thai','Giảm đau','Thuốc ngủ','Kháng sinh','Nước súc miệng','Đau nửa đầu','Viêm mũi dị ứng',
            'Chống sưng, phù nề','Trị mụn','Chữa sỏi thận'
        ]
        
        return random.choice(useAbleNameOfDrug)


class DrugQuatityStatus (BaseProvider):
    
    def quatityStatus ():
        stockStatus = [
            'Available', 'Out Of Stock'
        ]
        return random.choice(stockStatus)


fake.add_provider(EffectOfDrug)      #Add thêm provider vào faker (nguồn từ EffectOfDrug)
fake.add_provider(DrugQuatityStatus) #Add thêm provider vào faker (nguồn từ DrugQuantityStatus)

seteffectName  = EffectOfDrug.effectName()
setquantityStatus = DrugQuatityStatus.quatityStatus()

def get_shuffled_effect():
    random.shuffle(seteffectName)      #Biến đổi tuple tại effectName thành list
    return seteffectName


def get_shuffled_quatity():
    random.shuffle(setquantityStatus)      #Biến đổi tuple tại setquantityStatus thành list
    return setquantityStatus

