# Primeira versão do programa, funciona para os endereços mais simples

import re

def adress_organizer(user_adress):
    # Compila a expressão regular para extrair o nome da rua e o número da rua
    
    try:
        adress_pattern = re.compile(r'(?P<street_name>[\w\s]+)\s+(?P<street_number>[\w\d\s]+)')

    # Procura por uma correspondência na string do endereço
        correspondence = adress_pattern.search(user_adress)

        if correspondence:
        # Extrai os grupos nome_rua e numero_rua da correspondência
            street_name = correspondence.group('street_name').strip()
            street_number = correspondence.group('street_number').strip()

        # Retorna os resultados como uma tupla
            return street_name, street_number
        else:
        # Retorna None se não houver correspondência
            return
        
    #Exceção para erros relacionados a biblioteca re    
    except re.error:

        print('Ocorreu um erro na "expressão regular"')

    #Exceção para outros erros, garante que o programa não de erro apesar de ser uma "má prática"
        
    except Exception:

        print('Ocorreu um erro desconhecido')       

# Solicita ao usuário para inserir um endereço


# Chama a função e imprime o resultado
list_of_addresses = ['Miritiba 339',
                'Babaçu 500',
                'Cambuí 804B',
                'Rio Branco 23',
                'Quirino dos Santos 23b',
                '4, Rue de la République',
                '100 Broadway Av',
                'Calle Sagasta, 26',
                'Calle 44 No 1991']

for address in list_of_addresses:
    print(adress_organizer(address))
