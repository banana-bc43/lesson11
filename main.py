import streamlit as st
import pandas as pd

# 言語選択
language = st.sidebar.selectbox('言語を選択してください / Choose a language', ['日本語', 'English'])

# 言語によるテキストの設定
if language == '日本語':
    title = '📅 スケジュール表'
    intro_text = '予定を入力して、スケジュールを作成しよう！'
    time_label = '時間 (半角で入力: 例 09:00)'
    task_label = '予定を入力'
    add_button = '予定を追加'
    success_add = '新しい予定が追加されたよ！'
    error_message = '時間と予定の両方を入力してね！'
    select_label = '削除/修正する予定を選んでね'
    edit_time_label = '修正する時間'
    edit_task_label = '修正する予定'
    edit_button = '選択した予定を修正'
    delete_button = '選択した予定を削除'
    success_edit = '選択した予定が修正されたよ！'
    success_delete = '選択した予定が削除されたよ！'
    no_schedule = 'まだ予定が追加されていないよ。'
    sleep_message = "<h2 style='text-align: center; color: green;'>That nice! <br>いいルーティーンができたね！<br>本日もお疲れ様です。</h2>"
else:
    title = '📅 Schedule'
    intro_text = 'Enter your plans and create a schedule!'
    time_label = 'Time (Enter in half-width: e.g., 09:00)'
    task_label = 'Enter your task'
    add_button = 'Add Task'
    success_add = 'New task added!'
    error_message = 'Please enter both time and task!'
    select_label = 'Select a task to delete/edit'
    edit_time_label = 'Edit time'
    edit_task_label = 'Edit task'
    edit_button = 'Edit selected task'
    delete_button = 'Delete selected task'
    success_edit = 'Selected task edited!'
    success_delete = 'Selected task deleted!'
    no_schedule = 'No tasks added yet.'
    sleep_message = "<h2 style='text-align: center; color: green;'>That nice! <br>Great routine!<br>Good job today.</h2>"

# セッションステートを使ってスケジュールデータを保持
if 'schedule_data' not in st.session_state:
    st.session_state['schedule_data'] = []

# ストリームリットで表示
st.title(title)
st.write(intro_text)

# 新しい予定の入力
new_time = st.text_input(time_label, key='new_time')
new_task = st.text_input(task_label, key='new_task')

# 全角を半角に変換する関数
def to_half_width(input_str):
    return input_str.translate(str.maketrans('１２３４５６７８９：', '123456789:'))

# 追加ボタン
if st.button(add_button):
    # 時間を半角に変換
    new_time = to_half_width(new_time)
    
    if new_time and new_task:
        # 新しい予定をセッションステートに追加
        if language =="日本語":
            st.session_state['schedule_data'].append({'時間': new_time, '予定': new_task })
        else :
            st.session_state['schedule_data'].append({'time': new_time, 'schedule': new_task })
        st.success(success_add)
        # 「寝る」や「就寝」というキーワードが含まれているかチェック
        if '寝る' in new_task or '就寝' in new_task or 'Sleep' in new_task :
            st.balloons()
            # メッセージを中央に表示
            st.markdown(sleep_message, unsafe_allow_html=True)
    else:
        st.error(error_message)

# データフレームを作成
schedule_df = pd.DataFrame(st.session_state['schedule_data'])

# スケジュールを表示
if not schedule_df.empty:
    st.table(schedule_df)

    if language =="日本語":
        key_time = '時間'
        key_sche = '予定'
    else:
        key_time = 'time'
        key_sche = 'schedule' 
    # 削除または修正する行を選択
    selected_index = st.selectbox(select_label, range(len(schedule_df)), format_func=lambda x: f"{schedule_df.iloc[x][key_time]} - {schedule_df.iloc[x][key_sche]}", index=0)

    # 選択した予定の編集
    edit_time = st.text_input(edit_time_label, value=schedule_df.iloc[selected_index][key_time])
    edit_task = st.text_input(edit_task_label, value=schedule_df.iloc[selected_index][key_sche])

    # 修正ボタン
    if st.button(edit_button):
        st.session_state['schedule_data'][selected_index] = {key_time: to_half_width(edit_time), key_sche: edit_task}
        st.success(success_edit)

    # 削除ボタン
    if st.button(delete_button):
        st.session_state['schedule_data'].pop(selected_index)
        st.success(success_delete)
else:
    st.write(no_schedule)