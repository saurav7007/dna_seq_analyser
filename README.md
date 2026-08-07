# DNA Seq Analyser

DNA Seq Analyser is a simple application for basic DNA sequence analysis. It accepts a DNA sequence as input and provides the following analyses:

- Sequence length
- GC content
- Reverse sequence
- Complement sequence
- Reverse-complement sequence

## Installation

Download the binary for your operating system and run the application. [Latest Build](https://github.com/saurav7007/dna_seq_analyser/releases/latest)

### Linux

The application can be run directly after extraction. If you would like it to appear in your application menu with an icon, run the following commands:

```bash
unzip DNASeq-Analyser-linux.zip

mkdir -p ~/.dna-seq-analyser
mv DNASeq-Analyser-linux/* ~/.dna-seq-analyser/

ln -s ~/.dna-seq-analyser/dna-seq-analyser.desktop \
      ~/.local/share/applications/dna-seq-analyser.desktop
```
