# OLIONMUODOSTUS JA OLETUSARVOT

# ===========================

  

class RasekoMembers():
    """Greates a member of Raseko organisation"""

    def __init__(self, firstname,lastname,role='Student'):

        self.firstname = firstname

        self.lastname = lastname

        self.role = role

def palautaMerkkijono()->str | int | bool:
    volue = 154
    return volue 

if __name__ == '__main__':

  

    student = RasekoMembers('Jonne', 'Janttari')
    print(f'{student.firstname} rooli orgisaatiossa on {student.role}')
    teacher = RasekoMembers('Mikko', 'Viljanen', 1)

    print(f'{teacher.firstname} rooli organisaatiossa on {teacher.role}')
    
    print(palautaMerkkijono())
    