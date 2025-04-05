import re;
import streamlit as st;


st.set_page_config(page_title="Password Strength Meter", page_icon="🔐" , layout="centered")

# page title and description:
st.title("🔐 Password Strength Meter")
st.write("📌Enter your password and check password its security in few seconds!")

def password_strength(password):
    score = 0
    feedback = []

    # condition for length:
    if len(password) >= 8:
        score += 1
    else :
     feedback.append("❌ Password should  be at least **8** characters long")

    # condition for alphabets
    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
      score +=1
    else : 
      feedback.append("❌ Password should contain both **uppercase** (A-Z) & **lowercase** (a-z) letters")
      
    # condition for digit
    if re.search(r"\d",password):
      score +=1
    else:
      feedback.append("❌ Password should include at least **one digit** (0-9)")

    # condition for special character:
    if re.search(r"[!@#$%^&]",password) :
      score +=1
    else :
      feedback.append("❌ Password must have one **special character** (!@#$%^&*)")

    # display password strength:
    if score == 4:
      st.success("✅ Strong Password!")
    elif score == 3:
      st.info("⚠️ Moderate Password - Consider adding more security features.") 
    else : st.error("❌ Weak Password - Improve it using the suggestions below.")

    # feedback:
    if feedback:
      with st.expander("💡Improve Your Password"):
        for item in feedback:
          st.write(item)

 # input from user
password = st.text_input("Enter your Password:", type="password",help="Ensure your password is strong")

 # button to check
if st.button("🚀 Check Password Strength"):
  if password:
    password_strength(password)
  else:
    st.warning("🔹Please enter a password first!")