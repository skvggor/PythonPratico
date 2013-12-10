from tkinter import ttk
from tkinter import N, W, E, S
import tkinter as tk

import base64

import xorcypher

class Janela(ttk.Frame):
  def __init__(self, pai):
    super().__init__(pai, padding = "3 3 12 12")
    self.pack()
    self.senha = tk.StringVar()

    # Label senha
    ttk.Label(
        self,
        text = "Senha: "
    ).grid(
        column = 1,
        row = 2,
        sticky = E
    )

    # Botão cifrar
    self.botao = ttk.Button(
        self,
        text = 'Cifrar',
        command = self.cifrar
    )

    self.botao.grid(
      column = 3,
      row = 2,
      sticky = W
    )

    # Campo senha
    ttk.Entry(
        self,
        width = 50,
        textvariable = self.senha,
        show = '*'
    ).grid(
        column = 2,
        row = 2,
        sticky = (W, E)
    )

    # Campo cifrar
    self.texto = tk.Text(
        self,
        width = 80,
        height = 30
    )
    self.texto.grid(
        column = 1,
        row = 1,
        columnspan = 3,
        sticky = (W, E)
    )

  def cifrar(self):
    if self.botao['text'] == 'Cifrar':
      entrada = bytes(
          self.texto.get('1.0', 'end').rstrip(),
          encoding = 'utf-8'
      )

      senha = bytes(
          self.senha.get(),
          encoding = 'utf-8'
      )

      saida = xorcypher.xor_cypher(senha, entrada)
      self.texto.delete('1.0', 'end')
      self.texto.insert('1.0', base64.b64encode(saida))

app = tk.Tk()
app.title("Ofuscador de textos")
janela = Janela(app)
app.mainloop()