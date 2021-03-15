# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 08:10:25 2021

@author: YaoXin
"""

import six

'Etape 1 : Détermination de l’alphabet et des fréquences de caractères'

def open_text_et_count_carac(txt):
    '''cette fonction est pour retouner une liste de liste carac et son freq'''
    #ouvrir le texte en binaire
    text = open(txt,'rb').read()
    #creer un dic 
    count = {}
    #parcourir tous les carac dans le text
    #if carac pas dans count, le ajouter dans le dic count et count[carac]= 1
    #if carac deja dans count, count[carac]=count[carac]+1
    for carac in text:
        if carac not in count:
            count[carac]=1
        else:
            count[carac]=count[carac]+1
    #mise en ordre count: selon la valeur de count,faire l'ordre croissant
    count_avec_ordre = sorted(count.items(),key=lambda x:x[1])
    return count_avec_ordre
    

    


'Etape 2 : Construction de l’arbre de codage'
'Etape 3 : Codage du texte'
###=============================
#   cree une classe BNode
###=============================
class BNode:
    def __init__(self,label,frequant,l_child=None,r_child=None):
        self.label = label
        self.frequant = frequant
        self.l_child = l_child
        self.r_child = r_child
        
        
    def get_frequant(self):
        '''retouner la frequance du noeud'''
        return self.frequant
    
    def get_label(self):
        '''retourner le label(carac) du noeud'''
        return self.label



###=====================================================
#  creer une classe HuffmanTree de donnee recursive 
###=====================================================             
class HuffmanTree(BNode):
    def __init__(self,label,frequant,l_child,r_child):
        super().__init__(label,frequant,l_child,r_child)
    
    def root(self):
        '''retourner le root de l'arbre huffman'''
        return self
    
    def get_frequant(self):
        '''retouner la frequance de la racine pour l'arbre huffman'''
        return self.root().frequant
    
    def get_l_child(self):
        return self.l_child
    
    def get_r_child(self):
        return self.r_child
   
    def codage(self,dic_code,code):
        '''retouner un dictionnaire qui compose par un carac et son code pour l'arbre huffman donnee '''
        #parcourir l'arbre jusqu'a le noeud est une feuill
        #si ce noeud est une feuill, mettre le code dans le dictionnaire
        #on ajoute '0' si parcour a gauche, ajoute '1' si a droite
        if (self.root().get_l_child() == None) and (self.root().get_l_child()== None):
            dic_code[self.root().get_label()] = code
        else:
            self.get_l_child().codage(dic_code,code + '0')
            self.get_r_child().codage(dic_code,code + '1')
        #dic_code(type dic)
        return dic_code
    
    
###=====================================
#   Fonctions
###=====================================
        
    
def cree_arbres(list_count):
    '''trnsfere la liste de carac et son frequan à une liste de noeud et puis la retourner'''
    list_arbre = []
    #list_count est une liste de liste qui composee le carac et son frequan
    for i in list_count:
        #i[0] est carac(label)
        #i[1] est frequan
        h=HuffmanTree(i[0],i[1],None,None) 
        list_arbre.append(h)
    return list_arbre


def cree_arbre_huffman(list_arbres):
    '''retourner l'arbre huffman'''
        #car on va ajouter nouveau arbre(composee par deux noeud) dans list_arbres
        #donc,si len(list_arbre) >1, il faut mise en ordre chaque fois selon ses frequan
    while len(list_arbres) != 1:
        #si list_arbres est type dic: list_arbre_avec_ordre = sorted(list_arbre,key=lambda x:x.get_frequent())
        
        #ici, list_arbre(type list)
        list_arbres.sort(key=lambda x:x.get_frequant())
        #choisir les deux premier element dans list_arbres(les frequan sont plus petit)
        l_child = list_arbres[0]
        r_child = list_arbres[1]
        
        #creer un nouveau arbre(il composer par deux noeud)(noeud father)  
        fre = l_child.get_frequant() + r_child.get_frequant()
        new_node = HuffmanTree(None,fre,l_child,r_child)
        #suprimer les deux premier noeud dans list_arbres
        list_arbres = list_arbres[2:]
        #ajouter new_node dans list_arbres
        list_arbres.append(new_node)
    #le premier element dans list_arbres est le arbre que on veut
    return list_arbres[0]


'Etape 4 : le taux de compression obtenu'

def get_nb_carac_total_text(txt):
    '''retourner le nombre total du carac dans un texte donnee'''
    '''idem si on utilise text = open(txt,'r')
                          nb_total = text.tell()
                          return nb_total    '''
    text = open(txt,'r').read()
    words = text.rstrip()
    nb_carac_total_text = len(words)
    return nb_carac_total_text
    

def get_volume_initial(nb_carac_total_text):
    '''retourner le volume initial de texte donnee'''
    #d'apres ASCII, chaque caractere a 8 bits
    #volume initial = 8 * nb_carac_text
    return nb_carac_total_text*8

def get_volume_final(list_count,dic_codage):
    '''retourner le volume final de texte donnee'''
    volume = 0
    for i in list_count:
        #i[0] est carac(label)
        #i[1] est frequan
        for j in dic_codage.items():
            #j est chaque item pour dic_codage
            #j[0] est carac
            #j[1] est codage
            #volume final = somme de volume pour chaque carac
            #volume pour chaque carac = frequan_carac * nb_codage
            if i[0] == j[0]:
                #ici je transfere un nombre à une liste de str, par exemple 01001 -> [0,1,0,0,1]
                nb_codage = len(str(j[1]))
                volume = volume + i[1]*nb_codage
    return volume

def taux_compression(volume_init,volume_final):
    '''retourner le taux_compression'''
    return 1-(volume_final/volume_init)
            
    


'Etape 5 : le nombre moyen de bits de stockage d’un caractère dans le texte codé'
        
def nb_moy_text_compresse(volume_final,nb_carac_total_text):
    '''retourner le nombre moyen de bits de stockage d’un caractère'''
    return (volume_final/nb_carac_total_text)


'Etape 6 : compress'

def compress(txt,outputfilename):
    '''sortir un fichier.bin'''
    '''compress quatre partie: 1.le somme de different carac dans le texte(int)
                               2.carac(read par binaire, donc c'est un nombre entre [0,255]) et la frequance pour ce carac
                               3.les codes huffman pour ces caracs, il faut regrouper par 8 car il y a 8 bits dans un octet
                               4.traiter le code de moins de 8 bits restant'''
    #carac_freq,list_arbre (type list)
    carac_freq = open_text_et_count_carac(txt)
    list_arbre = cree_arbres(carac_freq)
    f = open(txt, 'rb')
    filedata = f.read()
    # le nombre total du carac dans un texte donnee
    filesize = f.tell()
    
    '''partie 1: compress le nombre du somme de different carac dans le texte'''
    #length est le somme de different carac dans le texte
    length = len(carac_freq)
    #ouvrir (cree,s'il exist pas) un fichier.bin
    output = open(outputfilename,'wb')
    #Un nombre de type int a 4 octets, il est donc divisé en 4 octets
    #un octet a 8 bits
    #par exemple 900 en binaire est 00000000 00000000 00000011 10000100, donc a4=10000100, a3=00000011 a2=a1=00000000
    a4 = length&255
    length = length>>8
    a3 = length&255
    length = length>>8
    a2 = length&255
    length = length>>8
    a1 = length&255
    output.write(six.int2byte(a1))
    output.write(six.int2byte(a2))
    output.write(six.int2byte(a3))
    output.write(six.int2byte(a4))
    #output.write(six.int2byte(length))
    
    '''partie 2: compress les carac et ses frequance'''
    for x in carac_freq:
        #x[0] est le carac
        output.write(six.int2byte(x[0]))
        #x[1] est le frequant de carac
        #type temp est int aussi
        temp = x[1]
        
        a4 = temp&255
        temp = temp>>8
        a3 = temp&255
        temp = temp>>8
        a2 = temp&255
        temp = temp>>8
        a1 = temp&255
        output.write(six.int2byte(a1))
        output.write(six.int2byte(a2))
        output.write(six.int2byte(a3))
        output.write(six.int2byte(a4))
        #output.write(six.int2byte(temp))
        
    ''''partie 3: compress les codage(combiaison de 01), regrouper par 8'''
    #cree l'arbre huffman
    arbre_huff = cree_arbre_huffman(list_arbre)
    #cree dic_codage
    dic_codage = arbre_huff.codage({},'')
    code_traite = ''
    for i in range(filesize):
        #key est le carac
        key = filedata[i]
        #dic_codage[key] est le code pour ce carac
        code_traite = code_traite + dic_codage[key]
        #out est le 8 premier element du code
        out = 0
        while len(code_traite) > 8:
            for x in range(8):
                out = out << 1
                if code_traite[x] == '1':
                    out = out | 1
            #on a bien le 8 premier element, cad 'out'
            #on supprimer le 8 premier element dans code et on ajouter 'out' dans le fichier.bin
            code_traite = code_traite[8:]
            output.write(six.int2byte(out))
            out = 0
            
    '''partie 4: traiter le code de moins de 8 bits restant'''
    #mettre il reste combien element de code_traite dans fichier.bin
    output.write(six.int2byte(len(code_traite)))
    #out ici est les restes elements de code_traite
    out = 0
    for i in range(len(code_traite)):
        out = out << 1
        if code_traite[i] == '1':
            out = out | 1
    #ajouter 0 a la fin du out pour regrouper par 8, par exemple out=1011, on le ajoute à out=1011 0000
    for i in range(8 - len(code_traite)):
        out = out << 1
    # mettre le derner carac dans le fichier de sortie(fichier.bin)
    output.write(six.int2byte(out))
    # fermer le fichier
    output.close()

'Etape 6 : mettre tout les cara et sa frequant dans le fichier.txt et le sort'  
def cree_fichier_carac_freq(txt,outputfilename):
    #ouvrir le texte
    text = open(txt,'r').read()
    count = {}
    for carac in text:
        if carac not in count:
            count[carac]=1
        else:
            count[carac]=count[carac]+1
    count_avec_ordre = sorted(count.items(),key=lambda x:x[1])
    
    data = open(outputfilename,'w+')
    #mettre le nombre de somme carac dedans
    print(len(count_avec_ordre),file=data)
    #mettre chaque carac et la frequance dedans
    for element in count_avec_ordre:
        print(element[0], '  ', element[1],file=data)
    data.close()




###=============================================
# Test
###=============================================

if __name__ == '__main__':
    #x est list de carac avec sa frequant
    x=open_text_et_count_carac("bon.txt")
    #y est le list de arbre(list de node)pour creer arbre huffman
    y=cree_arbres(x)
    #z est l'arbre huffman
    z=cree_arbre_huffman(y)
    #t est dic de codage pour chaque carac
    t= z.codage({},'')
    nb_carac_total_text = get_nb_carac_total_text("bon.txt")
    v_i = get_volume_initial(nb_carac_total_text)
    v_f = get_volume_final(x,t)
    
    print("Il y a ",nb_carac_total_text,"caractères dans cet article.")
    print("Le taux de compression pour cet article est: ",taux_compression(v_i,v_f))
    print("Le nombre moyen de caractères dans cet article est: ", nb_moy_text_compresse(v_f,nb_carac_total_text))
    compress("bon.txt","bon_compre.bin")
    cree_fichier_carac_freq("bon.txt","bon_freq.txt")




