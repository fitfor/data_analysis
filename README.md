# data_analysis
This repository provides data analysis and the ML-Backend of our data app.

The key technologies:
- MLxtend
- Flask
- Pandas

With Flask the REST-server was built. The MLxtend library provides an implementation for the association rules,
the convenient think is the C implementation. The Pandas package was used only for data manipulation.

The Algorithm used for the computation of personalised recommendations is called association rules. 

To run locally the Flask REST-server app, please follow the next steps:
1. setup a virtual environment
2. pip install the requirements.txt
3. execute: `python wsgi.py`

To see how to send requests to the REST-server please see `src/send_requests.py`.