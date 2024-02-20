list_of_addresses = ['Miritiba 339',
                'Babaçu 500',
                'Cambuí 804B',
                'Rio Branco 23',
                'Quirino dos Santos 23b',
                '4, Rue de la République',
                '100 Broadway Av',
                'Calle Sagasta, 26',
                'Calle 44 No 1991']
# Função principal do código
def address_formater(address):

    # Dividi o input por cada palavra
    splited_address = address.split()
    address_dict = {}
    
    # Verifica se existe um 'No' no endereço e o formata da maneira adequada
    if 'No' in splited_address:
         
         indice = splited_address.index('No')
         street_name = ' '.join(splited_address[:indice]).replace(",", "")
         street_number = ' '.join(splited_address[indice:]).replace(",", "")  
         address_dict[street_name] = street_number
    
    # Condição para endereços que começam pelo número
    elif splited_address[0].replace(",", "").isdigit():
        
        street_name = ' '.join(splited_address[1:]).replace(",", "")
        street_number =''.join(splited_address[0]).replace(",", "")
        address_dict[street_name] = street_number
            
    # Condição para endereços de nome composto
    elif len(splited_address) > 2:

        if splited_address[-1][0].isdigit():
            street_name = ' '.join(splited_address[:-1]).replace(",", "")
            street_number =''.join(splited_address[-1:]).replace(",", "")
            address_dict[street_name] = street_number
    
    # Condição dos endereços mais simples
    else:
        address_dict[splited_address[0]] = splited_address[1]
 
    return address_dict

