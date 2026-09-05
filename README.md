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



## sub

```
sub x10, x11, x12
sub x31, x0, x1
sub x0, x0, x0
```

## and

```
and x5, x6, x7
and x31, x31, x31 
and x0, x5, x6          
```

## or

```
or x8, x9, x10
or x31, x1, x0
or x0, x31, x31
```

## addi

```
addi x5, x6, 100
addi x7, x8, -1
addi x9, x0, 2047
addi x10, x0, -2048 
```

## andi

```
andi x5, x6, 0x0F
andi x7, x8, -1
andi x9, x0, 0x0F
```

## lw

```
lw x5, 8(x6)
lw x7, -8(x8)
lw x9, 0(x10)
lw x11, 2047(x12)
lw x13, -2048(x14)
```

## lb

```
lb x5, 4(x6)
lb x7, -4(x8)
lb x9, 0(x10)
```

## sw

```
sw x5, 12(x6)
sw x7, -12(x8)
sw x9, 0(x10)
sw x11, 2047(x12)
```

## sb

```
sb x5, 3(x6)
sb x7, -3(x8)
sb x9, 0(x10)
```

## beq

```
beq x5, x6, 8
beq x7, x8, -8
beq x0, x0, 0
beq x9, x10, 4094
beq x11, x12, -4096
```

## bne

```
bne x5, x6, 8
bne x7, x8, -8
bne x0, x0, 0
```
