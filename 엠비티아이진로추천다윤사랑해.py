import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 추천 🌟",
    page_icon="🚀",
    layout="centered"
)

st.title("🌟 MBTI 기반 진로 추천")
st.write("MBTI를 선택하면 너에게 어울릴 만한 진로를 추천해줄게! 😎")

career_data = {
    "INTJ": [
        {
            "career": "🧠 데이터 과학자",
            "major": "데이터사이언스학과, 통계학과, 컴퓨터공학과",
            "personality": "논리적으로 생각하고 문제를 분석하는 걸 좋아하는 사람에게 잘 맞아!"
        },
        {
            "career": "🏗️ 연구원",
            "major": "자연과학계열, 공학계열",
            "personality": "새로운 지식을 탐구하고 깊게 파고드는 성향에 적합해."
        }
    ],
    "INTP": [
        {
            "career": "💻 소프트웨어 개발자",
            "major": "컴퓨터공학과, 소프트웨어학과",
            "personality": "창의적으로 문제를 해결하고 새로운 아이디어를 생각하는 사람에게 추천!"
        },
        {
            "career": "🔬 과학자",
            "major": "물리학과, 화학과, 생명과학과",
            "personality": "호기심이 많고 탐구를 즐기는 성격과 잘 어울려."
        }
    ],
    "ENTJ": [
        {
            "career": "📈 경영 컨설턴트",
            "major": "경영학과, 경제학과",
            "personality": "목표를 세우고 사람들을 이끄는 능력이 뛰어난 사람에게 적합!"
        },
        {
            "career": "🚀 기업가",
            "major": "경영학과, 창업학과",
            "personality": "도전 정신이 강하고 리더십이 있는 사람에게 잘 맞아."
        }
    ],
    "ENTP": [
        {
            "career": "📢 마케팅 기획자",
            "major": "광고홍보학과, 경영학과",
            "personality": "새로운 아이디어를 내고 사람들과 소통하는 걸 좋아하는 사람!"
        },
        {
            "career": "🎙️ 방송 기획자",
            "major": "미디어커뮤니케이션학과",
            "personality": "창의력과 순발력이 뛰어난 성향에 추천해."
        }
    ],
    "INFJ": [
        {
            "career": "🩺 상담심리사",
            "major": "심리학과, 상담학과",
            "personality": "공감 능력이 높고 사람을 돕고 싶어 하는 사람에게 잘 맞아."
        },
        {
            "career": "📚 교사",
            "major": "교육학과, 각 교과교육과",
            "personality": "학생들의 성장을 돕는 일에 보람을 느끼는 사람에게 추천!"
        }
    ],
    "INFP": [
        {
            "career": "✍️ 작가",
            "major": "국어국문학과, 문예창작학과",
            "personality": "상상력이 풍부하고 감성이 깊은 사람에게 적합해."
        },
        {
            "career": "🎨 디자이너",
            "major": "시각디자인학과, 산업디자인학과",
            "personality": "창의성을 표현하는 걸 좋아하는 사람에게 추천!"
        }
    ],
    "ENFJ": [
        {
            "career": "🎓 진로상담사",
            "major": "교육학과, 상담학과",
            "personality": "사람을 이끌고 응원하는 걸 좋아하는 사람에게 적합!"
        },
        {
            "career": "🤝 인사담당자(HR)",
            "major": "경영학과, 심리학과",
            "personality": "사람을 이해하고 조직을 돕는 데 관심이 많은 사람에게 추천!"
        }
    ],
    "ENFP": [
        {
            "career": "📺 콘텐츠 크리에이터",
            "major": "미디어학과, 영상학과",
            "personality": "에너지가 넘치고 새로운 도전을 좋아하는 사람!"
        },
        {
            "career": "🎤 광고 기획자",
            "major": "광고홍보학과",
            "personality": "아이디어가 많고 표현력이 좋은 성격에 잘 맞아."
        }
    ],
    "ISTJ": [
        {
            "career": "⚖️ 공무원",
            "major": "행정학과, 법학과",
            "personality": "책임감이 강하고 꼼꼼한 사람에게 적합!"
        },
        {
            "career": "💰 회계사",
            "major": "회계학과, 경영학과",
            "personality": "정확성과 체계성을 중요하게 생각하는 사람에게 추천!"
        }
    ],
    "ISFJ": [
        {
            "career": "🏥 간호사",
            "major": "간호학과",
            "personality": "배려심이 많고 책임감이 강한 사람에게 잘 맞아."
        },
        {
            "career": "👩‍🏫 초등교사",
            "major": "초등교육과",
            "personality": "사람을 돕고 돌보는 것을 좋아하는 성향에 추천!"
        }
    ],
    "ESTJ": [
        {
            "career": "🏢 행정 관리자",
            "major": "행정학과, 경영학과",
            "personality": "조직을 운영하고 계획하는 능력이 뛰어난 사람!"
        },
        {
            "career": "👮 경찰관",
            "major": "경찰행정학과",
            "personality": "규칙을 중요하게 생각하고 책임감이 강한 사람에게 적합!"
        }
    ],
    "ESFJ": [
        {
            "career": "💉 보건교육사",
            "major": "보건학과, 간호학과",
            "personality": "사람들과 협력하고 돕는 걸 좋아하는 사람!"
        },
        {
            "career": "🎉 행사 기획자",
            "major": "관광학과, 이벤트학과",
            "personality": "사교성이 좋고 분위기를 만드는 걸 좋아하는 성향에 추천!"
        }
    ],
    "ISTP": [
        {
            "career": "🔧 기계 엔지니어",
            "major": "기계공학과",
            "personality": "직접 만들고 고치는 걸 좋아하는 사람에게 적합!"
        },
        {
            "career": "🚁 드론 전문가",
            "major": "항공학과, 전자공학과",
            "personality": "실용적이고 문제 해결 능력이 뛰어난 사람에게 추천!"
        }
    ],
    "ISFP": [
        {
            "career": "📸 사진작가",
            "major": "사진영상학과",
            "personality": "감각적이고 자유로운 표현을 좋아하는 사람!"
        },
        {
            "career": "🎵 음악 프로듀서",
            "major": "실용음악과",
            "personality": "예술적 감각과 창의성이 풍부한 사람에게 적합!"
        }
    ],
    "ESTP": [
        {
            "career": "🏆 스포츠 마케터",
            "major": "스포츠산업학과, 경영학과",
            "personality": "활동적이고 도전을 즐기는 사람에게 추천!"
        },
        {
            "career": "📺 방송 리포터",
            "major": "미디어커뮤니케이션학과",
            "personality": "순발력이 좋고 사람들과 소통하는 걸 좋아하는 성향에 적합!"
        }
    ],
    "ESFP": [
        {
            "career": "🎬 배우",
            "major": "연극영화과",
            "personality": "사람들 앞에서 표현하는 걸 좋아하는 사람!"
        },
        {
            "career": "🎤 아나운서",
            "major": "언론정보학과, 미디어학과",
            "personality": "밝고 사교적인 성격에 잘 어울려."
        }
    ]
}

mbti = st.selectbox(
    "👇 너의 MBTI를 선택해줘!",
    list(career_data.keys())
)

if st.button("✨ 진로 추천 받기"):
    st.success(f"{mbti} 유형에게 어울리는 진로를 소개할게!")

    for idx, item in enumerate(career_data[mbti], start=1):
        st.markdown(f"## {idx}. {item['career']}")
        st.write(f"📚 **추천 학과:** {item['major']}")
        st.write(f"💡 **어울리는 성격:** {item['personality']}")
        st.divider()

    st.balloons()

st.markdown("---")
st.caption("💖 MBTI는 참고용일 뿐! 가장 중요한 건 네가 좋아하는 것과 잘하는 것이야 😊")
