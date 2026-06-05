PIM\_VI\_RESUMO



**Objetivo:**



proposta prevê o desenho e a implementação de um ecossistema web para clínicas

populares, integrando prontuário eletrônico simplificado, agendamento e gestão de filas

em tempo quase real, apoiado em práticas de engenharia de software ágil orientadas

à qualidade, em modelagem de banco de dados relacional com apoio de recursos NoSQL,

em princípios de UX/UI centrados no usuário e em técnicas de machine learning e análise

de dados aplicadas ao acompanhamento e à previsão de indicadores assistenciais. 



**Objetivos específicos**



 Estruturar o projeto de software com base em métodos ágeis, produzindo backlog de

produto, sprints planejados, critérios de aceite e mecanismos de verificação e validação

que incorporem requisitos funcionais e não funcionais de segurança, confidencialidade

de dados sensíveis e disponibilidade do sistema.



 Projetar e implementar um modelo de dados relacional em SQL Server para cadastros

de pacientes, profissionais de saúde, consultórios, agendamentos, atendimentos e filas,

complementado por um módulo NoSQL destinado a registros de log, trilhas de auditoria

e anotações clínicas livres, com consultas que atendam às rotinas diárias de recepção

e consultório.



 Conceber a experiência do usuário e o desenho das interfaces do sistema a partir

de técnicas de UX e UI Design, incluindo definição de personas (paciente, recepcionista,

profissional de saúde), mapa de jornada, fluxos de interação, wireframes e protótipos

navegáveis, avaliados por meio de testes de usabilidade com usuários simulados.



 Construir um pipeline de machine learning e análise de dados, utilizando ferramentas

como Python, Pandas, Scikit-learn e Jupyter Notebooks, para transformar registros de

atendimentos, tempos de espera, ausências e características básicas dos pacientes em

indicadores descritivos e modelos preditivos capazes de estimar risco de superlotação,

probabilidade de falta e tempo estimado de espera. 



 Documentar requisitos, arquitetura, decisões de projeto, modelo de dados, protótipos

de interface, experimentos de machine learning e evidências de teste em um dossiê

técnico que permita avaliar a aderência do sistema às necessidades do cenário proposto

e aos conteúdos das quatro disciplinas



**2.4. Ações a serem desenvolvidas e o relacionamento com as disciplinas**



**Engenharia de Software Ágil Aplicada**



 Na disciplina de Engenharia de Software Ágil Aplicada, as equipes deverão elaborar

a gestão completa do projeto de software e os artefatos de qualidade associados,

produzindo um documento de visão e escopo do sistema com a descrição sucinta

do problema da clínica popular, dos atores envolvidos, das restrições e dos objetivos

de negócio. Também será elaborado um conjunto de requisitos funcionais e não

funcionais, com destaque para aspectos de segurança, confidencialidade dos dados

de saúde, desempenho esperado para as operações de fila e critérios de usabilidade

alinhados a normas de qualidade de software. As equipes organizarão um backlog de

produto em formato de user stories, priorizado por valor para a clínica e contemplando

funcionalidades como cadastro de paciente, triagem simplificada, monitor de fila, painel

do médico, histórico de atendimentos e relatórios de indicadores, além de realizar

o planejamento de sprints, a definição de uma matriz de papéis e responsabilidades

e a manutenção de quadros Kanban, digitais ou físicos, que documentem o andamento

do trabalho. Será ainda construído um plano de verificação e validação, incluindo

a estratégia de testes unitários, de integração e de aceitação, acompanhado de evidências

mínimas de execução, como relatórios de ferramentas, capturas de tela e registros de

casos de teste.

==> **Entregáveis principais**, serão produzidos um documento de requisitos com

3 a 6 páginas, o backlog de produto e de sprints em planilha ou ferramenta escolhida,

um plano de testes com amostra de casos preenchidos e evidências de execução,

e um relato breve, de 1 a 2 páginas, analisando como as práticas ágeis, as normas

e os modelos de qualidade estudados na disciplina foram aplicados ao projeto.



**Modelagem de Banco de Dados e NoSQL**



 Na disciplina de Modelagem de Banco de Dados e NoSQL, as equipes deverão projetar

o repositório de dados que sustentará o prontuário eletrônico e a gestão de filas, começando

pela elaboração de um diagrama Entidade-Relacionamento com as principais entidades,

como Pacientes, Profissionais, Agendamentos, Atendimentos, Filas, Unidades e Usuários

do sistema, com seus atributos e relacionamentos. Será necessária a aplicação de regras

de normalização até pelo menos a terceira forma normal, de modo a evitar redundâncias

indevidas e anomalias de atualização, justificando, quando necessário, eventuais pontos

de desnormalização em função de requisitos de desempenho. As equipes deverão criar

scripts SQL (DDL) para definição de esquemas, tabelas, chaves primárias e estrangeiras

e índices para consultas críticas, como busca de pacientes, listagem de fila por consultório

e recuperação do histórico de atendimentos de um paciente, bem como implementar um

