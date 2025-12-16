import streamlit as st
from task_dashboard.services.metrics_service import calc_basic_metrics
from task_dashboard.db.seed_data import init_db



def main():
    st.title("Backoffice Metrics Demo")

    if st.button("Инициализировать базу задач"):
        init_db()
        st.success("База tasks.db создана и заполнена данными")

    if st.button("Показать базовые метрики"):
        metrics = calc_basic_metrics()
        st.write(metrics)


if __name__ == "__main__":
    main()
