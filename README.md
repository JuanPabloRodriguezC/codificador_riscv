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

