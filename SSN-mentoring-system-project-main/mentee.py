"""Author: Badri"""
class mentee:

    def __init__(self,fname=None,lname=None,BloodGroup=None,EmailId=None,
    MobileNumber=None,gender=None,nationality=None,religion=None,MotherTongue=None,
    ProgramName=None,ModeOfAdm=None,AdmissionCategory=None,AssociatedDepartment='Information Technology'):

        self._fname = fname
        self._lname = lname
        self._fullname = fname+" "+lname
        self._blood_group = BloodGroup
        self._EmailId = EmailId
        self._MobileNumber=MobileNumber
        self._gender=gender
        self._nationality = nationality 
        self._religion = religion 
        self._MotherTongue= MotherTongue
        self._ProgramName=ProgramName
        self._AssociatedDepartment = AssociatedDepartment
        self._ModeOFAdm = ModeOfAdm
        self._AdmissionCategory=AdmissionCategory
    
class AdmissionDetails:

    def __init__(self,ProgramName=None,AssociatedDepartment=None,ModeOfAdm=None,AdmissionCategory=None):
        self._ProgramName=ProgramName
        self._AssociatedDepartment = AssociatedDepartment
        self._ModeOFAdm = ModeOfAdm
        self._AdmissionCategory=AdmissionCategory

class parents(mentee):

    def __init__(self,DigitalId=None,mothername=None,mothermobilenumber=None,fathername=None,fathermobilenumber=None):
        super().__init__(DigitalId)
        self._mothername=mothername
        self._fathername=fathername
        self._m1 = mothermobilenumber
        self._m2 = fathermobilenumber



