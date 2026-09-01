'''
Hard Problem 2 – Hospital Management with Treatment Plans
Context A hospital needs a system to manage patients, doctors, and treatment plans. Each patient has a medical history, and doctors can prescribe treatments. The system must also handle billing and insurance claims.

Task Create the following classes:

Person (abstract base)
Attributes: name, age, contact (private).
Abstract method: get_role() – returns "Patient" or "Doctor".
Patient (inherits Person)
Adds: patient_id, medical_history (list of strings), insurance_provider.
Methods:
add_record(record)
get_history()
Doctor (inherits Person)
Adds: specialization, employee_id, schedule (dict: day -> list of time slots).
Methods: is_available(date, time).
Treatment (abstract)
Attributes: name, cost, duration_days.
Abstract method: calculate_insurance_coverage(insurance) – returns amount covered.
MedicationTreatment (inherits Treatment)
Adds: drug_name, dosage.
Coverage: 80% of cost if insurance covers drugs.
SurgeryTreatment (inherits Treatment)
Adds: surgery_type, surgeon.
Coverage: 60% of cost.
Appointment
Private: __patient, __doctor, __date, __time, __treatment (Treatment).
Methods:
schedule()
cancel()
generate_bill() – returns (total, insurance_paid, patient_pays).
Hospital
Manages: lists of doctors, patients, appointments.
Methods:
add_doctor(doctor)
add_patient(patient)
schedule_appointment(patient, doctor, date, time, treatment)
get_appointments_for_patient(patient)
Additional Requirements

Use ABC and @abstractmethod.
Implement __str__ for all classes.
Use class variables to track total patients and doctors.
Override __eq__ and __hash__ for Patient and Doctor to allow set operations.
'''


from abc import ABC, abstractmethod

class Person(ABC):
  def __init__(self,name,age,contact=None):
    self.name = name
    self.age = age
    self.__contact = contact
  
  @abstractmethod
  def get_role(self):
    pass


class Patient(Person):
  def __init__(self,name,age,contact,id,insurance,history=[]):
    super().__init__(name,age,contact)
    self.patient_id = id
    self.insurance_provider = insurance
    self.medical_history = history

  def add_record(self,record):
    self.medical_history.append(record)
    return True

  def get_history(self):
    return self.medical_history

  def get_role(self):
    return 'Patient'


class Doctor(Person):
  def __init__(self,name,age,contact,specialization,id):
    super().__init__(name,age,contact)
    self.specialization = specialization
    self.employee_id = id 
    self.booked_time_slots = []

  def is_available(self,date,time):
    for d,t in self.booked_time_slots:
      if d == date and t == time:
        return False
    return True

  def get_name(self):
    return self.name

  def get_role(self):
    return 'Doctor'


class Treatment(ABC):
  def __init__(self,name,cost,duration):
    self.name = name
    self.cost = cost 
    self.duration = duration 

  @abstractmethod
  def calculate_insurance_coverage(self,insurance):
    pass


class MedicationTreatment(Treatment):
  def __init__(self,name,cost,duration,drug_name,dosage):
    super().__init__(name,cost,duration)
    self.drug_name = drug_name
    self.dosage = dosage

  def calculate_insurance_coverage(self, insurance):
    if insurance == 'jubille' or insurance == 'BlueCross':
      return self.cost * 0.80
    else:
      return self.cost * 0.40


class SurgeryTreatment(Treatment):
  def __init__(self,name,cost,duration,surgery_type):
    super().__init__(name,cost,duration)
    self.surgery_type = surgery_type

  def calculate_insurance_coverage(self,insurance):
    return self.cost * 0.60


class Appointment():
  def __init__(self,patient,doctor,date,time,treatment):
    self.__patient = patient
    self.__doctor = doctor
    self.__date = date
    self.__time = time
    self.__treatment = treatment
    self.status = False

  def schedule(self):
    if self.__doctor.is_available(self.__date,self.__time):
      self.__doctor.booked_time_slots.append([self.__date,self.__time])
      self.status = True
      return True
    return False

  def get_patient(self):
    return self.__patient

  def get_doctor(self):
    return self.__doctor

  def get_time(self):
    return self.__time

  def get_date(self):
    return self.__date
  
  def cancel(self):
    if self.status:
      self.__doctor.booked_time_slots.remove([self.__date,self.__time])
      self.status = False
      return True
    return False

  def generate_bill(self):
    total = self.__treatment.cost
    insurance_paid = self.__treatment.calculate_insurance_coverage(self.__patient.insurance_provider)
    patient_pays = total - insurance_paid
    data = [total,insurance_paid,patient_pays]
    return data


