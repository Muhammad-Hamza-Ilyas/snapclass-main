import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time

@st.dialog("Enroll in Subject")
def enroll_dialog():
    st.write('Enter the subject code provided by your teacher to enroll')
    join_code = st.text_input('Subject Code', placeholder='Eg. CS101')
    
    if st.button('Enroll now', type='primary', width='stretch'):
        if join_code:
            # Fetch the subject details based on the entered join_code
            res = supabase.table('subjects').select('subject_id', 'name', 'subject_code').eq('subject_code', join_code).execute()
            
            if res.data:
                subject = res.data[0]
                student_id = st.session_state.student_data['student_id']
                
                # Check if the student is already enrolled in this subject
                check = supabase.table('subject_students').select('*').eq('subject_id', subject['subject_id']).eq('student_id', student_id).execute()
                
                if check.data:
                    st.warning('You are already enrolled in this program')
                else:
                    # Enroll the student and refresh the app state
                    enroll_student_to_subject(student_id, subject['subject_id'])
                    st.success('Successfully enrolled!')
                    time.sleep(1)
                    st.rerun()
            else:
                st.error('Invalid subject code. Please try again.')
        else:
            st.warning('Please enter a subject code')

# To test or run the dialog in your main app file, you would call it like this:
# if st.button("Open Enrollment"):
#     enroll_dialog()