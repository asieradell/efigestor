import os
import sys
import time as t
#Comprobar si es usuario root
if os.geteuid() != 0:
    print('Debes tener privilegios root para este script.')
    sys.exit(1)#Sale del programa
banner = os.system("figlet efigestor by asieradell")
print("Comprobando si tienes UEFI o BIOS....................... ")
print("Puede tardar un rato..........")
t.sleep(10.99)
os.path.exists('/sys/firmware/efi/efivars')
if os.path.exists('/sys/firmware/efi/efivars') == True:
    print("Puedes continuar efigestor by asieradell porque tienes UEFI...")
    print("Cargando .......................................")
    t.sleep(8)
else:
    print("No puedes continuar porque tienes BIOS...")
    sys.exit(1)
print("list-efivars/list-mok-variables")
op = input("Escriba una opcion que desea hacer")
if op == "list-efivars":
    os.system("ls /sys/firmware/efi/efivars")
elif op == "list-mok-variables":
    os.system("ls /sys/firmware/efi/mok-variables")