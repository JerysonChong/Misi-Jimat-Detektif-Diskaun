import random
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Misi Jimat • Detektif Diskaun",page_icon="🛍️",layout="wide",initial_sidebar_state="expanded")

# ----------- Identiti visual: gaya kartun ceria terinspirasi Shinchan -----------
st.markdown('''<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');
html, body, [class*="css"], [data-testid="stApp"] { font-family: 'Nunito', sans-serif; }
.stApp { background:linear-gradient(155deg,#fff7d6 0%,#f8e7fd 52%,#eaf8ff 100%);color:#2b2444; }
[data-testid="stSidebar"] { background:#fff3bd; }
[data-testid="stSidebar"] * { color:#2b2444!important; }
h1,h2,h3,p,label {color:#2b2444!important;}
h1 {font-weight:900!important;letter-spacing:-1px;}
[data-testid="stMetric"] { background:white; border:3px solid #2b2444; border-radius:19px; padding:14px; box-shadow:5px 5px 0 #2b2444; }
[data-testid="stMetricLabel"], [data-testid="stMetricValue"] {color:#2b2444!important;}
.stButton>button { background:#ff6d70!important;color:#20172c!important;border:3px solid #2b2444!important; border-radius:15px!important; font-weight:900!important;box-shadow:4px 4px 0 #2b2444; }
.stButton>button:hover { transform:translateY(-2px); background:#ffcb49!important; }
[data-testid="stAlert"] {border-radius:16px;}
.card {background:#fff;border:3px solid #2b2444;border-radius:20px;padding:20px;margin:12px 0;box-shadow:5px 5px 0 #2b2444;}
.hero {background:#ffdc55;border:4px solid #2b2444;border-radius:25px;padding:19px 25px;margin-bottom:20px;box-shadow:8px 8px 0 #2b2444;}
.hero h1 {font-size:2.5rem;margin:0;color:#2b2444!important;}
.hero p {font-weight:800;margin:6px 0 0;}
.chip {display:inline-block;background:#fff;border:2px solid #2b2444;border-radius:30px;padding:5px 12px;font-weight:900;margin-right:7px;margin-top:10px;}
.stTabs [data-baseweb="tab"] {font-weight:800;}
</style>''',unsafe_allow_html=True)

# Kartun SVG ringkas asli, bukan imej rasmi atau aset berhak cipta.
character = '''<svg width="150" height="156" viewBox="0 0 150 156" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Watak detektif kartun berbaju merah">
<ellipse cx="74" cy="143" rx="53" ry="8" fill="#dba844" opacity=".4"/>
<path d="M48 101h52l9 40H40z" fill="#ed5256" stroke="#2b2444" stroke-width="4"/>
<path d="M54 137h17v11H50zM83 137h17v11H80z" fill="#f6c33d" stroke="#2b2444" stroke-width="3"/>
<path d="M30 111l-12 16m106-16 10 13" stroke="#f4bd90" stroke-width="12" stroke-linecap="round"/>
<ellipse cx="75" cy="62" rx="51" ry="49" fill="#f9c399" stroke="#2b2444" stroke-width="4"/>
<path d="M27 43Q36 1 78 12Q119 7 124 43Q105 29 84 27Q56 25 27 43Z" fill="#252031"/>
<path d="M40 54Q51 45 61 53M88 53Q100 45 111 53" stroke="#24202b" stroke-width="9" fill="none" stroke-linecap="round"/>
<circle cx="53" cy="69" r="4" fill="#24202b"/><circle cx="101" cy="69" r="4" fill="#24202b"/>
<path d="M66 88Q77 98 91 85" stroke="#9d454b" stroke-width="4" fill="none" stroke-linecap="round"/>
<circle cx="36" cy="83" r="8" fill="#f29e91" opacity=".6"/><circle cx="114" cy="83" r="8" fill="#f29e91" opacity=".6"/>
<circle cx="125" cy="117" r="12" fill="#a2e4ec" stroke="#2b2444" stroke-width="4"/><path d="M134 126l11 10" stroke="#2b2444" stroke-width="5"/>
</svg>'''

