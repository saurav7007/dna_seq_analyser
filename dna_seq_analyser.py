class DNASequence:
    def __init__(self, sequence):
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

        self.sequence = input_seq
    
    def len(self):
        seq = self.sequence
        return len(seq)
    
    def gc_content(self):
        seq = self.sequence
        return seq.count("G") + seq.count("C")
    
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
            else:
                com_seq += "G"
        
        return com_seq
    
    def reverse_complement(self):
        com_seq = self.complement()
        return com_seq[::-1]