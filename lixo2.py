lista = [
    ['Vinicius','Ferreira','viniciusreismf@gmail.com','11972237929'],
    ['Eliasibe','Vieira','cvadaltotristao@gmail.com','27997205528'],
    ['Marcelo','Souza','souza7611@gmail.com','21909090909'],
    ['Rene','Sa','sa.rene@hotmail.com','19988477725'],
    ['wellinton','santos','wellintonsantos555@gmail.com','12996154656'],
    ['Matheus','Guerreiro','matheusguerreirofla@hotmail.com','61983406915'],
    ['matheus','gonzaga','contato.matheusgonzaga@gmail.com','21971022878'],
    ['Gustavo','Magalhaes','gugamagalhaes2006@hotmail.com','11959819844'],
    ['Jhon','Veiga','joaobernardoveiga8@gmail.com','21990461902'],
    ['Douglas','Simões','usanegocios2.0@gmail.com','21975628822'],
    ['Fernando','Facchini','feer.facchini@gmail.com','19971124274'],
    ['Joao','Medeiros','joao.medeiros@globalsat.com','75992930985'],
    ['Maiko','Nascimento','maiko.nascimento@outlook.com','95991102340'],
    ['Amanda','Prado','silva.amandaprado@gmail.com','11952488801']
]


for i in lista:
    print (f"INSERT INTO clientes (nome,sobrenome,email,telefone) values ('{i[0]}','{i[1]}','{i[2]}','{i[3]}');")