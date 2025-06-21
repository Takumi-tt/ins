import streamlit as st

st.set_page_config(page_title="インスリン使用日数計算", page_icon="💉")

st.title("インスリン使用日数計算ツール（Streamlit版）")

st.markdown("1日のインスリン使用量と空打ち設定を入力すると、1本で何日分使えるかを計算します。")

# 入力欄（朝・昼・夕・寝前）
st.subheader("インスリン単位数の入力（空欄は0として扱われます）")
morning = st.number_input("朝の単位数", min_value=0.0, step=1.0, format="%.1f")
noon = st.number_input("昼の単位数", min_value=0.0, step=1.0, format="%.1f")
evening = st.number_input("夕の単位数", min_value=0.0, step=1.0, format="%.1f")
night = st.number_input("寝る前の単位数", min_value=0.0, step=1.0, format="%.1f")

# 空打ち設定
st.subheader("空打ちの設定")
prime_value = st.radio("各回の空打ち単位数を選んでください：", [0, 1, 2], format_func=lambda x: f"{x} 単位")

# 容量設定
st.subheader("インスリンの容量")
capacity = st.radio("インスリン1本の容量（単位）", [300, 450])

# 計算ボタン
if st.button("計算する"):
    total = morning + noon + evening + night
    injection_times = sum(1 for v in [morning, noon, evening, night] if v > 0)
    total += injection_times * prime_value

    if total == 0:
        st.error("1日の使用量が0では計算できません。")
    else:
        days = capacity / total
        result_text = f"{int(morning)}-{int(noon)}-{int(evening)}-{int(night)}空打ち{prime_value}単位/1本で{days:.1f}日"
        st.success(f"💉 {capacity}単位のペンは約 **{days:.1f}日分** 使用できます")
        st.text_area("コピー用出力", result_text, height=50)
