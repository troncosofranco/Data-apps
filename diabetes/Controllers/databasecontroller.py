from services.database import mydb
import streamlit as st
import models.Register as Register

#Add new register
def add(Register):
    mycursor = mydb.cursor()
    
    sql = "INSERT INTO register (id_patient, cpf, gender, age, urea, cr, hb1ac, chol, tg, hdl, ldl, vlsl, bmi, outcome) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (Register.id_patient, Register.cpf, Register.gender, Register.age, Register.urea, Register.cr, Register.hb1ac,
    Register.chol, Register.tg, Register.hdl, Register.ldl, Register.vlsl, Register.bmi, Register.outcome)
    
    mycursor.execute(sql, val)
    mydb.commit()

#Delete register
def delete(id):
    mycursor = mydb.cursor()
    
    sql = f'DELETE FROM register WHERE id = {id}'
    #st.write(sql)
    mycursor.execute(sql)
    mydb.commit()


#get all register
def get_all():
    query = "SELECT * from register;"
    
    with mydb.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

    

    
