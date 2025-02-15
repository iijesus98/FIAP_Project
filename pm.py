import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Analisando dados com a Associação Passos Mágicos", layout="wide")

# Definição do estilo CSS para os títulos
st.markdown("""
    <style>
        .titulo {
            font-size: 30px;
            font-weight: bold;
            text-align: center;
            color: #C0A48E;
        }
        .subtitulo {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            color: #C0A48E;
        }
    </style>
""", unsafe_allow_html=True)

# Exibir somente o menu 
st.sidebar.title("Menu")
opcao = st.sidebar.radio("", ("Introdução", "Insights", "Dashboard"))

# Exibe conteúdo conforme a opção escolhida
if opcao == "Introdução":
    st.markdown('<p class="titulo">Sobre a Associação</p>', unsafe_allow_html=True)
    st.write("""
        A Associação Passos Mágicos tem uma trajetória de 31 anos dedicada à transformação da vida de crianças e jovens de baixa renda, 
        oferecendo oportunidades que ampliam seu acesso à educação e ao desenvolvimento pessoal. 
        Por meio de programas estruturados, a instituição auxilia no fortalecimento da autoestima, na construção de um futuro mais promissor 
        e na inserção desses jovens em ambientes que antes pareciam inacessíveis.

        Iniciativas como as da Passos Mágicos são essenciais para reduzir desigualdades e criar um impacto positivo e duradouro na sociedade. 
        Ao investir no potencial de crianças e jovens, a instituição não apenas muda histórias individuais, mas também contribui para o desenvolvimento social e econômico, 
        promovendo um ciclo virtuoso de oportunidades e transformação.
    """)

    # Centraliza a imagem usando colunas
    cols = st.columns(3)
    with cols[1]:
        st.image(r"images.png", width=600)

    st.markdown('<p class="titulo">Sobre Nós</p>', unsafe_allow_html=True)
    st.write("""
        Somos alunos da FIAP e, neste último projeto, buscamos, por meio da coleta e análise de dados, evidenciar o impacto positivo que esta ONG tem gerado nas comunidades onde atua. 
        Além disso, queremos destacar o poder dos dados como ferramenta essencial para embasar decisões estratégicas, especialmente no contexto da educação, 
        demonstrando como a análise inteligente das informações pode impulsionar iniciativas sociais e transformar realidades.
    """)