st.markdown(f'''<div class="hero"><div style="display:flex;align-items:center;gap:20px;flex-wrap:wrap"><div style="flex:1;min-width:245px"><h1>🛍️ MISI JIMAT!</h1><p>DETEKTIF DISKAUN • EDISI KARTUN CERIA</p><span class="chip">📘 Matematik Tahun 5</span><span class="chip">🎯 Peratus & Wang</span><span class="chip">🐾 Belajar sambil bermain</span></div><div>{character}</div></div></div>''',unsafe_allow_html=True)

with st.sidebar:
    st.title("🎮 Pusat Misi")
    page=st.radio("Pilih aktiviti",["🏠 Pengenalan", "🛒 Kedai Maya", "🧩 5 Kaedah", "📈 Detektif Data", "🏆 Kuiz Cabaran", "📚 Panduan Tugasan"])
    st.divider()
    st.markdown("**Soalan teras:**\n\nBeg berharga **RM80**. Kedai A diskaun **20%**; Kedai B potongan tetap **RM10**. Yang mana lebih jimat? Bila pilihan berubah?")
    st.caption("Ilustrasi kartun asli; tema terinspirasi daripada suasana komedi keluarga Shinchan. Bukan aplikasi rasmi.")

def prices(x):
    return round(x*0.8,2),round(x-10,2)

def choice(x):
    a,b=prices(x)
    if abs(a-b)<1e-8:return "Sama harga"
    return "Kedai A" if a<b else "Kedai B"

def box(msg):
    st.markdown(f'<div class="card">{msg}</div>',unsafe_allow_html=True)

if page=="🏠 Pengenalan":
    st.header("📜 Misi kamu")
    box("<h3>Siapa lebih jimat?</h3>Bayangkan beg sekolah berharga <b>RM80</b>. Kedai A memberi diskaun <b>20%</b> dan Kedai B memberi potongan <b>RM10</b>. Pilih kedai paling murah, kemudian siasat apa jadi apabila harga asal berubah!")
    c1,c2=st.columns(2)
    with c1: st.info("🏪 **Kedai A** — Diskaun 20% daripada harga asal")
    with c2: st.info("🏬 **Kedai B** — Potongan tetap RM10")
    st.subheader("🎯 Objektif pembelajaran")
    st.write("1. Mengira harga selepas diskaun dan potongan tetap dengan betul.\n\n2. Membandingkan tawaran melalui gambar rajah, teka dan uji, jadual/pola, bekerja dari belakang serta simulasi digital.\n\n3. Menjelaskan mengapa pilihan kedai berubah apabila harga asal berubah.")
    st.caption("DSKP: fokus penyelesaian masalah harian melibatkan peratus (SP 2.4.1), dengan aplikasi wang.")

elif page=="🛒 Kedai Maya":
    st.header("🛒 Simulator Kedai Maya")
    st.write("Ubah harga dan **ramal dahulu** sebelum mendedahkan jawapan!")
    x=st.slider("💰 Harga asal beg (RM)",min_value=10,max_value=200,value=80,step=5,key="price_slider")
    guess=st.radio("🤔 Kedai mana lebih murah?",["Kedai A","Kedai B","Sama harga"],horizontal=True,key="shop_guess")
    if st.button("🔍 Semak ramalan",use_container_width=True):
        st.session_state["reveal"]=True
    if st.session_state.get("reveal",False):
        a,b=prices(x)
        ca,cb=st.columns(2)
        with ca: st.metric("🏪 Kedai A (−20%)",f"RM{a:.2f}",f"Jimat RM{x-a:.2f}",delta_color="off")
        with cb: st.metric("🏬 Kedai B (−RM10)",f"RM{b:.2f}","Jimat RM10.00",delta_color="off")
        actual=choice(x)
        if guess==actual:
            st.success(f"🎉 Tepat! Jawapan: {actual}. Beza harga RM{abs(a-b):.2f}.")
            st.balloons()
        else:st.warning(f"Cuba lagi! Jawapan sebenar: {actual}; beza harga RM{abs(a-b):.2f}.")
        st.write(f"**Langkah kira:** Kedai A = RM{x} × 80% = RM{a:.2f}; Kedai B = RM{x} − RM10 = RM{b:.2f}.")
    else: st.info("💡 Tekan ‘Semak ramalan’ untuk mendedahkan keputusan.")
    if st.button("🔄 Cuba misi baharu"):
        st.session_state["reveal"]=False
        st.rerun()

