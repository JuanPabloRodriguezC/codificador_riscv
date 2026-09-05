# Descripción de Arquitectura del código
El código utiliza una serie de diccionarios para hacer referencia a los datos relacionados con cada funcion de RISC-V. A medida que incrementaban los atributos para cada segmento de las instrucciones se presenta la evaluación de hacerlo a través de objetos. Sin embargo, el programa es suficientemente conciso y además, es un script mas no existe mucho código reutilizable, por lo que utilizar diccionarios para poder acceder a los valores necesarios se vuelve viable.

La función `encode_instruction` tiene como entrada la instrucción como texto. El texto se descompone según el nemónico que indica qué tipo de instrucción es. Para aquellas instrucciones que tienen inmediatos, usualmente se separan, con exepción del caso de las instrucciones tipo I. Para esto, se utiliza una serie de shifts que agarren el valor de los dígitos necesarios para el segmento y se hace un `and` lógico para borrar cualquier dígito más significativo del que se necesita para ese segmento. 

La función `explain_instruction` tiene como entrada la palabra de la instrucción codificada. De esta manera, se puede convertir directamente a un `string` lo que permite un acceso a través de indices, lo cual es más fácil de manejar que utilizar operaciones lógicas. Como esta función se ocupa únicamente de mostrar en la salida el resultado y no necesita operar sobre la palabra, se considera una solución útil.

# Fuente Consultada
Se utilizó el manual del conjunto de Instrucciones de RISC-V. 

Recuperado de  [Andrew Waterman and Krste Asanovic. The RISC-V Instruction Set Manual, Volume I:
User-Level ISA, Document Version 20191213. RISC-V Foundation, 2019.](https://docs.riscv.org/reference/isa/_attachments/riscv-unprivileged.pdf)

# Ejemplos de salida explicativa

## R
```
./run.sh "sub x10, x11, x12"
Formato: Tipo-R (funct7, rs2, rs1, funct3, rd, opcode)
funct7 (31:25): 0b0100000 = 32 => Campo de función 7 bits (propio del formato R)
rs2 (24:20): 0b01100 = 12 => Registro fuente 2
rs1 (19:15): 0b01011 = 11 => Registro fuente 1
funct3 (14:12): 0b000 = 0 => Campo de función 3 bits (propio de la instrucción)
rd (11:7): 0b01010 = 10 => Registro destino
opcode (6:0): 0b0110011 = 51 => Código de operación según el formato de instrucción

Representación completa de la instrucción: 01000000110001011000010100110011
Binario: 01000000110001011000010100110011
HEX: 0x40c58533
```

## I
```
./run.sh "addi x5, x6, 100" 
Formato: Tipo-I (imm, rs1, funct3, rd, opcode)
imm (31:20): 0b000001100100 = 100 => Inmediato de 12 bits
rs1 (19:15): 0b00110 = 6 => Registro fuente 1
funct3 (14:12): 0b000 = 0 => Campo de función 3 bits (propio de la instrucción)
rd (11:7): 0b00101 = 5 => Registro destino
opcode (6:0): 0b0010011 = 19 => Código de operación según el formato de instrucción
Valor inmediato: 000001100100

Representación completa de la instrucción: 00000110010000110000001010010011
Binario: 00000110010000110000001010010011
HEX: 0x06430293
```
## S
```
./run.sh "sw x5, 12(x6)"   
Formato: Tipo-S (imm[11:7], rs2, rs1, funct3, imm[6:0], opcode)
imm[11:7] (31:27): 0b00000 = 0 => Bits 11 a 7 del inmediato
rs2 (26:22): 0b00110 = 6 => Registro fuente 2
rs1 (21:17): 0b00101 = 5 => Registro fuente 1
funct3 (16:14): 0b010 = 2 => Campo de función 3 bits (propio de la instrucción)
imm[6:0] (13:7): 0b0001100 = 12 => Bits 6 a 0 del inmediato
opcode (6:0): 0b0100011 = 35 => Código de operación según el formato de instrucción
Valor inmediato: 000000001100

Representación completa de la instrucción: 00000001100010101000011000100011
Binario: 00000001100010101000011000100011
HEX: 0x018a8623
```

## B
```
./run.sh "bne x5, x6, 8"
Formato: Tipo-B (imm[12], imm[10:5], rs2, rs1, funct3, imm[4:1], imm[11], opcode)
imm[12] (31:31): 0b0 = 0 => Bit más significativo del inmediato (signo)
imm[10:5] (30:25): 0b000000 = 0 => Bits 10 a 5 del inmediato
rs2 (24:20): 0b00110 = 6 => Registro fuente 2
rs1 (19:15): 0b00101 = 5 => Registro fuente 1
funct3 (14:12): 0b001 = 1 => Campo de función 3 bits (propio de la instrucción)
imm[4:1] (11:8): 0b0100 = 4 => Bits 4 a 1 del inmediato
imm[11] (7:7): 0b0 = 0 => Bit 11 del inmediato
opcode (6:0): 0b1100011 = 99 => Código de operación según el formato de instrucción
Valor inmediato: 0000000001000

Representación completa de la instrucción: 00000000011000101001010001100011
Binario: 00000000011000101001010001100011
HEX: 0x00629463
```
