file = input("Enter a file name: ")
handle = open(file)

distribusi_jam = {}

for baris in handle:
    if baris.startswith('From '):
        kata_kata = baris.split()
        waktu = kata_kata[5].split(':')
        jam = waktu[0]
        distribusi_jam[jam] = distribusi_jam.get(jam, 0) + 1

distribusi_jam = sorted(distribusi_jam.items())

for jam,jumlah in distribusi_jam:
    print(jam,jumlah)

