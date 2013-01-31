import puzzleconfig
import board
import puzzle
import wires

class BoardFactory:
    def generate(lock):
        config = puzzleconfig.puzzle
        ident_inpput = config.getAllInputDevices()
