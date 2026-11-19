class Patient:
  def __init__(self, name, bill_amount):
    self.name = name
    self.bill_amount = bill_amount

  def get_name(self):
    return self.name

  def set_name(self, name):
    self.name = name

  def get_bill_amount(self):
    return self.bill_amount

  def set_bill_amount(self, bill_amount):
    self.bill_amount = bill_amount

  def calculate_bill(self):
    return self.bill_amount


class SeniorPatient(Patient):
  def __init__(self, name, bill_amount):
    super().__init__(name, bill_amount)
    self.name = name
    self.bill_amount = bill_amount

  def calculate_bill(self):
    return self.bill_amount * 0.8


class PHPatient(Patient):
  def __init__(self, name, bill_amount):
    super().__init__(name, bill_amount)
    self.name = name
    self.bill_amount = bill_amount

  def calculate_bill(self):
    return self.bill_amount * 0.85


first_patient = Patient("Yoru", 1200)
second_patient = SeniorPatient("Omen", 2100)
third_patient = PHPatient("Chamber", 3800)

print("Hospital Billing System")
print("-----------------------")
print(f"Patient Name: {first_patient.name}\nOriginal Bill: {first_patient.bill_amount}\nFinal Bill: {first_patient.calculate_bill()}")
print(f"\nPatient Name: {second_patient.name}\nOriginal Bill: {second_patient.bill_amount}\nFinal Bill: {second_patient.calculate_bill()}")
print(f"\nPatient Name: {third_patient.name}\nOriginal Bill: {third_patient.bill_amount}\nFinal Bill: {third_patient.calculate_bill()}")