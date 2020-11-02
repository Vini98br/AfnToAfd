import xml.etree.ElementTree as ET
import itertools 
from validate import validateAFN
 
tree = ET.parse('in.xml')
root = tree.getroot()

AFNtransitions = []
AFNsymbols = []
AFNstates = []
AFNinitialState = ''
AFNfinalStates = []

for child in root:
  if(child.tag == 'Alphabet'):
    for symbol in child.findall('Symbol'):
      if(AFNsymbols.count(symbol.text) == 0):
        AFNsymbols.append(symbol.text)
  elif(child.tag == 'States'):
    for state in child.findall('State'):
      if(AFNstates.count(state.text) == 0):
        AFNstates.append(state.text)
  elif(child.tag == 'Transitions'):
    for transition in child.findall('Transition'):
      if(
        transition.get('from') is not None and 
        transition.get('symbol') is not None and 
        transition.get('to') is not None
      ):
        AFNtransitions.append(transition.attrib)
      else:
        print('Erro: Toda <Transition> deve ter os atributos: from, symbol e to')
        exit(1)
  elif(child.tag == 'InitialState' and child.text is not None):
    AFNinitialState = child.text
  elif(child.tag == 'FinalState'):
    for final in child.findall('State'):
      if(AFNsymbols.count(final.text) == 0):
        AFNfinalStates.append(final.text)

validateAFN(AFNtransitions, AFNsymbols, AFNstates, AFNinitialState, AFNfinalStates)

print('AFNtransitions:', AFNtransitions)
print('AFNsymbols:', AFNsymbols)
print('AFNstates:', AFNstates)
print('AFNinitialState:', AFNinitialState)
print('AFNfinalStates:', AFNfinalStates)

AFDtransitions = []
AFDsymbols = AFNsymbols
AFDfinalStates = []
AFDinitialState = AFNinitialState
AFDstates = []
for x in range(1, AFNstates.__len__() + 1): 
  for y in list(itertools.combinations(AFNstates, r=x)):
    elem = list(y)
    AFDstates.append(elem)

for combinedStates in AFDstates:
  for state in combinedStates:
    if(AFNfinalStates.__contains__(state)):
      AFDfinalStates.append(combinedStates)

print('=====================')
print('AFDtransitions:', AFDtransitions)
print('AFDsymbols:', AFDsymbols)
print('AFDstates:', AFDstates)
print('AFDinitialState:', AFDinitialState)
print('AFDfinalStates:', AFDfinalStates)

# Todo: AFDtransitions

AFDroot = ET.Element('Automaton')
alphabet = ET.SubElement(AFDroot, 'Alphabet')
for symbol in AFDsymbols:
  ET.SubElement(alphabet, 'Symbol').text = symbol

states = ET.SubElement(AFDroot, 'States')
for state in AFDstates:
  ET.SubElement(states, 'State').text = str(state).replace('\'', '').replace('[','(').replace(']',')')

transitions = ET.SubElement(AFDroot, 'Transitions')

initialState = ET.SubElement(AFDroot, 'InitialState').text = AFDinitialState

finalState = ET.SubElement(AFDroot, 'FinalState')
for state in AFDfinalStates:
  ET.SubElement(finalState, 'State').text = str(state).replace('\'', '').replace('[','(').replace(']',')')

AFDtree = ET.ElementTree(AFDroot)

AFDtree.write('out.xml', xml_declaration=True, encoding='utf-8')