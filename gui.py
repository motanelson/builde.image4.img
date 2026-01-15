import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import os

class RamDiskBuilderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("linux Builder...")
        self.root.geometry("800x600")
        self.root.configure(bg="black")

        # Memória onde os ficheiros são ligados
        self.memory_buffer = b""
        self.loaded_files = []

        # Barra superior com botões
        top = tk.Frame(root, bg="black")
        top.pack(fill="x", pady=5)

        btn_style = {
            "bg": "white",
            "fg": "black",
            "activebackground": "#dddddd",
            "activeforeground": "black",
            "relief": "flat",
            "width": 10
        }

        tk.Button(top, text="OPEN", command=self.open_files, **btn_style).pack(side="left", padx=5)
        tk.Button(top, text="SAVE", command=self.save_file, **btn_style).pack(side="left", padx=5)
        tk.Button(top, text="CLEAR", command=self.clear_memory, **btn_style).pack(side="left", padx=5)

        # Área de texto (preview/debug)
        self.text = ScrolledText(
            root,
            bg="black",
            fg="white",
            insertbackground="white",
            font=("Consolas", 10)
        )
        self.text.pack(fill="both", expand=True, padx=5, pady=5)

        self.log("linux Builder startup.\n")

    def log(self, msg):
        self.text.insert("end", msg)
        self.text.see("end")

    def open_files(self):
        paths = filedialog.askopenfilenames(
            title="open files ",
            filetypes=[("elf files", "*"), ("All files", "*")]
        )
        if 0==0:
                os.system("umount /mnt/rams 2>/dev/null")
                os.system('dd if=/dev/zero of=tmp.img bs=1M count=12 status=progress')
                os.system("chmod 777 tmp.img 2>/dev/null")
                os.system("mkfs.ext2 -b 1024 -I 128 -O none  tmp.img")
                os.system("chmod 777 tmp.img 2>/dev/null")
                os.system("mkdir /mnt/rams 2>/dev/null")
                os.system("umount /mnt/rams 2>/dev/null")
                os.system("sudo mount -o loop tmp.img /mnt/rams")
        if not paths:
            return

        for path in paths:
            #try:
            if 0==0:
                os.system("cp $1 /mnt/rams ".replace("$1",path))
                os.system("chmod 777 /mnt/rams/* 2>/dev/null")
                os.system("chmod 777 /mnt/rams/*.* 2>/dev/null")
                self.log(f"[OK] Carregado: {path} \n")
            #except Exception as e:
            #    self.log(f"[ERRO] {path}: {e}\n")
        os.system("chmod 777 /mnt/rams/* ")
        os.system("umount /mnt/rams > /dev/null")
        

    def save_file(self):
        

        path = filedialog.asksaveasfilename(
            title="save disk",
            defaultextension=".iso",
            filetypes=[("iso", "*.iso"), ("All files", "*")]
        )

        if not path:
            return

        try:
            n=path
            os.system("umount /mnt/rams 2> /dev/null")
            os.system("dd if=/dev/zero of=boot.img bs=1M count=12 status=progress")
            os.system('chmod 777 boot.img 2>/dev/null')
            os.system("mkfs.fat -F 12 boot.img")
            os.system('chmod 777 boot.img 2>/dev/null')
            os.system("syslinux  boot.img")
            os.system("chmod 777 boot.img 2>/dev/null")
            os.system('mcopy -i boot.img syslinux.cfg ::/syslinux.cfg')
            os.system('mcopy -i boot.img initrd.gz ::/initrd.gz')
            os.system('mcopy -i boot.img vmlinuz ::/vmlinuz')
            os.system('chmod 777 boot.img 2>/dev/null')
            os.system('chmod 777 $1 2>/dev/null'.replace("$1",n))
            os.system('rm $1 2>/dev/null'.replace("$1",n))
            os.system('mv tmp.img $1'.replace("$1",n))
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def clear_memory(self):
        self.memory_buffer=""
        self.loaded_files.clear()
        self.text.delete("1.0", "end")
        self.log("memory clear.\n")
        if 0==0:
                os.system("umount /mnt/rams 2>/dev/null")
                



if __name__ == "__main__":
    root = tk.Tk()
    app = RamDiskBuilderGUI(root)
    root.mainloop()
