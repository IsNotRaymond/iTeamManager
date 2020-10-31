# iTeamManager
## 1. Resumo
Esse projeto apresenta a proposta de uma ferramenta de integração entre as matriz curriculares dos discentes e docentes do IFPI. A ferramenta disporá de duas frontes, um sistema de busca para encontrar pessoas com conhecimentos específicos para o seu projeto, e grupos onde os projetos gerados no sistema possam ser discutidos mais detalhadamente.

## 2. Justificativa
Este projeto busca resolver uma problemática que muitas vezes não é vista pelo grande público, a falta de acesso à outras áreas de conhecimento na realização de um projeto institucional. Sem uma visão ampla das possibilidades, o docente limita-se ao escopo que lhe é mostrado e nunca é desafiado com novas e inesperadas experiências. A integração destes viria de maneira natural caso tal facilidade fosse lhes apresentada.

## 3. Fundamentação Teórica
Não foi encontrada nenhuma ferramenta de gerenciamento de pesquisadores e grupos científicos como a proposta. No caso desta ferramenta, o que se destaca é a possibilidade de poder buscar alguém por sua área de estudo, a plataforma Lattes possui um sistema de busca de currículos por nome, mas não é muito intuitivo quando se procura alguma pessoa específica de uma área. Mas apesar disso, essa ferramenta não visa menosprezar o Lattes, e sim buscar uma forma de facilitar o trabalho de pessoas que tem algum projeto em mente, e busquem pessoas específicas.

## 4. Objetivo Geral
Construir um sistema que simplifique a integração entre discentes e/ou docentes de diferentes áreas do conhecimento em um projeto de pesquisa.

## 5. Objetivos específicos
* Desenvolver um sistema onde todos no instituto tenham acesso aos projetos cadastrados no sistema, sejam eles de sua área ou não.
* Aplicar sistema de notificação por interesse onde um usuário recebe propostas de projetos que lhe cabem.
* Disseminar e incentivar a idéia de projetos integrados.

## 6. Metodologia da Execução do Projeto
Será utilizada a metodologia ágil, mais especificadamente o Scrum. Pois um projeto simples como esse poderá e irá demandar novas funcionalidades a medida em que ele é desenvolvido. Além de ser adequado para uma equipe pequena.
Pretende-se a início focar no desenvolvimento da camada do servidor e em seguida focar em deixar a ferramenta visualmente atrativa.

## 7. Acompanhamento e Avaliação do Projeto Durante a Execução
O orientador deverá observar os resultados do desenvolvimento do projeto a cada 2 semanas até que o mesmo se finalize. O orientador também deverá destacar os pontos bons e ruins do projeto para que a consistência do mesmo seja mantida, e que ele seja finalizado nas condições esperadas.

## 8. Resultados Esperados e Disseminação dos Resultados
Espera-se que uma ferramenta que possa atender aos objetivos gerais e específicos seja disponibilizada online. E disseminado através da utilização dos docentes e discentes em seus determinados projetos

## 9. Público Alvo
* Corpo docente
* Corpo discente

## 10. Funcionalidades do Sistema
| Nome | Atores | Descrição |
| ------ | ------ | ------ |
|Fazer login|Usuário|Esse caso de uso permite que o usuário entre no sistema|
|Exibir erro de Login|Usuário|Exibe-se uma tela de erro e o usuário volta para a tela de Login|
|Verificar senha|Usuário|Sistema verifica se a senha é compatível com a senha cadastrada pelo usuário|
|Pesquisar Projetos|Usuário|O usuário pode pesquisar projetos para ingressar|
|Solicitar Participação|Usuário|O usuário solicita a participação nos projetos que tem interesse|
|Selecionar Projeto|Usuário|O usuário seleciona um projeto de seu interesse para obter acesso a seus detalhes|
|Administrar Projetos|Moderador|O Moderador realiza ações que lhe foram permitidas pelo criador do projeto|
|Visualizar projeto|Usuário|O usuário obtém acesso aos detalhes de um projeto previamente selecionado|
|Editar projeto|Administrador|O usuário com permissão pode editar um projeto|
|Deletar projeto|Administrador, moderador|O usuário com permissão pode excluir um projeto|
|Administrar Projeto|Administrador|Gerenciar o ambiente do projeto para não se tornar toxico|
|Expulsar Participante|Administrador|O Administrador pode expulsar quem ele acha que está atrapalhando no projeto|
|Criar projeto|Pesquisador|Pesquisador pode criar um projeto, dentro desse projeto ele é o criador|
|Verificar Participação|Criador|Descrição - O criador de projeto verifica o perfil do Usuário antes de aceitar u negar sua participação|
|Aceitar Participação|Criador|O criador de projeto permite que o usuário entre para o seu projeto|
|Negar Participação|Criador|O Criador de projeto nega que o usuário entre para o projeto|
|Alocar cargos|Criador|O Criador de projetos pode alocar cargos para quem está abaixo dele na hierarquia do projeto|

## 11. Equipe

