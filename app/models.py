class Aluno:
    def __init__(self, nome, idade, github, linkedin, mini_bio, foto, serie, CPF, cidade, UF):
        self.nome = nome
        self.idade = idade
        self.github = github
        self.linkedin = linkedin
        self.mini_bio = mini_bio
        self.foto = foto
        self.serie = serie
        self.CPF = CPF
        self.cidade = cidade
        self.UF = UF

class Professor:
    def __init__(self, nome, github, linkedin, bio, foto, idade, email, telefone):
        self.nome = nome
        self.github = github
        self.linkedin = linkedin
        self.bio = bio
        self.foto = foto
        self.idade = idade
        self.email = email
        self.telefone = telefone
