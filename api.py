import gradio as gr
from crud import (
    add_sale,
    get_all_sales,
    update_sale,
    delete_sale,
    search_sales
)


def add_sale_ui(
    transaction_id,
    date,
    customer_id,
    gender,
    age,
    product_category,
    quantity,
    price_per_unit
):
    try:
        result = add_sale(
            transaction_id,
            date,
            customer_id,
            gender,
            age,
            product_category,
            quantity,
            price_per_unit
        )

        return result

    except Exception as e:
        return f"Error: {e}"


def get_sales_ui():
    try:
        return get_all_sales()

    except Exception as e:
        return f"Error: {e}"


def update_sale_ui(
    transaction_id,
    quantity,
    price_per_unit
):
    try:
        result = update_sale(
            transaction_id,
            quantity,
            price_per_unit
        )

        return result

    except Exception as e:
        return f"Error: {e}"


def delete_sale_ui(transaction_id):
    try:
        result = delete_sale(transaction_id)

        return result

    except Exception as e:
        return f"Error: {e}"


def search_sales_ui(search_text):
    try:
        return search_sales(search_text)

    except Exception as e:
        return f"Error: {e}"


with gr.Blocks(title="Inventory & Sales Analyzer") as app:

    gr.Markdown(
        """
        # 🛒 Inventory & Sales Analyzer

        Manage sales using Python, SQLite and Gradio.
        """
    )

    with gr.Tab("Sales"):

        gr.Markdown("## ➕ Add New Sale")

        with gr.Row():

            transaction_id = gr.Number(
                label="Transaction ID",
                precision=0
            )

            date = gr.Textbox(
                label="Date",
                placeholder="YYYY-MM-DD"
            )

            customer_id = gr.Textbox(
                label="Customer ID",
                placeholder="CUST001"
            )

        with gr.Row():

            gender = gr.Dropdown(
                choices=["Male", "Female"],
                label="Gender"
            )

            age = gr.Number(
                label="Age",
                precision=0
            )

            product_category = gr.Dropdown(
                choices=[
                    "Beauty",
                    "Clothing",
                    "Electronics"
                ],
                label="Product Category"
            )

        with gr.Row():

            quantity = gr.Number(
                label="Quantity",
                precision=0
            )

            price_per_unit = gr.Number(
                label="Price Per Unit"
            )

        add_button = gr.Button(
            "Add Sale",
            variant="primary"
        )

        add_result = gr.Textbox(
            label="Result"
        )

        add_button.click(
            fn=add_sale_ui,
            inputs=[
                transaction_id,
                date,
                customer_id,
                gender,
                age,
                product_category,
                quantity,
                price_per_unit
            ],
            outputs=add_result
        )

        gr.Markdown("## 📋 All Sales")

        view_button = gr.Button("Refresh Sales")

        sales_table = gr.Dataframe(
            label="Sales Data",
            interactive=False
        )

        view_button.click(
            fn=get_sales_ui,
            outputs=sales_table
        )

        gr.Markdown("## ✏️ Update Sale")

        update_transaction_id = gr.Number(
            label="Transaction ID",
            precision=0
        )

        update_quantity = gr.Number(
            label="New Quantity",
            precision=0
        )

        update_price = gr.Number(
            label="New Price Per Unit"
        )

        update_button = gr.Button(
            "Update Sale"
        )

        update_result = gr.Textbox(
            label="Result"
        )

        update_button.click(
            fn=update_sale_ui,
            inputs=[
                update_transaction_id,
                update_quantity,
                update_price
            ],
            outputs=update_result
        )

        gr.Markdown("## 🗑️ Delete Sale")

        delete_transaction_id = gr.Number(
            label="Transaction ID",
            precision=0
        )

        delete_button = gr.Button(
            "Delete Sale"
        )

        delete_result = gr.Textbox(
            label="Result"
        )

        delete_button.click(
            fn=delete_sale_ui,
            inputs=delete_transaction_id,
            outputs=delete_result
        )

    with gr.Tab("Search"):

        gr.Markdown("## 🔎 Search Sales")

        search_text = gr.Textbox(
            label="Search",
            placeholder="Enter transaction ID, customer ID, category or gender"
        )

        search_button = gr.Button(
            "Search"
        )

        search_results = gr.Dataframe(
            label="Search Results",
            interactive=False
        )

        search_button.click(
            fn=search_sales_ui,
            inputs=search_text,
            outputs=search_results
        )


app.launch()

