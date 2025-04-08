class MinimalCPU:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions
        self.pc = 0
        self.registers = {"A": 0, "B": 0}
        self.state_stack = []

    def step(self):
        if self.pc >= len(self.instructions):
            self.pc = 0

        instruction = self.instructions[self.pc]
        
        if instruction == "NOP":
            print(f"{self.name}: Executing NOP at PC = {self.pc}")
            self.pc += 1

        elif instruction == "JMP":

            print(f"{self.name}: Executing JMP at PC = {self.pc} - switching context")
            self.pc = 0
            return True

        elif instruction == "INT":

            print(f"{self.name}: Executing INT at PC = {self.pc} - interrupt triggered")
            self.interrupt()

        else:
            print(f"{self.name}: Unknown instruction '{instruction}' at PC = {self.pc}")
            self.pc += 1

        return False

    def interrupt(self):

        state = {"pc": self.pc, "registers": self.registers.copy()}
        self.state_stack.append(state)
        print(f"{self.name}: CPU state saved: {state}")

        asm_interrupt_handler(self)
        restored_state = self.state_stack.pop()
        self.pc = restored_state["pc"]
        self.registers = restored_state["registers"]
        print(f"{self.name}: CPU state restored: {restored_state}")

def asm_interrupt_handler(cpu):
    print(f"{cpu.name}: Assembly Interrupt Handler executing!")
    cpu.registers["A"] += 1
    print(f"{cpu.name}: Register 'A' modified to {cpu.registers['A']}")

def run_cpus(cpu1, cpu2):
    current_cpu = cpu1
    other_cpu = cpu2

    while True:
        context_switch = current_cpu.step()

        if context_switch:
            current_cpu, other_cpu = other_cpu, current_cpu

if __name__ == "__main__":
    program = ["NOP", "NOP", "INT", "NOP", "JMP"]

    cpu1 = MinimalCPU("CPU1", program)
    cpu2 = MinimalCPU("CPU2", program)

    run_cpus(cpu1, cpu2)
