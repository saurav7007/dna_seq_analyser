import tkinter as tk
import dna_seq_analyser as da

class AppGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("DNA Sequence Analyser")
        self.geometry("400x200")

        self.app_widgets()

    def app_widgets(self):
        self.label = tk.Label(self, text="Paste your DNA Sequence")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self, width=40)
        self.entry.pack(pady=10)

        self.button = tk.Button(
            self,
            text="Submit",
            command=self.submit_sequence
        )
        self.button.pack(pady=10)

        self.result = tk.Label(self, text="")
        self.result.pack()

    def submit_sequence(self):
        sequence = self.entry.get()
        
        dna = da.DNASequence(sequence)
        self.result.config(text=dna.complement())

if __name__ == "__main__":
    app = AppGUI()
    app.mainloop()