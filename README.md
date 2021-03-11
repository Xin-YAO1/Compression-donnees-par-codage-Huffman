# Compression-donnees-par-codage-Huffman
Le codage de Huffman, du nom de son concepteur, est une méthode statistique de compression de
données. Son principe est de remplacer un caractère (ou symbole) par une suite de bits de longueur
variable. L'idée sous-jacente est de coder ce qui est fréquent sur peu de bits et au contraire ce qui est
rare sur des séquences de bits plus longues. Il permet une compression sans perte, c’est-à-dire qu’une
suite de bits strictement identique à l’originale est restituée par décompression. Il nécessite cependant
que soit connues (ou estimées) les fréquences d’apparition des différents symboles à coder. Il existe
ainsi plusieurs variantes de l’algorithme de Huffman (statique, semi-adaptatif ou adaptatif)
aujourd’hui utilisées dans des algorithmes de compression de fichiers tels que gzip.
