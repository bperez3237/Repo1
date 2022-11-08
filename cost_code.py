

class CostCode:

    def __init__(self, bill_code, engineer, category,forecast_qty,forecast_mhs, current_qty, current_mhs, spent_to_date, areas = None):
        self.bill_code = bill_code
        self.phase_code = bill_code[5:12]
        self.engineer = engineer
        self.category = category
        self.forecast_qty =forecast_qty
        self.forecast_mhs =forecast_mhs
        self.current_qty = current_qty
        self.current_mhs = current_mhs
        self.spent_to_date = spent_to_date
        self.labor_rate = spent_to_date/current_mhs
        self.areas = areas

class AreaCode(CostCode):
    def __init__(self, sub_category):
        self.sub_category = sub_category
        CostCode.__init__(self, bill_code, engineer, category,forecast_qty,forecast_mhs, current_qty, current_mhs, spent_to_date, areas = None)
