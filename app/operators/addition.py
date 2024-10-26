class Addition:

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
        
    def sum_hex(self, first_hex_value, second_hex_value):
        first_hex_value = first_hex_value.upper()
        second_hex_value = second_hex_value.upper()
        
        # gerando lista de zeros com a soma dos tamanhos dos valores
        result = [0] * (len(first_hex_value) + len(second_hex_value))

        # iterando cada caractere dos dois valores ao mesmo tempo
        for position in range(len(result)-1):

            # convertendo cada valor para seu inteiro || condicional para evitar que o indice exceda o tamanho do hexadecimal
            int_char_1 = self.hex_to_int(first_hex_value[-1 - position] if position < len(first_hex_value) else "0")
            # [-1 - position] = usado para inverer a ordem dos valores
            int_char_2 = self.hex_to_int(second_hex_value[-1 - position] if position < len(second_hex_value) else "0")

            # soma simples de cada valor
            sum_values = int_char_1 + int_char_2

            # adicionando o produto da soma em sua respectiva posicao
            result[position] += sum_values 

            # passando o resultado da divisao inteira do valor para o valor da proxima posicao 
            result[position + 1] = result[position] // 16

            # atualizando o resultado da soma inicial para o resto de sua divisao
            result[position] %= 16

        # Converte a lista de inteiros em caracteres hexadecimais invertidos e remove zeros iniciais
        result = "".join(self.int_to_hex(x) for x in reversed(result)).lstrip("0")

        # retorna o resultado
        return result


Addition = Addition()