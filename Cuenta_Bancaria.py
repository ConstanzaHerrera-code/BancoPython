class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return (
            f"\n✨ Cliente: {self.nombre} {self.apellido} ✨\n"
            f"💳 Cuenta N°: {self.numero_cuenta}\n"
            f"💰 Balance actual: ${self.balance:.2f}\n"
        )

    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print(f"✅ ¡Depósito exitoso! Se han añadido ${monto_deposito:.2f} a tu cuenta.")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print(f"🛠️ ¡Retiro completado! Se han retirado ${monto_retiro:.2f}.")
        else:
            print("⚠️ Fondos insuficientes. No puedes retirar más de tu balance actual.")

def crear_clientes():
    print("\n👋 Bienvenido al Banco Python 🐍")
    nombre_cl = input('📝 Por favor, ingresa tu nombre: ')
    apellido_cl = input('📝 Ahora, ingresa tu apellido: ')
    numero_cuenta = input('🏦 Ingresa tu número de cuenta: ')
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta)
    print("\n🎉 ¡Tu cuenta ha sido creada con éxito! 🎉")
    return cliente

def inicio():
    mi_cliente = crear_clientes()
    print(mi_cliente)

    opcion = ''

    while opcion.upper() != 'S':
        print("\n¿Qué te gustaría hacer?")
        print("💵 [D] Depositar")
        print("💸 [R] Retirar")
        print("🚪 [S] Salir")
        opcion = input("👉 Tu elección: ").upper()

        if opcion == 'D':
            monto_dep = float(input("💵 ¿Cuánto deseas depositar?: "))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = float(input("💸 ¿Cuánto deseas retirar?: "))
            mi_cliente.retirar(monto_ret)
        elif opcion != 'S':
            print("❓ Opción no válida. Por favor, intenta de nuevo.")

        print(mi_cliente)

    print("\n🫡 Gracias por confiar en el Banco Python. ¡Que tengas un excelente día! 🎉")

inicio()
