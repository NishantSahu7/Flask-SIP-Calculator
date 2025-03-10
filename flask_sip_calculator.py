#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify

def calculate_sip(monthly_investment, years, rate_of_return):
    """
    Calculate the maturity value of a Normal SIP.
    """
    months = years * 12
    monthly_rate = (rate_of_return / 100) / 12
    
    # Future Value of SIP formula: FV = P * [(1 + r)^n - 1] * (1 + r) / r
    future_value = monthly_investment * (((1 + monthly_rate) ** months - 1) * (1 + monthly_rate) / monthly_rate)
    return round(future_value, 2)

# Initialize Flask App
app = Flask(__name__)

@app.route('/calculate_sip', methods=['GET'])
def sip_api():
    """
    API Endpoint to calculate SIP maturity value.
    Expects query parameters: monthly_investment, years, rate_of_return
    """
    try:
        monthly_investment = float(request.args.get('monthly_investment', 0))
        years = int(request.args.get('years', 0))
        rate_of_return = float(request.args.get('rate_of_return', 0))
        
        if monthly_investment <= 0 or years <= 0 or rate_of_return <= 0:
            return jsonify({'error': 'All inputs must be positive values'}), 400
        
        result = calculate_sip(monthly_investment, years, rate_of_return)
        return jsonify({'monthly_investment': monthly_investment, 'years': years, 'rate_of_return': rate_of_return, 'maturity_value': result})
    
    except ValueError:
        return jsonify({'error': 'Invalid input values'}), 400

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)

