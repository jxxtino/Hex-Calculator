from controllers.controllers import Controllers

class Addition:
        
    def sum_hex(self, first_hex_value, second_hex_value):
        first_hex_value = first_hex_value.upper()
        second_hex_value = second_hex_value.upper()
        
        # gerando lista de zeros com a soma dos tamanhos dos valores
        result = [0] * (len(first_hex_value) + len(second_hex_value))

        # iterando cada caractere dos dois valores ao mesmo tempo
        for position in range(len(result)-1):

            # convertendo cada valor para seu inteiro || condicional para evitar que o indice exceda o tamanho do hexadecimal
            int_char_1 = Controllers.hex_to_int(first_hex_value[-1 - position] if position < len(first_hex_value) else "0")
            # [-1 - position] = usado para inverer a ordem dos valores
            int_char_2 = Controllers.hex_to_int(second_hex_value[-1 - position] if position < len(second_hex_value) else "0")

            # soma simples de cada valor
            sum_values = int_char_1 + int_char_2

            # adicionando o produto da soma em sua respectiva posicao
            result[position] += sum_values 

            # passando o resultado da divisao inteira do valor para o valor da proxima posicao 
            result[position + 1] = result[position] // 16

            # atualizando o resultado da soma inicial para o resto de sua divisao
            result[position] %= 16

        # Converte a lista de inteiros em caracteres hexadecimais invertidos e remove zeros iniciais
        result = "".join(Controllers.int_to_hex(char) for char in reversed(result)).lstrip("0")

        # retorna o resultado
        return result


Addition = Addition()