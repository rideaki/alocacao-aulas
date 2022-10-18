from model.business.tableFactory import construct_class_table


# Classe relativa aos dados de cada turma
class ClassData:

    # Constructor
    def __init__(
            self,
            semester_number_arg,
            shift_arg,  # turno: MORNING, AFTERNOON ou NIGHT
            time_table_arg=construct_class_table(),
    ):
        self.semesterNumber = semester_number_arg
        self.shift = shift_arg  # turno: MORNING, AFTERNOON ou NIGHT
        self.timeTable = time_table_arg
