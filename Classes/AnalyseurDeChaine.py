class AnalyseurDeChaine:

    def est_palindrome(self, chaine):
        return chaine == chaine[::-1]

    def analyser_chaine(self, chaine):
        if self.est_palindrome(chaine):
            return f"{chaine[::-1]}, Bien dit !"
        else:
            return f"{chaine[::-1]}"