class Hospital():
  total_patients = 0
  total_doctors = 0

  def __init__(self):
    self.doctors = []
    self.patients = []
    self.appointments = []

  def add_doctor(self,doctor):
    if doctor not in self.doctors:
      self.doctors.append(doctor)
      Hospital.total_doctors+=1
      return True
    return False

  def add_patient(self,patient):
    if patient not in self.patients:
      self.patients.append(patient)
      Hospital.total_patients+=1
      return True
    return False

  def schedule_appointment(self,patient,doctor,date,time,treatment):
    appointment = Appointment(patient,doctor,date,time,treatment)
    result = appointment.schedule()
    if not result:
      return False
    else:
      self.appointments.append(appointment)
      return appointment

  def get_appointments_for_patient(self,patient):
    result = []
    for i in self.appointments:
      if i.get_patient() == patient:
        result.append(i)
    return result




# 6 Test cases 



# ============================================
# TEST BLOCK FOR HARD #2 
# ============================================

print("=" * 40)
print("TEST 1: Schedule Appointment + Generate Bill (Medication)")
print("=" * 40)

hospital = Hospital()
doc = Doctor("Dr. Smith", 45, "123-456-7890", "Cardiology", "D123")
patient = Patient("John Doe", 30, "987-654-3210", "P456", "BlueCross")
patient.add_record("Annual checkup")
hospital.add_doctor(doc)
hospital.add_patient(patient)

treatment_med = MedicationTreatment("Antibiotics", 200, 7, "Amoxicillin", "500mg")
appt1 = hospital.schedule_appointment(patient, doc, "2026-08-01", "10:00", treatment_med)

total, insurance_paid, patient_pays = appt1.generate_bill()
print(f"Total cost: ${total}")
print(f"Insurance covers (80%): ${insurance_paid}")
print(f"Patient pays: ${patient_pays}")

print("\n" + "=" * 40)
print("TEST 2: Schedule Appointment + Generate Bill (Surgery)")
print("=" * 40)

treatment_surgery = SurgeryTreatment("Heart Bypass", 50000, 5, "Open")
appt2 = hospital.schedule_appointment(patient, doc, "2026-08-01", "14:00", treatment_surgery)

total2, insurance_paid2, patient_pays2 = appt2.generate_bill()
print(f"Total cost: ${total2}")
print(f"Insurance covers (60%): ${insurance_paid2}")
print(f"Patient pays: ${patient_pays2}")

print("\n" + "=" * 40)
print("TEST 3: Double-Booking Prevention (Using if/else)")
print("=" * 40)

# Try to book the SAME doctor at the SAME time (10:00)
result3 = hospital.schedule_appointment(patient, doc, "2026-08-01", "10:00", treatment_med)

if result3 == False:
    print("✅ Successfully prevented double-booking. (Returned False)")
else:
    print("❌ ERROR: Double-booking allowed! (Returned an appointment object)")

print("\n" + "=" * 40)
print("TEST 4: Hospital Manager - Get Appointments for Patient")
print("=" * 40)

appointments = hospital.get_appointments_for_patient(patient)
print(f"Number of appointments for John Doe: {len(appointments)}")  # Should be 2

for appt in appointments:
    print(f"  - {appt.get_doctor().get_name()} at {appt.get_time()} on {appt.get_date()}")

print("\n" + "=" * 40)
print("TEST 5: Edge Case - Patient with NO appointments")
print("=" * 40)

new_patient = Patient("Jane Doe", 25, "111-222-3333", "P789", "Aetna")
hospital.add_patient(new_patient)

appts_empty = hospital.get_appointments_for_patient(new_patient)
print(f"Appointments for Jane Doe: {appts_empty}")  # Should be []
print(f"Type: {type(appts_empty)}")  # Should be <class 'list'>

print("\n" + "=" * 40)
print("TEST 6: Doctor Availability Check (is_available)")
print("=" * 40)

print(f"Is Dr. Smith available at 10:00 on 2026-08-01? {doc.is_available('2026-08-01', '10:00')}")  # Should be False
print(f"Is Dr. Smith available at 11:00 on 2026-08-01? {doc.is_available('2026-08-01', '11:00')}")  # Should be True