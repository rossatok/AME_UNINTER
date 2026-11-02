import streamlit as st
import streamlit.components.v1 as components
import uuid

# Gera o identificador único invisível assim que a página é aberta
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Configuração Básica da Página
st.set_page_config(
    page_title="Conhecendo a AME - Trabalho Acadêmico",
    page_icon="🧬",
    layout="wide"
)

# --- ESTILIZAÇÃO ---
st.markdown("""
<style>
    .main-title {
        color: #2e7d32;
        text-align: center;
        font-weight: bold;
    }
    .section-header {
        color: #1565c0;
        margin-top: 20px;
    }
    .highlight-box {
        background-color: #f1f8e9;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #8bc34a;
    }
</style>
""", unsafe_allow_html=True)


# --- TÍTULO PRINCIPAL ---
st.markdown("<h1 class='main-title'>Conhecendo a AME: Atrofia Muscular Espinhal</h1>", unsafe_allow_html=True)
st.markdown("---")


# --- SEÇÃO 1: O QUE É ---
st.markdown("<h2 class='section-header'>1. O que é a AME?</h2>", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.write("""
    A Atrofia Muscular Espinhal (AME) é uma doença **genética**, **rara**, **progressiva** e, se não tratada, **fatal**. 
    Ela afeta a capacidade do corpo de produzir uma proteína essencial para a sobrevivência dos neurônios motores, que são as células nervosas responsáveis por enviar sinais do cérebro para os músculos.

    Sem esses sinais, os músculos tornam-se fracos, atrofiados e param de funcionar. Isso impacta atividades básicas como:
    *   Andar;
    *   Engatinhar;
    *   Sentar-se;
    *   Engolir;
    *   Respirar.

    A AME afeta aproximadamente 1 em cada 10.000 nascidos vivos e é a principal causa genética de morte em bebês.
    """)

with col2:
    st.info("🧬 **Origem:** Mutação no gene SMN1.")


# --- SEÇÃO 2: OS TIPOS DE AME ---
st.markdown("<h2 class='section-header'>2. Os Tipos de AME</h2>", unsafe_allow_html=True)

st.write("A doença é classificada em cinco tipos (de 0 a 4) com base na idade de início dos sintomas e no maior marco motor alcançado:")

st.markdown("""
**Tipo 0**
* **Início:** Durante a gestação (fase pré-natal).
* **Marcos:** É a forma mais rara e grave de todas. Pode ser percebida ainda na gravidez pela diminuição dos movimentos do feto. O bebê já nasce com fraqueza muscular extrema e ausência de reflexos.
* **Riscos:** Insuficiência respiratória grave imediata ao nascer e dificuldades de deglutição. A expectativa de vida é muito reduzida sem suporte avançado de vida imediato.

**Tipo 1**
* **Início:** Antes dos 6 meses de idade.
* **Marcos:** É a forma mais comum. O bebê não consegue sentar sem apoio.
* **Riscos:** Rápida perda de força, alto risco de insuficiência respiratória e dificuldade para engolir. Exige suporte de vida imediato.

**Tipo 2**
* **Início:** Entre 6 e 18 meses.
* **Marcos:** A criança senta sem apoio, mas não consegue andar de forma independente.
* **Riscos:** Fraqueza progressiva nas pernas e braços, problemas ortopédicos (como escoliose grave) e complicações respiratórias.

**Tipo 3**
* **Início:** Após 18 meses (infância/adolescência).
* **Marcos:** Consegue andar de forma independente, mas pode perder essa habilidade com o passar dos anos.
* **Riscos:** Dificuldade para subir escadas, quedas frequentes e fadiga. A expectativa de vida é normal.

**Tipo 4**
* **Início:** Fase adulta (geralmente após os 30 anos).
* **Marcos:** Forma mais branda e rara. O paciente mantém a mobilidade ao longo da vida.
* **Riscos:** Fraqueza muscular leve a moderada e tremores. Não afeta a expectativa de vida nem a capacidade respiratória.
""")


# --- SEÇÃO 3: COMO É DESCOBERTA (DIAGNÓSTICO) ---
st.markdown("<h2 class='section-header'>3. Como diagnosticar a AME?</h2>", unsafe_allow_html=True)

st.write("""
O diagnóstico da AME geralmente segue dois caminhos: a observação de sintomas ou a triagem neonatal.
""")

with st.expander("👀 Observação de Sintomas Clínicos", expanded=True):
    st.write("""
    Em muitos casos, os pais ou pediatras notam que o bebê ou criança não está atingindo os marcos de desenvolvimento motor esperados (como segurar a cabeça, sentar sem apoio ou andar). 
    Os principais sinais incluem:
    - **Hipotonia:** Fraqueza muscular extrema ("bebê molinho").
    - **Arreflexia:** Ausência ou redução de reflexos.
    - **Tremores** nas mãos.
    - **Dificuldade respiratória** ou para mamar/engolir.

    Ao suspeitar desses sinais, o médico solicita um **exame genético de sangue** (como o teste de MLPA) para confirmar a ausência ou mutação no gene SMN1.
    """)

with st.expander("👶 Triagem Neonatal (Teste do Pezinho)"):
    st.write("""
    Esta é a forma mais eficaz de descoberta. O diagnóstico precoce pode ser feito através da **versão ampliada do Teste do Pezinho**. 
    Este exame identifica a doença dias após o nascimento, **antes mesmo de qualquer sintoma aparecer**. 

    No Brasil, a Lei nº 14.154/2021 incluiu a AME no Teste do Pezinho do SUS, mas a implementação ainda está ocorrendo de forma gradual pelos estados.
    """)


# --- SEÇÃO 4: IMPORTÂNCIA DO DIAGNÓSTICO PRECOCE ---
st.markdown("<h2 class='section-header'>4. A Importância Crítica do Diagnóstico Precoce</h2>", unsafe_allow_html=True)

st.markdown("""
<div class='highlight-box'>
    <strong>O tempo é neurônio.</strong> Na AME, a perda de neurônios motores é rápida, progressiva e irreversível. Uma vez que o neurônio morre, ele não pode ser recuperado.<br><br>
    Descobrir a doença **antes do início dos sintomas** permite que o tratamento comece imediatamente. Isso pode:<br>
    <ul>
        <li>Impedir a progressão da atrofia muscular;</li>
        <li>Garantir que a criança atinja marcos de desenvolvimento próximos aos de uma criança saudável (como andar);</li>
        <li>Salvar vidas e melhorar drasticamente a qualidade de vida.</li>
    </ul>
</div>
""", unsafe_allow_html=True)


# --- SEÇÃO 5: TRATAMENTOS DISPONÍVEIS ---
st.markdown("<h2 class='section-header'>5. Tratamentos Atuais e Estimativas de Custo</h2>", unsafe_allow_html=True)

st.write("""
Até poucos anos atrás, não existia tratamento para a AME, apenas cuidados paliativos. Hoje, existem terapias revolucionárias que, embora não curem a doença, mudam completamente o seu prognóstico. As principais disponíveis no mundo e no Brasil (algumas via SUS e outras via planos de saúde) são:
""")

tab1, tab2, tab3 = st.tabs(["Nusinersena", "Risdiplam", "Terapia Gênica"])

with tab1:
    st.subheader("Nusinersena (Spinraza®)")
    st.write("""
    É um medicamento injetado diretamente no fluido espinhal (via intratecal). Ele ajuda o corpo a produzir mais proteína funcional a partir de um gene "reserva" (SMN2). Requer doses de manutenção ao longo da vida.
    """)
    st.warning("💰 **Custo estimado:** Cerca de R$ 555 mil por frasco. O primeiro ano de tratamento (que exige 6 doses de ataque) pode ultrapassar a marca de R$ 3,3 milhões. A manutenção nos anos seguintes (3 doses anuais) fica em torno de R$ 1,67 milhão por ano.")

with tab2:
    st.subheader("Risdiplam (Evrysdi®)")
    st.write("""
    É o primeiro tratamento oral para a AME. É um xarope tomado diariamente em casa. Ele funciona de forma semelhante ao Nusinersena, aumentando a produção da proteína SMN funcional pelo gene SMN2.
    """)
    st.warning("💰 **Custo estimado:** O frasco custa em média de R$ 70 mil a R$ 114 mil. Como a dosagem é ajustada continuamente conforme o peso do paciente, o tratamento anual costuma ultrapassar R$ 1 milhão ao longo de toda a vida.")

with tab3:
    st.subheader("Onasemnogene Abeparvoveque (Zolgensma®)")
    st.write("""
    É conhecido como a "terapia gênica". É um tratamento de dose única, administrado por via intravenosa. Ele funciona entregando uma cópia funcional do gene SMN1 diretamente para as células do corpo, permitindo que elas produzam a proteína necessária. É indicado para crianças pequenas, dependendo de critérios médicos específicos.
    """)
    st.warning("💰 **Custo estimado:** Historicamente apelidado de 'remédio mais caro do mundo', o valor atual da sua dose única no Brasil costuma orbitar entre R$ 6 milhões e R$ 7 milhões por paciente, podendo variar de acordo com o câmbio e acordos de compra do Ministério da Saúde.")


# --- SEÇÃO 6: O ALTO CUSTO E A LUTA DAS FAMÍLIAS ---
st.markdown("<h2 class='section-header'>6. O Alto Custo e o Desafio do Acesso</h2>", unsafe_allow_html=True)

st.write("""
Apesar dos enormes avanços científicos, o acesso às terapias para a AME esbarra em um obstáculo gigantesco: **o valor financeiro**. 
Medicamentos para a doença, como a terapia gênica, já foram classificados entre os "remédios mais caros do mundo", podendo ultrapassar a marca de milhões de reais por paciente.
""")

col_a, col_b = st.columns(2)

with col_a:
    st.info("""
    🏥 **A Situação no SUS e Planos de Saúde**\n
    Embora o Sistema Único de Saúde (SUS) e os planos de saúde tenham incorporado tratamentos para a AME, a realidade é complexa. Existem critérios clínicos rígidos para que o paciente tenha direito a receber a medicação. 
    Muitas vezes, pacientes não se encaixam nesses protocolos específicos do governo ou sofrem com a burocracia e atrasos no fornecimento de um remédio que não pode ser interrompido.
    """)

with col_b:
    st.warning("""
    🤝 **A Mobilização das Famílias**\n
    Na AME, cada dia de espera significa a perda irreversível de neurônios motores. Devido a essa urgência e às dificuldades com o governo ou convênios, as famílias recorrem à justiça (judicialização). \n
    Para custear o tratamento inicial, advogados, e a caríssima infraestrutura de suporte à vida (respiradores, cadeiras adaptadas, fisioterapia diária e fonoaudiologia), as famílias criam **campanhas de arrecadação, vaquinhas online, rifas e pedágios solidários**. A rede de apoio da sociedade se torna fundamental pela sobrevivência da criança.
    """)


# --- SEÇÃO 7: REDES DE APOIO E HISTÓRIAS DE VIDA ---
st.markdown("---")
st.markdown("<h2 class='section-header' style='text-align: center;'>7. Conheça e Apoie: Redes e Histórias no Instagram</h2>", unsafe_allow_html=True)

st.write("""
Acompanhar o dia a dia de quem convive com a AME é a melhor forma de entender a doença e apoiar a causa. Abaixo, destacamos alguns perfis no Instagram de pacientes, campanhas e institutos de apoio:
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("💖 **Instituto INAME**")
    st.write("O Instituto Nacional da Atrofia Muscular Espinhal é uma das maiores associações brasileiras na luta pelos direitos e qualidade de vida das famílias.")
    st.markdown("[👉 Visitar @instituto_iname](https://www.instagram.com/instituto_iname/)", unsafe_allow_html=True)

with col2:
    st.markdown("👶 **Apoie Campanhas de Famílias**")
    st.write("Abaixo estão alguns perfis de crianças e famílias que lutam diariamente contra a AME. Siga, acompanhe a rotina e ajude a divulgar suas histórias:")
    st.markdown("""
    * [👉 @amerenally](https://www.instagram.com/amerenally/)
    * [👉 @ame.bianca](https://www.instagram.com/ame.bianca/)
    * [👉 @amebryanravi](https://www.instagram.com/amebryanravi/)
    * [👉 @amenicolas](https://www.instagram.com/amenicolas/)
    * [👉 @ame.maju](https://www.instagram.com/ame.maju/)
    * [👉 @ame.matheusvmotta](https://www.instagram.com/ame.matheusvmotta/)
    * [👉 @amelaurapires](https://www.instagram.com/amelaurapires/)
    * [👉 @familiathury](https://www.instagram.com/familiathury/)
    """)

with col3:
    st.markdown("👶 **Campanhas e Famílias**")
    st.write("Existem centenas de famílias de bebês recém-diagnosticados buscando apoio para os tratamentos. Você pode contatá-las através do Instagram e fazer sua contribuição.")


# --- HIPERLINK ---
st.markdown("---")
st.markdown("<h3 style='text-align: center; color: #7e57c2;'>Conheça Histórias de Vida</h3>", unsafe_allow_html=True)

col_l, col_c, col_r = st.columns([1, 2, 1])
with col_c:
    st.markdown(
        """
        <a href="https://www.instagram.com/explore/tags/atrofiamuscularespinhal/" target="_blank">
            <button style="
                width: 100%;
                background-color: #e1306c;
                color: white;
                padding: 15px;
                border: none;
                border-radius: 10px;
                font-size: 18px;
                font-weight: bold;
                cursor: pointer;
                transition: background-color 0.3s;">
                👉 Ver no Instagram perfis da comunidade AME
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

st.write("""
<p style='text-align: center; font-size: 12px; color: grey; margin-top: 10px;'>
O link acima direciona para a tag #atrofiamuscularespinhal no Instagram, onde você encontrará perfis de famílias, pacientes e associações que compartilham suas rotinas.
</p>
""", unsafe_allow_html=True)


# --- SEÇÃO 8: COMENTÁRIOS ---
from supabase import create_client

# Conecta ao Supabase usando as chaves secretas do Streamlit
@st.cache_resource
def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_connection()

st.header("8. Espaço do Leitor")
st.write("Deixe seu comentário, dúvida ou mensagem de apoio abaixo para registrar sua visita e ajudar no engajamento deste projeto acadêmico!")

nome = st.text_input("Seu Nome:")
mensagem = st.text_area("Escreva sua mensagem aqui:")

if st.button("Enviar Comentário"):
    if nome and mensagem:
        try:
            # Envia o comentário junto com a identificação da sessão gerada no topo do script
            supabase.table("comentarios_ame").insert({
                "nome": nome, 
                "mensagem": mensagem,
                "session_id": st.session_state.session_id
            }).execute()
            st.success("Comentário salvo com sucesso! Obrigado pelo apoio.")
        except Exception as e:
            st.error("Erro ao salvar comentário. Tente novamente.")
    else:
        st.warning("Por favor, preencha seu nome e a mensagem.")

st.markdown("### Comentários Registrados:")
try:
    resposta = supabase.table("comentarios_ame").select("*").order("created_at", desc=True).execute()
    comentarios_bd = resposta.data
    
    if comentarios_bd:
        for c in comentarios_bd:
            st.info(f"**{c['nome']}** comentou: {c['mensagem']}")
    else:
        st.write("Seja o primeiro a comentar!")
except Exception as e:
    st.error("Não foi possível carregar os comentários no momento.")



# --- RODAPÉ ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; font-size: 12px; color: grey;'>
        Trabalho Acadêmico - UNINTER | Curso GESTÃO DA TECNOLOGIA DA INFORMAÇÃO <br>
        Conteúdo meramente informativo. Sempre consulte profissionais de saúde.
    </div>
    """,
    unsafe_allow_html=True
)
