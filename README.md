# Exemplo de códigos aplicados em IA

Os códigos neste repositório são códigos que apresentam ativadades realizadas em aula.
Conteúdo apenas para armazenamento e aprendizado.

## Lista de Classes Contidas
### + Node
> - `Construtor (value)` : Instancia um Node e define value como um associado a ele
> - `printNode (short = false)` : Printa o valor do node e o nome dos seus filhos vinculados, se a opção `short` : estiver verdadeira ele irá apenas printar o seu nome
> - `addAdjacencies(node, distance)` : Adiciona um Node como adjascente a ele, o que possui um determinado custo de distancia. Os nodes adjascentes também recebem ele como atributo, além da mesma distância
> - `searchAdjacencies(node)` : Procura se um determinado Node possui adjascência com ele mesmo, caso tenha retorna a distância senão retorna `None`

### + Defaults
> - `Load(defaultParam)` : Carrega um Dicionário de Nodes predefinidos e retorna (Valores Disponíveis {"cidades", "riverproblem"}) 
> - `printParams(_mappedNodes, expectationTarget)` : Carrega um Dicionário de Expectativas predefinidas e retorna (Valores Disponíveis {"cbucareste"}) 
> - `printParams()` : Imprime os nomes do dicionários de Nodes
> - `printParamExpectations()` : Imprime as expectativas predefindas

### + Utils
> - `contaisInList(list, obj):` : Verifica se um determinado Objeto está contido em uma lista

### + Graph
> - `dictParentToList(dictx, last)` : Transforma um dicionário de pais em uma lista encadeada do primeiro pai até seu ultimo filho. Recebe como parametro o ultimo filho e o dicionário de paternidade
> - `BFSearch( final, queue = [] , traveled = [], parent = {})` : Realiza uma busca em largura dos nodes em uma fila até o objetivo final. É possível também entregar os dados no meio de uma busca setando as variaveis `traveled` e `parent`
> - `DjikstraSearch(final, queue = [], traveled = [], parent = {}, euristic = {})` : Realiza uma busca usando o algoritmo de Djikstra uma fila de prioridades até o objetivo final. É possível também entregar os dados no meio de uma busca setando as variaveis `traveled`, `parent` e `euristic`
> - `ASearch(expectations, final, queue = [], traveled = [], parent = {}, euristic = {})` : Realiza uma busca usando o algoritmo de A* uma fila de prioridades até o objetivo final. É possível também entregar os dados no meio de uma busca setando as variaveis `traveled`, `parent` e `euristic`

### + RiverProblem
> - `createStateFromStringParam(stringParam)` : Retorna um `RiverProblemState` com a predefinição de `stringParam` (Valores {"b": Barqueiro, "t" : Trigo, "g": Galinha, "r": Raposa})

### + RiverProblemState
> - `Construtor (left, side)` : Cria um Objeto com os estados possíveis para cada lado do rio
> - `print()` : Retorna em um texto padronizado o seu próprio estado