| Nome | Github |
| ------ | ------ |
| Artur Oliveira Carvalho | https://github.com/IsNotRaymond |
| Firmo Lopes de Oliveira Neto | https://github.com/ |
| João Victor Sousa Oliveira | https://github.com/ |
| Luiz Araujo da Conceição Junior | https://github.com/Lacj2000 |
| Phelyppe Matheus Silva Da Costa | https://github.com/PhePheMath |

## 12. Casos de Uso
![alt text](documentation/UCiTeM.png)

## 13. Especificações dos casos de uso
| UC-01 | Fazer Login |
| ------ | ------ |
|Ator Principal|Usuário|
|Descrição Geral|Esse caso de uso permite que o usuário entre no sistema|
|Pré Condições|O usuário está devidamente registrado no sistema|
|Pós Condições|Verificar as credenciais|
|Fluxo Principal| 1. Usuário aguarda o sistema verificar as credenciais de login <br/> 2. O sistema libera a entrada do usuário ao sistema|
|Fluxo Alternativo|2.1. O usuário erra os dados cadastrados de Login, indo para “Exibir erro de Login”|

| UC-02 | Exibir erro de Login |
| ------ | ------ |
|Ator Principal|Usuário|
|Descrição Geral|Exibe-se uma tela de erro e o usuário volta para a tela de Login|
|Pré Condições|Usuário tentar entrar no sistema|
|Pós Condições|Retornar para a tela de login|
|Fluxo Principal| 1. O Sistema exibe uma tela de erro <br/> 2. Após alguns segundos o usuário é redirecionado para a tela de Login|
|Fluxo Alternativo||

| UC-03 | Verificar senha |
| ------ | ------ |
|Ator Principal|Usuário|
|Descrição Geral|Sistema verifica se a senha é compatível com a senha cadastrada pelo usuário|
|Pré Condições|O usuário tenta fazer o Login|
|Pós Condições|Entrada no sistema|
|Fluxo Principal| 1. O sistema verifica as credenciais do usuário <br/> 2. O usuário adentra ao sistema|
|Fluxo Alternativo|2.1. Inicia o caso de uso “Exibir erro de Login”|

| UC-04 | Solicitar Participação |
| ------ | ------ |
|Ator Principal|Usuário|
|Descrição Geral|O usuário solicita a participação nos projetos que tem interesse|
|Pré Condições|Usuário necessita selecionar um projeto|
|Pós Condições|Não há|
|Fluxo Principal| 1. O usuário encontra um projeto que atraia o seu interesse <br/> 2. O usuário submete a sua inscrição no projeto que viu no feed|
|Fluxo Alternativo|1.1 O usuário pesquisa por um nome chave de algum projeto|

| UC-05 | Selecionar Projeto |
| ------ | ------ |
|Ator Principal|Usuário|
|Descrição Geral|O usuário seleciona um projeto de seu interesse para obter acesso a seus detalhes|
|Pré Condições|Usuário necessita estar devidamente logado no sistema|
|Pós Condições|Não há|
|Fluxo Principal| 1. Usuário clica em algum projeto <br/> 2. Usuário recebe como resposta as informações do projeto como escopo, criador, requisitos para participar, etc ...<br/> 3. Recebe também a opção de solicitar participação e tirar esse projeto das recomendações|
|Fluxo Alternativo|Não há|

| UC-06 | Administrar Projeto |
| ------ | ------ |
|Ator Principal|Moderador|
|Descrição Geral|O Moderador realiza ações que lhe foram permitidas pelo criador do projeto.|
|Pré Condições|O usuário tem que possuir a característica de moderador|
|Pós Condições|Não há|
|Fluxo Principal| 1. Usuário clica em algum projeto <br/> 2. Usuário visualiza características de projetos, como nome e escopo <br/> 3. Usuário pondera se deve apagar ou apenas intimar o projeto|
|Fluxo Alternativo|Não há|

| UC-07 | Visualizar Projeto |
| ------ | ------ |
|Ator Principal|Usuário|
|Descrição Geral|O usuário obtém acesso aos detalhes de um projeto previamente selecionado.|
|Pré Condições|Usuário necessita estar devidamente logado no sistema|
|Pós Condições|Não há|
|Fluxo Principal| 1. Usuário clica em algum projeto <br/> 2. Usuário recebe como resposta as informações do projeto|
|Fluxo Alternativo|Não há|

| UC-08 | Editar Projeto |
| ------ | ------ |
|Ator Principal|Administrador|
|Descrição Geral|O usuário com permissão pode editar um projeto|
|Pré Condições|O usuário ter permissões de Administrador|
|Pós Condições|Não há|
|Fluxo Principal| 1. O usuário seleciona o projeto <br/> 2. Seleciona a opção editar projeto <br/> 3. ele pode alterar nome, escopo, entre outras modalidades|
|Fluxo Alternativo|Não há|

