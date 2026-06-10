import streamlit as st

st.set_page_config(
    page_title="MBTI 포켓몬 추천 ⚡",
    page_icon="⚡"
)

pokemon_data = {
    "INTJ": {
        "pokemon": "뮤츠",
        "image": "https://img.pokemondb.net/artwork/large/mewtwo.jpg",
        "personality": "🧠 전략적이고 독립적인 성향! 항상 미래를 생각하며 계획을 세우는 타입이야."
    },

    "ENFP": {
        "pokemon": "피카츄",
        "image": "https://img.pokemondb.net/artwork/large/pikachu.jpg",
        "personality": "⚡ 밝고 활발하며 사람들과 어울리는 걸 좋아해!"
    },

    "ISTP": {
        "pokemon": "루카리오",
        "image": "https://img.pokemondb.net/artwork/large/lucario.jpg",
        "personality": "🥋 실용적이고 행동력이 뛰어나. 문제 해결에 강해!"
    }
}

st.title("⚡ MBTI 포켓몬 추천")

mbti = st.selectbox(
    "👇 MBTI를 선택해줘!",
    list(pokemon_data.keys())
)

if st.button("✨ 결과 보기"):

    data = pokemon_data[mbti]

    st.success(f"{mbti} 유형에게 어울리는 포켓몬!")

    st.image(
        data["image"],
        width=350,
        caption=data["pokemon"]
    )

    st.header(f"⚡ {data['pokemon']}")
    st.write(data["personality"])

    st.balloons()
