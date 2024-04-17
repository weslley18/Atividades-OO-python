from Aluno import Aluno
from Disciplina import Disciplina
from Curso import Curso
from Endereco import Endereco
from Sala import Sala
from Professor import Professor


print('aluno')
aluno1 = Aluno()
aluno1.cadastrar_aluno()
print(aluno1)
print('aluno')
aaa = Disciplina()
aaa.adicionar_disciplina()
print(aaa)
print('aluno')
sala1 = Sala()
sala1.cadastrar_sala()
print(sala1)
print('aluno')
curso = Curso()
curso.cadastrar_curso()
print(curso)
curso.cadastra_disciplina()
print(curso)

print('professor')
prof = Professor()
prof.cadastrar_professor()
print(prof)