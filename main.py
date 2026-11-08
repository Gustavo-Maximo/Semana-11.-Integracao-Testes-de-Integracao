from aluno import AlunoClass
from turma import TurmaClass

# Criando alunos
aluno1 = AlunoClass('Fabio', 'Teixeira', 10)
aluno2 = AlunoClass('Gustavo', 'Silva', 8)

# Criando turma
turma = TurmaClass()

# Cadastrando alunos na turma
turma.cadastrarAlunos([aluno1, aluno2])

# Exibindo alunos
for aluno in turma.alunos:
    print(aluno.mostrarAluno())
