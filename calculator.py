def penjumlahan(a,b):
  return a + b
def main():
  first_insert = input("masukkan angka pertama: ")
  second_insert = input("masukkan angka kedua: ")
  print(first_insert)
  print(second_insert)
  print("penjumlahan = " + str(first_insert) + " + " + str(second_insert) + " = " + str(penjumlahan(int(first_insert),int(second_insert))))
if __name__ == "__main__":
  main()