elif page=="🧩 5 Kaedah":
    st.header("🧩 Lima strategi, satu masalah")
    method=st.selectbox("Pilih pendekatan",["1. Gambar rajah bar", "2. Teka dan uji", "3. Jadual dan pola", "4. Bekerja dari belakang", "5. Simulasi digital"])
    if method.startswith("1"):
        st.subheader("🎨 Gambar rajah (RM80)")
        st.write("Kedai A: lima bahagian sama besar. Satu bahagian = RM16 (20%); empat bahagian = RM64.")
        st.markdown("**Kedai A** — 🟥 🟪 🟪 🟪 🟪  = RM16 diskaun + RM64 baki")
        st.write("Kedai B: lapan bahagian sama besar. Satu bahagian = RM10; tujuh bahagian = RM70.")
        st.markdown("**Kedai B** — 🟥 🟦 🟦 🟦 🟦 🟦 🟦 🟦  = RM10 potongan + RM70 baki")
        st.success("Untuk RM80, Kedai A lebih murah sebanyak RM6.")
    elif method.startswith("2"):
        st.subheader("🎲 Teka dan uji")
        x=st.select_slider("Pilih harga untuk diuji (RM)",options=[20,30,40,50,60,80,100,120],value=80)
        a,b=prices(x)
        st.write(f"Harga RM{x}: Kedai A **RM{a:.2f}**; Kedai B **RM{b:.2f}** → **{choice(x)}**.")
        st.caption("Uji RM40, RM50, RM80 dan RM100 lalu bandingkan keputusan.")
    elif method.startswith("3"):
        st.subheader("📋 Jadual mengenal pasti pola")
        dat=[]
        for x in [20,30,40,50,60,80,100]:
            a,b=prices(x); dat.append({"Harga asal (RM)":x,"Kedai A (RM)":a,"Kedai B (RM)":b,"Lebih murah":choice(x)})
        st.dataframe(pd.DataFrame(dat),hide_index=True,use_container_width=True)
        st.info("Pola: bawah RM50 → B; tepat RM50 → sama; atas RM50 → A.")
    elif method.startswith("4"):
        st.subheader("🔄 Bekerja dari belakang")
        st.latex(r"0.20x=x-(x-10)=10")
        st.latex(r"x=\frac{10}{0.20}=50")
        st.write("Semak: Kedai A = RM50 − RM10 = **RM40**; Kedai B = RM50 − RM10 = **RM40**.")
        st.caption("Mula dengan syarat kedua-dua harga sama, kemudian cari harga asal.")
    else:
        st.subheader("🖥️ Simulasi digital")
        x=st.slider("Ubah harga asal (RM)",10,200,80,5,key="method_slider")
        a,b=prices(x)
        st.success(f"RM{x}: A = RM{a:.2f}, B = RM{b:.2f} → {choice(x)}.")
        st.write("Ini pendekatan digital yang dibina sendiri menggunakan Python + Streamlit.")

