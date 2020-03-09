def cesar_chiffre_nb(x, k):
  return (x + k) % 26
def cesar_dechiffre_nb(x, k):
  return (x - k) % 26
def cesar chiffre_mot(mot, k):
  message_code = []
for lettre in mot:
  nb = ord(lettre) - 65
nb_crypte = cesar_chiffre_nb(nb, k)
lettre_crypte = chr(nb_crypte + 65)
message_code.append(lettre_crypte)
message_code = "".join(message_code)
return (message_code)
def cesar_attaque(mot):
  for k in range(26):
  print(cesar_chiffre_mot(mot, -k))
return None

def statistiques(phrase):
  liste_stat = [0
    for x in range(26)
  ]
for lettre in phrase:
  i = ord(lettre) - 65
if 0 <= i < 26:
  liste_stat[i] = liste_stat[i] + 1
return (liste_stat)

def vigenere(mot, cle):
  message_code␣ = ␣ []
k = len(cle)
i = 0# Rang dans le bloc
for lettre in mot: #Pour chaque lettre
nomb = ord(lettre) - 65# Lettre devient nb de 0 à 25
nomb_code = (nomb + cle[i]) % 26# Vigenère: on ajoute n i
lettre_code = chr(nomb_code + 65)# On repasse aux lettres
i = (i + 1) % k# On passe au rang suivant
message_code.append(lettre_code)# Ajoute lettre au message
message_code = "".join(message_code)# Revient à chaine caractères
return (message_code)

# Euclide!!

  def euclide(a, b):
  while b != 0:
  a, b = b, a % b
return a

def euclide_etendu(a, b):
  x = 1;
xx = 0
y = 0;
yy = 1
while b != 0:
  q = a // b
a, b = b, a % b
xx, x = x - q * xx, xx
yy, y = y - q * yy, yy
return (a, x, y)

def inverse(a, n):
  c, u, v = euclide_etendu(a, n)# pgcd et coeff de Bézout
if c != 1: #Si pgcd différent de 1 renvoie 0
return 0
else :
  return u % n# Renvoie l 'inverse

# Chiffrement RSA:
  def cle_privee(p, q, e):
  n = p * q
phi = (p - 1) * (q - 1)
c, d, dd = euclide_etendu(e, phi)# Pgcd et coeff de Bézout
return (d % phi)# Bon représentant

def codage_rsa(m, n, e):
  return pow(m, e, n)
def decodage_rsa(x, n, d):
  return pow(x, d, n)

# Puissance
def puissance(x, k, n):
  puiss = 1# Résultat
while (k > 0):
  if k % 2 != 0: #Si k est impair
puiss = (puiss * x) % n
x = x * x % n# Vaut x, x ^ 2, x ^ 4, ...
  k = k // 2
return (puiss)