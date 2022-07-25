def criar_emails_acadêmicos(alunos):
    emails_acadêmicos = []
    for nomes in alunos:
        nome = nomes
        nomes = nomes.lower()
        nomes = nomes.split()
        nomes = '.'.join(nomes)
        nomes = nomes.replace('.da', '')
        nomes = nomes.replace('.de', '')
        nomes = nomes.replace('.das', '')
        nomes = nomes.replace('.dos', '')
        nomes = nomes.replace('.do', '')
        email_acadêmico = nomes
        email_acadêmico = email_acadêmico + '@academico.ufgd.edu.br'
        emails_acadêmicos.append((nome, email_acadêmico))

    return emails_acadêmicos
