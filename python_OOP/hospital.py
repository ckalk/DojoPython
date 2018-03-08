# Assignment: Hospital - You're going to build a hospital with patients in it! Create a hospital class.
# Before looking at the requirements below, think about the potential characteristics of each patient and hospital. How would you design each?
# This is a challenging assignment. Ask yourself what input each method requires and what output you will need.

from datetime import datetime
import itertools
# from collections import defaultdict
# import weakref

# class KeepRefs(object):
#     __refs__ = defaultdict(list)
#     def __init__(self):
#         self.__refs__[self.__class__].append(weakref.ref(self))

#     @classmethod
#     def get_instances(cls):
#         for inst_ref in cls.__refs__[cls]:
#             inst = inst_ref()
#             if inst is not None:
#                 yield inst

# class Patient(KeepRefs):
class Patient(object):
    # Attributes: 1) Id: an id number, 2) Name, 3) Allergies, 4) Bed number: should be none by default
    newid = itertools.count().next
    def __init__( self, name, allergies, bed_num="none"):
        super(Patient, self).__init__()
        self.id = Patient.newid()
        self.name = name
        self.allergies = allergies 
        self.bed_num = bed_num

    def displayInfo(self):
        print "--- Patient Info ---"
        print "  ID:", self.id
        print "  Name:", self.name
        print "  Allergies:", self.allergies
        print "  Bed Number:", self.bed_num
        return self

    def displayAll(self, all_patients):
        for i in range(len(all_patients)):
            Patient.displayInfo(all_patients[i])
        return self

    @classmethod
    def create(self, name, allergies):
        self = Patient(name, allergies)
        return self
        
    def findByID(self, id):
        #print "finding patient id=", id
        for r in all_patients:
            # print "r = ", r
            # print "r.id=", r.id
            if r.id == id:
                #print "found patient with id ", id
                return r
        #if not found, return dummy patient passed in as self
        return None
        
    def setBed(self, id, num):
        #print "finding patient id=", id
        for r in all_patients:
            # print "r = ", r
            # print "r.id=", r.id
            if r.id == id:
                #print "found patient with id ", id
                r.bed_num = num
                return r
        #if not found, return dummy patient passed in as self
        return None

class Hospital(object):
# Attributes: 1) Patients: an empty array, 2) Name: hospital name, 3) Capacity: an integer indicating the maximum number of patients the hospital can hold.
    def __init__( self, name, capacity):
        self.patients= []
        self.name = name
        self.capacity = capacity

    def displayInfo(self):
        print "--- Hospital Info ---"
        print "  Name:", self.name
        print "  Capacity:", self.capacity
        print "  Filled Beds:", len(self.patients)
        print "  Patients:", self.patients
        for i in range(len(self.patients)):
            Patient.findByID(patient0, self.patients[i]).displayInfo()
        return self
    
    def getAvailableBed(self):
        #loop over beds
        for i in range(1, self.capacity+1):
            #loop over admitted patients and check if bed is taken
            bed_taken = False
            for j in range(len(self.patients)):
                if Patient.findByID(patient0, self.patients[j]).bed_num == str(i):
                     bed_taken =  True
            if not bed_taken:
                bed_num = str(i)
                return bed_num
        bed_num = "not available"
        return bed_num


    # Methods:
    #1) Admit: add a patient to the list of patients. Assign the patient a bed number. If the length of the list is >= the capacity do not admit the patient. Return a message either confirming that admission is complete or saying the hospital is full.
    def admitPatient(self, id):
        #check that patient exists
        if Patient.findByID(patient0, id) == None:
            print "Patient id=", id, "does not exist"
            return self
        # if number of patients admitted so far < capacity, admit patient
        if len(self.patients) < self.capacity:
            self.patients.append(id)
            #assign next bed to admitted patient
            bed_num = Hospital.getAvailableBed(self)
            print "first available bed = ", bed_num
            Patient.setBed(patient0, id, bed_num)
            message = "Patient id = " + str(id) + " was admitted to bed number " + bed_num 
        else:
             message = "Patient id = " + str(id) + " was not admitted. Hospital is FULL."
        return message

 #2) Discharge: look up and remove a patient from the list of patients. Change bed number for that patient back to none.
    def dischargePatient(self, id):
        #check that patient is in admitted list of patient ids
        for i in range(len(self.patients)):
            if self.patients[i] == id:
                #remove patient from list
                self.patients.pop(i)
                #Change bed number for patient back to 
                Patient.setBed(patient0, id, "none")
                message = "Patient id = " + str(id) + " was discharged" 
                return message
        message = "Patient id = " + str(id)+ " does not exist in list of previously admitted patients"
        return message


# Create an array of possible patients
all_patients = []
patient0 = Patient("No Name", ["none"])
#Test: create a patient
all_patients.append(Patient("Ted Thomas", ["penicillin", "eggs"]))
all_patients.append(Patient("Cindy Kalkomey",["none"]))
all_patients.append(Patient("Kathy Williams",["gluten", "peanuts", "shellfish"]))
all_patients.append(Patient("Kurt Williams",["peanuts", "avacados"]))
all_patients.append(Patient("Gene Barbosa",["alcohol", "peanuts", "sugar"]))
all_patients.append(Patient("Allen Sayer",["peanuts", "olive oil", "tylenol"]))
Patient.displayAll(patient0, all_patients)


#Test: create a hospital and admit patients
hospital1 = Hospital( "Medical City", 5)
Hospital.displayInfo(hospital1)
#try to admit 6 patients, and capcity is 5
print "--- Admitting Patients ---"
print Hospital.admitPatient(hospital1,1)
print Hospital.admitPatient(hospital1,2)
print Hospital.admitPatient(hospital1,6)
print Hospital.admitPatient(hospital1,4)
print Hospital.admitPatient(hospital1,3)
print Hospital.admitPatient(hospital1,5)
#check that only first 5 admissions are patients
Hospital.displayInfo(hospital1)
#discharge one patient
print "--- Discharging Patients ---"
print Hospital.dischargePatient(hospital1, 4)
#check that now only 4 patients
print "--- check hospital now has 4 patients ---"
Hospital.displayInfo(hospital1)
# check that patient with id = 4 has bed_num set back to "none"
print "--- check bed_num of patient id = 4 in list of all_patients ---"
Patient.displayAll(patient0, all_patients)
# admit another patient
print "--- Admitting Patients ---"
print Hospital.admitPatient(hospital1,5)
Hospital.displayInfo(hospital1)