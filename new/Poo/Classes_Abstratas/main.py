""" from abc import ABC,abstractclassmethod
Não se pode instânciar classes abstratas
# abc = abstratct class

  """
from Poo.Classes_Abstratas.classes.cp import * # ContaPoupanca
from Poo.Classes_Abstratas.classes.cc import * #ContaCorrente

cp = ContaPoupanca(1111, 2222,0)
cp.depositar(10)
cp.depositar(500)
cp.sacar(60)
cp.sacar(450) 

print('##############')
 
cc = ContaCorrente(agencia=1111, conta=2222,saldo=0, limite=500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(100)

