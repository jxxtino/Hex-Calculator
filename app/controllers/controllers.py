class Controllers:

    def hex_to_int(self, hex_value):
        # verifica primeiro o intervalo qual o caractere pertence 
        if "0" <= hex_value <= "9":
            # ord( ) retorna o UNICODE INT de um caractere | ord("0") é a referência
            return ord(hex_value) - ord("0")
        elif "A" <= hex_value <= "F":
            return ord(hex_value) - ord("A") + 10
        else:
            return None

    def int_to_hex(self, int_value):
        # verificando o intervalo pertencente
        if 0 <= int_value <= 9:
            # chr( ) transforma o UNICODE INT em um UNICODE CHAR | ord("0") é a referência
            return chr(ord("0") + int_value)
        elif 10 <= int_value <= 15:
            return chr(ord("A") + int_value - 10)
        else:
            return None

    def check_hex_values(self, first_hex_value, second_hex_value):
        # verificando se existe valores hexadecimais vazios
        if not(first_hex_value) or not(second_hex_value):
            raise Exception("\nValores Hexadecimais em Branco\n")
        
        # verificando se os valores inseridos estão dentro do padrão hexadecimal
        elif not all(char in "0123456789ABCDEF" for char in (first_hex_value+second_hex_value)):
            raise Exception("\nValores Hexadecimais Inválidos\n")

Controllers = Controllers()