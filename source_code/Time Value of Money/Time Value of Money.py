# This function calculates the future value of an investment or loan.
# Parameters:
# pv (present value): The initial amount of money.
# rate: The annual interest rate as a decimal (e.g., 0.05 for 5%).
# periods: The number of years or time periods.
def future_value(pv, rate, periods):
    return pv * (1 + rate) ** periods


# This function calculates the present value of a future amount of money.
# Parameters:
# fv (future value): The amount of money expected in the future.
# rate: The annual interest rate as a decimal (e.g., 0.05 for 5%).
# periods: The number of years or time periods.
def present_value(fv, rate, periods):
    return fv / (1 + rate) ** periods


# This function calculates the net present value (NPV) of a series of cash flows.
# Parameters:
# cash_flows: A list of cash flows (negative values for costs, positive for revenue).
# rate: The discount rate (e.g., interest rate as a decimal).
# Uses: Iterates over each cash flow, discounts it back to the present time period, and sums them up.
def net_present_value(cash_flows, rate):
    return sum(cf / (1 + rate) ** i for i, cf in enumerate(cash_flows))


# Example Usage
if __name__ == "__main__":
    # Define input values
    pv = 1000  # Present value of an investment
    rate = 0.05  # Annual interest rate (5%)
    periods = 10  # Investment period in years

    # Calculate and print the future value of the investment
    fv_result = future_value(pv, rate, periods)
    print(f"Future Value: ${fv_result:.2f}")

    fv = 1628.89  # Future value amount
    # Calculate and print the present value of the future money
    pv_result = present_value(fv, rate, periods)
    print(f"Present Value: ${pv_result:.2f}")

    cash_flows = [-1000, 300, 400, 500, 600]  # Series of cash flows over time
    # Calculate and print the net present value of the cash flows
    npv_result = net_present_value(cash_flows, rate)
    print(f"Net Present Value: ${npv_result:.2f}")