elif page=="📈 Detektif Data":
    st.header("📈 Graf dan analisis pola")
    maximum=st.slider("Harga asal maksimum dalam graf (RM)",60,300,150,10)
    values=list(range(10,maximum+1,5))
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=values,y=[prices(i)[0] for i in values],name="Kedai A • Diskaun 20%",mode="lines+markers",line=dict(color="#874ce1",width=4)))
    fig.add_trace(go.Scatter(x=values,y=[prices(i)[1] for i in values],name="Kedai B • Potongan RM10",mode="lines+markers",line=dict(color="#ef5d82",width=4)))
    fig.add_trace(go.Scatter(x=[50],y=[40],mode="markers+text",text=["(50, 40)"],textposition="top center",marker=dict(size=15,color="#2b2444"),name="Titik sama"))
    fig.update_layout(title="Harga selepas potongan mengikut harga asal",xaxis_title="Harga asal (RM)",yaxis_title="Harga selepas potongan (RM)",paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="white",font=dict(color="#2b2444"),legend=dict(orientation="h",y=-0.3),margin=dict(l=20,r=20,t=60,b=80))
    st.plotly_chart(fig,use_container_width=True)
    st.markdown("""**Kesimpulan graf:** Kedai B lebih murah apabila **RM10 ≤ harga asal < RM50**; kedua-dua harga sama pada **RM50**; Kedai A lebih murah jika harga asal **> RM50**. Persilangan (50, 40) bermaksud harga asal RM50 menghasilkan harga akhir RM40 di kedua-dua kedai.""")
    df=pd.DataFrame([{"Harga asal (RM)":v,"Kedai A (RM)":prices(v)[0],"Kedai B (RM)":prices(v)[1],"Lebih murah":choice(v)} for v in values])
    st.download_button("⬇️ Muat turun data analisis (CSV)",df.to_csv(index=False).encode("utf-8-sig"),"analisis_diskaun.csv","text/csv")

elif page=="🏆 Kuiz Cabaran":
    st.header("🏆 Kuiz Detektif Diskaun")
    st.write("Jawab lima soalan. Setiap jawapan betul mendapat 20 markah!")
    qs=[
        ("Jika harga asal RM80, berapakah harga Kedai A?",["RM64","RM70","RM16"],"RM64"),
        ("Jika harga asal RM40, kedai manakah lebih murah?",["Kedai A","Kedai B","Sama harga"],"Kedai B"),
        ("Pada harga asal berapakah kedua-dua kedai sama murah?",["RM40","RM50","RM80"],"RM50"),
        ("Apakah harga selepas potongan di kedua-dua kedai apabila harga asal RM50?",["RM35","RM40","RM45"],"RM40"),
        ("Jika harga asal RM100, berapakah beza harga kedua-dua kedai?",["RM10","RM5","RM20"],"RM10")
    ]
    with st.form("quiz_form"):
        answers=[]
        for i,(q,opts,correct) in enumerate(qs):
            answers.append(st.radio(f"Soalan {i+1}. {q}",opts,index=None,key=f"q_{i}"))
        submit=st.form_submit_button("✅ Semak semua jawapan",use_container_width=True)
    if submit:
        if any(a is None for a in answers):st.warning("Jawab semua soalan dahulu, ya!")
        else:
            n=sum(a==q[2] for a,q in zip(answers,qs))
            st.metric("Skor",f"{n*20}/100")
            if n==5:
                st.success("🎊 Hebat! Semua jawapan betul!")
                st.balloons()
            else:
                st.info("Terus cuba! Jawapan yang betul:")
                for i,(a,q) in enumerate(zip(answers,qs)):
                    st.write(f"{i+1}. {'✅' if a==q[2] else '❌'} **{q[2]}**")

else:
    st.header("📚 Panduan dokumentasi Tugasan 4")
    st.markdown("""**Masalah matematik tunggal:** Beg RM80; Kedai A diskaun 20%, Kedai B potongan RM10. Tentukan kedai lebih murah, kaji kesan perubahan harga asal dan cari harga asal yang menghasilkan harga akhir sama.

**Bukti yang boleh diambil:**
- Paparan misi dan objektif (pengenalan).
- Simulator RM80: A RM64, B RM70 (penyelesaian).
- Tab 5 Kaedah (pelbagai pendekatan).
- Graf dan titik persilangan (50, 40) (analisis pola).
- Kuiz dan skor (ciri gamifikasi).

**Untuk laporan:** sertakan pautan aplikasi setelah diterbitkan, tangkapan layar, refleksi pembinaan projek, sumber DSKP dan rujukan APA 7. Nyatakan bantuan AI secara beretika jika digunakan.

**Nota:** Keputusan aplikasi ialah simulasi matematik; jangan mendakwa ia meningkatkan pencapaian murid tanpa ujian pengguna.""")

st.divider()
st.caption("Misi Jimat • Projek Matematik Tahun 5 KSSR • Dibangunkan dengan Python & Streamlit")
