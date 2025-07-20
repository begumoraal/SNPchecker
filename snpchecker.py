import csv

def load_dna_file(filename):
    snp_data = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row or row[0].startswith('#'):
                continue
            snp_id, chrom, pos, genotype = row
            snp_data[snp_id.strip()] = genotype.strip()
    return snp_data

def check_snps(snp_data, snp_list_string):
    snp_list = [s.strip() for s in snp_list_string.strip().split()]
    print("Results:\n")
    for snp in snp_list:
        genotype = snp_data.get(snp)
        if genotype:
            print(f"{snp}: {genotype}")
        else:
            print(f"{snp}: Not found in your data")

if __name__ == "__main__":
    filename = "C:/Users/begum/Desktop/MyHeritage_raw_dna_data.csv"  # ← change this to your filepath
    dna_data = load_dna_file(filename)

    print("\nPaste your SNPs (space or newline separated), then press Enter + Ctrl+D (Linux/Mac) or Ctrl+Z (Windows) to submit: ")
    try:
        snp_input = ''
        while True:
            snp_input += input() + '\n'
    except EOFError:
        pass

    check_snps(dna_data, snp_input)