elif opcao == "Insights":
    st.markdown('<p class="titulo">Analisando Dados com Passos Mágicos</p>', unsafe_allow_html=True)

    # Subtítulo
    st.markdown('<p class="subtitulo">Perfil dos Alunos</p>', unsafe_allow_html=True)

    st.write("""
    Entre os anos de 2022 e 2024, a Passos Mágicos teve 1.586 alunos matriculados, dos quais 132 foram bolsistas. 
    A média de idade dos alunos no período foi de 14 anos. A maioria dos alunos possuía 13 anos de idade quando matriculado. 
    Entre a entrada e saída de alunos em cada ano, o volume variou de 860 em 2022 a 1.054 em 2024, com um aumento de 22,6% no número de matrículas no período. 
    A análise do número de alunos por ano de ingresso mostra que há uma parcela de alunos que se mantém vinculada à Passos Mágicos por até 9 anos.
    """)

    # Centralizando a primeira imagem
    cols = st.columns(3)
    with cols[1]:
        st.image(r"Ano Ingresso.png", width=600)

    st.write("""
    A maior parte dos alunos vem de escolas públicas, chegando a mais de 89% dos alunos matriculados no período. 
    Aproximadamente 9% vêm da Rede Decisão, e uma minoria de alunos vem de instituições privadas.
    """)

    # Centralizando a segunda imagem
    cols = st.columns(3)
    with cols[1]:
        st.image(r"Tipo de Inst.png", width=600)

    st.write("""
    Todos os alunos bolsistas do período pertenciam à Rede Pública de ensino. Do total de alunos do período, cerca de 15% teve indicação para recebimento de bolsa de estudos:
    """)

    # Centralizando a terceira imagem
    cols = st.columns(3)
    with cols[1]:
        st.image(r"Indicado Bolsa.png", width=600)

    st.write("""
    No que se refere ao sexo dos alunos, há uma leve predominância de alunas do sexo feminino, que representam 53,6% do corpo discente da instituição e 50% dos bolsistas no período.
    """)

    st.markdown('<p class="subtitulo">Análise de Desempenho: Avaliação das Notas</p>', unsafe_allow_html=True)
    st.write("""
    As notas médias dos alunos nas disciplinas no período ficaram entre 6,16 pontos e 6,43 pontos. O pior desempenho médio dos alunos foi na disciplina de Matemática (6,16), seguido pela disciplina de Inglês (6,29). O melhor desempenho médio se deu na disciplina de Português, com 6,43 pontos em média.
    """)

    # Centralizando a  imagem
    cols = st.columns(3)
    with cols[1]:
        st.image(r"Média.png", width=600)
        
    st.write("""
    As notas médias dos alunos bolsistas são, de modo geral, superiores que as dos demais alunos, com médias de 6,73, 6,79 e 6,42 nas disciplinas de Português, Matemática e Inglês, respectivamente. Ainda no que diz respeito ao desempenho dos alunos, nota-se um melhor desempenho médio das alunas do sexo feminino. Este fator pode indicar a necessidade de estabelecer ações para melhorar o engajamento e a aprendizagem de alunos com foco no alunos do sexo masculino.
    """)
    cols = st.columns(3)
    with cols[1]:
        st.image(r"Média_Gen.png", width=600)


    st.write("""
    O ano com maior queda no desempenho médio dos alunos nas disciplinas foi o de 2022, com resultados abaixo de 6 pontos em duas disciplinas: Matemática e Inglês. Aquele ano apresentou um pico de ingresso de alunos do sexo masculino, o que pode ter contribuído para a baixa no desempenho geral, tanto por fatores relacionados ao sexo dos alunos matriculados, como também pela própria condição de ingressante, que por si só pode significar uma maior dificuldade do aluno, ainda em adaptação à organização.
    """)
    cols = st.columns(3)
    with cols[1]:
        st.image(r"Ev_Medias_Ano.png", width=600)
    
    st.write("""
    Pesquisas sugerem que diferenças no desenvolvimento entre os sexos podem influenciar no desempenho de habilidades específicas, refletindo no desempenho escolar. Além disso, estereótipos de gênero podem afetar a autoconfiança e o interesse em certas áreas, especialmente entre alunos do sexo masculino. Outros fatores relacionados à diferença na socialização de meninos e meninas podem implicar em traços de comportamento que desfavorecem o desempenho escolar. Essas relações não são absolutas, no entanto, são amplamente observadas em estudos na área pedagógica e educacional. Ações voltadas para minimizar os efeitos desses fatores sobre os alunos e a adoção de métodos de ensino pensados para esta finalidade podem contribuir para mitigar essas diferenças.
    Ao avaliar o perfil das médias de nota por idade, é possível verificar uma tendência à relação inversa entre médias de notas e a idade, com uma queda progressiva no desempenho médio das notas, especialmente entre os 12 e 17 anos de idade. O desempenho de alunos mais velhos passa a se sobressair positivamente nas faixas de 22 e 24 anos, contudo, vale destacar que os alunos adultos, com mais de 18 anos, são minoria dentre o público da Passos Mágicos, equivalente a menos de 9% do universo.

    """)
    cols = st.columns(3)
    with cols[1]:
        st.image(r"Medias_Por_Idade.png", width=600)

    st.write("""
    Ao observar o perfil de defasagem dos alunos, verifica-se que, apesar das diferenças de desempenho entre meninos e meninas, a distribuição dos alunos entre anos de defasagem segue comportamentos semelhantes para ambos os públicos.
    """)

    cols = st.columns(3)
    with cols[1]:
        st.image(r"Defasagem.png", width=600)

    st.write("""
    De modo geral, é observada uma tendência de redução gradual nos níveis de defasagem negativos aos longo dos anos, com uma consequente redução na distorção idade-série, e aumento progressivo na adequação do nível dos alunos, visto no aumento do percentual de alunos com defasagem zero de 28,72% em 2022 para 39,94% em 2024. Esse comportamento dos dados evidencia o sucesso da instituição em melhorar o desempenho e adequar os níveis educacionais dos alunos:
    """)

    cols = st.columns(3)
    with cols[1]:
        st.image(r"Desafagem Escolar .png", width=600)
    

    st.write("""
    Do mesmo modo, pode ser observada uma melhora progressiva nos índices educacionais dos alunos, refletida no Índice do Desenvolvimento Educacional (INDE) do aluno, que consiste em uma métrica do processo avaliativo geral do aluno, dada pela ponderação dos indicadores: Indicador de Ponto de Virada (IPV); Indicador de Adequação ao Nível (IAN); Indicador de Auto Avaliação (IAA); Indicador de Engajamento (IEG); Indicador Psicossocial (IPS); Indicador de Aprendizagem (IDA); e Indicador Psicopedagógico (IPP).
    A partir das médias do INDE, os alunos recebem uma classificação relacionada a uma Pedra: Ágata, Ametista, Quartzo ou Topázio – sendo a última a mais bem avaliada. As classificações se dão de acordo com as equivalências: Quartzo – 2,405 a 5,506; Ágata – 5,506 a 6,868; Ametista – 6,868 a 8,230; Topázio – 8,230 a 9,294.
    """)

    cols = st.columns(3)
    with cols[1]:
        st.image(r"Pedra.png", width=600)

    st.write("""
    
    A distribuição das classificações dos alunos por tipo de Pedra ao longo dos anos demonstra o sucesso no desenvolvimento dos alunos, com um aumento de 250% no total de alunos com a Pedra Topázio. Nota-se que, ao longo dos anos, os volumes de alunos na classe de Pedra Ametista apresentaram crescimento de cerca de 12%, comportamento diferente do observado nos volumes das demais classificações. Esse comportamento dos dados pode sinalizar uma maior dificuldade dos alunos em superar e vencer o estágio em questão, quando comparada com a transição para os demais estágios. Isso sinaliza para uma necessidade de maiores investigações sobre os fatores críticos que podem determinar a limitação do desenvolvimento dos alunos neste estágio.

    """)

    # Subtítulo
    st.markdown('<p class="subtitulo">Análise de Desempenho: Avaliações Comportamentais</p>', unsafe_allow_html=True)
    
    st.write("""
O desempenho educacional dos alunos da Passos Mágicos é avaliado não apenas por suas notas acadêmicas, 
mas também por indicadores comportamentais que refletem seu engajamento, adaptação e evolução ao longo do tempo. 
Nesta seção, analisamos os principais padrões e fatores que influenciam esses indicadores. 
""")
    st.markdown("### **Indicadores Educacionais e Padrões Observados**")
    st.write("Os alunos são avaliados por meio de sete principais indicadores comportamentais:")

    # Lista de indicadores
    st.markdown("""
    - **Índice de Desenvolvimento Educacional (INDE):** indicador geral que pondera os demais índices.
    - **Indicador de Ponto de Virada (IPV):** avalia mudanças significativas na trajetória escolar.
    - **Indicador de Adequação ao Nível (IAN):** mede a conformidade do aluno ao nível de ensino esperado.
    - **Indicador de Autoavaliação (IAA):** reflete a percepção do aluno sobre seu próprio aprendizado.
    - **Indicador de Engajamento (IEG):** avalia o nível de envolvimento e participação nos estudos.
    - **Indicador Psicossocial (IPS):** analisa fatores emocionais e sociais que influenciam o desempenho.
    - **Indicador de Aprendizagem (IDA):** mede a evolução acadêmica ao longo do tempo.
    """)

    st.write("""
    A análise dos dados mostra que houve uma melhora progressiva nesses índices ao longo dos anos, 
    indicando que os alunos estão se desenvolvendo não apenas academicamente, mas também em aspectos comportamentais. 
    O **Índice de Desenvolvimento Educacional (INDE)** apresentou crescimento contínuo, refletindo o impacto positivo das estratégias adotadas pela instituição.
    """)

    # Fatores de Influência no Desempenho Comportamental
    st.markdown("### **Fatores de Influência no Desempenho Comportamental**")

    st.markdown("""
    1. **Diferença de Engajamento entre Gêneros:** Alunos do sexo feminino apresentam maiores índices de engajamento (**IEG**) e notas médias superiores. 
       Essa diferença pode estar relacionada a fatores pedagógicos e comportamentais, sugerindo a necessidade de estratégias para aumentar a motivação dos alunos do sexo masculino.
    2. **Impacto do Perfil Escolar na Progressão Acadêmica:** Alunos bolsistas apresentam desempenho superior aos demais, sugerindo que os critérios de concessão de bolsas são eficazes na seleção de alunos com alto potencial acadêmico. Esse resultado reforça a importância da manutenção e possível ampliação do programa de bolsas.
    3. **Dificuldade de Progressão na Pedra Ametista:** A classificação dos alunos em categorias (Pedra Ágata, Ametista, Quartzo e Topázio) mostra que a transição da **Pedra Ametista** para os níveis superiores tem sido mais lenta. Esse padrão indica que alunos neste estágio podem enfrentar desafios adicionais que dificultam sua progressão, sugerindo a necessidade de um acompanhamento mais próximo e estratégias direcionadas para apoiar essa transição.
    4. **Correlação entre Engajamento e Desempenho:** Os alunos com maior **Índice de Engajamento (IEG)** apresentam, em média, melhores resultados acadêmicos. Esse fator reforça a importância de iniciativas que incentivem a participação ativa dos estudantes, como metodologias interativas e acompanhamento pedagógico personalizado.
    """)

    # Insights e Conclusões
    st.markdown("### **Insights e Conclusões**")
    st.markdown("""
    - O **melhor desempenho dos alunos bolsistas** em comparação aos que não receberam bolsa no período sugere efetividade nos critérios de concessão e manutenção de bolsas.
    - Há uma diferença de desempenho entre alunos do sexo masculino e feminino que sugere a necessidade de investimento em **ações voltadas para manutenção da motivação e engajamento de alunos do sexo masculino**.
    - Existe uma tendência à queda de desempenho com a progressão da idade dos alunos, o que ressalta a importância de **ações em prol do engajamento e retenção dos alunos**.
    - A Passos Mágicos tem tido sucesso em **melhorar o desempenho escolar dos alunos**, ao elevar as notas médias dos alunos entre 2022 e 2023, bem como os seus indicadores educacionais.
    - O nível relacionado à **Pedra Ametista** parece ser um ponto crítico para os alunos, sugerindo a necessidade de acompanhamento profundo dos alunos durante este período. O aumento no volume de alunos neste estágio ao longo do tempo sugere que existem alunos que ficam represados neste nível.
    - Além do desempenho acadêmico, o progresso dos alunos da Passos Mágicos é influenciado por fatores comportamentais e socioemocionais, que impactam diretamente a aprendizagem e a adaptação ao ambiente escolar.
    - O estudo desses índices permite identificar padrões de comportamento que influenciam a trajetória escolar dos alunos, destacando desafios e oportunidades para fortalecer as estratégias pedagógicas da instituição.
    - A evolução dos indicadores educacionais e comportamentais ao longo dos anos demonstra uma progressiva melhora na adaptação dos alunos ao ambiente escolar. O **Índice de Desenvolvimento Educacional (INDE)** teve crescimento contínuo, refletindo o impacto positivo das estratégias adotadas pela instituição.
    - Os alunos com maior **Índice de Engajamento (IEG)** apresentam, em média, melhores resultados acadêmicos. Isso reforça a necessidade de incentivar metodologias que estimulem a participação ativa dos estudantes, como atividades interativas e acompanhamento pedagógico personalizado.
    - A análise dos indicadores de aprendizagem sugere que a transição de alunos da **Pedra Ametista** para níveis superiores pode ser um ponto de atenção. A dificuldade de progressão nessa etapa pode estar relacionada a desafios específicos que demandam estratégias pedagógicas direcionadas.
    - Os alunos bolsistas, além de apresentarem um desempenho acadêmico superior, também possuem índices comportamentais mais elevados. Isso indica que a concessão de bolsas não só facilita o acesso à educação, mas também contribui para um maior engajamento e comprometimento dos alunos com o aprendizado.
    """)

# Seção do Dashboard, controlada pela variável opcao
if opcao == "Dashboard":
    st.markdown('<p class="titulo">Dashboard</p>', unsafe_allow_html=True)
    # Integrando o Power BI com iframe
    cols = st.columns(3)
    with cols[1]:
        components.iframe("https://app.powerbi.com/view?r=eyJrIjoiNzc0NjI1OWItYzkxMS00NmNkLWFmNmQtYjY2Yzg3OWI2NjNlIiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9", width=800, height=600)


