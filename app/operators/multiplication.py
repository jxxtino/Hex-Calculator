class Multiplication():

    def hex_to_int(self, hex_value):
        # verifica primeiro o intervalo qual o caractere pertence 
        if "0" <= hex_value <= "9":
            # ord( ) retorna o UNICODE INT de um caractere | ord("0") é a referência
            return ord(hex_value) - ord("0")
        elif "A" <= hex_value <= "F":
            return ord(hex_value) - ord("A") + 10

    def int_to_hex(self, int_value):
        # verificando o intervalo pertencente
        if 0 <= int_value <= 9:
            # chr( ) transforma o UNICODE INT em um UNICODE CHAR | ord("0") é a referência
            return chr(ord("0") + int_value)
        elif 10 <= int_value <= 15:
            return chr(ord("A") + int_value - 10)

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
                int_char_1 = self.hex_to_int(char_1)
                int_char_2 = self.hex_to_int(char_2)

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
        result = "".join(self.int_to_hex(x) for x in reversed(result)).lstrip("0")
        
        # retornando o resultado
        return result

    
Multiplication = Multiplication()