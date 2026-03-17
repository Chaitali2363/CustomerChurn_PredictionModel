from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTE
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer , KNNImputer 
from sklearn.preprocessing import MinMaxScaler , OneHotEncoder , LabelEncoder

'''
WORKFLOW DESIGN:

1. Data Load
2. Clean the unwanted columns from the Dataset
3. Split the dataset into X and y
4. Split the dataset into Train and Test
5. Split the data into Categorical and Numerical Col
6. Use Pipeline for Numerical and Categorical columns
7. Use Column Transformer to fit our model
8. Use SMOTE Technique and then  PCA (for dimensional reductionality)
9. Return X_train , X_test , y_train , y_test

'''
# Step1: Data Load
def data_preprocessing(df):
    
    #step2: Clean Duplicate values
    df = df.drop_duplicates()
    
    #step3: Split Dataset into X and y
    X = df.drop(columns=['Churn','customer_ID'])
    y = df['Churn']

    #step4: Split Dataset into Train and Test
    X_train ,X_test , y_train , y_test = train_test_split(X,y,
                                                          test_size= 0.3,
                                                          randon_state=1)
    
    #Step5: Segregate into numerical and categorical columns
    numerical_col = X_train.select_dtypes(exclude='object').columns
    categorical_col = X_train.select_dtypes(include='object').columns

    #Step6: Using Numerical_Pipeline and Categorical_Pipeline
    

