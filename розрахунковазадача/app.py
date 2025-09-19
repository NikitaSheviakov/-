import streamlit as st

# Налаштування сторінки
st.set_page_config(page_title="Min, Max, Average Calculator", page_icon="📊")

st.title("Інтерактивна програма")
st.write("Введіть 10 чисел (від 10 до 1000) через кому. Використовуйте крапку як роздільник дробової частини.")

# Поле вводу
user_input = st.text_input("Ваші числа:", "124, 890, 416, 974, 661, 12, 919, 931, 835, 938")

if st.button("Обчислити"):
    try:
        # Розділяємо рядок по комах
        parts = [p.strip() for p in user_input.split(",")]
        
        if len(parts) != 10:
            st.error("❌ Помилка: введіть рівно 10 чисел.")
        else:
            numbers = []
            for p in parts:
                n = float(p)
                if n < 10 or n > 1000:
                    raise ValueError("Число поза межами")
                numbers.append(n)

            min_val = min(numbers)
            max_val = max(numbers)
            avg_val = round(sum(numbers) / len(numbers), 2)

            st.success("✅ Результати обчислення:")
            st.markdown(f"**Min:** <span style='color:red'>{min_val}</span>", unsafe_allow_html=True)
            st.markdown(f"**Max:** <span style='color:blue'>{max_val}</span>", unsafe_allow_html=True)
            st.markdown(f"**Average:** {avg_val}")
    except:
        st.error("❌ Помилка: введені дані некоректні. Переконайтеся, що числа від 10 до 1000, розділені комами.")

st.write("Розробник: Твоє Шевяков Нікіта")

