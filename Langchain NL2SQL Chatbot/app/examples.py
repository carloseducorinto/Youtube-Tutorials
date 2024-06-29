examples = [
    {
        "input": "Find all market data entries recorded on 2024-03-28",
        "query": "SELECT * FROM market_data WHERE market_date = '2024-03-28';"
    },
    {
        "input": "List all clients who are of type 'Coporate'",
        "query": "SELECT * FROM clients WHERE client_type = 'Coporate';"
    },
    {
        "input": "Show the names and contact information of clients",
        "query": "SELECT client_name, contact_info FROM clients;"
    },
    {
        "input": "Get the details of derivative products that mature after January 1, 2025",
        "query": "SELECT * FROM derivative_products WHERE maturity_date > '2025-01-01';"
    },
    {
        "input": "Retrieve market data for the product with product_id 55",
        "query": "SELECT * FROM market_data WHERE product_id = 55;"
    },
    {
        "input": "Find all transactions that were 'buy' transactions",
        "query": "SELECT * FROM transactions WHERE transaction_type = 'buy';"
    },
    {
        "input": "List the names of all users",
        "query": "SELECT name FROM users;"
    },
    {
        "input": "Get the transaction details where the client_id is 124",
        "query": "SELECT * FROM transactions WHERE client_id = 124;"
    },
    {
        "input": "Show the product names and their underlying assets",
        "query": "SELECT product_name, underlying_asset FROM derivative_products;"
    },
    {
        "input": "List all clients along with their transactions",
        "query": "SELECT clients.client_name, transactions.* FROM clients JOIN transactions ON clients.client_id = transactions.client_id;"
    },
    {
        "input": "Summarize the total financial volume of transactions for each client",
        "query": "SELECT clients.client_name, SUM(transactions.transaction_price * transactions.quantity) AS total_volume FROM transactions JOIN clients ON transactions.client_id = clients.client_id GROUP BY clients.client_name;"
    },
    {
        "input": "Find the top clients by transaction volume for each product",
        "query": "SELECT derivative_products.product_name, clients.client_name, SUM(transactions.quantity) AS total_quantity FROM transactions JOIN clients ON transactions.client_id = clients.client_id JOIN derivative_products ON transactions.product_id = derivative_products.product_id GROUP BY derivative_products.product_name, clients.client_name ORDER BY derivative_products.product_name, total_quantity DESC;"
    },
    {
        "input": "Show the total transaction volume for each product type",
        "query": "SELECT product_type, SUM(quantity) AS total_volume FROM transactions JOIN derivative_products ON transactions.product_id = derivative_products.product_id GROUP BY product_type;"
    },
    {
        "input": "List the top 5 clients by total transaction volume",
        "query": "SELECT clients.client_name, SUM(transactions.quantity) AS total_volume FROM transactions JOIN clients ON transactions.client_id = clients.client_id GROUP BY clients.client_name ORDER BY total_volume DESC LIMIT 5;"
    },
    {
        "input": "Find the average transaction price for each product type",
        "query": "SELECT derivative_products.product_type, AVG(transactions.transaction_price) AS avg_price FROM transactions JOIN derivative_products ON transactions.product_id = derivative_products.product_id GROUP BY derivative_products.product_type;"
    },
    {
        "input": "Calculate the total volume of market data for each product",
        "query": "SELECT derivative_products.product_name, SUM(market_data.volume) AS total_volume FROM market_data JOIN derivative_products ON market_data.product_id = derivative_products.product_id GROUP BY derivative_products.product_name;"
    },
    {
        "input": "Show the maximum transaction price for each client",
        "query": "SELECT clients.client_name, MAX(transactions.transaction_price) AS max_price FROM transactions JOIN clients ON transactions.client_id = clients.client_id GROUP BY clients.client_name;"
    },
    {
        "input": "Get the number of transactions for each product type",
        "query": "SELECT derivative_products.product_type, COUNT(transactions.transaction_id) AS transaction_count FROM transactions JOIN derivative_products ON transactions.product_id = derivative_products.product_id GROUP BY derivative_products.product_type;"
    },
    {
        "input": "Find the minimum market price recorded for each product",
        "query": "SELECT derivative_products.product_name, MIN(market_data.market_price) AS min_price FROM market_data JOIN derivative_products ON market_data.product_id = derivative_products.product_id GROUP BY derivative_products.product_name;"
    },
    {
        "input": "Calculate the average volume of market data for currency products",
        "query": "SELECT AVG(market_data.volume) AS avg_volume FROM market_data JOIN derivative_products ON market_data.product_id = derivative_products.product_id WHERE derivative_products.product_type = 'Currency';"
    },
    {
        "input": "Show the total quantity of transactions for each client and product",
        "query": "SELECT clients.client_name, derivative_products.product_name, SUM(transactions.quantity) AS total_quantity FROM transactions JOIN clients ON transactions.client_id = clients.client_id JOIN derivative_products ON transactions.product_id = derivative_products.product_id GROUP BY clients.client_name, derivative_products.product_name;"
    }
]


from langchain_community.vectorstores import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_openai import OpenAIEmbeddings
import streamlit as st

@st.cache_resource
def get_example_selector():
    example_selector = SemanticSimilarityExampleSelector.from_examples(
        examples,
        OpenAIEmbeddings(),
        Chroma,
        k=2,
        input_keys=["input"],
    )
    return example_selector