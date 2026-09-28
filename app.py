import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="ImpactLab | Digital Growth",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# DATA
# =========================================================

SERVICES = {
    "SMM": {
        "icon": "◉",
        "title": "Social Media Management",
        "text": "Brendinizin sosial media hesablarını strategiya, kontent və davamlı inkişaf üzərindən idarə edirik.",
        "items": [
            "Instagram və TikTok strategiyası",
            "Kontent planlaşdırılması",
            "Səhifə idarəçiliyi",
            "Auditoriya analizi",
            "Aylıq inkişaf və nəticə analizi"
        ]
    },
    "Kreativ Kontent": {
        "icon": "✦",
        "title": "Creative Content",
        "text": "Brendinizin vizual kimliyinə uyğun diqqətçəkən postlar, Reels və digər sosial media kontentləri hazırlayırıq.",
        "items": [
            "Post dizaynları",
            "Reels ideyaları",
            "Video kontent",
            "Vizual konseptlər",
            "Kontent seriyaları"
        ]
    },
    "Digital Growth": {
        "icon": "↗",
        "title": "Digital Growth",
        "text": "Brendin rəqəmsal mühitdə daha düzgün mövqelənməsinə və böyüməsinə fokuslanırıq.",
        "items": [
            "Rəqəmsal inkişaf strategiyası",
            "Auditoriya böyüməsi",
            "Kontent performansının analizi",
            "Satış yönümlü kommunikasiya",
            "İnkişaf planı"
        ]
    },
    "Reklam": {
        "icon": "◎",
        "title": "Digital Advertising",
        "text": "Doğru auditoriyaya doğru mesajı çatdırmaq üçün rəqəmsal reklam strategiyaları qururuq.",
        "items": [
            "Reklam strategiyası",
            "Hədəf auditoriyanın seçilməsi",
            "Kampaniya planlaşdırılması",
            "Reklam kreativi",
            "Performans analizi"
        ]
    },
    "Strategiya": {
        "icon": "◇",
        "title": "Brand Strategy",
        "text": "Brendiniz üçün sosial mediada ardıcıl və məqsədli kommunikasiya sistemi formalaşdırırıq.",
        "items": [
            "Brend analizi",
            "Kontent strategiyası",
            "Kommunikasiya istiqaməti",
            "Rəqəmsal mövqeləndirmə",
            "Aylıq strategiya"
        ]
    },
    "Brend İnkişafı": {
        "icon": "✧",
        "title": "Brand Development",
        "text": "Brendinizin rəqəmsal görünüşünü daha güclü və tanınan hala gətirmək üçün kompleks yanaşma tətbiq edirik.",
        "items": [
            "Brend görünüşü",
            "Sosial media kimliyi",
            "Kontent istiqaməti",
            "Auditoriya ilə kommunikasiya",
            "Uzunmüddətli inkişaf"
        ]
    }
}

PORTFOLIO = [
    "WinKlaus",
    "OREL İnşaat",
    "Əsas Çözüm",
    "Fırat Elektrik",
    "Həyatla Üz-Üzə",
    "Mediport",
    "Sushi Style Baku"
]

RESULTS = [
    ("202B", "Baxış"),
    ("54.3B", "Baxış"),
    ("51.1B", "Baxış"),
    ("48.3B", "Baxış"),
    ("29.9B", "Baxış"),
    ("31.4B", "Baxış"),
    ("165B", "Baxış")
]

# =========================================================
# CSS + HTML
# =========================================================

st.html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body {
    font-family: 'Inter', sans-serif !important;
}

.stApp {
    background:
        radial-gradient(circle at 85% 5%, rgba(37,99,235,.20), transparent 30%),
        radial-gradient(circle at 10% 65%, rgba(59,130,246,.08), transparent 30%),
        #05070b;
    color: white;
}

header {
    display: none !important;
}

.block-container {
    max-width: 1250px;
    padding-top: 25px;
    padding-bottom: 80px;
}

/* NAV */

.nav {
    padding: 20px 26px;
    border: 1px solid rgba(255,255,255,.08);
    border-radius: 20px;
    background: rgba(255,255,255,.035);
    backdrop-filter: blur(20px);
    margin-bottom: 35px;
}

.logo {
    font-size: 26px;
    font-weight: 800;
    letter-spacing: -1px;
}

.logo-blue {
    color: #3b82f6;
}

.nav-info {
    color: #858d9a;
    font-size: 13px;
    margin-top: 5px;
}

/* =========================================================
   3D IMPACTLAB
   ========================================================= */

