import streamlit as st

st.set_page_config(
    page_title="MBTI 포켓몬 추천 ⚡",
    page_icon="⚡",
    layout="centered"
)

pokemon_data = {
    "INTJ": {
        "pokemon": "뮤츠",
        "image": "https://img.pokemondb.net/artwork/large/mewtwo.jpg",
        "personality": "🧠 전략적이고 독립적인 성향! 항상 미래를 생각하며 계획을 세우는 타입이야."
    },
    "INTP": {
        "pokemon": "후딘",
        "image": "https://img.pokemondb.net/artwork/large/alakazam.jpg",
        "personality": "🔬 지적 호기심이 많고 분석을 좋아해. 새로운 지식을 탐구하는 걸 즐겨!"
    },
    "ENTJ": {
        "pokemon": "리자몽",
        "image": "https://img.pokemondb.net/artwork/large/charizard.jpg",
        "personality": "🔥 강한 리더십과 추진력을 가진 타입! 목표를 향해 적극적으로 나아가."
    },
    "ENTP": {
        "pokemon": "팬텀",
        "image": "https://img.pokemondb.net/artwork/large/gengar.jpg",
        "personality": "😏 창의적이고 재치가 넘쳐. 새로운 아이디어를 내는 걸 좋아해."
    },
    "INFJ": {
        "pokemon": "루기아",
        "image": "https://img.pokemondb.net/artwork/large/lugia.jpg",
        "personality": "🌊 깊은 통찰력과 배려심을 가진 이상주의자!"
    },
    "INFP": {
        "pokemon": "뮤",
        "image": "https://img.pokemondb.net/artwork/large/mew.jpg",
        "personality": "🌈 상상력이 풍부하고 순수한 감성을 가진 타입!"
    },
    "ENFJ": {
        "pokemon": "가디안",
        "image": "https://img.pokemondb.net/artwork/large/gardevoir.jpg",
        "personality": "💖 타인을 돕고 이끄는 데서 보람을 느껴."
    },
    "ENFP": {
        "pokemon": "피카츄",
        "image": "https://img.pokemondb.net/artwork/large/pikachu.jpg",
        "personality": "⚡ 밝고 활발하며 사람들과 어울리는 걸 좋아해!"
    },
    "ISTJ": {
        "pokemon": "강철톤",
        "image": "https://img.pokemondb.net/artwork/large/steelix.jpg",
        "personality": "🛡️ 책임감이 강하고 신뢰를 중요하게 생각해."
    },
    "ISFJ": {
        "pokemon": "해피너스",
        "image": "https://img.pokemondb.net/artwork/large/blissey.jpg",
        "personality": "🤗 따뜻하고 배려심이 많아 주변 사람들을 챙겨."
    },
    "ESTJ": {
        "pokemon": "보스로라",
        "image": "https://img.pokemondb.net/artwork/large/aggron.jpg",
        "personality": "🏆 체계적이고 조직을 이끄는 능력이 뛰어나."
    },
    "ESFJ": {
        "pokemon": "님피아",
        "image": "https://img.pokemondb.net/artwork/large/sylveon.jpg",
        "personality": "💕 친절하고 사교적이며 사람들과 함께할 때 행복해."
    },
    "ISTP": {
        "pokemon": "루카리오",
        "image": "https://img.pokemondb.net/artwork/large/lucario.jpg",
        "personality": "🥋 실용적이고 행동력이 뛰어나. 문제 해결에 강해!"
    },
    "ISFP": {
        "pokemon": "이브이",
        "image": "https://img.pokemondb.net/artwork/large/eevee.jpg",
        "personality": "🎨 자유롭고 감성적인 예술가 타입!"
    },
    "ESTP": {
        "pokemon": "번치코",
        "image": "https://img.pokemondb.net/artwork/large/blaziken.jpg",
        "personality": "⚔️ 도전을 즐기고 에너지가 넘치는 행동파!"
    },
    "ESFP": {
        "pokemon": "푸린",
        "image": "https://img.pokemondb.net/artwork/large/jigglypuff.jpg",
        "personality": "🎤 밝고 매력적이며 사람들의 관심을 받는 걸 좋아해!"
    }
}

st.title("⚡ MBTI 포켓몬 추천")
st.write("MBTI를 선택하면 어울리는 포켓몬과 성격을 알려줄게! 😊")

mbti = st.selectbox(
    "👇 MBTI를 선택해줘!",
    list(pokemon_data.keys())
)

if st.button("✨ 결과 보기"):
    data = pokemon_data[mbti]

    st.success(f"{mbti} 유형에게 어울리는 포켓몬!")

    st.image(
        data["image"],
        width=300,
        caption=data["pokemon"]
    )

    st.header(f"⚡ {data['pokemon']}")
    st.write(data["personality"])

    st.balloons()

st.markdown("---")
st.caption("💛 재미로 보는 MBTI 포켓몬 매칭이야!")
