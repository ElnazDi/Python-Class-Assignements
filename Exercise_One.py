# Assignment 1 - Exercise 1 (COVID_19)
# Elnaz Dehkharghani - MatriculationNumber: 11015404
# Last Version For Submission


import random
import datetime

batch_num = 5
patients_recovered_num = 20


# Define a class for our patients
class Patient:
    name = ''
    date = ''

    def __init__(self, name, date):
        self.name = name
        self.date = date

    def test_for_covid(self):
        self.date = datetime.datetime.now()


# Define a class for the City
class City:
    city_name = ''
    patients_recovered_list = []
    patients_picked_or_tested = []

    def __init__(self, name):
        self.city_name = name

    def add_recovered_patients(self, num):
        '''Gets number of recovered patients, add to list'''
        for i in range(1, num + 1):
            patient_instance = Patient(f'P{i}', '')
            self.patients_recovered_list.append(patient_instance)

    def pick_a_batch(self, batch_num):
        '''Returns a list of patients as a batch'''
        picked_batch_tmp = []
        while True:
            if len(self.patients_recovered_list) > 0:
                patient_item = self.patients_recovered_list.pop(
                    random.randint(0, len(self.patients_recovered_list)-1))
                picked_batch_tmp.append(patient_item)
                self.patients_picked_or_tested.append(patient_item)

            if len(picked_batch_tmp) >= batch_num or len(self.patients_recovered_list) == 0:
                break

        return picked_batch_tmp

    def pick_a_patient_from_batch(self, batch):
        '''Gets a list of patients as batch, pick randomly and returns one patient'''
        return batch[random.randint(0, len(batch)-1)]


if batch_num < 1:
    print('Batch number is lower than 1. Not possible.')
    exit(1)


cityx = City('X')
cityx.add_recovered_patients(patients_recovered_num)
while True:
    picked_batch = cityx.pick_a_batch(batch_num)
    if len(picked_batch) < batch_num:
        break
    patient_instance = cityx.pick_a_patient_from_batch(picked_batch)
    patient_instance.test_for_covid()
    print(
        f'Patient {patient_instance.name} tested for COVID-19 in {patient_instance.date}')
