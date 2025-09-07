import streamlit as st
import pandas as pd

# セッションステートを使ってスケジュールデータを保持
if 'schedule_data' not in st.session_state:
    st.session_state['schedule_data'] = []

# ストリームリットで表示
st.title('📅 スケジュール表')
st.write('今日の予定を入力して、スケジュールを作成しましょう！')

# 新しい予定の入力
new_time = st.text_input('時間を入力してください (例: 09:00)', key='new_time')
new_task = st.text_input('予定を入力してください', key='new_task')

# 全角を半角に変換する関数
def to_half_width(input_str):
    return input_str.translate(str.maketrans('０１２３４５６７８９：', '0123456789:'))

# 追加ボタン
if st.button('予定を追加'):
    # 時間を半角に変換
    new_time = to_half_width(new_time)
    
    if new_time and new_task:
        # 新しい予定をセッションステートに追加
        st.session_state['schedule_data'].append({'時間': new_time, '予定': new_task})
        st.success('新しい予定が追加されました！')

        # 「寝る」や「就寝」というキーワードが含まれているかチェック
        if '寝る' in new_task or '就寝' in new_task:
            st.balloons()
            # メッセージを中央に表示
            st.markdown("<h2 style='text-align: center; color: green;'>That nice!<br>いいルーティーンができたね！本日もお疲れ様です。</h2>", unsafe_allow_html=True)
    else:
        st.error('時間と予定の両方を入力してください。')

# データフレームを作成
schedule_df = pd.DataFrame(st.session_state['schedule_data'])

# スケジュールを表示
if not schedule_df.empty:
    st.table(schedule_df)

    # 削除または修正する行を選択
    selected_index = st.selectbox('削除または修正する予定を選んでください', range(len(schedule_df)), format_func=lambda x: f"{schedule_df.iloc[x]['時間']} - {schedule_df.iloc[x]['予定']}")

    # 削除ボタン
    if st.button('選択した予定を削除'):
        st.session_state['schedule_data'].pop(selected_index)
        st.success('選択した予定が削除されました！')

    # 修正ボタン
    if st.button('選択した予定を修正'):
        st.session_state['schedule_data'][selected_index] = {'時間': new_time, '予定': new_task}
        st.success('選択した予定が修正されました！')
else:
    st.write('まだ予定が追加されていません。')