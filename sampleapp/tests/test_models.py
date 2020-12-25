from django.test import TestCase
from sampleapp.models import Address, Employee

# manage.py test sampleapp.tests.test_model.MappingTest.test_assign_emp_to_adr


class MappingTest(TestCase):

    def setUp(self) -> None:
        self.emplist = []
        for item in range (5):
            emp = Employee(id=item+1, name=f'AAA{item}', age=item+1, sal=2525.25+item)
            self.emplist.append(emp)
        Employee.objects.bulk_create(self.emplist)

        self.adrlist = []
        for item in range(5):
            adr = Address(id=item+101, city=f'Pune{item}', state=f'MH{item}', pincode=413101+item)
            self.adrlist.append(adr)
        Address.objects.bulk_create(self.adrlist)


    def tearDown(self) -> None:
        pass

    def setUpClass(cls):
        pass

    def tearDownClass(cls):
        pass

    def test_assign_emp_to_adr(self):
        # accessing first employee from emplist
        emp1 = self.emplist[0]
        emp1.save()
        # accessing first adress from adrlist
        adr1 = self.adrlist[0]
        adr1.save()
        # assigning employee to address
        adr1.emp = emp1
        # getting employee object from database
        dbemp = Employee.objects.filter(id=emp1.id).first()

        self.assertEqual(dbemp, emp1)
        self.assertEqual(adr1, dbemp.adr)

        dbadr = Address.objects.filter(id=adr1.id).first()

        self.assertEqual(dbadr, adr1)
        self.assertEqual(emp1, dbadr.emp)

    def test_assign_adr_to_emp(self):
        pass

    def test_assign_many_adrs_to_emp(self):
        pass

