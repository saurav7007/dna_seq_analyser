class DNASequence:
    def __init__(self, sequence):
        self.sequence = sequence
    
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

seq1 = DNASequence("ATGGCATTTA")

print(seq1.len())
print(seq1.gc_content())
print(seq1.reverse())
print(seq1.complement())
print(seq1.reverse_complement())