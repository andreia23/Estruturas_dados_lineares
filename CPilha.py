from CPaciente import Paciente

###Classe Pilha###
class Pilha:
  def __init__(self,top = None):
    self._top = top

#Getters e Setters
  def get_top(self):
    return self._top

#Métodos Basicos
  def push_pilha(self, nome, cpf, horario):
    p = Paciente(nome, cpf, horario)
    if self._top == None:
      self._top = p
    else:
      p.set_prox(self._top)
      self._top = p

  def pop_pilha(self):
    if self._top == None:
      return 'A pilha já está vazia'
    else:
      self._top = self._top.get_prox()
      return 'Remoção feita com sucesso'

  def isempty_pilha(self):
    if self._top == None:
      return True
    else:
      return False

  def size_pilha(self):
    if self._top == None:
      return 'A estrutura não possui nemhum elemento'
    else:
      tam = 0
      p = self._top
      while p != None:
        tam += 1
        p = p.get_prox()
      return tam

  def top_pilha(self):
    if self._top == None:
      return 'O valor do elemento é',None
    else:
      return 'Paciente 1: Nome: {}\tCPF: {}\tHorario: {}'.format(self._top.get_nome(), self._top.get_cpf(), self._top.get_horario())

#Print#
  def __str__(self):
    p = self._top
    v = ''
    while p != None:
      v += '[Nome:' + p.get_nome() + '\tCPF:' + p.get_cpf() + '\tHorário Marcado:' + p.get_horario() + ']' + '\n'
      p = p.get_prox()
    return 'Pilha:\n{}'.format(v)       
