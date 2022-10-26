from EscolaDB import *

dao = EscolaDB()

teacher1 = {
    'name': 'Renzo',
    'age': 31,
    'area': 'Software'
}

teacher2 = {
    'name': "Marcelo",
    'age': 30,
    'area': "Software"
}

teacher3 = {
    'name': "Joao",
    'age': 25,
    'area': "Hardware"
}

teacher4 = {
    'name': "Luis",
    'age': 50,
    'area': "Fisica"
}

dao.create(teacher1)
dao.create(teacher2)
dao.create(teacher3)
dao.create(teacher4)

matter1 = {
    'subject': "BD",
    'time': "19:30"
}

matter2 = {
    'subject': "Paradigmas",
    'time': "21:30"
}

matter3 = {
    'subject': "Micro",
    'time': "21:30"
}

matter4 = {
    'subject': "Calculo3",
    'time': "21:30"
}

dao.create_matter(matter1)
dao.create_matter(matter2)
dao.create_matter(matter3)
dao.create_matter(matter4)

dao.create_relation(teacher1, matter1, 2015)
dao.create_relation(teacher2, matter2, 2018)
dao.create_relation(teacher3, matter3, 2022)
dao.create_relation(teacher4, matter4, 2005)

