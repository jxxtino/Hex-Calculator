
class Multiplication():

    def hex_to_int(self,hex_value):
        if "0" <= hex_value <= "9":
            return (ord(hex_value) - ord("0"))
        elif "A" <= hex_value <= "F":
            return ((ord(hex_value) - ord("A")) + (ord("K") - ord("A")))

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


    
Multiplication = Multiplication()