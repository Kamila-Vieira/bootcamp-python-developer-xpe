projetos
  - projeto_id
  - nome
  - data_inicio
  - area_id
  - documento_id
  - colaborador_id
  
areas
  - area_id
  - nome
  
documentos
  - documento_id
  - titulo
  - descricao
  - tarefa_id
  
tarefas
  - tarefa_id
  - tipo
  - nome
  - componente_id
  - colaborador_id
  
componentes
  - componente_id
  - nome
  - categoria
  - colaborador_id
  
colaboradores
  - colaborador_id
  - matricula
  - nome
  - email
  
**Descrição:** Considere a seguinte demanda de uma área de projetos de uma empresa:
  
  - Para controlar os projetos de software, uma Fábrica de Software deseja desenvolver um sistema de gestão de seus projetos. Para que seja possível controlar seu ciclo de vida, será necessário armazenar o cadastro de projetos com seu nome, data de início, área e colaboradores que estão alocados em sua execução com matrícula, nome e e-mail.
  - Cada colaborador está dedicado exclusivamente a um projeto, mesmo que um projeto possa ter uma equipe composta por várias pessoas.
  - Cada projeto possui uma série de documentos que são utilizados para especificação, nos quais temos um título e a descrição. Cada documento pode gerar uma ou mais tarefas para o time, e cada tarefa pode ter sido gerada por um ou mais documentos.
  - As tarefas possuem nome e tipo (desenvolvimento, teste ou artefatos).
  - Todas as tarefas geram um componente de software que, por sua vez, pode ser gerado por uma ou mais tarefas. Cada componente de software tem nome e categoria (tela, backend etc.).
  - Cada tarefa possui um ou mais colaboradores responsáveis.
  - Cada componente é validado por um ou mais colaboradores.
  - Todos os projetos possuem um colaborador que é o Gerente do Projeto.
