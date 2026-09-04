#!/usr/bin/env python3
"""
Esqueleto del Codificador Educativo de Instrucciones RISC-V.
CE4301 Arquitectura de Computadores I — Proyecto Individual — 2026-II

Este esqueleto ya implementa el contrato de línea de comandos y de salida
requerido por la especificación. Usted debe completar las dos funciones
marcadas con TODO; puede modificar el resto del archivo si lo necesita,
siempre que se preserve el contrato de invocación y la línea "HEX: 0x...".

No es obligatorio usar este esqueleto ni Python: puede implementar su
propia herramienta desde cero, en el lenguaje que prefiera, siempre que
respete el mismo contrato (ver especificación, sección "Modo de operación").
"""
import sys

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'

SOPORTADAS = ["add", "sub", "and", "or", "addi", "andi",
              "lw", "lb", "sw", "sb", "beq", "bne"]


def encode_instruction(instruction: str) -> int:
    """
        Recibe una instrucción como texto, p. ej. "add x5, x6, x7", y debe
        retornar su codificación de 32 bits como entero (0 <= valor < 2**32).
    
        Debe soportar únicamente las instrucciones en SOPORTADAS. Los valores
        de opcode/funct3/funct7 de cada una NO se proveen aquí: deben
        investigarse en el manual oficial de la ISA RISC-V (ver referencia en
        la especificación) y documentarse en el README.
    """
    rs1 = 0b00000
    rs2 = 0b00000
    rd = 0b00000
    funct3 = 0b000
    funct7 = 0b0000000
    imm = 0b000000000000
    opcode = 0b0000000


    segment_lengths = {
        'rs1': 5,
        'rs2': 5,
        'rd': 5,
        'funct3': 3,
        'funct7': 7,
        'imm': 12,
        'opcode': 7
    }

    instruction_order = {
        'R': ['funct7', 'rs2', 'rs1', 'funct3', 'rd', 'opcode'],
        'I': ['imm', 'rs1', 'funct3', 'rd', 'opcode'],
        'S': ['imm >> 5', 'rs2', 'rs1', 'funct3', 'imm & 0b11111', 'opcode'],
        'B': ['imm >> 11', 'imm >> 5', 'rs2', 'rs1', 'funct3', '(imm >> 1) & 0b1111', 'imm >> 10 & 0b1', 'opcode']
    }

    opcode_dict = {
        "R": 0b0110011,
        "I": 0b0010011,
        "S": 0b0100011,
        "B": 0b1100011
    }

    instruction_formats = {
        "add": "R",
        "sub": "R",
        "and": "R",
        "or": "R",
        "addi": "I",
        "andi": "I",
        "lw": "I",
        "lb": "I",
        "sw": "S",
        "sb": "S",
        "beq": "B",
        "bne": "B"
    }

    funct3_dict = {
        "add": 0b000,
        "sub": 0b000,
        "and": 0b111,
        "or": 0b110,
        "addi": 0b000,
        "andi": 0b111,
        "lw": 0b010,
        "lb": 0b000,
        "sw": 0b010,
        "sb": 0b000,
        "beq": 0b000,
        "bne": 0b001
    }

    funct7_dict = {
        "add": 0b0000000,
        "sub": 0b0100000,
        "and": 0b0000000,
        "or": 0b0000000
    }

    split_instruction = instruction.split()
    
    mnemonic = split_instruction[0]

    if mnemonic not in SOPORTADAS:
        raise ValueError(f"Instrucción no soportada: {mnemonic}")

    instruction_format = instruction_formats[mnemonic]
    opcode = opcode_dict[instruction_format]

    return opcode


def explain_instruction(instruction: str, word: int):
    """
    Debe retornar un texto (para imprimirse en pantalla) que muestre, de
    forma visual, los 32 bits de 'word' divididos en los campos del
    formato correspondiente (R, I, S o B) — indicando el rango de bits y
    el valor de cada campo — junto con una breve explicación de cada uno.
    El formato visual (colores, tabla, arte ASCII, etc.) queda a su
    criterio, siempre que sea claro.
    """

    segment_lengths = {
        'rs1': 5,
        'rs2': 5,
        'rd': 5,
        'funct3': 3,
        'funct7': 7,
        'imm': 12,
        'opcode': 7
    }
    instruction_order = {
        'R': ['funct7', 'rs2', 'rs1', 'funct3', 'rd', 'opcode'],
        'I': ['imm', 'rs1', 'funct3', 'rd', 'opcode'],
        'S': ['imm >> 5', 'rs2', 'rs1', 'funct3', 'imm & 0b11111', 'opcode'],
        'B': ['imm >> 11', 'imm >> 5', 'rs2', 'rs1', 'funct3', '(imm >> 1) & 0b1111', 'imm >> 10 & 0b1', 'opcode']
    }

    opcode_dict = {
        "R": 0b0110011,
        "I": 0b0010011,
        "S": 0b0100011,
        "B": 0b1100011
    }

    instruction_formats = {
        "add": "R",
        "sub": "R",
        "and": "R",
        "or": "R",
        "addi": "I",
        "andi": "I",
        "lw": "I",
        "lb": "I",
        "sw": "S",
        "sb": "S",
        "beq": "B",
        "bne": "B"
    }

    funct3_dict = {
        "add": 0b000,
        "sub": 0b000,
        "and": 0b111,
        "or": 0b110,
        "addi": 0b000,
        "andi": 0b111,
        "lw": 0b010,
        "lb": 0b000,
        "sw": 0b010,
        "sb": 0b000,
        "beq": 0b000,
        "bne": 0b001
    }

    funct7_dict = {
        "add": 0b0000000,
        "sub": 0b0100000,
        "and": 0b0000000,
        "or": 0b0000000
    }

    split_instruction = instruction.split()
        
    mnemonic = split_instruction[0]

    format_type = instruction_formats[mnemonic]
    print(f"Formato: {format_type}-Type")

    for field in instruction_order[format_type]:
        print(format(0, '0' + str(segment_lengths[field]) + 'b'), end=' ')


def main():
    if len(sys.argv) != 2:
        print(f'Uso: {sys.argv[0]} "<instruccion>"', file=sys.stderr)
        print(f'Ejemplo: {sys.argv[0]} "add x5, x6, x7"', file=sys.stderr)
        sys.exit(2)

    instruction = sys.argv[1]
    word = encode_instruction(instruction)
    print(format(word, '032b'))

    explain_instruction(instruction, word)

    # No modificar el formato de la siguiente línea: la especificación la
    # requiere, literal, para permitir la validación automática.
    #print(f"HEX: 0x{word:08x}")


if __name__ == "__main__":
    main()
