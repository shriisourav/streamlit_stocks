import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from  markowitz import download_data,calculate_return,generate_portfolios,optimize_portfolio,print_optimal_portfolio

# Define a function to process the input and calculate results
def calculate_result(input_value, start_date, end_date):
    stocks=input_value
    dataset=download_data(input_value,start_date, end_date)
    log_daily_returns = calculate_return(dataset)
    pweights, means, risks = generate_portfolios(stocks,log_daily_returns)
    optimum = optimize_portfolio(stocks,pweights, log_daily_returns)
    optimal_portfolio, SharpeRatio=print_optimal_portfolio(optimum, log_daily_returns)
    # For demonstration, let's generate some random data
    #dates = pd.date_range(start=start_date, end=end_date)
    #data = np.random.randn(len(dates)) * int(input_value)
    return dataset, optimal_portfolio, SharpeRatio

# Streamlit app
def main():
    st.title("Stock and Graph Example")

    # User input for a number
    input_value = st.text_input("Enter the list of stocks for portfolio choice:", "AAPL,NVDA,MSFT")
    
    # Date range input
    start_date = st.date_input("Start date", pd.to_datetime('2023-01-01'))
    end_date = st.date_input("End date", pd.to_datetime('2023-12-31'))
    
    # Button to calculate and display results
    if st.button("Calculate"):
        # Validate input
        try:
            tickers = [ticker.strip() for ticker in input_value.split(',')]
        except ValueError:
            st.error("Please enter a valid number.")
            return
        
        # Calculate results
        dataset, optimal_portfolio, SharpeRatio = calculate_result(tickers, start_date, end_date)
        # Display the results
        st.write(f"Results for input value: {tickers}")
        st.write(f"Optimal portfolio: : {optimal_portfolio}")
        st.write(f"Expected return, volatility and Sharpe ratio: {SharpeRatio}")
        
        # Display the data as a table
        st.dataframe(dataset)
        st.line_chart(dataset)

if __name__ == "__main__":
    main()