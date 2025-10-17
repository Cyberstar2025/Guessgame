def main():
    data_mahasiswa = []

    while True:
        print("\n=== Input Nilai Mahasiswa ===")
        name = input("Nama: ")
        try:
            tugas = float(input("Nilai Tugas: "))
            uts = float(input("Nilai UTS: "))
            uas = float(input("Nilai UAS: "))
        except ValueError:
            print("❌ Input nilai harus angka. Coba lagi!")
            continue

        akhir = 0.3 * tugas + 0.3 * uts + 0.4 * uas

        if akhir >= 85:
            grade = 'A'
        elif akhir >= 70:
            grade = 'B'
        elif akhir >= 55:
            grade = 'C'
        elif akhir >= 40:
            grade = 'D'
        else:
            grade = 'E'

        keterangan = "LULUS" if akhir >= 55 else "TIDAK LULUS"

        data_mahasiswa.append([name, tugas, uts, uas, akhir, grade, keterangan])

        lagi = input("Tambah data lagi? (y/n): ").lower()
        if lagi != 'y':
            break

    print("\n=== Daftar Nilai Mahasiswa ===")
    print(f"{'Nama':<15}{'Tugas':<10}{'UTS':<10}{'UAS':<10}{'Akhir':<10}{'Grade':<8}{'Keterangan'}")
    print("-" * 70)
    for d in data_mahasiswa:
        print(f"{d[0]:<15}{d[1]:<10.2f}{d[2]:<10.2f}{d[3]:<10.2f}{d[4]:<10.2f}{d[5]:<8}{d[6]}")
    print("-" * 70)

    # Hitung rata-rata nilai akhir
    rata2 = sum(d[4] for d in data_mahasiswa) / len(data_mahasiswa)
    print(f"Rata-rata nilai akhir kelas: {rata2:.2f}")

if __name__ == "__main__":
    main()