conjunto de consultas SQL representativas (DML), incluindo filtros por data, profissional,

status de fila e estatísticas simples de atendimento. Além disso, será definido um pequeno

módulo NoSQL, por exemplo baseado em documentos JSON, voltado ao armazenamento

de logs de acesso ao prontuário, anotações livres de consulta ou eventos de atualização

de fila, com descrição do modelo de documentos e de consultas básicas.

==> **Entregáveis principais**, serão produzidos o diagrama ER e o dicionário de

dados do sistema, os scripts SQL Server (DDL) para criação do banco e scripts de exemplo

de inserção e consulta (DML), uma descrição textual de 1 a 2 páginas explicando

as escolhas de modelagem, os índices definidos e os pontos de desnormalização

adotados e a especificação do esquema NoSQL, com exemplos de registros

e de consultas.



**UX e UI Design**



 Na disciplina de UX e UI Design, o foco será a concepção da experiência de uso

do sistema para os diferentes atores da clínica popular, iniciando com uma pesquisa

exploratória baseada em entrevistas fictícias, relatos de casos ou observação de cenários,

cujo resultado deverá incluir pelo menos três personas representando o paciente típico de

clínica popular, a recepcionista e o profissional de saúde. A partir dessas personas, serão

construídos mapas de jornada do usuário para fluxos centrais, como marcar consulta,

chegar à clínica e entrar na fila, ser chamado para atendimento e consultar o histórico

de atendimentos, além da elaboração de fluxos de navegação e de wireframes de baixa

fidelidade para as telas fundamentais, como tela de login, painel da recepção, painel

do médico, painel da sala de espera e formulários de cadastro. Em seguida, as equipes

desenvolverão um protótipo interativo em ferramenta de prototipagem, como Figma

ou similar, aplicando princípios de hierarquia visual, tipografia adequada, contraste

e acessibilidade, e conduzirão pelo menos um ciclo de teste de usabilidade com colegas

atuando como usuários simulados, registrando as dificuldades encontradas e os ajustes

realizados no protótipo.

==> **Entregáveis principais** dessa disciplina serão um relatório de UX com 3 a 5

páginas, contendo as personas, as jornadas e a síntese da pesquisa, o conjunto de

wireframes das telas principais, um protótipo navegável, disponibilizado por capturas

de tela com descrição dos fluxos, e um relato curto sobre os testes de usabilidade

e as melhorias aplicadas.



**Machine Learning e Análise de Dados**



 Na disciplina de Machine Learning e Análise de Dados, os estudantes deverão

construir um conjunto de análises e modelos preditivos a partir de dados gerados ou

simulados pelo sistema de prontuário e fila, começando pela definição clara do problema

de aprendizado a ser tratado, como previsão de tempo estimado de espera, previsão de

falta a consultas (no-show) ou classificação do risco de superlotação da clínica em

determinados horários. Em seguida, será montado um conjunto de dados consolidado,

em formato aberto como CSV, a partir do modelo relacional e/ou do módulo NoSQL,

contendo variáveis de entrada, por exemplo horário, dia da semana, tipo de consulta,

histórico de atrasos e características básicas do paciente, e uma variável alvo adequada

ao problema escolhido. Os estudantes deverão realizar o pré-processamento dos dados,

incluindo limpeza, tratamento de valores ausentes, codificação de variáveis categóricas

e normalização ou padronização quando pertinente, para então conduzir uma análise

exploratória de dados com gráficos e estatísticas descritivas que permitam investigar

padrões de demanda, tempos de espera, distribuição de faltas e correlações entre variáveis.

Com base nesse diagnóstico, serão treinados pelo menos dois algoritmos de aprendizado

supervisionado, como Regressão Logística e Random Forest para classificação de noshow ou Regressão Linear e Gradient Boosting para estimativa de tempo de espera, com

breve justificativa da escolha, e os modelos serão avaliados com métricas adequadas

ao tipo de problema, como acurácia, precisão, recall, F1-score, RMSE ou curva ROC/

AUC, permitindo a comparação dos resultados e a seleção de um modelo principal para

o cenário da clínica. Também será realizado um pequeno experimento de ajuste de

hiperparâmetros, por exemplo, com Grid Search ou Random Search, registrando os

impactos nas métricas de desempenho e discutindo ganhos e limitações, e todo o código

será organizado em um caderno Jupyter, ou ferramenta equivalente, contendo todas as 

etapas do pipeline, desde a carga de dados, pré-processamento, análise exploratória

e modelagem até a avaliação e o salvamento dos resultados.

==> **Entregáveis principais**, serão fornecidos o conjunto de dados consolidado

em formato aberto, acompanhado de dicionário de dados, o caderno Jupyter com

o pipeline completo de análise e modelagem e um relatório técnico de 4 a 6 páginas,

descrevendo o contexto, a construção do dataset, as técnicas aplicadas, os resultados

obtidos, as limitações e as possibilidades de evolução dos modelos no contexto das

clínicas populares.

