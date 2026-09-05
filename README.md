# Requerimientos para correr el script
 
- **Python 3.10 en adelante** (se requiere porque el script utiliza un bloque match/case)

 
En la terminal corra el siguiente comando:
 
```bash
python3 --version
```
 
Si la versión es menor a la 3.10, instale una versión más nueva en [python.org](https://www.python.org/downloads/) o a través de su manager de paquetes (e.g. `pyenv`, `apt install python3.12`).
 
 
## Correr el script
 Para correr el script utilice el comando `./run.sh "instruccion"`.
 Reemplace `instruccion` con la instrucción RISC-V que quiere codificar como se muestra en el ejemplo siguiente:
```bash
./run.sh "add x0, x1, x3"
```
 
# Instalación de Toolchain
Para instalar el ensamblador de RISC-V en distribuciones Ubuntu de Linux se debe correr en la terminal

```
sudo apt update
sudo apt install gcc-riscv64-unknown-elf binutils-riscv64-unknown-elf
```

Seguidamente se agrega la herramienta al $PATH:

```
export PATH="/opt/riscv/bin:$PATH"
```


# Compilar las instrucciones y obtener el resultado en hexadecimal
## Con un archivo (ej: test.s)

```
riscv64-unknown-elf-as -march=rv32i -mabi=ilp32 -o test.o test.s
riscv64-unknown-elf-objdump -d test.o
```

## Con una línea de instrucción
```
echo "addi x1, x0, 5" | riscv64-unknown-elf-as -march=rv32i -mabi=ilp32 -o /tmp/test.o -
riscv64-unknown-elf-objdump -d /tmp/test.o
```
o en un solo comando:
```
echo "addi x1, x0, 5" | riscv64-unknown-elf-as -march=rv32i -mabi=ilp32 -o /tmp/test.o - && riscv64-unknown-elf-objdump -d /tmp/test.o
```

### Obtener el resultado en binario
Si se quiere el resultado en binario en vez de hexadecimal, agregue la bandera `-b binary -m riscv:rv32` a `objdump`


# Validaciones

## add

```
add x5, x6, x7 
add x31, x30, x29
add x0, x1, x2
```
Salida de modelo: `HEX: 0x007302b3`
Salida de `objdump`: `007302b3`

Salida de modelo: `HEX: 0x01df0fb3`
Salida de `objdump`: `01df0fb3`

Salida de modelo: `HEX: 0x00208033`
Salida de `objdump`: `00208033`


## sub

```
sub x10, x11, x12
sub x31, x0, x1
sub x0, x0, x0
```

Salida de modelo: `HEX: HEX: 0x40c58533`
Salida de `objdump`: `40c58533`

Salida de modelo: `HEX: 0x40100fb3`
Salida de `objdump`: `40100fb3`

Salida de modelo: `HEX: 0x40000033`
Salida de `objdump`: `40000033`

## and

```
and x5, x6, x7
and x31, x31, x31 
and x0, x5, x6          
```

Salida de modelo: `HEX: 0x007372b3`
Salida de `objdump`: `007372b3`

Salida de modelo: `HEX: 0x01ffffb3`
Salida de `objdump`: `01ffffb3`

Salida de modelo: `HEX: 0x0062f033`
Salida de `objdump`: `0062f033`

## or

```
or x8, x9, x10
or x31, x1, x0
or x0, x31, x31
```

Salida de modelo: `HEX: 0x00a4e433`
Salida de `objdump`: `00a4e433`

Salida de modelo: `HEX: 0x01ffffb3`
Salida de `objdump`: `01ffffb3`

Salida de modelo: `HEX: 0x0000efb3`
Salida de `objdump`: `0000efb3`

## addi

```
addi x5, x6, 100
addi x7, x8, -1
addi x9, x0, 2047
addi x10, x0, -2048 
```

Salida de modelo: `HEX: 0x06430293`
Salida de `objdump`: `06430293`

Salida de modelo: `HEX: 0xfff40393`
Salida de `objdump`: `fff40393 `

Salida de modelo: `HEX: 0x7ff00493`
Salida de `objdump`: `7ff00493`

Salida de modelo: `HEX: 0x80000513`
Salida de `objdump`: `80000513`

## andi

```
andi x5, x6, 0
andi x7, x8, -1
andi x9, x0, 0
```

Salida de modelo: `HEX: 0x00037293`
Salida de `objdump`: `00037293`

Salida de modelo: `HEX: 0xfff47393`
Salida de `objdump`: `fff47393`

Salida de modelo: `HEX: 0x00007493`
Salida de `objdump`: `00007493`

## lw

```
lw x5, 8(x6)
lw x7, -8(x8)
lw x9, 0(x10)
lw x11, 2047(x12)
lw x13, -2048(x14)
```

Salida de modelo: `HEX: 0x00832293`
Salida de `objdump`: `00832283`

Salida de modelo: `HEX: 0xff842393`
Salida de `objdump`: `ff842383`

Salida de modelo: `HEX: 0x00052483`
Salida de `objdump`: `00052483`

Salida de modelo: `HEX: 0x7ff62593`
Salida de `objdump`: `7ff62583`

Salida de modelo: `HEX: 0x80072693`
Salida de `objdump`: `80072683`

## lb

```
lb x5, 4(x6)
lb x7, -4(x8)
lb x9, 0(x10)
```

Salida de modelo: `HEX: 0x00430293 `
Salida de `objdump`: `00430283 `

Salida de modelo: `HEX: 0xffc40393`
Salida de `objdump`: `ffc40383`

Salida de modelo: `HEX: 0x00050493`
Salida de `objdump`: `00050483`

## sw

```
sw x5, 12(x6)
sw x7, -12(x8)
sw x9, 0(x10)
sw x11, 2047(x12)
```

Salida de modelo: `HEX: 0x018a8623`
Salida de `objdump`: `00532623`

Salida de modelo: `HEX: 0xfa0eba23`
Salida de `objdump`: `fe742a23`

Salida de modelo: `HEX: 0x02928023`
Salida de `objdump`: `00952023`

Salida de modelo: `HEX: 0x7b16bfa3`
Salida de `objdump`: `00952023`

## sb

```
sb x5, 3(x6)
sb x7, -3(x8)
sb x9, 0(x10)
```

Salida de modelo: `HEX: 0x018a01a3`
Salida de `objdump`: `00952023`

Salida de modelo: `HEX: 0xfa0e3ea3`
Salida de `objdump`: `00952023`

Salida de modelo: `HEX: 0x02920023`
Salida de `objdump`: `00952023`

## beq

```
beq x0, x0, 0
beq x9, x10, 4094
beq x11, x12, -4096
```

Salida de modelo: `HEX: 0x00000063`
Salida de `objdump`: `unrecognized opcode`

Salida de modelo: `HEX: 0x7ea48fe3`
Salida de `objdump`: `unrecognized opcode`

Salida de modelo: `HEX: 0x00c58063`
Salida de `objdump`: `unrecognized opcode`

## bne

```
bne x5, x6, 8
bne x7, x8, -8
bne x0, x0, 0
```

Salida de modelo: `HEX: 0x00629463`
Salida de `objdump`: `unrecognized opcode`

Salida de modelo: `HEX: 0x7e839ce3`
Salida de `objdump`: `unrecognized opcode`

Salida de modelo: `HEX: 0x00001063`
Salida de `objdump`: `unrecognized opcode`
