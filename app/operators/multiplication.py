from controllers.controllers import Controllers

class Multiplication():

    def multiply_hex(self, first_hex_value, second_hex_value):
        first_hex_value = first_hex_value.upper()
        second_hex_value = second_hex_value.upper()

        # gerando lista de zeros com a soma dos tamanhos dos valores
        result = [0] * (len(first_hex_value) + len(second_hex_value))

        # iterando cada valor do primeiro, de traz para a frente.
        for index_first, char_1 in enumerate(reversed(first_hex_value)):
            # sobre cada valor do segundo, tambem de traz para frente
            for index_second, char_2 in enumerate(reversed(second_hex_value)):

                # convertendo cada valor para seu inteiro
                int_char_1 = Controllers.hex_to_int(char_1)
                int_char_2 = Controllers.hex_to_int(char_2)

                # multiplicacao simples de cada valor
                multiply_product = int_char_1 * int_char_2

                # definindo a posicao em que o valor vai ser armazenado
                position = index_first + index_second

                # adicionando o produto em sua respectiva posicao
                result[position] += multiply_product

                # passando o resultado da divisao inteira do valor para o proximo 
                result[position + 1] += result[position] // 16
            
                # atualizando o resultado da multiplicacao inicial para o resto de sua divisao  
                result[position] %= 16
            
        # convertendo os valores de inteiros para hexadecimais, e removendo os zeros iniciais
        result = "".join(Controllers.int_to_hex(char) for char in reversed(result)).lstrip("0")
        
        # retornando o resultado
        print(result)
        return result

    
Multiplication = Multiplication()