**Projeto 02** – Criar um sistema analítico, com massivo processamento de consultas aos dados, com poucos momentos de inserção e sem atualizações nos dados, ou seja, um sistema de relatórios. Sabe-se que a carga de dados será responsabilidade de outro setor, mas considerando que os relatórios são distintos entre si, existe uma sinalização de um modelo de dados colunar para atendimento dessa demanda. Sua atuação como analista é descrever esse modelo de modo a permitir o melhor desempenho possível das consultas. Sabe-se que temos as seguintes informações:

  - Vendas:
    **i.** Valor de uma venda. 
    **ii.** Nome do produto vendido. 
    **iii.** Data da venda. 
    **iv.** Filial. 
    
  - Compras:
    **v.** Valor de uma compra. 
    **vi.** Produto comprado. 
    **vii.** Nome do vendedor. 
    **viii.** Nome do comprador. 
    
  - Propagandas: 
    **ix.** Nome da campanha. 
    **x.** Data de início da campanha. 
    **xi.** Data de finalização da campanha. 
    **xii.** Público-alvo. 
    
  **Regras:**
    - Em vendas, os dados utilizados em conjunto são valor e nome do produto, bem como filial e data de venda.
    - Em compras, o valor da compra é exibido sempre junto com o nome do produto, bem como data da venda e comprador.
    - Em propagandas, é importante exibir nome da campanha e público alvo sempre juntos.