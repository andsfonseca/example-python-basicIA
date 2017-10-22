# Exemplo de códigos aplicados em IA

Os códigos neste repositório são códigos que apresentam ativadades realizadas em aula.
Conteúdo apenas para armazenamento e aprendizado.

## Lista de Classes Contidas
### + Node
> - `Construtor (name)` : Instancia um Node e define name como um nome atribuido a ele.
> - `printNode (short = false)` : Printa o valor do node e o nome dos seus filhos vinculados, se a opção `short` : estiver verdadeira ele irá apenas printar o seu nome
> - `addAdjacencies(node, distance)` : Adiciona um Node como adjascente a ele, o que possui um determinado custo de distancia. Os nodes adjascentes também recebem ele como atributo, além da mesma distância
> - `searchAdjacencies(node)` : Procura se um determinado Node possui adjascência com ele mesmo, caso tenha retorna a distância senão retorna `None`

### + Defaults
> - `Load(defaultParam)` : Carrega um Dicionário de Nodes predefinidos e retorna (Valores Disponíveis {"Cidades"}) 

### + Utils
> - `contaisInList(list, obj):` : Verifica se um determinado Objeto está contido em uma lista

### + Graph
> - `dictParentToList(dictx, last)` : Transforma um dicionário de pais em uma lista encadeada do primeiro pai até seu ultimo filho. Recebe como parametro o ultimo filho e o dicionário de paternidade
> - `BFSearch( final, queue = [] , traveled = [], parent = {})` : Realiza uma busca em largura dos nodes em uma fila até o objetivo final. É possível também entregar os dados no meio de uma busca setando as variaveis `traveled` e `parent`
> - `DjikstraSearch(final, queue = [], traveled = [], parent = {}, expectation = {})` : Realiza uma busca usando o algoritmo de Djikstra uma fila de prioridades até o objetivo final. É possível também entregar os dados no meio de uma busca setando as variaveis `traveled`, `parent` e `expectation`