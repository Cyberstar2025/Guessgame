history = []

def calculate():
    try:
        a = int(input("Masukkan angka pertama: "))
        op = input("Masukkan operator (+, -, *, /, %, **): ")
        b = int(input("Masukkan angka kedua: "))
    except ValueError:
        print("Input harus berupa angka!")
        return

    if op == '+':
        r = a + b
    elif op == '-':
        r = a - b
    elif op == '*':
        r = a * b
    elif op == '/':
        if b == 0:
            print("Error: pembagian dengan nol")
            return
        r = a / b
    elif op == '%':
        r = a % b
    elif op == '**':
        r = a ** b
    else:
        print("Operator tidak dikenal")
        return
    hasil_str = f"{a} {op} {b} = {r}"
    print(hasil_str)
    history.append(hasil_str)

def show_history():
    if not history:
        print("Belum ada histori perhitungan.")
    else:
        print("\n=== Histori Perhitungan ===")
        for i, h in enumerate(history, 1):
            print(f"{i}. {h}")

if __name__ == "__main__":
    while True:
        perintah = input("\nKetik 'exit' untuk keluar, 'history' untuk melihat histori, atau Enter untuk lanjut: ")

        if perintah.lower() in ("exit", "quit"):
            break
        elif perintah.lower() == "history":
            show_history()
        else:
            calculate()
