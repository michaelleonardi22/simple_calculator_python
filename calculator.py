def perkalian(angka1, angka2):
  return angka1 * angka2

def pembagian(angka1, angka2):
  return angka1 / angka2

def penjumlahan(a,b):
  return a + b
def pengurangan(a,b):
  return a - b
def main():
  first_insert = input("masukkan angka pertama: ")
  second_insert = input("masukkan angka kedua: ")
  print(first_insert)
  print(second_insert)
  
  hasil =  perkalian(int(first_insert), int(second_insert))
  print(f'Hasil Perkalian dari {first_insert} dan {second_insert} = {hasil}')

  hasil =  pembagian(int(first_insert), int(second_insert))
  print(f'Hasil Pembagian dari {first_insert} dan {second_insert} = {hasil:.2f}')

  print("penjumlahan = " + str(first_insert) + " + " + str(second_insert) + " = " + str(penjumlahan(int(first_insert),int(second_insert))))
  print("pengurangan = " + str(first_insert) + " - " + str(second_insert) + " = " + str(pengurangan(int(first_insert),int(second_insert))))
if __name__ == "__main__":
  main()