| UC-09 | Deletar Projeto |
| ------ | ------ |
|Ator Principal|Administrador, Moderador|
|Descrição Geral|O usuário com permissão pode excluir um projeto|
|Pré Condições|O usuário ter permissões de Administrador ou Moderador|
|Pós Condições|Não há|
|Fluxo Principal| 1. O usuário seleciona o projeto <br/> 2. Seleciona a opção editar projeto <br/> 3. ele pode alterar nome, escopo, entre outras modalidades|
|Fluxo Alternativo|Não há|

| UC-10 | Administrar Projeto |
| ------ | ------ |
|Ator Principal|Administrador|
|Descrição Geral|Gerenciar o ambiente do projeto para não se tornar toxico|
|Pré Condições|O usuário ter permissões de Administrador|
|Pós Condições|1. Gerar relatórios de qualidade e produção para o criador <br/> 2. Caso algum usuário seja expulso, gerar motivo de expulsão|
|Fluxo Principal| 1. Administrador vê o andamento do projeto <br/> 2. O administrador pondera sobre a participação dos integrantes do projeto <br/> 3. O administrador decide se expulsa ou adverte quem tiver comportamentos não condizentes com a postura esperada do projeto|
|Fluxo Alternativo|Não há|

| UC-11 | Expulsar Participante |
| ------ | ------ |
|Ator Principal|Administrador|
|Descrição Geral|O Administrador pode expulsar quem ele acha que está atrapalhando no projeto|
|Pré Condições|O usuário ter permissões de Administrador|
|Pós Condições|Gerar motivo da expulsão|
|Fluxo Principal| 1. administrador percebe que usuário diminui a eficiência e atrapalha os outros integrantes do projeto <br/> 2. Administrador seleciona o usuário desejado <br/> 3. Aparecem as opções visualizar perfil, e expulsar do time|
|Fluxo Alternativo|Não há|

| UC-12 | Criar Projeto |
| ------ | ------ |
|Ator Principal|Pesquisador|
|Descrição Geral|Pesquisador pode criar um projeto, dentro desse projeto ele é o criador|
|Pré Condições|Estar efetivamente logado no sistema|
|Pós Condições|1. Criação de um projeto <br/> 2. Torna-se criador do projeto criado|
|Fluxo Principal| 1. O usuário abre a aplicação <br/> 2. Pressiona no botão de gerar novo projeto <br/> 3. Da um nome e um escopo para o projeto <br/> 4. Pode gerar convites e chamar outros usuários para participar|
|Fluxo Alternativo|Não há|

| UC-13 | Verificar Participação |
| ------ | ------ |
|Ator Principal|Criador|
|Descrição Geral|O criador de projeto verifica o perfil do Usuário antes de aceitar ou negar sua participação|
|Pré Condições|O usuário envia a solicitação de participação para o projeto|
|Pós Condições|Aceitar ou negar a solicitação|
|Fluxo Principal| 1. O criador abre a tela de solicitações pendentes <br/> 2. O Criador seleciona um usuário de seu interesse da tabela <br/> 3. O criador pode ver o perfil e a quais outros projetos aquele perfil está atrelado|
|Fluxo Alternativo|Não há|

| UC-14 | Aceitar Participação |
| ------ | ------ |
|Ator Principal|Criador|
|Descrição Geral|O criador de projeto permite que o usuário entre para o seu projeto|
|Pré Condições|O usuário envia a solicitação de participação para o projeto e o Criador verifica o seu perfil|
|Pós Condições|Criador define qual papel o usuário exercerá no projeto|
|Fluxo Principal| 1. Criador analisa solicitações pendentes <br/> 2. Criador percebe que o perfil da solicitação se enquadra e/ou é compatível com o escopo do projeto <br/> 3. criador aceita a participação do usuário|
|Fluxo Alternativo|Não há|

| UC-15 | Negar Participação |
| ------ | ------ |
|Ator Principal|Criador|
|Descrição Geral|O Criador de projeto nega que o usuário entre para o projeto|
|Pré Condições|O usuário envia a solicitação de participação para o projeto e o Criador verifica o seu perfil|
|Pós Condições|Não há|
|Fluxo Principal| 1. Criador analisa solicitações pendentes <br/> 2. Criador percebe que o perfil da solicitação não se enquadra e/ou não é compatível com o escopo do projeto <br/> 3. criador nega a participação do usuário|
|Fluxo Alternativo|Não há|

| UC-16 | Alocar cargos |
| ------ | ------ |
|Ator Principal|Criador|
|Descrição Geral|O Criador de projetos pode alocar cargos para quem está abaixo dele na hierarquia do projeto|
|Pré Condições|1. Já haverem participantes no projeto <br/> 2.Algum usuário ter solicitado a participação no projeto|
|Pós Condições|Não há|
|Fluxo Principal| 1. Criador pesquisa um participante do grupo <br/> 2. Criador seleciona o participante <br/> 3. Criador escolhe cargo a ser atribuído ao participante selecionado <br/> 4. Participante recebe as permissões do cargo|
|Fluxo Alternativo|1. Criador aceita um novo participante <br/> 2. Criador atribui o cargo ao participante na hora de aceita-lo|
