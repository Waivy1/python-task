from this_is_a_package.module1 import FirstLastName
from this_is_a_package.module2 import get_born_year

Vika = FirstLastName('Vika', 22)
print(Vika.get_name())

print(get_born_year(Vika.age))
