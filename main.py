import streamlit as st
import pandas as pd

# スケジュールデータを格納するリスト
schedule_data = []

# ストリームリットで表示
st.title('スケジュール表')
st.write('今日の予定を入力して、スケジュールを作成しましょう！')

# 新しい予定の入力
new_time = st.text_input('時間を入力してください (例: 09:00)')
new_task = st.text_input('予定を入力してください')

# 追加ボタン
if st.button('予定を追加'):
    if new_time and new_task:
        # 新しい予定をリストに追加
        schedule_data.append({'時間': new_time, '予定': new_task})
        st.success('新しい予定が追加されました！')
    else:
        st.error('時間と予定の両方を入力してください。')

# データフレームを作成
schedule_df = pd.DataFrame(schedule_data)

# スケジュールを表示
if not schedule_df.empty:
    st.table(schedule_df)
else:
    st.write('まだ予定が追加されていません。')