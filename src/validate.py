def validateAFN(AFNtransitions, AFNsymbols, AFNstates, AFNinitialState, AFNfinalStates):
  if(AFNfinalStates.__len__() == 0):
    print('Erro: É necessário informar ao menos 1 estado final')
    exit(1)
  else:
    for state in AFNfinalStates:
      if(AFNstates.count(state) == 0):
        print('Erro: Todos o estados finais devem pertencer ao conjunto de estados do autômato')
        exit(1)
    
  if(AFNsymbols.__len__() == 0):
    print('Erro: É necessário informar ao menos 1 símbolo')
    exit(1)

  if(AFNstates.__len__() == 0):
    print('Erro: É necessário informar ao menos 1 estado')
    exit(1)

  if(AFNinitialState == ''):
    print('Erro: É necessário informar o estado inicial')
    exit(1)
  elif(AFNstates.count(AFNinitialState) == 0):
    print('Erro: O estado inicial deve pertencer ao conjunto de estados do autômato')
    exit(1)

  for transition in AFNtransitions:
    if(AFNstates.count(transition.get('from')) == 0):
      print("Erro: O estado do atributo 'from' deve pertecer ao conjunto de estados do autômato")
      exit(1)
    elif(AFNstates.count(transition.get('to')) == 0):
      print("Erro: O estado do atributo 'to' deve pertecer ao conjunto de estados do autômato")
      exit(1)
    elif(AFNsymbols.count(transition.get('symbol')) == 0):
      print("Erro: O símoblo do atributo 'symbol' deve pertecer ao alfabeto do autômato")
      exit(1)
