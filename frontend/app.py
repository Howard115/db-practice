import streamlit as st
import requests
import json

# Set up the base URL for the API
BASE_URL = "http://localhost:8000"
# 设置API的基础URL

def main():
    st.title("🦸‍♂️ Superhero Management System")
    # 设置应用标题为"超级英雄管理系统"

    # Sidebar menu
    menu = st.sidebar.selectbox(
        "Choose an action",
        ["View All Heroes", "Add Hero", "Update Hero", "Delete Hero"]
    )
    # 在侧边栏创建菜单选择框

    if menu == "View All Heroes":
        display_all_heroes()
    elif menu == "Add Hero":
        add_hero()
    elif menu == "Update Hero":
        update_hero()
    elif menu == "Delete Hero":
        delete_hero()

def display_all_heroes():
    st.header("All Superheroes")
    # 显示所有超级英雄的标题
    
    try:
        response = requests.get(f"{BASE_URL}/heroes/")
        heroes = response.json()
        
        for hero in heroes:
            with st.expander(f"🦸‍♂️ {hero['name']}"):
                st.write(f"ID: {hero['id']}")
                st.write(f"Age: {hero['age'] if hero['age'] else 'Unknown'}")
    except Exception as e:
        st.error(f"Error fetching heroes: {str(e)}")
    # 尝试获取并显示所有英雄信息

def add_hero():
    st.header("Add New Superhero")
    # 添加新超级英雄的标题
    
    with st.form("add_hero_form"):
        name = st.text_input("Hero Name")
        secret_name = st.text_input("Secret Identity")
        age = st.number_input("Age", min_value=0, value=0)
        
        if st.form_submit_button("Add Hero"):
            try:
                response = requests.post(
                    f"{BASE_URL}/heroes/",
                    json={"name": name, "secret_name": secret_name, "age": age if age > 0 else None}
                )
                if response.status_code == 200:
                    st.success("Hero added successfully!")
                else:
                    st.error("Failed to add hero")
            except Exception as e:
                st.error(f"Error: {str(e)}")
    # 创建添加英雄的表单

def update_hero():
    st.header("Update Superhero")
    # 更新超级英雄的标题
    
    hero_id = st.number_input("Hero ID", min_value=1)
    
    with st.form("update_hero_form"):
        name = st.text_input("New Hero Name (optional)")
        secret_name = st.text_input("New Secret Identity (optional)")
        age = st.number_input("New Age (optional)", min_value=0, value=0)
        
        if st.form_submit_button("Update Hero"):
            update_data = {}
            if name:
                update_data["name"] = name
            if secret_name:
                update_data["secret_name"] = secret_name
            if age > 0:
                update_data["age"] = age
                
            try:
                response = requests.patch(
                    f"{BASE_URL}/heroes/{hero_id}",
                    json=update_data
                )
                if response.status_code == 200:
                    st.success("Hero updated successfully!")
                else:
                    st.error("Failed to update hero")
            except Exception as e:
                st.error(f"Error: {str(e)}")
    # 创建更新英雄的表单

def delete_hero():
    st.header("Delete Superhero")
    # 删除超级英雄的标题
    
    hero_id = st.number_input("Hero ID to delete", min_value=1)
    
    if st.button("Delete Hero"):
        try:
            response = requests.delete(f"{BASE_URL}/heroes/{hero_id}")
            if response.status_code == 200:
                st.success("Hero deleted successfully!")
            else:
                st.error("Failed to delete hero")
        except Exception as e:
            st.error(f"Error: {str(e)}")
    # 创建删除英雄的功能

if __name__ == "__main__":
    main()
