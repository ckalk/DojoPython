# Assignment: Hospital - You're going to build a hospital with patients in it! Create a hospital class.
# Before looking at the requirements below, think about the potential characteristics of each patient and hospital. How would you design each?

# Hospital:
 #2) Discharge: look up and remove a patient from the list of patients. Change bed number for that patient back to none.
# This is a challenging assignment. Ask yourself what input each method requires and what output you will need.

from datetime import datetime
import itertools
from collections import defaultdict
import weakref

class KeepRefs(object):
    __refs__ = defaultdict(list)
    def __init__(self):
        self.__refs__[self.__class__].append(weakref.ref(self))

    @classmethod
    def get_instances(cls):
        for inst_ref in cls.__refs__[cls]:
            inst = inst_ref()
            if inst is not None:
                yield inst

class Patient(KeepRefs):
    # Attributes: 1) Id: an id number, 2) Name, 3) Allergies, 4) Bed number: should be none by default
    newid = itertools.count().next
    def __init__( self, name, allergies, bed_num=None):
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

    @classmethod
    def create(self, name, allergies):
        self = Patient(name, allergies)
        return self
        
    def findPatientByID(self, id):
        #print "finding patient id=", id
        for r in Patient.get_instances():
            # print "r = ", r
            # print "r.id=", r.id
            if r.id == id:
                #print "found patient with id ", id
                return r
        #if not found, return dummy patient passed in as self
        return self
        

class Hospital(object):
# Attributes: 1) Patients: an empty array, 2) Name: hospital name, 3) Capacity: an integer indicating the maximum number of patients the hospital can hold.
    def __init__( self, patients, name, capacity):
        self.patients= patients
        self.name = name
        self.capacity = capacity 

    def displayInfo(self):
        print "--- Hospital Info ---"
        print "  Name:", self.name
        print "  Capacity:", self.capacity
        print "  Patients:", self.patients
        for i in range(len(self.patients)):
            Patient.findPatientByID(patient0, self.patients[i]).displayInfo()
        return self

    # Methods:
    #1) Admit: add a patient to the list of patients. Assign the patient a bed number. If the length of the list is >= the capacity do not admit the patient. Return a message either confirming that admission is complete or saying the hospital is full.
    def admitNewPatient(self, id):
        self.patients.append(id)
        self.queue_size+=1
        print "added call to end of queue"
        return self

all_patients = []
#Test: create a patient
all_patients.append(Patient("No Name", ["none"]))
all_patients.append(Patient("Cindy Kalkomey",["none"]))
all_patients.append(Patient("Kathy Williams",["gluten", "peanuts", "shellfish"]))
print all_patients
#Patient.create(patient0, "No Name", ["none"])
# patient1 = Patient("Cindy Kalkomey",["none"])
# Patient.displayInfo(patient1)
# patient2 = Patient("Kathy Williams",["gluten", "peanuts", "shellfish"])
# Patient.displayInfo(patient2)

#Test: create a hospital
hospital1 = Hospital([1,2], "Medical City", 100)
Hospital.displayInfo(hospital1)

# Test findPatientByID
# findID=1
# print "---- Finding Patient with ID=",findID,"----"
# Patient.findPatientByID(patient0, findID).displayInfo()
