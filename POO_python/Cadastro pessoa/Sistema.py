
from datetime import date, datetime
from Pessoa import Endereco, PessoaFisica, PessoaJuridica


def main():
    lista_pf = []
    lista_pj = []
    while True:
        opcao = int(input("Escolha uma opção: 1 - Pessoa física / 2 - Pessoa juridica / 0 - Sair"))

        if opcao == 1:
            while True:
                opcao_pf = int(input("Escolha uma opção: 1 - Cadastrar pessoa física / 2 - Listar pessoa física / 3 - Remover pessoa / 4 - Atualizar pessoa fisica / 0 - Voltar ao menu anterior: "))

                if opcao_pf == 1:
                    novaPessoa = PessoaFisica()
                    novoEndereco = Endereco()
                    
                    novaPessoa.nome = input("Digite o nome da pessoa física: ")
                    novaPessoa.cpf = input("Digite o cpf: ")
                    novaPessoa.rendimento = float(input("Digite o rendimento (somente numeros): "))

                    data_nascimento = input("Digite a date de nascimento (dd/mm/aaaa): ")
                    novaPessoa.dataNascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
                    idade = (date.today() - novaPessoa.dataNascimento).days // 365

                    if idade >= 18:
                        print("A pessoa tem mais de 18 anos")
                    else:
                        print("A pessoa tem menos de 18 anos. Retorne ao menu...")
                        continue
                    
                    novoEndereco.logradouro = input("Informe o logradouro: ")
                    novoEndereco.numero = input("Informe o numero: ")
                    enderecoComercial = input("Este endereço é comercial: S/N: ")
                    novoEndereco.endereco_Comercial = enderecoComercial.strip().upper() == 'S'
                    
                    novaPessoa.endereco = novoEndereco

                    lista_pf.append(novaPessoa)

                    print("Cadastro realizado com sucesso!!")
                elif opcao_pf == 2:
                    if lista_pf:
                        for pessoa in lista_pf:
                            print(pessoa.nome)
                            print(pessoa.cpf)
                            print(f"Endereço: {pessoa.endereco.logradouro}, {pessoa.endereco.numero}")
                            print(f"Imposto a ser pago: {pessoa.calcular_imposto(pessoa.rendimento)}")
                            print("Digite 0 para sair: ")
                            input()
                    else:
                        print("Lista Vazia")
                elif opcao_pf == 3:
                    cpf_buscado = input("Digite o cpf da pessoa a ser removida")
                    busca = False
                    for i in range(len(lista_pf)):
                        busca = lista_pf[i].cpf == cpf_buscado
                        if busca:
                            lista_pf.pop(i)
                            print(f"Pessoa com o cpf {cpf_buscado} removida")
                    if busca == False:
                        print("pessoa não encontrada")
                elif opcao == 0: 
                    print("Voltando ao menu interior")
                    break
                else: 
                    print("Opção inválida, por favor digite uma das opções inidicadas: ")
        elif opcao == 2: 
            while True:
                opcao_pj = int(input("Escolha uma opção: 1 - Cadastrar pessoa juridica / 2 - Listar pessoa juridica / 3 - Remover pessoa juridica / 4 - Atualizar pessoa juridica / 0 - Voltar ao menu anterior: "))

                if opcao_pj == 1:
                    nome = input("Informe o nome da empresa: ")
                    cnpj = input("Informe o cnpj da empresa: ")
                    rendimento = input("Informe o rendimento da empresa: ")
                    logradouro = input("Informe o logradouro: ")
                    numero = input("Informe o numero do logradouro: ")
                    comercial =input("O endereço é comercial? S/N: ").upper()

                    enderecoPj = Endereco()
                    novoPj = PessoaJuridica()
                    enderecoPj.numero = numero
                    enderecoPj.logradouro = logradouro
                    enderecoPj.endereco_Comercial = comercial
                    novoPj.endereco = enderecoPj
                    novoPj.nome = nome
                    novoPj.cnpj = cnpj
                    novoPj.rendimento = rendimento

                    lista_pj.append(novoPj)
                    print("Pessoa juridica cadastrada com sucesso")

                elif opcao_pj == 2:
                    if len(lista_pj) > 0:
                        for p in lista_pj:
                            print()
                            print(f"Nome: {p.nome}")
                            print(f"Cnpj: {p.cnpj}")
                            print(f"Rendimento: {rendimento}")
                            print(f"Endereco: {logradouro}, {numero}")
                            print(f"Endereco comercial?: {comercial} ")
                            print()
                    else:
                        print("A lista está vazia")
                elif opcao_pj == 3:
                    cnpj_buscado = input("Informe o cnpj que deseja excluir: ")
                    encontrado = False
                    for p in lista_pj:
                        if p.cnpj == cnpj_buscado:
                            lista_pj.remove(p)
                            encontrado = True
                            print("Empresa excluída com sucesso")
                    if encontrado == False: 
                        print("Empresa não encontrada")
                elif opcao_pj == 4:
                    cnpj_atualizado = input("Informe o Cnpj para atualizar a pessoa juridica: ")
                    if len(lista_pj):
                        pjAtualizada = False
                        for pessoaAtual in lista_pj:
                            if pessoaAtual.cnpj == cnpj_atualizado:
                                pessoaAtual.rendimento = input("Informe o novo rendimento da empresa: ")
                                pessoaAtual.logradouro = input("Informe o novo logradouro da empresa: ")
                                pessoaAtual.numero = input("Informe o novo numero do endereco da empresa: ")

                                pjAtualizada = True
                                print("Pessoa juridica atualizad com sucesso")
                            if pjAtualizada == False:
                                print("Se fudeu")
                else:
                    break
        elif opcao == 0:
            print("Obrigado por utilizar o nome sistema! Valeu!")
            break
        else: 
            print("Opção inválida, por favor digite uma das opções válidas!")

if __name__ == "__main__":
    main()
                            


                    