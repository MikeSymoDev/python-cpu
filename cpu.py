class MinimalCPU:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions
        self.pc = 0

    def step(self):
        if self.pc >= len(self.instructions):
            self.pc = 0

        instructions = self.instructions[self.pc]
        if instructions == "NOP":
            print(f"{self.name}: Executing NOP at PC = {self.pc}")
            self.pc += 1
            return False
        elif instructions == "JMP":
            print(f"{self.name}: Executing JMP at PC = {self.pc} - switching context")
            self.pc = 0
            return True
        else:
            print(f"{self.name}: Unknown instruction '{instructions}' at PC = {self.pc}")
            self.pc += 1
            return False

def run_cpus(cpu1, cpu2):
    current_cpu = cpu1
    other_cpu = cpu2

    while True:
        context_switch = current_cpu.step()
        if context_switch:
            current_cpu, other_cpu = other_cpu, current_cpu

if __name__ == "__main__":
    program = ["NOP", "NOP", "JMP"]

    cpu1 = MinimalCPU("CPU1", program)
    cpu2 = MinimalCPU("CPU2", program)

    run_cpus(cpu1, cpu2)
