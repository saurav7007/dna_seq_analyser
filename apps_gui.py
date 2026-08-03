import tkinter as tk
import dna_seq_analyser as da

class AppGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("DNA Sequence Analyser")
        self.geometry("600x400")

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
            text="Paste your DNA Sequence"
        )
        self.label.pack(pady=10)

        self.entry = tk.Entry(
            self.input_frame,
            width=40
        )
        self.entry.pack(pady=10)

        self.button = tk.Button(
            self.input_frame,
            text="Submit",
            command=self.submit_sequence
        )
        self.button.pack(pady=10)

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


        self.analysis_result = tk.Label(
            self.analysis_frame,
            text=""
        )
        self.analysis_result.grid(
            row=5,
            column=0,
            columnspan=2,
            pady=10
        )

    def show_input_frame(self):

        self.analysis_frame.pack_forget()
        self.input_frame.pack(fill="both", expand=True)

    def show_analysis_frame(self):

        self.input_frame.pack_forget()
        self.analysis_result.config(text="")

        self.analysis_frame.pack(fill="both", expand=True)

    def submit_sequence(self):

        input_seq = self.entry.get()
        
        try:
            self.sequence = da.DNASequence(input_seq)

            self.result.config(
                text=""
            )

            self.sequence_label.config(
                text=f"The Submitted DNA Sequence: {self.sequence.sequence}",
                fg="green"
            )
            self.show_analysis_frame()

        except (TypeError, ValueError) as e:
            self.result.config(
                text=str(e),
                fg="red"
            )

    def show_length(self):

        length = self.sequence.length()

        self.analysis_result.config(
            text=f"Sequence Length: {length}",
            fg="green"
        )

    def show_gc_content(self):

        gc_content = self.sequence.gc_content()

        self.analysis_result.config(
            text=f"GC Content: {gc_content}%",
            fg="green"
    )

    def show_reverse(self):

        reverse = self.sequence.reverse()

        self.analysis_result.config(
            text=f"Reverse Sequence: {reverse}",
            fg="green"
    )

    def show_complement(self):

        complement = self.sequence.complement()

        self.analysis_result.config(
            text=f"Complement Sequence: {complement}",
            fg="green"
    )

    def show_reverse_complement(self):

        reverse_complement = self.sequence.reverse_complement()

        self.analysis_result.config(
            text=f"Reverse Complement: {reverse_complement}",
            fg="green"
    )   

if __name__ == "__main__":
    app = AppGUI()
    app.mainloop()
    