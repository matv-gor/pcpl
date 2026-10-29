class Computer:

    def __init__(self, id, name):
        self.id = id
        self.name = name

class Program:

    def __init__(self, id, name, size, computer_id):
        self.id = id
        self.name = name
        self.size = size
        self.computer_id = computer_id

class Installation:

    def __init__(self, program_id, computer_id):
        self.program_id = program_id
        self.computer_id = computer_id

computers = [
    Computer(1, "Компьютер учебный"),
    Computer(2, "Компьютер рабочий"),
    Computer(3, "Ноутбук"),
]

programs = [
    Program(1, "Архиватор", 120, 1),
    Program(2, "Браузер", 350, 1),
    Program(3, "Антивирус", 800, 2),
    Program(4, "Редактор", 250, 2),
    Program(5, "Плеер", 180, 3),
]

installations = [
    Installation(1, 1),
    Installation(1, 2),
    Installation(2, 1),
    Installation(3, 2),
    Installation(3, 3),
    Installation(5, 3)
]


def main():
    print("Запрос Е1")

    for computer in computers:
        if "компьютер" in computer.name.lower():
            print(f"{computer.name}: ", end="")

            separator = ""
            for program in programs:
                if program.computer_id == computer.id:
                    print(f"{separator}{program.name}", end="")
                    separator = ", "

            print()
    print()

    print("Запрос Е2")

    result = []
    for computer in computers:
        total_size = 0
        amount = 0

        for program in programs:
            if(program.computer_id == computer.id):
                total_size += program.size
                amount += 1

        average_size = round(total_size / amount, 2)
        result.append((computer.name, average_size))

    result.sort(key=lambda item: item[1])
    for name, average in result:
        print(f"{name}: {average:.2f} МБ")
    print()


    print("Запрос Е3")

    for program in programs:

        if (program.name.lower().startswith("а")):
            print(f"{program.name}: ", end="")
            separator = ""

            for installation in installations:
                if (installation.program_id == program.id):

                    for computer in computers:
                        if (computer.id == installation.computer_id):
                            print(f"{separator}{computer.name}", end="")
                            separator = ", "
            print()

if __name__ == "__main__":
    main()
