class DNASequence:
    def __init__(self, sequence):
        # Convert Fasta file to single string
        header, sequence = self.parse_fasta(sequence)
        
        # DNA Sequence validation
        # 1. Check String type
        if not isinstance(sequence, str):
            raise TypeError("Input value is not a string.")
        
        # 2. Check valid base
        input_seq = sequence.upper().strip()
        valid_bases = set("ATGCN")
        invalid_bases = set(input_seq) - valid_bases

        if len(invalid_bases) > 0:
            raise ValueError(f"Invalid DNA base found. {', '.join(invalid_bases)}.")

        self.header = header
        self.sequence = input_seq

    def parse_fasta(self, sequence):
        lines = sequence.strip().splitlines()

        if not lines:
            raise ValueError("Input is empty.")

        if lines[0].startswith(">"):
            header = lines[0].lstrip(">").strip()
            sequence = "".join(line.strip() for line in lines[1:])
        else:
            header = "unnamed"
            sequence = "".join(line.strip() for line in lines)

        return header, sequence
    
    def length(self):
        seq = self.sequence
        return len(seq)
    
    def gc_content(self):
        seq = self.sequence
        gc_count = seq.count("G") + seq.count("C")
        gc_percent = round((gc_count/len(seq) * 100), 2)

        return gc_percent
    
    def reverse(self):
        seq = self.sequence
        return seq[::-1]
    
    def complement(self):
        seq = self.sequence
        
        com_seq = "" 

        for nt in seq:
            if nt == "A":
                com_seq += "T"
            elif nt == "T":
                com_seq += "A"
            elif nt == "G":
                com_seq += "C"
            elif nt == "C":
                com_seq += "G"
            else:
                com_seq += nt
        
        return com_seq
    
    def reverse_complement(self):
        com_seq = self.complement()
        return com_seq[::-1]