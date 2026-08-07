import tkinter as tk
from tkinter import filedialog
import dna_seq_analyser as da

class AppGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("DNA Sequence Analyser")
        self.geometry("600x420")

        self.sequence = None

        self.create_input_frame()
        self.create_analysis_frame()

    def create_input_frame(self):

        self.input_frame = tk.Frame(self)
        self.input_frame.pack(
            fill="both",
            expand=True
        )

        self.label = tk.Label(
            self.input_frame,
            text="Paste your DNA Sequence",
            font=("Arial", 12, "bold")
        )
        self.label.pack(pady=10)

        self.entry = tk.Text(
            self.input_frame,
            height=15,
            width=60
        )
        self.entry.pack(pady=10)

        self.button = tk.Button(
            self.input_frame,
            text="Submit",
            command=self.submit_sequence
        )
        self.button.pack(pady=5)

        self.upload_button = tk.Button(
            self.input_frame,
            text="Upload FASTA",
            command=self.upload_sequence
        )
        self.upload_button.pack(pady=5)

        self.result = tk.Label(
            self.input_frame,
            text=""
        )
        self.result.pack()

    def create_analysis_frame(self):

        self.analysis_frame = tk.Frame(self)

        for i in range(2):
            self.analysis_frame.columnconfigure(i, weight=1)

        #for i in range(6):
        #   self.analysis_frame.rowconfigure(i, weight=1)

        self.analysis_label = tk.Label(
            self.analysis_frame,
            text="DNA Sequence Analysis"
        )
        self.analysis_label.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=10
        )

        self.sequence_label = tk.Label(
            self.analysis_frame,
            text=""
        )
        self.sequence_label.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=10,
            pady=10
        )

        self.length_button = tk.Button(
            self.analysis_frame,
            text="Length",
            command=self.show_length
        )

        self.gc_button = tk.Button(
            self.analysis_frame,
            text="GC Content",
            command=self.show_gc_content
        )

        self.reverse_button = tk.Button(
            self.analysis_frame,
            text="Reverse",
            command=self.show_reverse
        )

        self.complement_button = tk.Button(
            self.analysis_frame,
            text="Complement",
            command=self.show_complement
        )

        self.reverse_complement_button = tk.Button(
            self.analysis_frame,
            text="Reverse Complement",
            command=self.show_reverse_complement
        )

        self.back_button = tk.Button(
            self.analysis_frame,
            text="Back",
            command=self.show_input_frame
        )

        self.length_button.grid(
            row=2,
            column=0,
            padx=5,
            pady=5
        )

        self.gc_button.grid(
            row=2,
            column=1,
            padx=5,
            pady=5
        )

        self.reverse_button.grid(
            row=3,
            column=0,
            padx=5,
            pady=5
        )

        self.complement_button.grid(
            row=3,
            column=1,
            padx=5,
            pady=5
        )

        self.reverse_complement_button.grid(
            row=4,
            column=0,
            padx=10,
            pady=10
        )

        self.back_button.grid(
            row=4,
            column=1,
            padx=10,
            pady=10
        )


        self.analysis_result = tk.Text(
            self.analysis_frame,
            height=10,
            width=60,
            wrap="word",
            bg="#f0f0f0",
            relief="flat",
            cursor="arrow"
        )
        self.analysis_result.config(state="disabled")
        self.analysis_result.grid(
            row=5,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky="nsew"
        )

    def show_input_frame(self):

        self.analysis_frame.pack_forget()
        self.input_frame.pack(fill="both", expand=True)

    def show_analysis_frame(self):

        self.input_frame.pack_forget()
        self.set_result_text("")

        self.analysis_frame.pack(fill="both", expand=True)

    def process_sequence(self, input_seq):

        try:
            self.sequence = da.DNASequence(input_seq)
            self.header = self.sequence.header

            self.result.config(
                text=""
            )

            self.sequence_label.config(
                text=f"The Submitted DNA Sequence: {self.header}",
                fg="green"
            )
            self.show_analysis_frame()

        except (TypeError, ValueError) as e:
            self.result.config(
                text=str(e),
                fg="red"
            )

    def submit_sequence(self):

        input_seq = self.entry.get("1.0", tk.END)
        self.process_sequence(input_seq)

    def upload_sequence(self):

        filepath = filedialog.askopenfilename(
            filetypes=[("FASTA files", "*.fasta *.fa *.txt"), ("All files", "*.*")]
        )
        if not filepath:
            return  # user cancelled the dialog

        with open(filepath, "r") as f:
            input_seq = f.read()

        self.process_sequence(input_seq)

    def set_result_text(self, text, color="green"):
        self.analysis_result.config(state="normal")
        self.analysis_result.delete("1.0", tk.END)
        self.analysis_result.insert("1.0", text)
        self.analysis_result.tag_add("colored", "1.0", tk.END)
        self.analysis_result.tag_config("colored", foreground=color)
        self.analysis_result.config(state="disabled")

    def show_length(self):

        length = self.sequence.length()

        self.set_result_text(f"Sequence Length: {length}")

    def show_gc_content(self):

        gc_content = self.sequence.gc_content()

        self.set_result_text(f"GC Content: {gc_content}%")

    def show_reverse(self):

        reverse = self.sequence.reverse()

        self.set_result_text(f"Reverse Sequence: {reverse}")

    def show_complement(self):

        complement = self.sequence.complement()

        self.set_result_text(f"Complement Sequence: {complement}")

    def show_reverse_complement(self):

        reverse_complement = self.sequence.reverse_complement()

        self.set_result_text(f"Reverse Complement: {reverse_complement}")
 

if __name__ == "__main__":
    app = AppGUI()
    app.mainloop()
    