.impact-3d-wrapper {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    perspective: 1000px;
    padding: 35px 0 5px;
}

.impact-3d-scene {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    transform-style: preserve-3d;
}

.impact-glow {
    position: absolute;
    width: 420px;
    height: 150px;
    background: rgba(37,99,235,.28);
    filter: blur(65px);
    border-radius: 50%;
    z-index: 0;
}

.impact-3d {
    position: relative;
    z-index: 1;
    font-size: clamp(55px, 9vw, 120px);
    font-weight: 800;
    letter-spacing: -6px;
    line-height: 1;
    color: #ffffff;
    transform-style: preserve-3d;

    text-shadow:
        1px 1px 0 #dbeafe,
        2px 2px 0 #bfdbfe,
        3px 3px 0 #93c5fd,
        4px 4px 0 #60a5fa,
        5px 5px 0 #3b82f6,
        6px 6px 18px rgba(37,99,235,.50);

    animation: impactFloat 5s ease-in-out infinite;
}

.impact-3d .impact-blue {
    background: linear-gradient(
        135deg,
        #93c5fd 0%,
        #60a5fa 25%,
        #3b82f6 55%,
        #2563eb 100%
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    filter: drop-shadow(
        0 12px 22px rgba(37,99,235,.40)
    );
}

@keyframes impactFloat {

    0% {
        transform:
            rotateX(0deg)
            rotateY(0deg)
            translateY(0px);
    }

    25% {
        transform:
            rotateX(4deg)
            rotateY(-5deg)
            translateY(-7px);
    }

    50% {
        transform:
            rotateX(0deg)
            rotateY(5deg)
            translateY(0px);
    }

    75% {
        transform:
            rotateX(-4deg)
            rotateY(-3deg)
            translateY(7px);
    }

    100% {
        transform:
            rotateX(0deg)
            rotateY(0deg)
            translateY(0px);
    }
}

/* HERO */

.hero {
    text-align: center;
    padding: 65px 10px 80px;
}

.badge {
    display: inline-block;
    padding: 9px 17px;
    border-radius: 999px;
    border: 1px solid rgba(59,130,246,.35);
    background: rgba(59,130,246,.08);
    color: #93c5fd;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 1px;
    margin-bottom: 25px;
}

.hero-title {
    font-size: clamp(48px, 7vw, 90px);
    line-height: .98;
    letter-spacing: -5px;
    font-weight: 800;
    margin-bottom: 28px;
}

.blue-text {
    background: linear-gradient(90deg,#60a5fa,#3b82f6,#93c5fd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-text {
    max-width: 690px;
    margin: auto;
    color: #929aa8;
    font-size: 18px;
    line-height: 1.75;
}

/* SECTION */

.section {
    margin-top: 90px;
    margin-bottom: 25px;
}

.section-title {
    font-size: 40px;
    font-weight: 800;
    letter-spacing: -2px;
}

.section-description {
    color: #858d9a;
    margin-top: 8px;
    line-height: 1.6;
}

/* CARDS */

.card {
    min-height: 210px;
    padding: 28px;
    border-radius: 24px;
    border: 1px solid rgba(255,255,255,.08);
    background: linear-gradient(
        145deg,
        rgba(255,255,255,.055),
        rgba(255,255,255,.018)
    );
    backdrop-filter: blur(16px);
}

.card-icon {
    font-size: 30px;
    color: #60a5fa;
    margin-bottom: 18px;
}

.card-title {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 10px;
}

.card-text {
    color: #858d9a;
    line-height: 1.65;
    font-size: 14px;
}

/* STATS */

.stat-card {
    text-align: center;
    padding: 28px 15px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,.06);
    background: rgba(255,255,255,.025);
}

.stat-number {
    font-size: 42px;
    font-weight: 800;
    background: linear-gradient(90deg,#fff,#60a5fa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.stat-label {
    color: #858d9a;
    font-size: 13px;
    margin-top: 5px;
}

/* DETAIL */

.detail-box {
    padding: 40px;
    border-radius: 28px;
    border: 1px solid rgba(255,255,255,.08);
    background:
        radial-gradient(circle at 90% 10%,rgba(59,130,246,.12),transparent 30%),
        rgba(255,255,255,.025);
}

.detail-title {
    font-size: 48px;
    font-weight: 800;
    letter-spacing: -2px;
}

.detail-text {
    color: #929aa8;
    font-size: 17px;
    line-height: 1.8;
    max-width: 760px;
}

/* FOOTER */

.footer {
    margin-top: 100px;
    padding-top: 30px;
    border-top: 1px solid rgba(255,255,255,.07);
    text-align: center;
    color: #646b76;
}

/* STREAMLIT BUTTONS */

.stButton > button,
.stLinkButton > a {
    border-radius: 12px !important;
    border: 1px solid rgba(59,130,246,.35) !important;
    background: rgba(59,130,246,.10) !important;
    color: #dbeafe !important;
    font-weight: 600 !important;
}

.stButton > button:hover,
.stLinkButton > a:hover {
    border-color: #3b82f6 !important;
    background: rgba(59,130,246,.18) !important;
}

</style>
""")

# =========================================================
# FUNCTIONS
# =========================================================

def navbar():
    st.html("""
    <div class="nav">
        <div class="logo">
            Impact<span class="logo-blue">Lab</span>
        </div>
        <div class="nav-info">
            SMM • Digital Marketing • Growth
        </div>
    </div>
    """)


def footer():
    st.html("""
    <div class="footer">
        ImpactLab — Digital Growth Studio
        <br><br>
        © 2026 ImpactLab
    </div>
    """)


def whatsapp_button():
    st.link_button(
        "WhatsApp ilə əlaqə →",
        "https://wa.me/994993631350"
    )


# =========================================================
# HOME
# =========================================================

def home():

    navbar()

    # =====================================================
    # 3D IMPACTLAB
    # =====================================================

    st.html("""
    <div class="impact-3d-wrapper">

        <div class="impact-3d-scene">

            <div class="impact-glow"></div>

            <div class="impact-3d">
                Impact<span class="impact-blue">Lab</span>
            </div>

        </div>

    </div>
    """)

    st.html("""
    <div class="hero">

        <div class="badge">
            DIGITAL GROWTH STUDIO
        </div>

        <div class="hero-title">
            Brendinizi<br>
            <span class="blue-text">
                rəqəmsal dünyada
            </span><br>
            böyüdürük.
        </div>

        <div class="hero-text">
            Bizneslər üçün satış yönümlü SMM,
            kreativ kontent və rəqəmsal strategiyalar
            hazırlayırıq.
        </div>

    </div>
    """)

    whatsapp_button()

    # STATS
    st.html("""
    <div class="section">
        <div class="section-title">
            Impact in numbers
        </div>

        <div class="section-description">
            Real layihələrdən əldə edilmiş seçilmiş nəticələr.
        </div>
    </div>
    """)

    cols = st.columns(4)

    stats = [
        ("6+", "İllik SMM təcrübəsi"),
        ("165B", "Seçilmiş nəticə"),
        ("7+", "Portfolio layihəsi"),
        ("∞", "Yaradıcı imkan")
    ]

    for col, (number, label) in zip(cols, stats):

        with col:

            st.html(f"""
            <div class="stat-card">
                <div class="stat-number">
                    {number}
                </div>

                <div class="stat-label">
                    {label}
                </div>
            </div>
            """)

    # SERVICES
    st.html("""
    <div class="section">
        <div class="section-title">
            Nə edirik?
        </div>

        <div class="section-description">
            Brendiniz üçün strategiyadan kontentə qədər rəqəmsal həllər.
        </div>
    </div>
    """)

    service_names = list(SERVICES.keys())

    for row_start in range(0, len(service_names), 3):

        row = service_names[row_start:row_start + 3]
        cols = st.columns(3)

        for col, name in zip(cols, row):

            service = SERVICES[name]

            with col:

                st.html(f"""
                <div class="card">

                    <div class="card-icon">
                        {service["icon"]}
                    </div>

                    <div class="card-title">
                        {service["title"]}
                    </div>

                    <div class="card-text">
                        {service["text"]}
                    </div>

                </div>
                """)

                if st.button(
                    f"{name} →",
                    key=f"service_{name}",
                    use_container_width=True
                ):
                    st.session_state.page = f"service_{name}"
                    st.rerun()

    # PORTFOLIO
    st.html("""
    <div class="section">
        <div class="section-title">
            Portfolio
        </div>

        <div class="section-description">
            ImpactLab tərəfindən hazırlanmış seçilmiş layihələr.
        </div>
    </div>
    """)

    cols = st.columns(3)

    for col, project in zip(cols, PORTFOLIO[:3]):

        with col:

            st.html(f"""
            <div class="card">

                <div class="card-icon">
                    ◆
                </div>

                <div class="card-title">
                    {project}
                </div>

                <div class="card-text">
                    Social media & digital content
                </div>

            </div>
            """)

    if st.button(
        "Bütün portfolioya bax →",
        key="portfolio_button"
    ):
        st.session_state.page = "portfolio"
        st.rerun()

    # ABOUT
    st.html("""
    <div class="section">

        <div class="section-title">
            ImpactLab
        </div>

        <div class="section-description">
            Brendinizi rəqəmsal dünyada böyüdürük.
        </div>

    </div>

    <div class="detail-box">

        <div class="card-title">
            Nəticə yönümlü SMM yanaşması
        </div>

        <div class="detail-text">
            ImpactLab bizneslər üçün satış yönümlü SMM,
            kreativ kontent və rəqəmsal strategiyalar hazırlayır.
            6+ illik SMM təcrübəsi və beynəlxalq sertifikatlarla
            brendlərin sosial mediada daha güclü görünməsinə çalışırıq.
        </div>

    </div>
    """)

    # CONTACT
    st.html("""
    <div class="section">

        <div class="section-title">
            Layihəniz var?
        </div>

        <div class="section-description">
            Gəlin birlikdə rəqəmsal strategiyanızı quraq.
        </div>

    </div>
    """)

    whatsapp_button()

    st.link_button(
        "Instagram →",
        "https://www.instagram.com/impactlab.az/"
    )

    st.link_button(
        "TikTok →",
        "https://www.tiktok.com/@impactlab.az"
    )

    footer()


# =========================================================
# SERVICE PAGE
# =========================================================

def service_page(service_name):

    navbar()

    service = SERVICES[service_name]

    if st.button("← Ana səhifəyə qayıt", key="back_service"):
        st.session_state.page = "home"
        st.rerun()

    st.write("")

    st.html(f"""
    <div class="detail-box">

        <div class="card-icon">
            {service["icon"]}
        </div>

        <div class="detail-title">
            {service["title"]}
        </div>

        <br>

        <div class="detail-text">
            {service["text"]}
        </div>

    </div>
    """)

    st.html("""
    <div class="section">
        <div class="section-title">
            Nələr daxildir?
        </div>
    </div>
    """)

    for item in service["items"]:

        st.html(f"""
        <div class="card" style="min-height:0;margin-bottom:12px;">

            <div class="card-text">
                <span style="color:#60a5fa;font-size:18px;">
                    ✓
                </span>

                &nbsp;&nbsp;

                {item}
            </div>

        </div>
        """)

    st.html("""
    <div class="section">

        <div class="section-title">
            Hazırsınız?
        </div>

        <div class="section-description">
            Layihəniz haqqında danışaq.
        </div>

    </div>
    """)

    whatsapp_button()

    footer()


# =========================================================
# PORTFOLIO PAGE
# =========================================================

def portfolio_page():

    navbar()

    if st.button(
        "← Ana səhifəyə qayıt",
        key="back_portfolio"
    ):
        st.session_state.page = "home"
        st.rerun()

    st.html("""
    <div class="hero">

        <div class="badge">
            SELECTED WORK
        </div>

        <div class="hero-title">
            ImpactLab<br>
            <span class="blue-text">
                Portfolio
            </span>
        </div>

        <div class="hero-text">
            Müxtəlif sahələrdə həyata keçirilmiş
            seçilmiş rəqəmsal layihələr.
        </div>

    </div>
    """)

    for row_start in range(0, len(PORTFOLIO), 3):

        row = PORTFOLIO[row_start:row_start + 3]
        cols = st.columns(3)

        for col, project in zip(cols, row):

            with col:

                st.html(f"""
                <div class="card">

                    <div class="card-icon">
                        ◆
                    </div>

                    <div class="card-title">
                        {project}
                    </div>

                    <div class="card-text">
                        SMM • Content • Digital
                    </div>

                </div>
                """)

    st.html("""
    <div class="section">

        <div class="section-title">
            Nəticələr
        </div>

    </div>
    """)

    cols = st.columns(4)

    for index, (number, label) in enumerate(RESULTS):

        with cols[index % 4]:

            st.html(f"""
            <div class="stat-card" style="margin-bottom:20px;">

                <div class="stat-number">
                    {number}
                </div>

                <div class="stat-label">
                    {label}
                </div>

            </div>
            """)

    whatsapp_button()

    footer()


# =========================================================
# ROUTER
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

page = st.session_state.page

if page == "home":

    home()

elif page == "portfolio":

    portfolio_page()

elif page.startswith("service_"):

    service_name = page.replace("service_", "", 1)
    if service_name in SERVICES:
        service_page(service_name)

    else:
        st.session_state.page = "home"
        st.rerun()