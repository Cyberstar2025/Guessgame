import random

def play(min_v=1, max_v=100):
    secret = random.randint(min_v, max_v)
    attempts = 0
    guesses = []  # fitur 1: riwayat tebakan
    lower_bound = min_v
    upper_bound = max_v

    print(f"Tebak angka antara {min_v} sampai {max_v}!")

    while True:
        try:
            guess = int(input("Masukkan tebakan: "))
        except ValueError:
            print("Input bukan angka, coba lagi.")
            continue

        attempts += 1
        guesses.append(guess)  # simpan ke history

        if guess < secret:
            print("Terlalu kecil.")
            lower_bound = max(lower_bound, guess + 1)
        elif guess > secret:
            print("Terlalu besar.")
            upper_bound = min(upper_bound, guess - 1)
        else:
            print(f"Benar! Kamu menebak dalam {attempts} percobaan.")
            print("\n=== Riwayat Tebakan ===")
            print(", ".join(map(str, guesses)))
            break

        # fitur 2: tampilkan rentang dinamis
        print(f"💡 Sekarang coba di antara {lower_bound} dan {upper_bound}.")

        # fitur 3: auto hint setelah 5 percobaan
        if attempts == 5:
            if secret % 2 == 0:
                print("🔍 Petunjuk: Angkanya genap.")
            else:
                print("🔍 Petunjuk: Angkanya ganjil.")
        elif attempts == 8:
            print(f"🔍 Petunjuk tambahan: Angka rahasia lebih dekat ke {min_v if secret < (min_v + max_v)//2 else max_v}.")

if __name__ == "__main__":
    play()