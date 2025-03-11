import streamlit as st
import re

st.set_page_config(page_title='Password Strength Meter',page_icon='🔐')
st.title('Password Strength Meter🔐')
st.markdown('''## Ensure Your Password is Secure! 
          Enter your password below to check its strength and get improvement tips.''')
password = st.text_input('Enter your password',type='password')
feedback = []
score = 0
if password:
   if len(password) >= 8:
      score += 1
   else:
      feedback.append('❌Password should be atleast 8 characters long.')    
   if re.search(r'[A-Z]',password) and re.search ('[a-z]', password) :
    score += 1
   else : 
      feedback.append('❌Password should contain both upper and lowercase characters.')
   if re.search(r'\d',password):
       score += 1
   else:
      feedback.append('❌Password should contain atleast one digit.')   
   if re.search(r'[!@#$%&*]',password):
      score += 1
   else:
      feedback.append('❌Password should contain atleast one special characters[!@#$%&*].')  
   if score == 4:
      feedback.append('✅Your password is strong!🎉')       
   elif score == 3:
      feedback.append('🟡Your password is moderate.It could be stronger.')   
   else:
      feedback.append('🔴Your  password is weak.Please make it stronger.')  
   if feedback:
      st.markdown('## Improvement Suggestions')
      for tip in feedback:
       st.write(tip)
   
       
else:
   st.info('Please enter your password to get started.')

