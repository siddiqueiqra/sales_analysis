import streamlit as st
from sklearn import tree
import pandas as pd

def load_data():
    data=pd.read_csv(r"C:\Users\Lenovo\Downloads\sales.csv")
    return data

data = load_data()

    
def predict_page():
    from sklearn.preprocessing import LabelEncoder
    le=LabelEncoder()
    le.fit(data['Category'])
    data['Category']=le.transform(data['Category'])
    
    le1=LabelEncoder()
    le1.fit(data['Sub Category'])
    data['Sub Category']=le1.transform(data['Sub Category'])
    
    le2 = LabelEncoder()
    le2.fit(data['City'])
    data['City'] = le2.transform(data['City'])

    X = data[["City", "Category", "Sub Category"]]
    y = data["Sales"]
    
    

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    clf = tree.DecisionTreeRegressor()
    clf = clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    from sklearn.metrics import mean_absolute_error, r2_score
    print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
    print("R-squared Score:", r2_score(y_test, y_pred))

    clf = tree.DecisionTreeRegressor()
    clf = clf.fit(X_train, y_train)

    def predict(City, Category, Sub_Category):
        prediction = clf.predict([[City, Category, Sub_Category]])
        return prediction

    st.title("Sales Prediction")

    City = st.selectbox("Select City",
                        options=data['City'].unique())
    category = st.selectbox("Select category", 
                            options=data["Category"].unique())    
    sub_category = st.selectbox("Select sub category", 
                            options=data["Sub Category"])
    if st.button("Predict"):
        result = predict(City, category, sub_category)
        st.success(f'Predicted Sales: {result}')
        return predict_page()

    
