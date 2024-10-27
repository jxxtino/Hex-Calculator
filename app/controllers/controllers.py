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


Controllers = Controllers()