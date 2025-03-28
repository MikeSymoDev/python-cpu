class MinimalCPU:
    def __init__(self, instructions=None):
        self.instructions = instructions if instructions is not None else []
        self.data_memory = {}
        self.pc = 0

    def execute_instruction(self, instruction):
        if instruction == "NOP":
            print(f"Executing NOP at PC = {self.pc}")
        else:
            print(f"Unbekannte Instruktion '{instruction}' bei PC = {self.pc}")

    def run(self):
        while self.pc < len(self.instructions):
            current_instruction = self.instructions[self.pc]
            self.execute_instruction(current_instruction)
            self.pc += 1


if __name__ == "__main__":
    program = ["NOP", "NOP", "NOP"]
    cpu = MinimalCPU(instructions=program)
    cpu.run()
