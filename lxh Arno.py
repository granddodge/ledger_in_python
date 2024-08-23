import json

if __name__ == '__main__':
    main()

def main():
    pass


# 自动输出当日日期
def date_today():
    pass


# 定义“金额”类
class Volume:

    # 基本属性：金额大小，金额种类，发生日期,用户备注
    def __init__(self, amount, category, date = date_today()):
        self.amount = amount
        self.date = date
        self.category = category
        self.footnote = None
        self.total_info = {'amount':self.amount, 'date':self.date, 'category':self.category, 'footnote':self.footnote}
        return self

    # 修改该笔金额基本属性
    def adjustment(self):
        pass

    # 删去该笔金额
    def delete(self):
        pass

    # 复制该笔金额
    def copy(self):
        pass

    # 为该金额添加备注
    def add_note(self):
        pass

    # 将该金额进行摊销
    def depreciation(self,):
        pass

    # 使得该金额周期性重复
    def repeat(self):
        pass


# 定义一个时间单位的类，这个类可以互相包含，通过嵌套来构成天、周、月、年的关系
class TimeUnit:
    # 基本属性：本时间单位，收入的列表, 支出的列表, 子时间单位列表，总收入金额，总收入笔数，总支出金额，总支出笔数，净收入金额，净支出金额，预算金额
    def __init__(self, timeUnit):
        self.timeUnit = timeUnit
        self.income_set = None
        self.expense_set = None
        self.sub_timeUnit = None # 这种命名方式合适吗？
        
        self.total_income = None
        self.num_income = None
        self.total_expense = None
        self.num_expense = None
        self.net_income = None
        self.net_expense = None
        self.budget = None

        return self
    
    #还没想好是否合适
    def add_subTimeUnit(self):

