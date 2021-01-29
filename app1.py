#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Arun Dubey
"""
import os
from flask import Flask, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/predict')
def predict_loan():
    """ OpenPay Scorecard Assignment - Arun Dubey 
    ---
    parameters:
      - name: FULL NAME
        in: query
        type: string
        required: false
      - name: DATE OF BIRTH (DD/MM/YYYY)
        in: query
        type: string
        required: false
      - name: DRIVER'S LICENCE
        in: query
        type: string
        required: false  
      - name: LOAN AMOUNT REQUESTED
        in: query
        type: number
        required: true
      - name: CURRENT PROPERTY VALUE
        in: query
        type: number
        required: true
      - name: OCCUPATIONAL CATEGORIES
        in: query
        type: string
        required: true
      - name: YEAR AT PRESENT JOB
        in: query
        type: number
        required: true
      - name: NO. OF DEROGATORY REPORTS
        in: query
        type: number
        required: true
      - name: NO. OF DELINQUENT CREDIT LINES
        in: query
        type: number
        required: true
      - name: AGE OF OLDEST CREDIT LINE
        in: query
        type: number
        required: true
      - name: NO. OF RECENT CREDIT INQ
        in: query
        type: number
        required: true
      - name: DEBT TO INC RATIO
        in: query
        type: number
        required: true
    definitions:
        value:
            type: object
            properties:
                value_name:
                    type: string
                    items:
                        $ref: '#/definitions/Color'
        Color:
          type: string
    responses:
        200:
            description: OK
            schema:
                $ref: '#/definitions/value'
    """
    FULL_NAME = request.args.get("FULL NAME")
    DOB = request.args.get("DATE OF BIRTH (DD/MM/YYYY)")
    DRL = request.args.get("DRIVER'S LICENCE")
    LOAN = request.args.get("LOAN AMOUNT REQUESTED")
    VALUE = request.args.get("CURRENT PROPERTY VALUE")
    JOB = request.args.get("OCCUPATIONAL CATEGORIES")
    YOJ = request.args.get("YEAR AT PRESENT JOB")
    DEROG = request.args.get("NO. OF DEROGATORY REPORTS")
    DELINQ = request.args.get("NO. OF DELINQUENT CREDIT LINES")
    CLAGE = request.args.get("AGE OF OLDEST CREDIT LINE")
    NINQ = request.args.get("NO. OF RECENT CREDIT INQ")
    DEBTINC = request.args.get("DEBT TO INC RATIO")
    
    # Scorecard
    if float(LOAN) > 0 and float(LOAN) <= 10000 :
        loan_score = -28.339632
    elif float(LOAN) > 10000 and float(LOAN) <= 15000 :
        loan_score = -2.812395
    elif float(LOAN) > 15000 and float(LOAN) <= 20000 :
        loan_score = 14.750160
    elif float(LOAN) > 20000 :
        loan_score = 15.349392
    else:
        loan_score = -99999

    if float(VALUE) > 0 and float(VALUE) <= 50000 :
        value_score = -32.281197
    elif float(VALUE) > 50000 and float(VALUE) <= 120000 :
        value_score = 2.095435
    elif float(VALUE) > 120000 and float(VALUE) <= 150000 :
        value_score = 6.114121
    elif float(VALUE) > 150000 :
        value_score = 15.411917
    else:
        value_score = -99999
    
    if JOB == 'Sales':
        job_score = -53.787692
    elif JOB == 'Self':
        job_score = -41.022992
    elif JOB == 'Other':
        job_score = -7.153751
    elif JOB == 'Mgr':
        job_score = -5.143486
    elif JOB == 'ProfExe':
        job_score = 15.418098
    elif JOB == 'Office':
        job_score = 27.425811
    else:
        job_score = -99999

    if   float(YOJ) <= 3 :
        yoj_score = -11.476887
    elif float(YOJ) > 3 and float(YOJ) <= 6 :
        yoj_score = -7.594468
    elif float(YOJ) > 6 and float(YOJ) <= 8 :
        yoj_score = 6.124229
    elif float(YOJ) > 8 :
        yoj_score = 9.006571
    else:
        yoj_score = -99999
    
    if   float(DEROG) <= 0 :
        derog_score = 11.278580
    elif float(DEROG) > 0 and float(DEROG) <= 1 :
        derog_score = -41.120649
    elif float(DEROG) > 1 and float(DEROG) <= 2 :
        derog_score = -63.529347
    elif float(DEROG) > 2 :
        derog_score = -109.132489
    else:
        derog_score = -99999
    
    if   float(DELINQ) <= 0 :
        delinq_score = 26.356399
    elif float(DELINQ) > 0 and float(DELINQ) <= 1 :
        delinq_score = -39.265617
    elif float(DELINQ) > 1 and float(DELINQ) <= 2 :
        delinq_score = -73.482306
    elif float(DELINQ) > 2 and float(DELINQ) <= 3 :
        delinq_score = -93.469941
    elif float(DELINQ) > 3 :
        delinq_score = -154.455561
    else:
        delinq_score = -99999
    
    if   float(CLAGE) <= 100 :
        clage_score = -31.197078
    elif float(CLAGE) > 100 and float(CLAGE) <= 150 :
        clage_score = -19.079252
    elif float(CLAGE) > 150 and float(CLAGE) <= 200 :
        clage_score = 6.224150
    elif float(CLAGE) > 200 and float(CLAGE) <= 250 :
        clage_score = 18.885538
    elif float(CLAGE) > 250 :
        clage_score = 44.680364
    else:
        clage_score = -99999

    if   float(NINQ) <= 0 :
        ninq_score = 14.133549
    elif float(NINQ) > 0 and float(NINQ) <= 1 :
        ninq_score = 1.130496
    elif float(NINQ) > 1 and float(NINQ) <= 2 :
        ninq_score = -11.230737
    elif float(NINQ) > 2 and float(NINQ) <= 3 :
        ninq_score = -14.877281
    elif float(NINQ) > 3 :
        ninq_score = -47.730547
    else:
        ninq_score = -99999

    if float(DEBTINC) > 0 and float(DEBTINC) <= 25  :
        debtinc_score = 63.119438
    elif float(DEBTINC) > 25 :
        debtinc_score = -4.351940
    else:
        debtinc_score = -99999    
    
    
    final_score = loan_score + value_score + job_score + yoj_score + derog_score + delinq_score + clage_score + ninq_score + debtinc_score + 574.0

    if final_score >= 744:
        rating = '12'
    elif final_score <= 742.476025 and final_score >= 701.812374 :
        rating = '11'
    elif final_score < 701.812374 and final_score >= 685.708029 :
        rating = '10'
    elif final_score < 685.708029 and final_score >= 664.009835 :
        rating = '9'
    elif final_score < 664.009835 and final_score >= 663.985483 :
        rating = '8'
    elif final_score < 663.985483 and final_score >= 644.044749 :
        rating = '7'
    elif final_score < 644.044749 and final_score >= 625.839816 :
        rating = '6'
    elif final_score < 625.839816 and final_score >= 605.739831 :
        rating = '4'
    elif final_score < 605.739831 and final_score >= 587.008424 :
        rating = '3'
    elif final_score < 587.008424 and final_score >= 586.899919 :
        rating = '2'
    elif final_score < 586.899919 and final_score >= 545.468884 :
        rating = '1'
    elif final_score < 545.468884:
        rating = '0'

    if rating == '12':
        loan_brac = '$1000-$55,000'
        interest = '4%'
    elif rating == '11' :
        loan_brac = '$1000-$40,000'
        interest = '4%'
    elif rating == '10' :
        loan_brac = '$1000-$33,000'
        interest = '5%'
    elif rating == '9' :
        loan_brac = '$1000-$33,000'
        interest = '7%'
    elif rating == '8' :
        loan_brac = '$1000-$30,000'
        interest = '10%'
    elif rating == '7' :
        loan_brac = '$1000-$30,000'
        interest = '12%'
    elif rating == '6' :
        loan_brac = '$1000-$20,000'
        interest = '14%'
    elif rating == '4' :
        loan_brac = '$1000-$20,000'
        interest = '17%'
    elif rating == '3' :
        loan_brac = '$1000-$20,000'
        interest = '21%'
    elif rating == '2' :
        loan_brac = '$1000-$15,000'
        interest = '25%'
    elif rating == '1' :
        loan_brac = '$1000-$10,000'
        interest = '28%'
    
    if(rating == '0'):
        return 'The customer risk profile is outside our risk appetite.'
    else:
        return 'Loan is approved for the given customer with credit rating: ' + rating + ' and score of ' + str(round(final_score,2)) +' with interest rate ' + interest + '. The appropriate loan bracket would be ' + loan_brac + '.'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    
    
    
    

    
    
    
    
    