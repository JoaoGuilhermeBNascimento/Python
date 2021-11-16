def master(função):
    def slave():
        função()
    # slave()
    return slave
def fala_oi():
    print('oi')   


variavel = master(fala_oi)

variavel()