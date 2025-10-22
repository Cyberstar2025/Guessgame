#incluude <iostream>
using namespace std;

void cetak() {
	string nama;
	int nik;
	int gajipokok = 0, tunjangan = 0, pajak = 0
	
	cout << "Masukkan Nama: " << endl;
	getline(cin, nama);
	
	cout << "Masukkan NIK: " << endl;
	cin >> nik;
	
	cout << "Masukkan Golongan: " << endl;
	cin >> gol;
	
	if(gol == "A") {
		gajipokok = 3500000;
		tunjangan = 1500000;
		pajak = 100000;
	} else if{
		gajipokok = 3500000;
		tunjangan = 1500000;
		pajak = 100000;
	}
	
	cout << "Masukkan Nama: " << endl;
	getline(cin, nama);
	
	
	cout << nama << endl;
	cout << nik << endl;
	cout << gol << endl;
	cout << gajipokok << endl;
	cout << tunjangan << endl;
	cout << pajak << endl;
}

int main() {
	cetak();
	return0;
}