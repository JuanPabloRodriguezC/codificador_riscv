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
from unittest import case

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'

SOPORTADAS = ["add", "sub", "and", "or", "addi", "andi",
              "lw", "lb", "sw", "sb", "beq", "bne"]

SEGMENT_LENGTHS = {
    'rs1': 5,
    'rs2': 5,
    'rd': 5,
    'funct3': 3,
    'funct7': 7,
    'imm': 12,
    'opcode': 7,
    'imm[12]': 1,
    'imm[11]': 1,
    'imm[11:7]': 5,
    'imm[11:5]': 6,
    'imm[10:5]': 6,
    'imm[6:0]': 7,
    'imm[4:1]': 4,

}

INSTRUCTION_ORDER = {
    'R': ['funct7', 'rs2', 'rs1', 'funct3', 'rd', 'opcode'],
    'I': ['imm', 'rs1', 'funct3', 'rd', 'opcode'],
    'S': ['imm[11:7]', 'rs2', 'rs1', 'funct3', 'imm[6:0]', 'opcode'],
    'B': ['imm[12]', 'imm[10:5]', 'rs2', 'rs1', 'funct3', 'imm[4:1]', 'imm[11]', 'opcode']
}

OPCODE_DICT = {
    "R": 0b0110011,
    "I": 0b0010011,
    "S": 0b0100011,
    "B": 0b1100011
}

INSTRUCTION_FORMATS = {
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

FUNCT3_DICT = {
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

FUNCT7_DICT = {
    "add": 0b0000000,
    "sub": 0b0100000,
    "and": 0b0000000,
    "or": 0b0000000
}


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

    split_instruction = instruction.split()
    mnemonic = split_instruction[0]

    if mnemonic not in SOPORTADAS:
        raise ValueError(f"Instrucción no soportada: {mnemonic}")

    instruction_format = INSTRUCTION_FORMATS[mnemonic]
    opcode = OPCODE_DICT[instruction_format]
    funct3 = FUNCT3_DICT[mnemonic]

    match instruction_format:
        case "R":
            if len(split_instruction) != 4:
                raise ValueError(f"Formato de instrucción desconocido: {instruction_format}")
            rd = int(split_instruction[1].strip('x').strip(','))
            rs1 = int(split_instruction[2].strip('x').strip(','))
            rs2 = int(split_instruction[3].strip('x').strip(','))
            funct7 = FUNCT7_DICT[mnemonic]
            
        case "I":
            if len(split_instruction) == 4:
                rd = int(split_instruction[1].strip('x').strip(','))
                rs1 = int(split_instruction[2].strip('x').strip(','))
                imm = int(split_instruction[3])
            elif len(split_instruction) == 3:
                rd = int(split_instruction[1].strip('x').strip(','))
                logic = split_instruction[2].split('(')
                imm = int(logic[0])
                rs1 = int(logic[1].strip('x').strip(')'))
            else:
                raise ValueError(f"Formato de instrucción desconocido: {instruction_format}")
            
        case "S":
            if len(split_instruction) != 3:
                raise ValueError(f"Formato de instrucción desconocido: {instruction_format}")
            rs1 = int(split_instruction[1].strip('x').strip(','))
            logic = split_instruction[2].split('(')
            imm = int(logic[0])
            rs2 = int(logic[1].strip('x').strip(')'))
        case "B":
            if len(split_instruction) != 4:
                raise ValueError(f"Formato de instrucción desconocido: {instruction_format}")
            rs1 = int(split_instruction[1].strip('x').strip(','))
            rs2 = int(split_instruction[2].strip('x').strip(','))
            imm = int(split_instruction[3])

        case default:
            raise ValueError(f"Formato de instrucción desconocido: {instruction_format}")

    values_dict = {
        'rs1': rs1,
        'rs2': rs2,
        'rd': rd,
        'funct3': funct3,
        'funct7': funct7,
        'imm': imm,
        'imm[12]': (imm >> 12) & 0b1,
        'imm[11]': (imm >> 11) & 0b1,
        'imm[11:7]': (imm >> 7) & 0b11111,
        'imm[11:5]': (imm >> 5) & 0b111111,
        'imm[10:5]': (imm >> 5) & 0b111111,
        'imm[6:0]': imm & 0b1111111,
        'imm[4:1]': (imm >> 1) & 0b1111,
        'opcode': opcode
    }

    order = INSTRUCTION_ORDER[instruction_format]
    result = 0b0
    accumulated_length = 0
    for segment in order[::-1]:
        segment_value = values_dict[segment] << accumulated_length
        result |= segment_value
        accumulated_length += SEGMENT_LENGTHS[segment]
    return result


def explain_instruction(instruction: str, word: int) -> str:
    """
    Debe retornar un texto (para imprimirse en pantalla) que muestre, de
    forma visual, los 32 bits de 'word' divididos en los campos del
    formato correspondiente (R, I, S o B) — indicando el rango de bits y
    el valor de cada campo — junto con una breve explicación de cada uno.
    El formato visual (colores, tabla, arte ASCII, etc.) queda a su
    criterio, siempre que sea claro.
    """
    print(f"Palabra codificada en binario: {word:032b}")

    split_instruction = instruction.split()      
    mnemonic = split_instruction[0]
    format_type = INSTRUCTION_FORMATS[mnemonic]
    print(f"Formato: Tipo-{format_type}")

    result = ""
    for field in INSTRUCTION_ORDER[format_type]:
        result += format(0, '0' + str(SEGMENT_LENGTHS[field]) + 'b') + ' '

    return result


def main():
    if len(sys.argv) != 2:
        print(f'Uso: {sys.argv[0]} "<instruccion>"', file=sys.stderr)
        print(f'Ejemplo: {sys.argv[0]} "add x5, x6, x7"', file=sys.stderr)
        sys.exit(2)

    instruction = sys.argv[1]
    word = encode_instruction(instruction)
    print(explain_instruction(instruction, word))

    # No modificar el formato de la siguiente línea: la especificación la
    # requiere, literal, para permitir la validación automática.
    print(f"HEX: 0x{word:08x}")


if __name__ == "__main__":
    main()
